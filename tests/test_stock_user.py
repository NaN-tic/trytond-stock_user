# This file is part of stock_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.tests.test_tryton import test_view, test_depends
import os
import sys
import trytond.tests.test_tryton
import unittest


class StockUserTestCase(unittest.TestCase):
    'Test Stock User module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('stock_user')

    def test0005views(self):
        'Test views'
        test_view('stock_user')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockUserTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
