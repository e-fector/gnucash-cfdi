# encoding: utf-8

import config

def genera_layout(repector=None, factura=None, lineas_factura=[]):
  # se calcula la fecha de emision en formato ISO 8601

  encabezado = unicode("""[Encabezado]
serie|
fecha|{fecha_factura}
folio|
tipoDeComprobante|ingreso
formaDePago|{forma_de_pago}
metodoDePago|{metodo_de_pago}
condicionesDePago|{condiciones}
NumCtaPago|{NumCtaPago}
subTotal|10.00
descuento|0.00
total|11.60
Moneda|MXN
noCertificado|
LugarExpedicion|{lugarDeExpedicion}
""","utf-8").format(**config.emisor)
  print encabezado

  encabezado += unicode("""
[Datos Adicionales]

tipoDocumento|Factura
observaciones|

[Emisor]

rfc|{emisor_rfc}
nombre|{emisor_nombre}
RegimenFiscal|REGIMEN GENERAL DE LEY

[DomicilioFiscal]

calle|Calle 
noExterior|Número Ext.
noInterior|Número Int.
colonia|Colonia
localidad|Localidad
municipio|Municipio
estado|Nuevo León
pais|México
codigoPostal|66260

[ExpedidoEn]
calle|Calle sucursal
noExterior|
noInterior|
colonia|
localidad|
municipio|Nuevo León
estado|Nuevo León
pais|México
codigoPostal|77000

[Receptor]
rfc|XAXX010101000
nombre|PÚBLICO EN GENERAL

[Domicilio]
calle|Calle
noExterior|Num. Ext
noInterior|
colonia|Colonia
localidad|San Pedro Garza Garcia
municipio|
estado|Nuevo Leon
pais|Mexico
codigoPostal|66260

[DatosAdicionales]

noCliente|09871
email|edgar.duran@facturacionmoderna.com

""","utf-8").format(**encabezado_factura)

  cfdi = encabezado + unicode("""
[Concepto]

cantidad|1
unidad|No aplica
noIdentificacion|
descripcion|Servicio Profesional
valorUnitario|10.00
importe|10.00


[ImpuestoTrasladado]

impuesto|IVA
importe|1.60
tasa|16.00
""","utf-8")


  return cfdi #.encode('ascii', "ignore");

genera_layout()
