# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import addons
import logging
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools

_logger = logging.getLogger(__name__)

# duoc them boi dotran

class hr_reward(osv.osv):
    _name="hr.reward"
    _description = "Reward"
    _columns = {
            'employee_id':fields.many2one('hr.employee','Employee'),
            "name":fields.char("Name",size=64,required=True), # Hinh thuc khen thuong
            "year":fields.date("Date",required=True), # Nam duoc khen thuong
            'Document': fields.binary("Document"),
           
                    }
    _defaults = {  
          
        }
hr_reward()
class hr_punishment(osv.osv):
    _name="hr.punishment"
    _description = "Punishment"
    _columns = {
            "name":fields.char("Name",size=64,required=True), # Hinh thuc ky luạt
            "year":fields.date("Date",required=True), # Nam ky luat
           'employee_id':fields.many2one('hr.employee','Employee'),
           'Document': fields.binary("Document"),
                    }
    _defaults = {  
          
        }
hr_punishment()
class hr_health(osv.osv):
    _name='hr.health'
    _columns = {
            'employee_id':fields.many2one('hr.employee','Employee'),
            'name':fields.char('Name',size=64),# Tinh trang suc khoe
            'height':fields.float('Height'), # Chieu cao
            'weight':fields.float('Weight'), # Can nang
            'blood':fields.char('Blood',size=32), # Nhom mau
                    }
    _defaults = {  
      
        }
hr_health()
class hr_wound(osv.osv):
    _name='hr.wound'
    _columns = {
            'name':fields.char('Name'),# thuong binh hang
            'type':fields.char('Type'), # Con gia dinh chinh sach
                    }
    _defaults = {  
          
                }
hr_wound()

class hr_work(osv.osv):
    _name='hr.work'
    _columns = {
            'name':fields.char('Name',size=64,required=True), # Chuc danh
            'company': fields.char('Company', size=64),# Cong ty, 
            'from_time':fields.date('From time'), # tu ngay thang nam    
            'to_time':fields.date('To time'), # Den ngay thang nam
            'employee':fields.many2one('hr.employee','Employee'),
            'job': fields.char('Job',size=64), # Chuyen mon nghiep vu
                            }
hr_work()

class hr_works(osv.osv):
    _name='hr.works'
    _columns = {
            'from_time':fields.date('From time',required=True), # tu ngay thang nam    
            'to_time':fields.date('To time',required=True), # Den ngay thang nam
            'employee_id':fields.many2one('hr.employee','Employee'),
            'note': fields.text('Note',required=True), # Chuyen mon nghiep vu
                            }
hr_works()

class hr_offical(osv.osv):
    _name='hr.offical'
    _columns = {
            'name':fields.char('Name',size=128),# Ten ngach
            'code':fields.char('Code',size=64),# Ma ngach
                    }
    _defaults = {  
        
        }
hr_offical()
class hr_salary(osv.osv):
    _name='hr.salary'
    _columns = {
            'name':fields.many2one('hr.offical','Name',required=True),# Ten Ngach cong chuc, vien chuc    
            'date':fields.date('Date'),# thang-nam
            'wage':fields.char('Wage',size=10),# bac
            'cost':fields.float('Cost'),# he so luong
            'employee':fields.many2one('hr.employee','Employee'),
            'allowance':fields.float('Allowance'),# Phu cap chuc vu
            'other_allowance':fields.float('Other_allowance'),# Phu cap khac
                            }
    _defaults = {  
            
                }
hr_salary()

class hr_salarys(osv.osv):
    _name='hr.salarys'
    _columns = {
            'name':fields.many2one('hr.offical','Name',required=True),# Ten Ngach cong chuc, vien chuc    
            'date':fields.date('Date'),# thang-nam
            'wage':fields.char('Wage',size=10),# bac
            'cost':fields.float('Cost'),# he so luong
            'employee_id':fields.many2one('hr.employee','Employee'),
            
                            }
    _defaults = {  
            
                }
hr_salarys()

