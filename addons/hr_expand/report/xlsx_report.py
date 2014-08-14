# -*- coding: utf-8 -*- 
from xlsxwriter.workbook import Workbook
import base64 
import os
from openerp.osv import osv, fields
import glob
import time
from datetime import datetime

class xlsx_report(osv.osv):
    _name='xlsx.report'
    
    def add_cell(self,cr,uid,ids,merge_cell,wb,ws,data,format,context=None):
        bold= format['bold']
        italic= format['italic']
        border=format['border']
        align=format['align']
        valign=format['valign']
        fontsize=format['fontsize']
        fontname=format['fontname']
        text_wrap=format['text_wrap']
        merge_format = wb.add_format({
                    'bold':bold,
                    'italic':italic,
                    'border':border,
                    'align':align,
                    'valign': valign,
                    'text_wrap':text_wrap,})
        merge_format.set_font_size(fontsize)
        merge_format.set_font_name(fontname)
        ws.merge_range(merge_cell,data, merge_format)
    
    def write_cell(self,cr,uid,ids,cell,wb,ws,data,format,context=None):
        bold= format['bold']
        italic= format['italic']
        border=format['border']
        align=format['align']
        valign=format['valign']
        fontsize=format['fontsize']
        fontname=format['fontname']
        text_wrap=format['text_wrap']
        format = wb.add_format({
                    'bold':bold,
                    'italic':italic,
                    'border':border,
                    'align':align,
                    'valign': valign,
                    'text_wrap':text_wrap,})
        format.set_font_size(fontsize)
        format.set_font_name(fontname)
        ws.write(cell, data,format)
   
    def add_cell_with_colour(self,cr,uid,ids,merge_cell,wb,ws,data,format,context=None):
        bold= format['bold']
        italic= format['italic']
        border=format['border']
        align=format['align']
        valign=format['valign']
        fontsize=format['fontsize']
        fontname=format['fontname']
        text_wrap=format['text_wrap']
        merge_format = wb.add_format({
                    'bold':bold,
                    'italic':italic,
                    'border':border,
                    'align':align,
                    'valign': valign,
                    'text_wrap':text_wrap,})
        merge_format.set_font_size(fontsize)
        merge_format.set_font_name(fontname)
        merge_format.set_pattern(1)  
        merge_format.set_bg_color('yellow')
        ws.merge_range(merge_cell,data, merge_format)
    