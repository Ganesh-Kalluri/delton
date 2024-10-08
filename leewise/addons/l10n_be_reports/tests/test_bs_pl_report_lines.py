from leewise.tests import tagged

from leewise.addons.account_reports.tests.common import TestAccountReportsCommon


@tagged('post_install_l10n', 'post_install', '-at_install')
class TestBsPlReportLines(TestAccountReportsCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)
        cls.setup_company_data('BE Company', 'be_comp')
        cls.setup_company_data('BE Association', 'be_asso')

    def test_similar_lines_balance_sheet(self):
        bs_versions = ('comp_acon', 'comp_acap', 'comp_fcon', 'comp_fcap', 'asso_a', 'asso_f')
        balance_sheets = self.env['account.report']
        for bs_version in bs_versions:
            balance_sheets |= self.env.ref('l10n_be_reports.account_financial_report_bs_' + bs_version)
        self.assertIdenticalLines(balance_sheets)

    def test_similar_lines_profit_and_loss(self):
        pl_versions = ('comp_a', 'comp_f', 'asso_a', 'asso_f')
        pl_reports = self.env['account.report']
        for pl_version in pl_versions:
            pl_reports |= self.env.ref('l10n_be_reports.account_financial_report_pl_' + pl_version)
        self.assertIdenticalLines(pl_reports)