class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    
    _columns = {
        'job_id_m': fields.one2many('hr.job.m', 'employee_id','Job Many'),
       
        'date':fields.date('Date'),
        #'address_home_id': fields.many2one('hr.address', 'Home Address'),
        'general_education':fields.char('General education',size=64), # Giao duc pho thong
        'highest_diploma':fields.char('Highest Diploma',size=64), # Trinh do chuyen mon cao nhat
        #'political_theory':fields.char('Political Theory',size=64),# Ly luan chinh tri
        
        'political_theory':fields.selection([('cc', 'Cao cấp'), ('tc', 'Trung cấp'),('sc', 'Sơ cấp')], 'Political Theory'),
        'state_management':fields.char('State Management',size=64),# Quan ly nha nuoc
        'foreign_language':fields.char('Foreign Language',size=64),# Ngoai ngu
        'it':fields.char('Information Technology',size=64),# Tin hoc,
        
        'address_home_id_txt': fields.text('Home Address'),
        
        # code added by Dotran
        'major':fields.char('Major',size=64), # So truong cong tac
        'reward':fields.one2many('hr.reward','employee_id','Reward'), # khen thuong
        'health':fields.one2many('hr.health','employee_id','Health'), # tinh trang suc khoe
        'wound':fields.many2one('hr.wound','Wound'), # Thuong binh
        'work':fields.one2many('hr.work','employee','Work'), # qua trinh cong tac
        'salary':fields.one2many('hr.salary','employee','Salary'), # Luong
        'salarys_id':fields.one2many('hr.salarys','employee_id','Salarys'), # Qua tring luong
        'comment':fields.text('Comment'),# Nhan xet danh gia
        'detention':fields.text('Detention'), # Tu day, giam cam
        'rw_frcompany':fields.text('RwForeignCompany'), # Quan he voi to chuc nuoc ngoai
        'rw_frperson':fields.text('RwForeignPerson'),# Than nhan o nuoc ngoai
        'punishment':fields.one2many('hr.punishment','employee_id','Punishment'), # Ky luat
        # code added by Hoang Pham
        #2
        'other_name': fields.char('Other Name', size=64),
        #4
        'birthplace_id': fields.many2one('res.partner', 'Place of Birth'),
        #'birthplace_id' : fields.many2one('hr.wards', 'Place of Birth'),
        'birthplace_id_txt' : fields.text('Place of Birth'),
        #5
        'hometown_id': fields.many2one('res.partner', 'Hometown'),
        #'hometown_id': fields.many2one('hr.wards', 'Hometown'),
        'hometown_id_txt': fields.text('Hometown'),
        #6
        'ethnic_id': fields.many2one('hr.ethnic', 'Ethnic'),
        #7
        'religion_id': fields.many2one('hr.religion', 'Religion'),
        #8
        'permanent_address_id': fields.many2one('res.partner', 'Permanent Address'),
        #'permanent_address_id': fields.many2one('hr.address', 'Permanent Address'),
        'permanent_address_id_txt': fields.text('Permanent Address'),
        #10
        'last_job': fields.char('Last Job', size=32),
        #11
        'recruitment_date': fields.date('Recruitment Date'),
        'recruitment_agency': fields.many2one('res.company','Recruitment Agency'),
        #13
        'key_task': fields.char('Key Task', size=64),
        #16
        'CP_join_date': fields.date('Communist Party Join Date'),
        'CP_official_join_date': fields.date('Official Join Date'),
        #17
        'sociopolitical_organization_id': fields.many2one('hr.sociopolitical_organization', 'Socipolitical Organization'),
        'sopo_organization_join_date': fields.date('Socipolitical Organization Join Date'),
        #18
        'enlistment_date': fields.date('Enlistment Date'),
        'demobilized_date': fields.date('Demobilized Date'),
        'highest_army_rank_id': fields.many2one('hr.army_rank', 'Highest Army Rank'),
        #19
        'highest_reward_rank': fields.char('Highest Reward Rank', size=64),
        #27
        'education_id': fields.one2many('hr.education', 'employee_id', 'Education'),
        'training_id':fields.one2many('hr.training','employee_id','Training'),
        'works_id':fields.one2many('hr.works','employee_id','Works'),
        'work_history':fields.one2many('hr.work.history','employee_id','Work History'),
        #30
        'relationship_id': fields.one2many('hr.relationship', 'employee_id', 'Relationship'),
        'bd_date':fields.integer('Birthday Date'),
        'bd_month':fields.integer('Birthday Month'),
        'bd_year':fields.integer('Birthday Year'),
        
        
    }
    def _default_department(self, cr, uid, context=None):
        if context is None:
            context = {}
        if 'department_id' in context and context['department_id']:
            department_id= context['department_id']
            return department_id
            
        else:
            return False
   
        
    _defaults = {
       
        #'department_id' : _default_department,
              
        
        
    }
    def onchange_birthday(self, cr, uid, ids, birthday, context=None):
        if birthday:
            array= birthday.split('-')
            year = int(array[0])
            month= int(array[1])
            date= int(array[2])
            return {'value': {'bd_year': year, 'bd_month':month,'bd_date':date}}
        return {'value': {}}
    
    
