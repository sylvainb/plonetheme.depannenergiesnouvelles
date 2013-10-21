import unittest
import doctest

from plone.testing import layered

from plonetheme.depannenergiesnouvelles.testing import PLONETHEME_INTEGRATION_TESTING

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('doctests.rst',
                                     optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                                                 doctest.NORMALIZE_WHITESPACE | 
                                                 doctest.ELLIPSIS), 
                layer=PLONETHEME_INTEGRATION_TESTING),
    ])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

