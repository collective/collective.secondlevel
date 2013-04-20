from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from plone.app.layout.viewlets.interfaces import IPortalHeader
from Products.CMFCore.interfaces import ISiteRoot
from plone.memoize.instance import memoize

grok.context(Interface)
grok.templatedir('templates')

class SecondLevelMenu(grok.Viewlet):
  grok.viewletmanager(IPortalHeader)

  def update(self):
    """ Set up variable containing the second level navigation menu """
    self.ulclass = ''
    self.list = self.buildMenu(self.context)

  @memoize
  def buildMenu(self,context):
    """
    @return: String containing html for the second level menu

    Example::

        html = buildMenu(self.context)
        print (html) 

    @param context: Current context
    """
    list = ''
    chain = self.getAcquisitionChain(context)
    first,second = self.getElements(chain)
    if first:
      self.ulclass = first.id # Update now when we have the information available
      children = first.getChildNodes()
      for x in children:
        # The description may be one line or more
        desc = x.description
        if len(desc.splitlines())>0:
          desc = desc.splitlines()[0]
        # Plain if not in path
        cssclass = 'plain' 
        if x == second:
          cssclass = 'selected'
        # Add the content to list
        list += '<li id="secondlevel-'+x.id+'" class="'+cssclass+'"><a href="'+x.absolute_url_path()+'"'
        if len(str(desc))>0:
          list += ' title="'+desc+'"'
        list += '>'+x.title+'</a></li>'
    return list

  def getMenu(self):
    """ Getter used by the template """
    return self.list

  def available(self):
    """ The view will be default available. """
    return True

  @memoize
  def getElements(self,object):
    """
    @return: Tuplet of the first and the second sublevel of navigation on the tree. 

    Example::

        first,second = getElements(acquisitionchain)
        print "First level after Site:" + str(first)
        print "Second level after Site:" + str(second)

    @param object: Acquisition chain (see getAcquisitionChain) iterable 
    """
    reversed = list(object)[::-1]
    first = None
    second = None
    level = 0
    for x in reversed:
      if x.portal_type != 'Plone Site':
       if level == 0:
         first = x
         level = level +1
         continue
       if level == 1:
         second = x
         level = level +1
         break
    return first, second

  @memoize
  def getAcquisitionChain(self,object):
    """
    @return: List of objects from context, its parents to the portal root

    Example::

        chain = getAcquisitionChain(self.context)
        print "I will look up objects:" + str(list(chain))

    @param object: Any content object
    @return: Iterable of all parents from the direct parent to the site root
    """
    # It is important to use inner to bootstrap the traverse,
    # or otherwise we might get surprising parents
    # E.g. the context of the view has the view as the parent
    # unless inner is used
    inner = object.aq_inner
    iter = inner
    while iter is not None:
        yield iter
        if ISiteRoot.providedBy(iter):
           break
        if not hasattr(iter, "aq_parent"):
            raise RuntimeError("Parent traversing interrupted by object: " + str(parent))
        iter = iter.aq_parent
