# encoding: utf-8

from facturacion_moderna import facturacion_moderna
from datetime import datetime
import base64
from M2Crypto import RSA
from lxml import etree as ET
import sha
import os
import re

import gnucash
from gnucash.gnucash_business import Customer, Employee, Vendor, Job, \
    Address, Invoice, Entry, TaxTable, TaxTableEntry, BillTerm

from factura import Factura

input_url = "./gnucash/prueba.gnucash"

try:
    session = gnucash.Session(input_url,ignore_lock=True)
except Exception as exception:
    print "Problem opening input."
    print exception

factura = session.book.InvoiceLookupByID("125")

registro = Factura()


#emisor
#conf.agrega_cta_pago(factura.GetOwner().GetAddr().GetFax())
#conf.agrega_metodo_de_pago(factura.GetOwner().GetNotes())

#receptor
print factura.GetOwner().GetName()
print factura.GetOwner().GetAddr().GetAddr1()   
print factura.GetOwner().GetAddr().GetAddr2()   
print factura.GetOwner().GetAddr().GetAddr3()   
registro.edita_rfc_receptor(factura.GetOwner().GetAddr().GetAddr4())
print factura.GetOwner().GetAddr().GetEmail()   

#print dir(factura)
fecha = factura.GetDatePosted()
registro.edita_factura_fecha_factura(fecha.isoformat())

print factura.GetNotes()
print factura.GetTotalTax()
print factura.GetTotalSubtotal()
print factura.GetTotal()
registro.edita_encabezado_condiciones(factura.GetTerms().GetName())

for concepto in factura.GetEntries():
    concepto = Entry(instance=concepto)
    registro.agrega_linea(
        cantidad=gnucash.GncNumeric(instance=concepto.GetQuantity()),
        unidad=concepto.GetAction(),
        noIdentificacion="N/D",
        descripcion=concepto.GetDescription(),
        valorUnitario=gnucash.GncNumeric(instance=concepto.GetInvPrice()),
        importe="importe",
        impuesto=gnucash.GncNumeric(instance=concepto.ReturnTaxValue(concepto.GetInvTaxable())),
        importe_impuesto=concepto.GetInvTaxIncluded(),
        tasa=TaxTable(instance=concepto.GetInvTaxTable())
        )
    #print 
    #print gnucash.GncNumeric(instance=www.ReturnValue(www.GetInvTaxable()))

    
    
    
#from genera_layout import genera_layout
#print genera_layout(registro.encabezado, registro.receptor, registro.factura, \
#                        registro.lineas_factura, registro.emisor)
print registro
