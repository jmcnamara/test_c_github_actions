###############################################################################
#
# Tests for libxlsxwriter.
#
# Copyright 2014-2022, John McNamara, jmcnamara@cpan.org
#

import base_test_class

class TestCompareXLSXFiles(base_test_class.XLSXBaseTest):
    """
    Test file created with libxlsxwriter against a file created by Excel.

    """

    def test_chart_title01(self):
        self.run_exe_test('test_chart_title01')

    def test_chart_title02(self):
        self.run_exe_test('test_chart_title02')

    def test_chart_title03(self):
        self.run_exe_test('test_chart_title03')
