from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    analytic_account = fields.Many2one("account.analytic.account")

    @api.onchange("analytic_account")
    def onchange_account_analytic(self):
        for rec in self:
            if rec.analytic_account:
                for line in rec.order_line:
                    line.analytic_distribution = {
                        rec.analytic_account.id: 100.0
                    }
            else:
                for line in rec.order_line:
                    line.analytic_distribution = {
                        "": 100.0
                    }


class SaleOrder(models.Model):
    _inherit = "sale.order"

    analytic_account = fields.Many2one("account.analytic.account")

    @api.onchange("analytic_account")
    def onchange_account_analytic(self):
        for rec in self:
            if rec.analytic_account:
                for line in rec.order_line:
                    line.analytic_distribution = {
                        rec.analytic_account.id: 100.0
                    }
            else:
                for line in rec.order_line:
                    line.analytic_distribution = {
                        "": 100.0
                    }


class AccountMove(models.Model):
    _inherit = "account.move"

    analytic_account = fields.Many2one("account.analytic.account")

    @api.onchange("analytic_account")
    def onchange_account_analytic(self):
        for rec in self:
            if rec.analytic_account:
                for line in rec.line_ids:
                    line.analytic_distribution = {
                        rec.analytic_account.id: 100.0
                    }
            else:
                for line in rec.line_ids:
                    line.analytic_distribution = {
                        "": 100.0
                    }