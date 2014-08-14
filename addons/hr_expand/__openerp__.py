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

{
    'name': 'Employee Directory Expand',
    'version': '1.1',
    'author': 'Tran Binh Do',
    'category': 'Human Resources',
     'depends': ['hr'],
    'sequence': 21,
    'website': 'http://www.haproinfo.com',
    'summary': 'Jobs, Departments, Employees Details',
    'description': """
Human Resources Management
==========================

This application enables you to manage important aspects of your company's staff and other details such as their skills, contacts, working time...


You can manage:
---------------
* Employees and hierarchies : You can define your employee with User and display hierarchies
* HR Departments
* HR Jobs
    """,
    'author': 'Tran Binh Do',
    'website': 'http://www.haproinfo.vn',
  
    'data': [
             
        'security/hr_security.xml',
        'hr_view.xml',
		'hr_report.xml',
        #
		'wizard/wizard_hr_report_view.xml',
        'hr_department_view.xml',
       
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
