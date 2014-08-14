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


class general_report_employee(osv.osv):
    _name='general.report.employee'
    def export_2_excel(self, cr, uid,ids,filepath,data, context=None):
        
        #init excel
        full_path = os.path.realpath(__file__)
        folder_path= os.path.dirname(full_path)
        workbook = Workbook(filepath)
        worksheet = self.init_ws_excel(cr,uid,ids,workbook,context)
        #end init
        
        # data heading
        if "Linux" in platform.system():
            document = ElementTree.parse( folder_path+'/general_report.xml' )
        else:
            document = ElementTree.parse( folder_path+'\general_report.xml' )
        self.excel_heading_title(cr, uid, ids, workbook, worksheet, document,data, context)
        self.excel_heading_table(cr, uid, ids, workbook, worksheet, document, context)
        self.excel_table_data(cr, uid, ids, workbook, worksheet,data, context)
        workbook.close()
        
    def init_ws_excel(self,cr,uid,ids,wb,context=None):
        worksheet = wb.add_worksheet('BM01')
        worksheet.set_column('A:A', 6)
        worksheet.set_column('B:B', 17)
        worksheet.set_column('C:C', 4)
        worksheet.set_column('D:D', 4)
        worksheet.set_column('E:E', 4)
        worksheet.set_column('F:F', 4)
        worksheet.set_column('G:G', 4)
        worksheet.set_column('H:H', 4)
        worksheet.set_column('I:I', 4)
        worksheet.set_column('J:J', 4)
        worksheet.set_column('K:K', 4)
        worksheet.set_column('L:L', 7)
        worksheet.set_column('M:M', 4)
        worksheet.set_column('N:N', 4)
        
        worksheet.set_column('O:O', 4)
        worksheet.set_column('P:P', 4)
        worksheet.set_column('Q:Q', 4)
        worksheet.set_column('R:R', 4)
        worksheet.set_column('S:S', 4)
        worksheet.set_column('T:T', 4)
        worksheet.set_column('U:U', 4)
        worksheet.set_column('V:V', 4)
        worksheet.set_column('W:W', 4)
        worksheet.set_column('X:X', 4)
        worksheet.set_column('Y:Y', 4)
        worksheet.set_column('Z:Z', 4)
        
        worksheet.set_column('AA:AA', 4)
        worksheet.set_column('AB:AB', 4)
        worksheet.set_column('AC:AC', 4)
        worksheet.set_column('AD:AD', 4)
        worksheet.set_column('AE:AE', 4)
        worksheet.set_column('AF:AF', 4)
        worksheet.set_column('AG:AG', 4)
        worksheet.set_column('AH:AH', 4)
        worksheet.set_column('AI:AI', 4)
        worksheet.set_column('AJ:AJ', 4)
        worksheet.set_column('AK:AK', 4)
        worksheet.set_column('AL:AL', 4)
        
        worksheet.set_column('AM:AM', 4)
        worksheet.set_column('AN:AN', 4)
        worksheet.set_column('AO:AO', 4)
        worksheet.set_column('AP:AP', 4)
        worksheet.set_column('AQ:AQ', 4)
        worksheet.set_column('AR:AR', 6)
        worksheet.set_column('AS:AS', 6)
        worksheet.set_column('AT:AT', 6)
        worksheet.set_column('AU:AU', 6)
        worksheet.set_column('AV:AV', 6)
       
        worksheet.set_row(10, 40)
        worksheet.set_row(11, 30)
        
        worksheet.set_margins(0.1,0.1,0.1,0.1)
        worksheet.set_landscape()
        return worksheet

    def excel_heading_title(self,cr,uid,ids,workbook,worksheet,document,data,context=None):
        
        date_end= data['form']['date_end']
        datetime.strptime('2011-03-07','%Y-%m-%d')
        date_end_format=time.strftime('%d/%m/%Y',time.strptime(date_end,'%Y-%m-%d')) 
        heading1= document.findall( 'heading1/heading1' )[0]
        datahd1= heading1.attrib[ 'name' ]
        heading2= document.findall( 'heading2/heading2' )[0]
        datahd2= heading2.attrib[ 'name' ]
        heading3= document.findall( 'heading3/heading3' )[0]
        datahd3= heading3.attrib[ 'name' ]+ ' '+ date_end_format
        heading4= document.findall( 'heading4/heading4' )[0]
        datahd4= heading4.attrib[ 'name' ]
        # end data heading
        format={'bold':1,'border':0,'italic':0,'text_wrap':1,'align':'center','valign':'vcenter','fontsize':16,'fontname':'Times New Roman'}
        xlsx_report_obj=self.pool.get('xlsx.report')
        xlsx_report_obj.add_cell(cr,uid,ids,'A2:I2',workbook,worksheet,datahd1,format,context)
        xlsx_report_obj.add_cell(cr,uid,ids,'A4:AT4',workbook,worksheet,datahd2,format,context)
        format={'bold':1,'border':0,'italic':1,'text_wrap':1,'align':'center','valign':'vcenter','fontsize':16,'fontname':'Times New Roman'}
        xlsx_report_obj.add_cell(cr,uid,ids,'A5:AT5',workbook,worksheet,datahd3,format,context)
        format2={'bold':1,'border':1,'italic':0,'text_wrap':1,'align':'center','valign':'vcenter','fontsize':12,'fontname':'Times New Roman'}
        xlsx_report_obj.write_cell(cr,uid,ids,'B16',workbook,worksheet,datahd4,format2,context)
    def excel_heading_table(self,cr,uid,ids,workbook,worksheet,document,context=None):
        xlsx_report_obj=self.pool.get('xlsx.report')
        format={'bold':1,'border':1,'italic':0,'text_wrap':1,'align':'center','valign':'vcenter','fontsize':8,'fontname':'Times New Roman'}
        for i in range (1,60):
            table_heading= 'table/heading'+str(i)
            hdtable= document.findall( table_heading )[0]
            data_table_deading= hdtable.attrib[ 'name' ]
            cell_table_heading= 'table/heading'+str(i)+'/cellheading'+str(i)
            cellhdtable= document.findall( cell_table_heading )[0]
            data_cell = cellhdtable.attrib[ 'name' ]
            xlsx_report_obj.add_cell(cr,uid,ids,data_cell,workbook,worksheet,data_table_deading,format,context)
        
    def get_department(self,cr,uid,ids,company_id,context=None):
        rec=[]
        result=[]
        cr.execute("select id,name from hr_department where id  in (select distinct department_id from hr_job_m where  company_id="+str(company_id)+" ) ORDER BY sequence ASC ")
        rec=cr.dictfetchall()
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
        
    def excel_table_data(self,cr,uid,ids,workbook,worksheet,data,context=None):
        format={'bold':1,'border':1,'italic':0,'text_wrap':1,'align':'left','valign':'vcenter','fontsize':8,'fontname':'Times New Roman'}
        format1={'bold':1,'border':1,'italic':0,'text_wrap':1,'align':'center','valign':'vcenter','fontsize':8,'fontname':'Times New Roman'}
        company_id= data['form']['company_id']
       
        department = self.get_department(cr, uid, ids,company_id, context)
        xlsx_report_obj=self.pool.get('xlsx.report')
        count=1
        for rec in department:
            depid=rec['id']
            seq= rec['number']
            depname= rec['name']
            cellbegin= 16+count
            cell1= 'A'+str(cellbegin)
            xlsx_report_obj.write_cell(cr,uid,ids,cell1,workbook,worksheet,seq,format1,context)
            cell2= 'B'+str(cellbegin)
            xlsx_report_obj.write_cell(cr,uid,ids,cell2,workbook,worksheet,depname,format,context)
            cell3='C'+str(cellbegin)
            qty1=self.count_employee_department(cr, uid, ids, depid, context)
            xlsx_report_obj.write_cell(cr,uid,ids,cell3,workbook,worksheet,qty1,format1,context)
            cell4='D'+str(cellbegin)
            qty2=self.getQtyGender(cr, uid, ids, depid, 'male')
            xlsx_report_obj.write_cell(cr,uid,ids,cell4,workbook,worksheet,qty2,format1,context)
            cell5='E'+str(cellbegin)
            qty3=self.getQtyGender(cr, uid, ids, depid, 'female')
            xlsx_report_obj.write_cell(cr,uid,ids,cell5,workbook,worksheet,qty3,format1,context)
            
            
            
            cell6='F'+str(cellbegin)
            qty6=self.getQtyByCP(cr, uid, ids, depid,'male')
            xlsx_report_obj.write_cell(cr,uid,ids,cell6,workbook,worksheet,qty6,format1,context)
            cell7='G'+str(cellbegin)
            qty7=self.getQtyByCP(cr, uid, ids, depid,'female')
            xlsx_report_obj.write_cell(cr,uid,ids,cell7,workbook,worksheet,qty7,format1,context)
            
            # Tinh trang hop dong
            cell8='H'+str(cellbegin)
            qty8=self.getQtyByContract(cr, uid, ids, depid, 1) # thoi vu
            xlsx_report_obj.write_cell(cr,uid,ids,cell8,workbook,worksheet,qty8,format1,context)
            cell9='I'+str(cellbegin)
            qty9=self.getQtyByContract(cr, uid, ids, depid, 2) # thu viec
            xlsx_report_obj.write_cell(cr,uid,ids,cell9,workbook,worksheet,qty9,format1,context)
            cell10='J'+str(cellbegin)
            qty10=self.getQtyByContract(cr, uid, ids, depid, 3) # duoi 1 nam
            xlsx_report_obj.write_cell(cr,uid,ids,cell10,workbook,worksheet,qty10,format1,context)
            cell11='K'+str(cellbegin)
            qty11=self.getQtyByContract(cr, uid, ids, depid, 4) # 1-3 nam
            xlsx_report_obj.write_cell(cr,uid,ids,cell11,workbook,worksheet,qty11,format1,context)
            cell12='L'+str(cellbegin)
            qty12=self.getQtyByContract(cr, uid, ids, depid, 5) # Khong XDTH
            xlsx_report_obj.write_cell(cr,uid,ids,cell12,workbook,worksheet,qty12,format1,context)
            # end
            
            # Ket cau theo do tuoi
            
            cell13='M'+str(cellbegin)
            qty13=self.getQtyByBirthday(cr, uid, ids, depid, 18, 30) # 18-30
            xlsx_report_obj.write_cell(cr,uid,ids,cell13,workbook,worksheet,qty13,format1,context)
            cell14='N'+str(cellbegin)
            qty14=self.getQtyByBirthday(cr, uid, ids, depid, 31, 45) # 18-30
            xlsx_report_obj.write_cell(cr,uid,ids,cell14,workbook,worksheet,qty14,format1,context)
            cell15='O'+str(cellbegin)
            qty15=self.getQtyByBirthday(cr, uid, ids, depid, 46, 60) # 46-60
            xlsx_report_obj.write_cell(cr,uid,ids,cell15,workbook,worksheet,qty15,format1,context)
            cell16='P'+str(cellbegin)
            qty16=self.getQtyByBirthday(cr, uid, ids, depid, 60,'') # >60
            xlsx_report_obj.write_cell(cr,uid,ids,cell16,workbook,worksheet,qty16,format1,context)
            # end 
            
            
            # BHXXH
            cell17='Q'+str(cellbegin)
            qty17=self.getQtyByInsurance(cr, uid, ids, depid, 'male')
            xlsx_report_obj.write_cell(cr,uid,ids,cell17,workbook,worksheet,qty17,format1,context)
            cell18='R'+str(cellbegin)
            qty18=self.getQtyByInsurance(cr, uid, ids, depid, 'female')
            xlsx_report_obj.write_cell(cr,uid,ids,cell18,workbook,worksheet,qty18,format1,context)
            # end
            
            # Trinh do chuyen mon
            
                #    Tren dai hoc
            cell19='S'+str(cellbegin)
            qty19=self.getQtyByMajor(cr, uid, ids, depid, 'tdh', 'male')
            xlsx_report_obj.write_cell(cr,uid,ids,cell19,workbook,worksheet,qty19,format1,context)
            cell20='T'+str(cellbegin)
            qty20=self.getQtyByMajor(cr, uid, ids, depid, 'tdh', 'female')
            xlsx_report_obj.write_cell(cr,uid,ids,cell20,workbook,worksheet,qty20,format1,context)
                #    end
            cell21='U'+str(cellbegin)
            qty21=self.getQtyByMajor(cr, uid, ids, depid, 'dh', 'male')
            xlsx_report_obj.write_cell(cr,uid,ids,cell21,workbook,worksheet,qty21,format1,context)
            cell22='V'+str(cellbegin)
            qty22=self.getQtyByMajor(cr, uid, ids, depid, 'dh', 'female')
            xlsx_report_obj.write_cell(cr,uid,ids,cell22,workbook,worksheet,qty22,format1,context)
                #    Dai hoc
            cell23='W'+str(cellbegin)
            qty23=self.getQtyByMajor_1(cr, uid, ids, depid, 3) # NT
            xlsx_report_obj.write_cell(cr,uid,ids,cell23,workbook,worksheet,qty23,format1,context)
            cell24='X'+str(cellbegin)
            qty24=self.getQtyByMajor_1(cr, uid, ids, depid, 3) # TM
            xlsx_report_obj.write_cell(cr,uid,ids,cell24,workbook,worksheet,qty24,format1,context)  
            cell25='Y'+str(cellbegin)
            qty25=self.getQtyByMajor_1(cr, uid, ids, depid, 3) # KTQD
            xlsx_report_obj.write_cell(cr,uid,ids,cell25,workbook,worksheet,qty25,format1,context) 
            cell26='Z'+str(cellbegin)
            qty26=self.getQtyByMajor_1(cr, uid, ids, depid, 3) # HVTC
            xlsx_report_obj.write_cell(cr,uid,ids,cell26,workbook,worksheet,qty26,format1,context) 
            cell27='AA'+str(cellbegin)
            qty27=self.getQtyByMajor_1(cr, uid, ids, depid, 3) # Kỹ thuật
            xlsx_report_obj.write_cell(cr,uid,ids,cell27,workbook,worksheet,qty27,format1,context) 
            cell28='AB'+str(cellbegin)
            qty28=self.getQtyByMajor_1(cr, uid, ids, depid, 3) # Ngoai ngu
            xlsx_report_obj.write_cell(cr,uid,ids,cell28,workbook,worksheet,qty28,format1,context) 
            cell29='AC'+str(cellbegin)
            qty29=self.getQtyByMajor_1(cr, uid, ids, depid, 3) # Luat
            xlsx_report_obj.write_cell(cr,uid,ids,cell29,workbook,worksheet,qty29,format1,context)
            cell30='AD'+str(cellbegin)
            qty30=self.getQtyByMajor_1(cr, uid, ids, depid, 3) # Khac
            xlsx_report_obj.write_cell(cr,uid,ids,cell30,workbook,worksheet,qty30,format1,context) 
            
                #    end
                #    Cao dang, trung cap
            cell31='AE'+str(cellbegin)
            qty31=self.getQtyByMajor(cr, uid, ids, depid, 'cd', 'male')+self.getQtyByMajor(cr, uid, ids, depid, 'tc', 'male')
            xlsx_report_obj.write_cell(cr,uid,ids,cell31,workbook,worksheet,qty31,format1,context)
            cell32='AF'+str(cellbegin)
            qty32=self.getQtyByMajor(cr, uid, ids, depid, 'cd', 'female')+self.getQtyByMajor(cr, uid, ids, depid, 'tc', 'female')
            xlsx_report_obj.write_cell(cr,uid,ids,cell32,workbook,worksheet,qty32,format1,context)
                
                #    end
                
                #    Cao đang
            cell33='AG'+str(cellbegin)
            qty33=self.getQtyByMajor_2(cr, uid, ids, depid, 'cd')
            xlsx_report_obj.write_cell(cr,uid,ids,cell33,workbook,worksheet,qty33,format1,context)
            cell34='AH'+str(cellbegin)
            qty34=self.getQtyByMajor_2(cr, uid, ids, depid, 'tc')
            xlsx_report_obj.write_cell(cr,uid,ids,cell34,workbook,worksheet,qty34,format1,context)
            cell35='AI'+str(cellbegin)
            qty35=self.getQtyByMajor_2(cr, uid, ids, depid, 'cnkt')
            xlsx_report_obj.write_cell(cr,uid,ids,cell35,workbook,worksheet,qty35,format1,context)
            cell36='AJ'+str(cellbegin)
            qty36=self.getQtyByMajor_2(cr, uid, ids, depid, 'ldpt')
            xlsx_report_obj.write_cell(cr,uid,ids,cell36,workbook,worksheet,qty36,format1,context)
            #    end cao dang, trung cap
            # Trinh do ngoai ngu
            cell37='AK'+str(cellbegin)
            qty37=self.getQtyByMajor_3(cr, uid, ids, depid,'A')
            xlsx_report_obj.write_cell(cr,uid,ids,cell37,workbook,worksheet,qty37,format1,context)
            cell38='AL'+str(cellbegin)
            qty38=self.getQtyByMajor_3(cr, uid, ids, depid,'B')
            xlsx_report_obj.write_cell(cr,uid,ids,cell38,workbook,worksheet,qty38,format1,context)
            cell39='AM'+str(cellbegin)
            qty39=self.getQtyByMajor_3(cr, uid, ids, depid,'C')
            xlsx_report_obj.write_cell(cr,uid,ids,cell39,workbook,worksheet,qty39,format1,context)
            #end
            
            # Ly luan chinh tri
            cell40='AN'+str(cellbegin)
            qty40=self.getQtyByMajor_4(cr, uid, ids, depid, 'sc')
            xlsx_report_obj.write_cell(cr,uid,ids,cell40,workbook,worksheet,qty40,format1,context)
            cell41='AO'+str(cellbegin)
            qty41=self.getQtyByMajor_4(cr, uid, ids, depid, 'tc')
            xlsx_report_obj.write_cell(cr,uid,ids,cell41,workbook,worksheet,qty41,format1,context)
            cell42='AP'+str(cellbegin)
            qty42=self.getQtyByMajor_4(cr, uid, ids, depid, 'cc')
            xlsx_report_obj.write_cell(cr,uid,ids,cell42,workbook,worksheet,qty42,format1,context)
            # end
            
            # Dieu dong, bo nhiem
            date_start= data['form']['date_start']
            date_end= data['form']['date_end']
            cell43='AQ'+str(cellbegin)
            qty43=self.getQtyByWork(cr, uid, ids, depid,'dd' ,date_start, date_end)
            xlsx_report_obj.write_cell(cr,uid,ids,cell43,workbook,worksheet,qty43,format1,context)
            cell44='AR'+str(cellbegin)
            qty44=self.getQtyByWork(cr, uid, ids, depid,'bn' ,date_start, date_end)
            xlsx_report_obj.write_cell(cr,uid,ids,cell44,workbook,worksheet,qty44,format1,context)
            cell45='AS'+str(cellbegin)
            qty45=self.getQtyByWork(cr, uid, ids, depid,'tm' ,date_start, date_end)
            xlsx_report_obj.write_cell(cr,uid,ids,cell45,workbook,worksheet,qty45,format1,context)
            cell46='AT'+str(cellbegin)
            qty46=self.getQtyByWork(cr, uid, ids, depid,'cd' ,date_start, date_end)
            xlsx_report_obj.write_cell(cr,uid,ids,cell46,workbook,worksheet,qty46,format1,context)
            # end
            count=count+1
    
    def count_employee_department(self,cr,uid,ids,depid,context=None):
        rec=[]
        cr.execute("SELECT count( distinct  id) as qty FROM hr_job_m where department_id="+str(depid))
        rec=cr.dictfetchall()
        return rec[0]['qty']
    def getQtyGender(self,cr,uid,ids,depid,gender):
        rec=[]
        cr.execute("SELECT count( distinct  id) as qty  FROM hr_employee where gender='"+gender+"' and id in (select employee_id from hr_job_m where department_id="+str(depid)+")")
        rec=cr.dictfetchall()
        return rec[0]['qty']
    def getQtyByInsurance(self,cr,uid,ids,depid,gender):
        rec=[]
        cr.execute("SELECT count( distinct  id) as qty  FROM hr_employee where gender='"+gender+"' and sinid is not null and id in (select employee_id from hr_job_m where department_id="+str(depid)+")")
        rec=cr.dictfetchall()
        return rec[0]['qty']
    def getQtyByCP(self,cr,uid,ids,depid,gender):
        rec=[]
        cr.execute("SELECT count( distinct  id) as qty  FROM hr_employee where gender='"+gender+"' and "'"CP_join_date"'" is not null and "'"CP_official_join_date"'" is not null and id in (select employee_id from hr_job_m where department_id="+str(depid)+")")
        rec=cr.dictfetchall()
        return rec[0]['qty']
    def getQtyByContract(self,cr,uid,ids,depid,contract_id):
        rec=[]
        cr.execute("select count(employee_id) as qty from hr_contract where  employee_id in (select employee_id from hr_job_m where department_id="+str(depid)+") and   type_id = "+str(contract_id)+" ")
        rec=cr.dictfetchall()
        return rec[0]['qty']
    def getQtyByBirthday(self,cr,uid,ids,depid,from_year,to_year):
        rec=[]
        if(to_year!=''):
            cr.execute( "select count(birthday) as qty from hr_employee where  id in (select employee_id from hr_job_m where department_id="+str(depid)+") and (date_part('year',NOW())-date_part('year', birthday))>="+str(from_year)+"and (date_part('year',NOW())-date_part('year', birthday))<="+str(to_year))
        else:
            cr.execute( "select count(birthday) as qty from hr_employee where  id in (select employee_id from hr_job_m where department_id="+str(depid)+") and (date_part('year',NOW())-date_part('year', birthday))>="+str(from_year))
        rec=cr.dictfetchall()
        return rec[0]['qty']
    def getQtyByMajor(self,cr,uid,ids,depid,level_school,gender):
        rec=[]
        cr.execute("select count( distinct employee_id) as qty from hr_training \
         where level_school='"+str(level_school)+"'\
          and employee_id in (select id from hr_employee where gender ='"+str(gender)+"') \
           and employee_id in (select employee_id from hr_job_m where department_id="+str(depid)+")")
        rec=cr.dictfetchall()
        return rec[0]['qty']  
    def getQtyByMajor_1(self,cr,uid,ids,depid,school_id):
        rec=[]
        cr.execute("select count( distinct employee_id) as qty from hr_training \
         where level_school='dh'\
         and school ="+str(school_id)+" \
           and employee_id in (select employee_id from hr_job_m where department_id="+str(depid)+")")
        rec=cr.dictfetchall()
        return rec[0]['qty']
    def getQtyByMajor_2(self,cr,uid,ids,depid,level_school):
        rec=[]
        cr.execute("select count( distinct employee_id) as qty from hr_training \
         where level_school='"+str(level_school)+"'\
           and employee_id in (select employee_id from hr_job_m where department_id="+str(depid)+")")
        rec=cr.dictfetchall()
        return rec[0]['qty']    
    def getQtyByMajor_3(self,cr,uid,ids,depid,diploma_level):
        rec=[]
        cr.execute("SELECT count(distinct id) as qty \
          FROM hr_employee where foreign_language like '%"+str(diploma_level)+"' \
            and id in (select employee_id from hr_job_m where department_id="+str(depid)+")")
        rec=cr.dictfetchall()
        return rec[0]['qty']  
    def getQtyByMajor_4(self,cr,uid,ids,depid,political_theory):
        rec=[]
        cr.execute("SELECT count(distinct id) as qty \
          FROM hr_employee where political_theory = '"+str(political_theory)+"' \
            and id in (select employee_id from hr_job_m where department_id="+str(depid)+")")
        rec=cr.dictfetchall()
        return rec[0]['qty'] 
    def getQtyByWork(self,cr,uid,ids,depid,type_work,date_start,date_end):
        rec=[]
        sql="SELECT count(distinct employee_id) as qty \
                      FROM hr_work_history where  \
                        type_work= '"+str(type_work)+"' and \
                        employee_id in (select employee_id from hr_job_m where department_id="+str(depid)+") and \
                        date between '"+str(date_start)+"' and '"+str(date_end)+"'"
        cr.execute(sql)
        rec=cr.dictfetchall()
        return rec[0]['qty']  
    