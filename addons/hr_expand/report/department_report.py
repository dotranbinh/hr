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
class report_hr_department(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_hr_department, self).__init__(cr, uid, name, context=context)
        self.localcontext.update( {
            'time': time,
            'datetime': datetime,
            'getQtyByMajor':self.getQtyByMajor,
            'getQtyByMajor_0':self.getQtyByMajor_0,
            'getQtyByMajor_1':self.getQtyByMajor_1,
            'getQtyByMajor_2':self.getQtyByMajor_2,
			'getNameDepartment':self.getNameDepartment,
			'getQtyEmployee':self.getQtyEmployee,
            'getQtyGender':self.getQtyGender,
            'getQtyByCP':self.getQtyByCP,
            'getQtyByContract':self.getQtyByContract,
            'getQtyByBirthday':self.getQtyByBirthday,
            'getQtyByInsurance':self.getQtyByInsurance,
            'getQtyBySchool':self.getQtyBySchool,
        })
        self.context = context
        
    def getQtyGender(self,department_id,company_id,gender):
        rec=[]
        self.cr.execute("select count(id) as qty from hr_employee where recruitment_agency="+str(company_id)+" and department_id="+str(department_id)+" and gender='"+str(gender)+"'")
        rec=self.cr.dictfetchall()
        return rec
    def getQtyByInsurance(self,department_id,company_id,gender):
        rec=[]
        self.cr.execute("select count(id) as qty from hr_employee where  recruitment_agency="+str(company_id)+" and department_id="+str(department_id)+" and sinid is not null and gender='"+str(gender)+"'")
        rec=self.cr.dictfetchall()
        return rec
    def getQtyBySchool(self,department_id,company_id,school_id):
        rec=[]
        self.cr.execute("select count(employee_id) as qty from hr_education,hr_employee  where hr_education.employee_id = hr_employee.id  and recruitment_agency="+str(company_id)+" and hr_employee.department_id="+str(department_id)+" and  school_id ="+str(school_id))
        rec=self.cr.dictfetchall()
        return rec
    def getQtyByBirthday(self,department_id,company_id,from_year,to_year):
        rec=[]
        if(to_year!=''):
            self.cr.execute( "select count(birthday) as qty from hr_employee where recruitment_agency="+str(company_id)+" and department_id="+str(department_id)+" and (date_part('year',NOW())-date_part('year', birthday))>="+str(from_year)+"and (date_part('year',NOW())-date_part('year', birthday))<="+str(to_year))
        else:
            self.cr.execute( "select count(birthday) as qty from hr_employee where recruitment_agency="+str(company_id)+" and  department_id="+str(department_id)+" and (date_part('year',NOW())-date_part('year', birthday))>="+str(from_year))
        rec=self.cr.dictfetchall()
        return rec          
    def getQtyByContract(self,department_id,company_id,contract_id):
        rec=[]
        self.cr.execute("select count(employee_id) as qty from hr_contract,hr_employee where  hr_contract.employee_id = hr_employee.id and  recruitment_agency="+str(company_id)+" and hr_employee.department_id="+str(department_id)+" and type_id = (select id from hr_contract_type where id='"+str(contract_id)+"')")
        rec=self.cr.dictfetchall()
        return rec
    def getQtyByCP(self,department_id,company_id,gender):
        rec=[]
        self.cr.execute("select count(id) as qty from hr_employee where  recruitment_agency="+str(company_id)+" and "'"CP_join_date"'" is not null and "'"CP_official_join_date"'" is not null and department_id="+str(department_id)+" and gender='"+str(gender)+"'")
        rec=self.cr.dictfetchall()
        return rec
    def getNameDepartments(self):
        obj= self.pool.get('hr.department')
        ids=obj.search(self.cr,self.uid,[])
        res = obj.read(self.cr, self.uid, ids, ['name', 'id'])
        return res
    def getNameDepartment(self,company_id):
        rec=[]
        result=[]
        self.cr.execute("select * from hr_department where id  in (select distinct department_id from hr_employee where recruitment_agency="+str(company_id)+")")
        rec=self.cr.dictfetchall()
        i=1
        res={}
        for line in rec:
            res={}
            res['name']=line['name']
            res['id']=line['id']
            res['number']=i
            result.append(res)
            i=i+1
        return result
    def getQtyEmployee(self,department_id,company_id):
        rec=[]
        self.cr.execute("select count(id) as qty from hr_employee where recruitment_agency="+str(company_id)+" and department_id="+str(department_id))
        rec=self.cr.dictfetchall()
        return rec
    def getQtyByMajor(self, department_id,company_id, major_id):
        rec = []
        self.cr.execute("SELECT COUNT(edu.id) FROM hr_education edu INNER JOIN hr_diploma dip ON dip.id=edu.diploma_id WHERE edu.employee_id IN\
        (SELECT e.id FROM hr_employee e WHERE e.recruitment_agency="+str(company_id)+" and e.department_id="+str(department_id)+") AND dip.major_id="+str(major_id))
        rec = self.cr.dictfetchall()
        return rec
    def getQtyByMajor_0(self, department_id,company_id, diploma_level_id):
        rec = []
        self.cr.execute("SELECT COUNT(edu.id) FROM hr_education edu INNER JOIN hr_diploma dip ON dip.id=edu.diploma_id WHERE edu.employee_id IN\
        (SELECT e.id FROM hr_employee e WHERE  e.recruitment_agency="+str(company_id)+" and e.department_id="+str(department_id)+") AND dip.diploma_level_id="+str(diploma_level_id))
        rec = self.cr.dictfetchall()
        return rec
    def getQtyByMajor_1(self, department_id,company_id, diploma_level_id, gender):
        rec = []
        self.cr.execute("SELECT COUNT(edu.id) FROM hr_education edu INNER JOIN hr_diploma dip ON dip.id=edu.diploma_id WHERE edu.employee_id IN\
        (SELECT e.id FROM hr_employee e WHERE e.recruitment_agency="+str(company_id)+" and  e.department_id="+str(department_id)+" AND e.gender='"+str(gender)+"') AND dip.diploma_level_id="+str(diploma_level_id))
        rec = self.cr.dictfetchall()
        return rec
        
    def getQtyByMajor_2(self, department_id,company_id, diploma_level_id_1, diploma_level_id_2, gender):
        rec = []
        self.cr.execute("SELECT COUNT(edu.id) FROM hr_education edu INNER JOIN hr_diploma dip ON dip.id=edu.diploma_id WHERE edu.employee_id IN\
        (SELECT e.id FROM hr_employee e WHERE e.recruitment_agency="+str(company_id)+" and e.department_id="+str(department_id)+" AND e.gender='"+str(gender)+"') AND (dip.diploma_level_id="+str(diploma_level_id_1)+" OR dip.diploma_level_id="+str(diploma_level_id_2)+")")
        rec = self.cr.dictfetchall()
        return rec
report_sxw.report_sxw('report.hr.department.report', 'hr.department', 'addons/hr/report/department_report.rml', parser=report_hr_department, header=False)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
