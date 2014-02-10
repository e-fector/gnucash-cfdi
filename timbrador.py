# encoding: utf-8

from facturacion_moderna import facturacion_moderna
from datetime import datetime
import base64
import os

debug = False

import gnucash
from gnucash.gnucash_business import Customer, Employee, Vendor, Job, \
    Address, Invoice, Entry, TaxTable, TaxTableEntry, BillTerm

from factura import Factura
from mail import mail

input_url = "./gnucash/prueba.gnucash"
#session = Session('mysql://USER:PASSWORD <at> localhost/gnucash')

try:
    session = gnucash.Session(input_url,ignore_lock=True)
except Exception as exception:
    print "Problem opening input."
    print exception

import sys
import getpass
sys.stdout.write("Folio de factura a timbrar:")
id_factura =  raw_input().lower()


factura = session.book.InvoiceLookupByID(id_factura)

registro = Factura()


#emisor
#conf.agrega_cta_pago(factura.GetOwner().GetAddr().GetFax())
#conf.agrega_metodo_de_pago(factura.GetOwner().GetNotes())

#receptor
registro.edita_receptor_nombre_fiscal(factura.GetOwner().GetName())
registro.edita_receptor_calle(factura.GetOwner().GetAddr().GetAddr1())
registro.edita_receptor_colonia(factura.GetOwner().GetAddr().GetAddr2())
registro.edita_receptor_municipio(factura.GetOwner().GetAddr().GetAddr3())   
registro.edita_rfc_receptor(factura.GetOwner().GetAddr().GetAddr4())
registro.edita_receptor_email(factura.GetOwner().GetAddr().GetEmail())
registro.edita_receptor_pais("Mexico")

#print dir(factura)
from datetime import datetime
fecha = factura.GetDatePosted()
registro.edita_factura_fecha_factura(datetime(fecha.year,
                                     fecha.month, 
                                     fecha.day).isoformat())


registro.edita_encabezado_notas(factura.GetNotes())
registro.edita_encabezado_condiciones(factura.GetTerms().GetName())
registro.edita_encabezado_forma_de_pago(factura.GetOwner().GetAddr().GetPhone())
registro.edita_encabezado_NumCtaPago(factura.GetOwner().GetAddr().GetFax())
registro.edita_receptor_noCliente(factura.GetOwner().GetID())
#print factura.GetBillingID()

for concepto in factura.GetEntries():
    concepto = Entry(instance=concepto)

    cantidad=str(gnucash.GncNumeric(instance=concepto.GetQuantity()))
    valorUnitario=str(gnucash.GncNumeric(instance=concepto.GetInvPrice()))

    registro.agrega_linea(
        unidad=concepto.GetAction(),
        noIdentificacion=concepto.GetDescription(),
        descripcion=concepto.GetDescription(),
        cantidad=cantidad,
        valorUnitario=valorUnitario,
        importe=str(float(cantidad) * float(valorUnitario))
        )

registro.edita_encabezado_subtotal(str(eval("1.0*"+factura.GetTotalSubtotal().to_string())))
registro.edita_encabezado_total(str(eval("1.0*"+factura.GetTotal().to_string())))

registro.edita_impuesto("IVA")
registro.edita_importe_impuesto(str(eval("1.0*"+factura.GetTotalTax().to_string())))
registro.edita_impuesto_tasa("16.00")
        
# RFC utilizado para el ambiente de pruebas
rfc_emisor = registro.emisor["emisor_rfc"]

# Datos de acceso al ambiente de pruebas
url_timbrado = "https://t1demo.facturacionmoderna.com/timbrado/wsdl"
user_id = "UsuarioPruebasWS";
user_password = "b9ec2afa3361a59af4b4d102d3f704eabdf097d4"

cfdi = str(registro)

params = {'emisorRFC': rfc_emisor, 'UserID': user_id, 'UserPass': user_password}
options = {'generarCBB': True, 'generarPDF': True, 'generarTXT': True}
cliente = facturacion_moderna.Cliente(url_timbrado, params, False)

if debug == True:
    factura.SetNotes("")

if factura.GetNotes().find("noCertificadoSAT") > 0 and not factura.IsPosted():
    print "FACTURA YA TIMBRADA"
    exit(0)

if cliente.timbrar(cfdi, options):
  folder = 'comprobantes'
  if not os.path.exists(folder): os.makedirs(folder)
  comprobante = os.path.join(folder, cliente.uuid)
  for extension in ['xml', 'pdf', 'png', 'txt']:
    if hasattr(cliente, extension):
      with open(("%s.%s" % (comprobante, extension)), 'w') as f: f.write(getattr(cliente, extension))
      print("%s almacenado correctamente en %s.%s" % (extension.upper(), comprobante, extension))
  print 'Timbrado exitoso'
  os.popen("./run_viewer.sh "+comprobante+".pdf")
  print "Preparando para mandar por correo"


  info = open(comprobante + ".txt","r")
  txt = ""
  for line in info:
      txt += line

  
  factura.SetNotes(factura.GetNotes() + "\n" + txt)
  session.save()
  try:
      email_a_mandar = str(registro.receptor["email"])
  
      correo_env = mail(email_a_mandar,
                        "Factura electronica (%s)" % id_factura,
                        "A continuacion anexamos nuestra factura electronica. ",
                        comprobante+".pdf",
                        comprobante+".xml")
      print str(correo_env)

  except Exception as e:
      print str(e)
      print "Correo no enviado"

  print "Programa finalizado"
  

else:
  print("[%s] - %s" % (cliente.codigo_error, cliente.error))
