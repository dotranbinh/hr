from openerp.osv import osv, fields
class sale_order(osv.osv):
    _inherit='sale.order'
    _columns={
              'so_payment':fields.text('Sale Order Payment'),
              'so_shipment':fields.text('Sale Order Shipment'),
              'so_note':fields.text('Sale Order Note'),
              
              }