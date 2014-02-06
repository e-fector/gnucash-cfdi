# encoding: utf-8

def genera_layout(encabezado = None, receptor=None, factura=None, \
                    emisor = None, lineas_factura=[]):
  # se calcula la fecha de emision en formato ISO 8601

  if not encabezado and not receptor and not factura and \
        not lineas_factura and not emisor:
    return "Falla, datos insuficientes"


  cfdi = unicode("""[Encabezado]
serie|{serie}
fecha|{fecha_factura}
folio|{folio}

""","utf-8").format(**factura)
  
  cfdi += unicode("""tipoDeComprobante|ingreso
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

""","utf-8").format(**encabezado)

  cfdi += unicode("""
[Emisor]

rfc|{emisor_rfc}
nombre|{emisor_nombre}
RegimenFiscal|{regimen_fiscal}

[DomicilioFiscal]

calle|{domicilio_calle}
noExterior|{domicilio_noExterior}
noInterior|{domicilio_noInterior}
colonia|{domicilio_colonia}
localidad|{domicilio_localidad}
municipio|{domicilio_municipio}
estado|{domicilio_estado}
pais|{domicilio_pais}
codigoPostal|{domicilio_cp}

[ExpedidoEn]
calle|{expedidoen_calle}
noExterior|{expedidoen_noExterior}
noInterior|{expedidoen_noInterior}
colonia|{expedidoen_colonia}
localidad|{expedidoen_localidad}
municipio|{expedidoen_municipio}
estado|{expedidoen_estado}
pais|{expedidoen_pais}
codigoPostal|{expedidoen_cp}

""","utf-8").format(**emisor)

  cfdi += unicode("""
[Receptor]
rfc|{rfc_receptor}
nombre|{nombre_fiscal}

[Domicilio]
calle|{calle}
noExterior|{noExterior}
noInterior|{noInterior}
colonia|{colonia}
localidad|{localidad}
municipio|{municipio}
estado|{estado}
pais|{pais}
codigoPostal|{cp}

[DatosAdicionales]

noCliente|{noCliente}
email|{email}

""","utf-8").format(**receptor)
  for linea in lineas_factura:
    cfdi += unicode("""
[Concepto]

cantidad|{cantidad}
unidad|{unidad}
noIdentificacion|{noIdentificacion}
descripcion|{descripcion}
valorUnitario|{valorUnitario}
importe|{importe}

[ImpuestoTrasladado]

impuesto|{impuesto}
importe|{importe}
tasa|{tasa}
""","utf-8").format(**linea)


  return cfdi #.encode('ascii', "ignore");

 

if __name__ == '__main__':
  
  encabezado = {
    "forma_de_pago":"Transferencia",
    "metodo_de_pago":"Pago en una sola exhibicion",
    "condiciones":"Contado",
    "NumCtaPago":"1234",
    "lugarDeExpedicion":"Victoria de Durango",
    }
  receptor = {
    "rfc_receptor":"",
    "nombre_fiscal":"",
    "calle":"",
    "noExterior":"",
    "noInterior":"",
    "colonia":"",
    "localidad":"",
    "municipio":"",
    "estado":"",
    "pais":"",
    "cp":"",
    "noCliente":"",
    "email":"",
    }
  factura = {
    "fecha_factura":"10-10-2010",
    "serie":"A",
    "folio":"123"
    }
  emisor = {
    "domicilio_calle":"Lic. Alberto Terrones Benitez #101 NTE",
    "domicilio_noExterior":"101 NTE",
    "domicilio_noInterior":"",
    "domicilio_colonia":"Durango",
    "domicilio_localidad":"Victoria de Durango",
    "domicilio_municipio":"Durango",
    "domicilio_estado":"Durango",
    "domicilio_pais":"Mexico",
    "domicilio_cp":"34000",
    "expedidoen_calle":"Av. 20 de Noviembre",
    "expedidoen_noExterior":"1002 Ote",
    "expedidoen_noInterior":"",
    "expedidoen_colonia":"Centro",
    "expedidoen_localidad":"Victoria de Durango",
    "expedidoen_municipio":"Durango",
    "expedidoen_estado":"Durango",
    "expedidoen_pais":"Mexico",
    "expedidoen_cp":"34000",
    "emisor_rfc":"RAV751222956",
    "emisor_nombre":"Rectificaciones Avina SA de CV",
    "regimen_fiscal":"Regimen general de personas morales",
    }
  lineas_factura = []
  for item in [1,2,3,4,5]:
    lineas_factura.append( {
        "cantidad":"1",
        "unidad":"No aplica" + str(item),
        "noIdentificacion":"SERV",
        "descripcion":"Servicio Profesional",
        "valorUnitario":"10.00",
        "importe":"10.00",
        "impuesto":"IVA",
        "importe":"1.60",
        "tasa":"16.00",
        })

  print genera_layout(encabezado, receptor, factura, emisor, lineas_factura)

