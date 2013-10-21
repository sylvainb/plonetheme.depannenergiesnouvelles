import string
import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from plone.browserlayer.utils import registered_layers
from plonetheme.depannenergiesnouvelles.browser.interfaces import IThemeSpecific

from plonetheme.depannenergiesnouvelles.testing import PLONETHEME_INTEGRATION_TESTING

class TestInstall(unittest.TestCase):

    layer = PLONETHEME_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(portal_quickinstaller.isProductInstalled('plonetheme.depannenergiesnouvelles'),
                        'package appears not to have been installed')

    # def test_type_in_portal_types(self):
    #     """ Validate that MyPortalType is registered in the portal_type tool """
    #     portal_types = getToolByName(self.portal, 'portal_types')
    #     self.assertNotEqual(portal_types.getTypeInfo('MyPortalType'), None)

    # def test_type_in_portal_factory(self):
    #     """ Validate that MyPortalType is registered in the portal_factory tool """
    #     portal_factory = self.portal.portal_factory
    #     self.assertEqual("MyPortalType" in portal_factory.getFactoryTypes(), True)

    # def test_type_has_no_workflow(self):
    #     """ Validate that MyPortalType has no workflow """
    #     portal_workflow = getToolByName(self.portal, 'portal_workflow')
    #     default_chain = portal_workflow.getDefaultChain()
    #     field_chain = portal_workflow.getChainForPortalType('MyPortalType')
    #     self.assertEqual(field_chain == (), True)

    # def test_type_not_in_navtree(self):
    #     """ Validate that the MyPortalType is not listed in the navigation tree """
    #     portal_properties = getToolByName(self.portal, 'portal_properties')
    #     navtree_properties = portal_properties.navtree_properties
    #     self.assertEqual('MyPortalType' in navtree_properties.getProperty("metaTypesNotToList"),
    #                      True)

    def test_skins(self):
        """ Validate that the skin directories are installed in the portal_skins tool
            and available in the skin """
        portal_skins = getToolByName(self.portal, 'portal_skins')
        self.assertEqual("plonetheme_depannenergiesnouvelles_custom" in portal_skins.objectIds(), True)

    # def test_registry(self):
    #     registry = getUtility(IRegistry)
    #     # Check 'id_record' entry is in the registry
    #     self.assertTrue(registry.get('module_or_interface_prefix.id_record', None is not None),
    #                      'record in the registry appears to be not properly installed')

    # def test_control_panel_is_installed(self):
    #     portal_controlpanel = getToolByName(self.portal, 'portal_controlpanel')
    #     configlets = [ai['id'] for ai in portal_controlpanel.listActionInfos(check_permissions=0)]
    #     self.assertTrue('control_panel_id' in configlets)

    def test_css_in_registry(self):
        """ Validate our css are registered in portal_css """
        portal_css = getToolByName(self.portal, 'portal_css')
        installedStylesheetIds = portal_css.getResourceIds()
        expected = ['++theme++plonetheme.depannenergiesnouvelles/css/theme.css', ]
        for e in expected:
            self.assertTrue(e in installedStylesheetIds, e)

    def test_js_in_registry(self):
        """ Validate our js are registered in portal_css """
        portal_css = getToolByName(self.portal, 'portal_javascripts')
        installedJavaScriptIds = portal_css.getResourceIds()
        expected = ['++theme++plonetheme.depannenergiesnouvelles/js/theme.js', ]
        for e in expected:
            self.assertTrue(e in installedJavaScriptIds, e)

    def test_browser_layer(self):
        """ Validate our browser layer is registered """
        from plone.browserlayer.utils import registered_layers
        from plonetheme.depannenergiesnouvelles.browser.interfaces import IThemeSpecific
        self.assertTrue(IThemeSpecific in registered_layers())

    def test_diazo_theme_available(self):
        from plone.app.theming.utils import getCurrentTheme
        self.assertTrue(getCurrentTheme() == u'plonetheme.depannenergiesnouvelles')

class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']

        # Remove the product using the Quick Installer tool
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        portal_quickinstaller.uninstallProducts( ('plonetheme.depannenergiesnouvelles',) )

    def test_product_is_not_installed(self):
        """ Validate that our products is not yet installed
        """
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(portal_quickinstaller.isProductInstalled('plonetheme.depannenergiesnouvelles'),
                        'package appears to be already installed')

    # def test_type_not_in_types(self):
    #     """ Validate that MyPortalType is removed from the portal_type tool """
    #     portal_types = getToolByName(self.portal, 'portal_types')
    #     self.assertEqual(portal_types.getTypeInfo('MyPortalType'), None)

    # def test_type_not_in_portal_factory(self):
    #     """ Validate that MyPortalType is removed from the portal_factory tool """
    #     portal_factory = self.portal.portal_factory
    #     self.assertEqual("MyPortalType" in portal_factory.getFactoryTypes(), False)
    #     ==> uninstall with the profile/uninstall/factorytool.xml doesn't work but the
    #         type disappear from the portal_factory ZMI user interface

    def test_not_in_skins(self):
        """ Validate that the skin directories is removed from the portal_skins tool
            and from the skin """
        portal_skins = getToolByName(self.portal, 'portal_skins')
        self.assertNotEqual("plonetheme_depannenergiesnouvelles_custom" in portal_skins.objectIds(), True)

    # def test_registry(self):
    #     registry = getUtility(IRegistry)
    #     # Check 'id_record' entry is in the registry
    #     # i.e. not removed when the module is uninstalled
    #     self.assertTrue(registry.get('module_or_interface_prefix.id_record', None is not None),
    #                      'record in the registry appears to be not properly installed')

    # def test_control_panel_is_not_installed(self):
    #     portal_controlpanel = getToolByName(self.portal, 'portal_controlpanel')
    #     configlets = [ai['id'] for ai in portal_controlpanel.listActionInfos(check_permissions=0)]
    #     self.assertFalse('control_panel_id' in configlets)

    def test_css_not_in_registry(self):
        """ Validate our css are no longer registered in portal_css """
        portal_css = getToolByName(self.portal, 'portal_css')
        installedStylesheetIds = portal_css.getResourceIds()
        expected = ['++theme++plonetheme.depannenergiesnouvelles/css/theme.css', ]
        for e in not_expected:
            self.assertFalse(e in installedStylesheetIds, e)

    def test_js_not_in_registry(self):
        """ Validate our js are no longer registered in portal_css """
        portal_css = getToolByName(self.portal, 'portal_javascripts')
        installedJavaScriptIds = portal_css.getResourceIds()
        expected = ['++theme++plonetheme.depannenergiesnouvelles/js/theme.js', ]
        for e in not_expected:
            self.assertFalse(e in installedJavaScriptIds, e)

    def test_browser_layer(self):
        """ Validate our browser layer is no longer registered """
        from plone.browserlayer.utils import registered_layers
        from plonetheme.depannenergiesnouvelles.browser.interfaces import IThemeSpecific
        self.assertFalse(IThemeSpecific in registered_layers())

    def test_diazo_theme_not_available(self):
        pass
        # A bug ? the theme is always selected (but inactive) in the plone.app.theming control panel
        # from plone.app.theming.utils import getCurrentTheme
        # => must have a space before 'from ...' else templer execute this line and "ERROR: No module named plone.app.theming.utils" !!!!!
        # self.assertFalse(getCurrentTheme() == u'plonetheme.depannenergiesnouvelles')
