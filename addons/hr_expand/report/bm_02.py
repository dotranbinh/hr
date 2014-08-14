# -*- coding: utf-8 -*- 
from xlsxwriter.workbook import Workbook
import base64 
import os
from openerp.osv import osv, fields
import glob
import time
from datetime import datetime
from xml.etree import ElementTree
import platform
import os

class hr_bm_02(osv.osv):
    _name   =   'hr.bm.02'
    def export_2_excel(self, cr, uid,ids,filepath, context=None):
        
        #init excel
        full_path = os.path.realpath(__file__)
        folder_path= os.path.dirname(full_path)
        workbook = Workbook(filepath)
        worksheet = self.init_ws_excel(cr,uid,ids,workbook,context)
        #end init
        # data heading
        if "Linux" in platform.system():
            document = ElementTree.parse( folder_path+'/BM02.xml' )
        else:
            document = ElementTree.parse( folder_path+'\BM02.xml' )
        self.excel_heading_title(cr, uid, ids, workbook, worksheet, document, context)
        self.excel_heading_table(cr, uid, ids, workbook, worksheet, document, context)
        self.excel_table_data(cr, uid, ids, workbook, worksheet, context)
        
        workbook.close() 
      
    def init_ws_excel(self,cr,uid,ids,wb,context=None):
        worksheet = wb.add_worksheet('BM02')
        worksheet.set_column('A:A', 5)
        worksheet.set_column('B:B', 5)
        worksheet.set_column('C:C', 15)
        worksheet.set_column('D:D', 9)
        worksheet.set_column('E:E', 9)
        worksheet.set_column('F:F', 10)
        worksheet.set_column('G:G', 11)
        worksheet.set_column('H:H', 14)
        worksheet.set_column('I:I', 14)
        worksheet.set_column('J:J', 14)
        worksheet.set_column('K:K', 14)
        worksheet.set_column('L:L', 14)
        worksheet.set_column('M:M', 14)
        worksheet.set_column('N:N', 20)
        
        worksheet.set_column('O:O', 6)
        worksheet.set_column('P:P', 6)
        worksheet.set_column('Q:Q', 6)
        worksheet.set_column('R:R', 14)
        worksheet.set_column('S:S', 14)
        worksheet.set_column('T:T', 14)
        
        worksheet.set_row(5, 30)
        worksheet.set_row(10, 30)
        worksheet.set_row(11, 30)
        worksheet.set_row(12, 30)
        
        worksheet.set_margins(0.1,0.1,0.1,0.1)
        worksheet.set_landscape()
        return worksheet
    def excel_heading_title(self,cr,uid,ids,workbook,worksheet,document,context=None):
        heading1= document.findall( 'heading1/heading1' )[0]
        datahd1= heading1.attrib[ 'name' ]
        heading2= document.findall( 'heading2/heading2' )[0]
        datahd2= heading2.attrib[ 'name' ]
        heading3= document.findall( 'heading3/heading3' )[0]
        datahd3= heading3.attrib[ 'name' ]
       
        # end data heading
        format={'bold':1,'border':0,'italic':0,'text_wrap':1,'align':'center','valign':'vcenter','fontsize':10,'fontname':'Times New Roman'}
        xlsx_report_obj=self.pool.get('xlsx.report')
        xlsx_report_obj.add_cell(cr,uid,ids,'A1:E2',workbook,worksheet,datahd1,format,context)
        xlsx_report_obj.add_cell(cr,uid,ids,'A5:T5',workbook,worksheet,datahd2,format,context)
        format={'bold':1,'border':0,'italic':1,'text_wrap':1,'align':'center','valign':'vcenter','fontsize':10,'fontname':'Times New Roman'}
        xlsx_report_obj.add_cell(cr,uid,ids,'F6:P6',workbook,worksheet,datahd3,format,context)

    def excel_heading_table(self,cr,uid,ids,workbook,worksheet,document,context=None):
        xlsx_report_obj=self.pool.get('xlsx.report')
        format={'bold':1,'border':1,'italic':0,'text_wrap':1,'align':'center','valign':'vcenter','fontsize':8,'fontname':'Times New Roman'}
        for i in range (1,25):
            table_heading= 'table/heading'+str(i)
            hdtable= document.findall( table_heading )[0]
            data_table_deading= hdtable.attrib[ 'name' ]
            cell_table_heading= 'table/heading'+str(i)+'/cellheading'+str(i)
            cellhdtable= document.findall( cell_table_heading )[0]
            data_cell = cellhdtable.attrib[ 'name' ]
            xlsx_report_obj.add_cell(cr,uid,ids,data_cell,workbook,worksheet,data_table_deading,format,context)
    
    def get_employee_id(self,cr,uid,ids,seq,context=None):
        rec1=[]
        rec2=[]
        result=[]
        cr.execute("select id from hr_job_position where sequence > "+str(seq)+" order by sequence desc")
        rec1=cr.dictfetchall()
        i=1
        res={}
        for line in rec1:
            employee_id=  line['id']
            cr.execute("select employee_id from hr_job_m where job_position="+str(employee_id)+"")
            rec2=cr.dictfetchall()
            for line2 in rec2:
                res={}
                res['id']=line2['employee_id']
                result.append(res)
                i=i+1
        return result 
    
    def excel_table_data(self,cr,uid,ids,workbook,worksheet,context=None):
        format={'bold':1,'border':1,'italic':0,'text_wrap':1,'align':'left','valign':'vcenter','fontsize':8,'fontname':'Times New Roman'}
        listEmployee=self.get_employee_id(cr, uid, ids,45, context)
        xlsx_report_obj=self.pool.get('xlsx.report')
        count=1
        for rec in listEmployee:
            cellbegin= 13+count
            cell1= 'A'+str(cellbegin)
            xlsx_report_obj.write_cell(cr,uid,ids,cell1,workbook,worksheet,'',format,context)
            cell2= 'B'+str(cellbegin)
            xlsx_report_obj.write_cell(cr,uid,ids,cell2,workbook,worksheet,count,format,context)
            cell3='C'+str(cellbegin)
            xlsx_report_obj.write_cell(cr,uid,ids,cell3,workbook,worksheet,'Tran Binh Do',format,context)
            
            count+=1