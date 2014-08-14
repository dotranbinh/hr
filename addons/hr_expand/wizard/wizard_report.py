
import datetime
import time
from openerp.osv import fields, osv
import uuid

PATH= 'C:\\Wamp\\www\\test\\'
URL = 'http://localhost:8080/test/'
 
class wizard_hr_report(osv.osv_memory):
    _name = 'wizard.hr.report'
 
    _columns = {
        'date_start' : fields.date('Start',required=True),
        'date_end' : fields.date('End',required=True),
        'company':fields.many2one('res.company','Company',readonly=False, required=True),
        'company_id': fields.related('company', 'id', type='integer'),
        'company_name':fields.related('company', 'name', type='char'),
    }
 
    _defaults = { # make default start, end date
        'date_start' : lambda *a: time.strftime('%Y-%m-%d'),
        'date_end' : lambda *a: time.strftime('%Y-%m-%d'),
        'company':1,
     }
 
    def print_report(self, cr, uid, ids, context={}):
        data = {}
        data['form'] = self.read(cr, uid, ids, ['date_start', 'date_end','company_id','company_name'], context=context)[0]
        
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'hr.department.report',
            'datas': data,
        }
    def export_excel(self, cr, uid, ids, context={}):
        general_report_emp_obj = self.pool.get('general.report.employee')
        filename='BM01.xlsx'
        #filename = self.my_random_string(cr, uid, ids, context, 30)+'.xlsx'
        filepath = PATH+filename
        data = {}
        data['form'] = self.read(cr, uid, ids, ['date_start', 'date_end','company_id','company_name'], context=context)[0]
        general_report_emp_obj.export_2_excel(cr,uid,ids,filepath,data,context)
       
        return {
                'name'     : 'Go to website', 
                'type': 'ir.actions.act_url',
                'res_model':'ir.actions.act_url', 
                'nodestroy': True,
                'url': URL+filename,
                'target':'new'}
       
    def my_random_string(self, cr, uid, ids, context={},string_length=10):
        """Returns a random string of length string_length."""
        random = str(uuid.uuid4()) # Convert UUID format to a Python string.
        random = random.upper() # Make all characters uppercase.
        random = random.replace("-","") # Remove the UUID '-'.
        return random[0:string_length] # Return the random string.
wizard_hr_report()


class hr_wizard_bm_02(osv.osv_memory):
    _name   =   'hr.wizard.bm.02'
    _columns={
              
              }
    def export_excel(self, cr, uid, ids, context={}):
        hr_bm_02_obj = self.pool.get('hr.bm.02')
        filename='BM02.xlsx'
        #filename = self.my_random_string(cr, uid, ids, context, 30)+'.xlsx'
        filepath = PATH+filename
        hr_bm_02_obj.export_2_excel(cr,uid,ids,filepath,context)
       
        return {
                'name'     : 'Go to website', 
                'type': 'ir.actions.act_url',
                'res_model':'ir.actions.act_url', 
                'nodestroy': True,
                'url': URL+filename,
                'target':'new'}
    def my_random_string(self, cr, uid, ids, context={},string_length=10):
        """Returns a random string of length string_length."""
        random = str(uuid.uuid4()) # Convert UUID format to a Python string.
        random = random.upper() # Make all characters uppercase.
        random = random.replace("-","") # Remove the UUID '-'.
        return random[0:string_length] # Return the random string.