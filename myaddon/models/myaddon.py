from odoo import models, fields, api
from xpinyin import Pinyin
from odoo.exceptions import ValidationError

class ProductCustom(models.Model):
    _name = 'product.product'
    _inherit = ['product.product']

    type = fields.Selection([
        ('product', 'Stockable Product')],
        string='Product Type',
        default='product',
        required=True,
        )

    code = fields.Char(
        'Reference', copy=False, compute='_compute_product_code')

    @api.one
    def _compute_product_code(self):
        self.code = Pinyin().get_initials(chars=self.name,splitter='')

    _sql_constraints = [
        ('barcode_uniq', 'unique(barcode)', "A barcode can only be assigned to one product !"),
        ('default_code_uniq','unique(default_code)',"Internal Reference must be unique "),
    ]