hr_employee()


class hr_work_history(osv.osv):
    _name='hr.work.history'
    _columns={
              'type_work':fields.selection([('dd','Điều Động'),('bn','Bổ nhiệm'),('tm','Tuyển Mới'),('cd','Chấm dứt HĐLĐ')],'Type Work',required=True),
              'date':fields.date('Date Action Work',required=True),
              'employee_id':fields.many2one('hr.employee','Employee'),
              'note':fields.text('Note')
              }

class hr_job_m(osv.osv):
    _name = 'hr.job.m'
    _columns = {
                'description': fields.text('Job Description'),
                'requirements': fields.text('Requirements'),
                'department_id': fields.many2one('hr.department', 'Department'),
                'company_id': fields.many2one('res.company', 'Company'),
                'employee_id':fields.many2one('hr.employee','Employee'),
                'job_position':fields.many2one('hr.job.position','Job Position')
                }
    _defaults = {
                'company_id': lambda self,cr,uid,c: self.pool.get('res.company')._company_default_get(cr, uid, '', context=c),
    }
class hr_job_poistion(osv.osv):
    _name='hr.job.position'
    _order='sequence'
    _columns={
              'name': fields.char('Name', size=64, required=True),
              'description': fields.text('Description of Poistion'),
              'sequence':fields.integer('Sequence'),
              }
# code added by Hoang Pham    
class hr_religion(osv.osv):
    _name='hr.religion'
    _columns = {
        'name': fields.char('Name', size=32, required=True),
        'description': fields.text('Description'),
    }
hr_religion()
    
class hr_ethnic(osv.osv):
    _name='hr.ethnic'
    _columns = {
        'name': fields.char('Name', size=16, required=True),
        'description': fields.text('Description'),
    }
hr_ethnic()

class hr_school(osv.osv):
    _name='hr.school'
    _columns = {
        'name': fields.char('Name', size=32, required=True),
        'nation': fields.char('Nation', size=16),
    }
hr_school()

class hr_training_form(osv.osv):
    _name='hr.training_form'
    _columns = {
        'name': fields.char('Name', size=16, required=True),
    }
hr_training_form()

class hr_majors(osv.osv):
    _name='hr.majors'
    _columns = {
        'name': fields.char('Major', size=64, required=True),
    }
hr_majors()
class hr_major_category(osv.osv):
    _name='hr.major.category'
    _columns = {
        'name': fields.char('Major Category', size=128, required=True),
    }
hr_majors()

class hr_diploma_level(osv.osv):
    _name='hr.diploma_level'
    _columns = {
        'name': fields.char('Level', size=64, required=True),
    }
hr_diploma_level()

class hr_diploma(osv.osv):
    _name='hr.diploma'
    def _get_name (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids):
            res[record.id] = record.major + " - " + record.diploma
        return res
    _columns = {
        'name': fields.function(_get_name, methor=True, type='char', string='Name', size=128, store=True),
        'major_id': fields.many2one('hr.majors', 'Major', required=True),
        'major': fields.related('major_id', 'name', type='char', string='Major'),
        'diploma_level_id': fields.many2one('hr.diploma_level', 'Diploma Level', required=True),
        'diploma': fields.related('diploma_level_id', 'name', type='char', string='Diploma Level'),
    }
hr_diploma()

class hr_education(osv.osv):
    _name='hr.education'
    def _get_name (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids):
            res[record.id] = record.diploma
        return res
    _columns = {
        'name': fields.function(_get_name, methor=True, type='char', string='Name', size=128, store=True),
        'employee_id': fields.many2one('hr.employee', 'Employee'),
        'school_id': fields.many2one('hr.school', 'School', required=True),
        'diploma_id': fields.many2one('hr.diploma', 'Diploma', required=True),
        'diploma': fields.related('diploma_id', 'name', type='char', string='Diploma'),
        'from_time': fields.date('From', required=True),
        'to_time': fields.date('To', required=True),
        'training_form_id': fields.many2one('hr.training_form', 'Training Form', required=True),
        
    }
    _defaults = {
    }
