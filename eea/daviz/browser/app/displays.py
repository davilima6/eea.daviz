# -*- coding: utf-8 -*-

__author__ = """European Environment Agency (EEA)"""
__docformat__ = 'plaintext'
__credits__ = """contributions: Alin Voinea"""

from zope.interface import implements
from zope.component import adapts
from Products.CMFDynamicViewFTI import interfaces as cmfdynifaces
from eea.daviz.interfaces import IExhibitJson

class DynamicViews(object):
    """ Display
    """
    implements(cmfdynifaces.IDynamicallyViewable)
    adapts(IExhibitJson)

    def __init__(self, context):
        self.context = context

    def getAvailableViewMethods(self):
        """Get a list of registered view method names
        """
        return [view for view, _name in self.getAvailableLayouts()]

    def getDefaultViewMethod(self):
        """Get the default view method name
        """
        return 'daviz-view.html'

    def getAvailableLayouts(self):
        """Get the layouts registered for this object.
        """
        return (("daviz-view.html", "Daviz View"),)