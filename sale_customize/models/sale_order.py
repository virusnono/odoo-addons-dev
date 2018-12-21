# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_type_id = fields.Selection([('default', 'Default Order'), ('sample', 'Sample Order'), ('exhibition', 'Exhibition Order')],
                                    string='销售类型', default='default', required=True);