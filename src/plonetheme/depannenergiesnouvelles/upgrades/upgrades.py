from Products.CMFCore.utils import getToolByName
PROFILEID = 'profile-plonetheme.depannenergiesnouvelles:default'

def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILEID)
#    setup.runImportStepFromProfile(PROFILEID,
#                                   'jsregistry', run_dependencies=False,
#                                   purge_old=False)
