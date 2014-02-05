# encoding: utf-8

from facturacion_moderna import facturacion_moderna
from datetime import datetime
import base64
from M2Crypto import RSA
from lxml import etree as ET
import sha
import os
import re

from mail import mail


from xml.dom.minidom import parse

import sys
import getopt

import gnucash
from gnucash.gnucash_business import Customer, Employee, Vendor, Job, \
    Address, Invoice, Entry, TaxTable, TaxTableEntry, GNC_AMT_TYPE_PERCENT, \
    GNC_DISC_PRETAX

input_url = "/home/sebastianavina/prueba.gnucash"

try:
    session = gnucash.Session(input_url,ignore_lock=True)
except Exception as exception:
    print "Problem opening input."
    print exception

factura = session.book.InvoiceLookupByID("124")

print factura.GetOwner().GetName()
print factura.GetOwner().GetAddr().GetAddr1()   
print factura.GetOwner().GetAddr().GetAddr2()   
print factura.GetOwner().GetAddr().GetAddr3()   
print factura.GetOwner().GetAddr().GetAddr4()   

#print dir(factura)

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
    print dir(www)
    print gnucash.GncNumeric(instance=www.ReturnTaxValue(www.GetInvTaxable()))
    print gnucash.GncNumeric(instance=www.ReturnValue(www.GetInvTaxable()))

    
    
    

print "Y así empieza"
