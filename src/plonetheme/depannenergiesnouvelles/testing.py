from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from Products.CMFCore.utils import getToolByName

from plonetheme.depannenergiesnouvelles.tests.utils import PLONE_VERSION

class PloneThemeSandboxLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML, install the products and call its initialize() function 
        import plonetheme.depannenergiesnouvelles
        self.loadZCML(package=plonetheme.depannenergiesnouvelles)
        z2.installProduct(app, 'plonetheme.depannenergiesnouvelles')

    def setUpPloneSite(self, portal):
        # Configure the products using the Quick Installer tool 
        portal_quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        portal_quickinstaller.installProducts( ('plonetheme.depannenergiesnouvelles',) )

    def tearDownZope(self, app):
        # Uninstall products
        z2.uninstallProduct(app, 'plonetheme.depannenergiesnouvelles')

    def tearDownPloneSite(self, portal):
        # Unconfigure the products using the Quick Installer tool
        portal_quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        portal_quickinstaller.uninstallProducts( ('plonetheme.depannenergiesnouvelles',) )

PLONETHEME_FIXTURE = PloneThemeSandboxLayer()
PLONETHEME_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PLONETHEME_FIXTURE, ),
                       name="plonetheme.depannenergiesnouvelles:Integration")
PLONETHEME_FUNCTIONNAL_TESTING = \
    FunctionalTesting(bases=(PLONETHEME_FIXTURE, ),
                      name="plonetheme.depannenergiesnouvelles:Functional")