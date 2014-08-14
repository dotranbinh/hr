# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import datetime
import time
from report import report_sxw
from openerp.tools.translate import _
#
# Use period and Journal for selection or resources
#
class report_hr_employee(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_hr_employee, self).__init__(cr, uid, name, context=context)
        self.localcontext.update( {
            'time': time,
            'datetime': datetime,
            'get_edu_level': self.get_edu_level,
            'get_relationship': self.get_relationship,
            'get_major':self.get_major,
            'get_latest_salary':self.get_latest_salary,
            'get_latest_reward':self.get_latest_reward,
            'get_latest_punishment':self.get_latest_punishment,
        })
        self.context = context
	
    def get_edu_level(self, employee_id, major_id):
		rec = []
		self.cr.execute("SELECT l.name AS diploma\
                        FROM hr_diploma_level l, hr_diploma d, hr_education e\
                        WHERE l.id=d.diploma_level_id AND d.major_id="+str(major_id)+" AND e.diploma_id=d.id AND e.employee_id="+str(employee_id))
		rec = self.cr.dictfetchall()
		return rec
	
    def get_relationship(self, employee_id, inlaw):
		rec = []
		self.cr.execute("SELECT t.type, rel.full_name, rel.birth_date, rel.additional_information\
						FROM hr_relationship rel, hr_relationship_type t\
						WHERE rel.relationship_type_id = t.id AND t.in_law="+str(inlaw)+" AND rel.employee_id="+str(employee_id))
		rec = self.cr.dictfetchall()
		return rec
        
    def get_major(self, employee_id):
        rec=[]
        self.cr.execute("select name  \
                        from hr_work \
                        where employee="+str(employee_id)+" \
                        order by to_time desc limit 1;")
        rec=self.cr.dictfetchall()
        return rec
		
    def get_latest_salary(self, employee_id):
        rec=[]
        self.cr.execute("select off.name,off.code, s.wage,s.cost,s.allowance,s.other_allowance,s.date \
                         from hr_offical off, hr_salary s \
                         where off.id= s.name and s.employee="+str(employee_id)+"\
                          order by date desc limit 1;")
        rec=self.cr.dictfetchall()
        return rec
    def get_latest_reward(self, employee_id):
        rec=[]
        self.cr.execute("select r.name,r.year \
                         from hr_reward r  \
                         where r.employee_id="+str(employee_id)+"\
                          order by r.year desc limit 1;")
        rec=self.cr.dictfetchall()
        return rec
    def get_latest_punishment(self, employee_id):
        rec=[]
        self.cr.execute("select p.name,p.year \
                         from hr_punishment p  \
                         where p.employee_id="+str(employee_id)+"\
                          order by p.year desc limit 1;")
        rec=self.cr.dictfetchall()
        return rec
report_sxw.report_sxw('report.hr.employee.report', 'hr.employee', 'addons/hr_expand/report/employee_report.rml', parser=report_hr_employee, header=False)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
