# -*- coding: iso-8859-15 -*-
#Importaciones
import os
import glob
import smtplib
import doctest
import textwrap
from gdata.youtube.data import YtPlaylistId
#from suds.sudsobject import Facade

def f1(self,x,y):
    return x,y

class core_generic:
    
    ##Constructor
    def __init__(self, initiate,finaly):
        self.initiate = initiate
        self.finaly   = finaly
        self.metho=f1(self,self.initiate,self.finaly)
        self.core_finaly()
        
        #print dir(os)
        #print glob.glob('*.py')
        
    def core_initiates(self):
        doct="""El método wrap() es como fill(), excepto que devuelve
                una lista de strings en lugar de una gran string con saltos de
                línea como separadores.
             """
        #print textwrap.fill(doct, width=40)
        return

    def core_finaly(self):
        self.core_initiates()
        return

f=core_generic(10,9)
#f.core_finaly()
#doctest.testmod()

#te={'uno':1,'dos':3,'tres':3}
#print te
#tr=te.keys()
#print tr
#lista=['uno']

#for seq in lista:
#    if seq in tr:
#        print 'ttt'
from datetime import date
import datetime
import time
from datetime import datetime, timedelta
import time

#fac='001-010-000000001'
#print fac
#print fac.split('-')[1]
#fr=fr.replace('-','/')
#print fr[:10]
#tr=datetime.datetime(*time.strptime(fr[:10],"%Y/%m/%d")[0:5])
#tr=tr.strftime('%Y-%m-%d')
#print tr
#print type(tr)
#print
def process_date_format(fecha, context):
    dates_str=''
    for formate in ['%Y-%m-%d %H:%M:%S','%Y/%m/%d %H:%M:%S','%d/%m/%Y %H:%M:%S','%m/%d/%Y %H:%M:%S']:
        try:
            dates_str=fecha
            if(not context):##Especifica Fecha Normal               
                for format_date in ['%Y-%m-%d','%d-%m-%Y','%m-%d-%Y','%Y/%m/%d','%d/%m/%Y','%m/%d/%Y']:
                    try:
                        dt_obj = datetime.strptime(dates_str,format_date)
                        dt_obj = dt_obj.strftime(format_date)
                        return dt_obj
                    except:
                        pass
            elif(context):
                dt_obj = datetime.strptime(dates_str,formate)
                return dt_obj
        except:
            pass
    return True

tr=time.strftime('%Y-%m-%d')
tr='2016-09-28 00:00:00'
di={'R':''}
#di={}
print len(tr)
print process_date_format(tr,di)


query="""
"""
#print query
##uu=uu.replace('select','')
query_edit=query.split(',')
dicty={}
conteo=0
for query_edit_lit in query_edit:
    query_edit_change=(query_edit_lit.strip()).split(' ')
    for lit in range(len(query_edit_change)):
        #print query_edit_change
        if(query_edit_change[lit] in ('as',)):
            print query_edit_change[lit+1]
            dicty[conteo]=query_edit_change[lit+1]
            conteo+=1
            break
        else:
            pass
#print dicty

ytp={'date_invoice': '2016-07-08', 'nombre': 'QUIFATEX SA', 'partner_id': 8, 'id': 25, 'number': '001-010-000000011'}
print ytp
for index, col in ytp.items():
    print index
    print col
    
    
xml_d="""<detalleExportaciones>%
<tpIdClienteEx>{}</tpIdClienteEx>%
<idClienteEx>{}</idClienteEx>%
<parteRelExp>{}</parteRelExp>%
<tipoRegi>{}</tipoRegi>%
<paisEfecPagoParFis>{}</paisEfecPagoParFis>%
<paisEfecExp>{}</paisEfecExp>%
<exportacionDe>{}</exportacionDe>%
<tipIngExt>{}</tipIngExt>%
<ingExtGravOtroPais>{}</ingExtGravOtroPais>%
<tipoComprobante>{}</tipoComprobante>%
<fechaEmbarque>{}</fechaEmbarque>%
<valorFOB>{}</valorFOB>%
<valorFOBComprobante>{}</valorFOBComprobante>%
<establecimiento>{}</establecimiento>%
<puntoEmision>{}</puntoEmision>%
<secuencial>{}</secuencial>%
<autorizacion>{}</autorizacion>%
<fechaEmision>{}</fechaEmision>%
</detalleExportaciones>%
"""
text_tags=''
exe_result=['1','2','3','4','5','6','7','8','9','10','11','12','13']
fields_tags=xml_d.split('%')
print fields_tags
for data_seq in range(len(fields_tags)):
    if(fields_tags[data_seq].find('{}')!=-1):
        text_tags+=fields_tags[data_seq].replace('{}','')
    else:
        text_tags+=fields_tags[data_seq]
print text_tags

from decimal import *
import math
#"%.2f" %
value_round=(795.20*28.57/100)
#value_round=(270.54*16.67/100)
print value_round
#print 270.54 - float(value_round)
#re=Decimal(value_round).quantize(Decimal('0.09'))#-(Decimal(str(dic_cabezera['totalDescuento'])).quantize(Decimal('0.01'))
#print re
def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n
#print [truncate(value_round, n) for n in range(3)]                                                     


t=4.057224
p=round(t,2)
print p*140

l=567.9800
#print round(l,2)
print [truncate(t, n) for n in range(5)]




kkk= "-|8"
import re#[\w.%+-]|[\w.%+-]
if re.match("^[\w.%+-]{1}[^ \t\n\r\f\v]{1}[1-9]{1}$",kkk):#[1-9]
    print "siiiiiiiiiiiiiiiii"#[1-9]
print kkk.split('|')
if '|' in kkk.split('|'):
    print 'si'
    
import ast
dict_string={'estado':'sin_respuesta'}
print ast.literal_eval(str(dict_string))



import REPORT
html="""<html>
<body>
"""+REPORT.string_html()+"""
</form>
</html>"""

import webbrowser
import tempfile
path=tempfile.gettempdir()
path+='/'+'new_3'
def check_filestore(filestore):
    try:
        dir_path = os.path.dirname(filestore)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except OSError, e:
        print e
    return True
    
def save_file(name, b64_file):
    check_filestore(name)
    with open(name, 'w') as ofile:
        ofile.write(b64_file)
    return True

save_file(path,html)
webbrowser.open_new(path)


import os
#from win32com.client import Dispatch
#xl = Dispatch('Excel.Application')
#xl.Workbooks.Open('C:\Foo\Bar.xlsx')
#xl.Visible = True -- optional
#xl.Application.Run("SaveHTML")
#xl.Workbooks.Close
#import xlwt
 
#libro = xlwt.Workbook()

#saveFormat = libro.SaveFormat
#workbook = libro.Workbook(libro.dataDir + "Book1.xls")
#Save the document in PDF format
#workbook.save(libro.dataDir + "OutBook1.html", saveFormat.HTML)
# Print message
#print "\n Excel to HTML conversion performed successfully."