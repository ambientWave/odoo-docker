from odoo import models, fields, tools, api
from odoo.exceptions import UserError

class ZeroQuantityInWHTransfer(models.Model):
    _inherit = 'stock.picking'

        
    @api.onchange('location_id', 'picking_type_id', 'move_ids_without_package') #  ,'picking_type_id', 'location_id', 'location_dest_id', 'move_id', 'product_id', 'product'
    def onchange_product_quantity_check(self):
        """The function is executed whenever the user attempt to modify the aforementioned fields.
        For each inventory transfer line, it checks whether the demanded product has a stock of zero and
        whether the demanded quantity of product is less than or equal the available quantity in the specified invnetory

        :raise UserError: if the conditions are met
        """
        if self:
            # checks if the type of operation field in operation type field is one of instances that involve products being transfered/pulled FROM a source inventory
            if self.picking_type_id.code == 'outgoing' or 'internal' or 'mrp_operation':
                # iterate through transfer lines
                for rec in self.move_ids_without_package:
                    # setting an accumulator variable that would hold the sum of available quantities of product in one line
                    inventory_available_quantity_total = 0
                    # using an ORM method to extract all stock records of the product in the specified inventory, in the form of iterable list of dictionaries
                    search_stock_quantity_in_source_location = self.env['stock.quant'].sudo().search([('location_id', '=', self.location_id.id), 
                    ('product_id', '=', rec.product_id.id)])
                    # summing available quantities in the extracted records
                    for line in search_stock_quantity_in_source_location:
                        inventory_available_quantity_total += line.available_quantity
                        # raise exception if the available quantity is less than or equal 0
                    if (inventory_available_quantity_total <= 0) and (rec.description_picking != False):
                        raise UserError("You cannot sale a product whose quantity of stock is less than 0")
                        # raise exception if the available quantity is less than quantity asked for
                    elif ((inventory_available_quantity_total - rec.product_uom_qty) < 0 ) and (rec.description_picking != False):
                        raise UserError("The stock quantity of the product is less than the desired quantity")