hr_education()
class hr_training(osv.osv):
    _name='hr.training'
    _columns={
        'employee_id':fields.many2one('hr.employee','Employee'),
        'school':fields.many2one('hr.training.school','School',required=True),
        'major':fields.char('Major',required=True),
        'diploma':fields.char('Diploma'),
        'from_time': fields.date('From'),
        'to_time': fields.date('To'),
        'training_form': fields.char('Training Form'),
        'Document': fields.binary("Document"),
        'name': fields.many2one('hr.major.category', 'Major Category', required=True),
        'level_school':fields.selection([('dh', 'Đại học'), ('tdh', 'Trên đại học'),('cd', 'Cao đẳng'),('tc', 'Trung cấp'),('cnkt', 'CN Kỹ thuật'),('ldpt', 'LĐ Phổ thông')], 'Level', required=True),
              }
    _defaults={}
hr_training()

class hr_training_school(osv.osv):
    _name='hr.training.school'
    _columns={
              'name':fields.char('Name of School',size=64,required=True),
              #'code':fields.char('Code',size=32),
              }
class hr_sociopolitical_organization(osv.osv):
    _name='hr.sociopolitical_organization'
    _columns = {
        'name': fields.char('Name', size=32, required=True),
        'description': fields.text('Description'),
    }
hr_sociopolitical_organization()

class hr_army_rank(osv.osv):
    _name='hr.army_rank'
    _columns = {
        'name': fields.char('Name', size=32, required=True),
        'value': fields.integer('Value', required=True),
    }
hr_army_rank()

class hr_relationship_type(osv.osv):
    _name='hr.relationship_type'
    def _get_name (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids):
            if record.in_law:
                res[record.id] = record.type + " vợ (chồng)".decode('utf8')
            else:
                res[record.id] = record.type
        return res
    _columns = {
        'name': fields.function(_get_name, methor=True, type='char', string='Name', size=64, store=True),
        'type': fields.char('Name', size=16, required=True),
        'in_law': fields.boolean('In-law Relationship'),
    }
hr_relationship_type()

class hr_relationship(osv.osv):
    _name='hr.relationship'
    def _get_name (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids):
            res[record.id] = record.relationship_type + " - " + record.full_name
        return res
    _columns = {
        'name': fields.function(_get_name, methor=True, type='char', string='Name', size=128, store=True),
        'employee_id': fields.many2one('hr.employee', 'Employee', required=True),
        'full_name': fields.char('Full Name', size=64, required=True),
        'birth_date': fields.date('Date of Birth', required=True),
        'relationship_type_id': fields.many2one('hr.relationship_type', 'Relationship Type', required=True),
        'relationship_type': fields.related('relationship_type_id', 'name', type='char'),
        'additional_information': fields.text('Additional Information'),
    }
    _defaults = {
    }
hr_relationship()

class hr_province(osv.osv):
    _name='hr.province'
    _columns = {
        'name': fields.char('Name', size=16, required=True),
    }

class hr_district(osv.osv):
    _name='hr.district'
    def _get_name (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids):
            res[record.id] = record.district + " - " + record.province
        return res
    _columns = {
        'name': fields.function(_get_name, methor=True, type='char', string='Name', size=35, store=True),
        'district': fields.char('Name', size=16, required=True),
        'province_id': fields.many2one('hr.province', 'Province', required=True),
        'province': fields.related('province_id', 'name', type='char'),
    }
hr_district()

class hr_wards(osv.osv):
    _name='hr.wards'
    def _get_name (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids):
            res[record.id] = record.wards + " - " + record.district
        return res
    _columns = {
        'name': fields.function(_get_name, methor=True, type='char', string='Name', size=54, store=True),
        'wards': fields.char('Name', size=16, required=True),
        'district_id': fields.many2one('hr.district', 'District', required=True),
        'district': fields.related('district_id', 'name', type='char'),
    }
hr_wards()

class hr_address(osv.osv):
    _name='hr.address'
    def _get_name (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids):
            res[record.id] = record.number + " " + record.street + " - " + record.wards
        return res
    _columns = {
        'name': fields.function(_get_name, methor=True, type='char', string='Name', size=128, store=True),
        'wards_id': fields.many2one('hr.wards', 'Wards', required=True),
        'wards': fields.related('wards_id', 'name', type='char'),
        'street': fields.char('Street', size=32, required=True),
        'number': fields.char('Number', size=16, required=True),
    }
hr_address()

