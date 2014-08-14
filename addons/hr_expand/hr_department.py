from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools

class hr_department(osv.osv):
    _inherit = 'hr.department'
    
    _columns = {
                'sequence':fields.integer('Sequence'),
                
                }
    _order='sequence'