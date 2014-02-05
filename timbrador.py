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

import config
input_url = config.archivo

try:
    session = gnucash.Session(input_url,ignore_lock=True)
except Exception as exception:
    print "Problem opening input."
    print exception

factura = session.book.InvoiceLookupByID("125")

#emisor
print dir(session)

#receptor
print factura.GetOwner().GetName()
print factura.GetOwner().GetAddr().GetAddr1()   
print factura.GetOwner().GetAddr().GetAddr2()   
print factura.GetOwner().GetAddr().GetAddr3()   
print factura.GetOwner().GetAddr().GetAddr4()   
print factura.GetOwner().GetAddr().GetEmail()   

#print dir(factura)
print factura.GetNotes()
print factura.GetTotalTax()
print factura.GetTotalSubtotal()
print factura.GetTotal()
print factura.GetTerms().GetName()

for concepto in factura.GetEntries():
    www = Entry(instance=concepto)
    print www.GetAction()
    print www.GetDescription()
    print gnucash.GncNumeric(instance=www.GetQuantity())
    print gnucash.GncNumeric(instance=www.GetInvPrice())
    print www.GetInvTaxIncluded()
    print TaxTable(instance=www.GetInvTaxTable())
    print www.GetInvTaxable()
    print www.GetNotes()
    print www.GetOrder()
    #print dir(www)
    print gnucash.GncNumeric(instance=www.ReturnTaxValue(www.GetInvTaxable()))
    print gnucash.GncNumeric(instance=www.ReturnValue(www.GetInvTaxable()))

    
    
    

print "Y así empieza"
