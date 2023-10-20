from odoo import models, fields, api
from odoo.exceptions import UserError

class ZeroQuantityInSaleOrder(models.Model):
    _inherit = 'sale.order'

    source_location_id = fields.Many2one(
        'stock.location', "Source Inventory Location", readonly=False,
        check_company=True, required=True,
        states={'sent': [('readonly', True)], 'sale': [('readonly', True)], 'done': [('readonly', True)]})
    
    @api.onchange('stock.location', 'order_line')
    def onchange_product_quantity_in_inventory_check(self):
        """The function is executed whenever the user attempt to modify the aforementioned fields is modified.
        For each sale order line, it checks whether the demanded product has a stock of zero and
        whether the demanded quantity of product is less than or equal the available quantity in the specified invnetory

        :raise UserError: if the conditions are met
        """
        if self.order_line:
            # iterate through sale order lines
            for rec in self.order_line:
                if rec:
                    # setting an accumulator variable that will hold the sum of available quantities of product in one line
                    inventory_available_quantity_total = 0
                    # using an ORM method to extract all stock records of the product in the specified inventory, in the form of iterable list of dictionaries
                    search_stock_quantity_in_source_location = self.env['stock.quant'].sudo().search([('location_id', '=', self.source_location_id.id), 
                    ('product_id', '=', rec.product_id.id)])
                    # summing available quantities in the extracted records
                    for line in search_stock_quantity_in_source_location:
                        inventory_available_quantity_total += line.available_quantity
                    if (inventory_available_quantity_total <= 0) and (rec.name != False):
                        raise UserError("You cannot sale a product whose quantity of stock is less than 0")
                    elif ((inventory_available_quantity_total - rec.product_uom_qty) < 0 ) and (rec.name != False):
                        raise UserError("The stock quantity of the product is less than the desired quantity")

