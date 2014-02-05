def genera_layout(emisor, repector, factura, lineas_factura):
  # se calcula la fecha de emision en formato ISO 8601

  encabezado_factura = {
      "fecha_factura" : "2014-01-01T15:15:19.390390",
      "emisor_rfc" : emisor[0]["vat"][2:],
      "emisor_nombre" :  "Rectificaciones Avina",#emisor[0]["name"],
      "emisor_regimen_fiscal" : "PENDIENTE",
      "forma_de_pago" : "PAGO EN UNA SOLA EXHIBICIoN",
      "metodo_de_pago" : "Transferencia electronica",
      "condiciones" : "Contado",
      "NumCtaPago" : "No Identificado",
      "lugarDeExpedicion" : "Durango, DGO. MX"
      }

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
