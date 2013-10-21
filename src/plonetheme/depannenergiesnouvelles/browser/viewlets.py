#!/usr/bin/env python
# -*- coding: utf-8 -*-

from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface

class CallUsViewlet(grok.Viewlet):
    """Display the call us subject
    """

    grok.name('silvio.themes.CallUsViewlet')
    # On all content by default.
    grok.context(Interface)
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader)

    def render(self):
        return """
        <div id="header_phone_text">
          <span>Un renseignement, un devis ?</span>
          <br />
          <span> 06 76 49 62 18</span>
        </div>
        """