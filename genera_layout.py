# encoding: utf-8

def genera_layout(encabezado = None, receptor=None, factura=None, \
                    emisor = None, lineas_factura=[], impuesto=None):
  # se calcula la fecha de emision en formato ISO 8601

  if not encabezado and not receptor and not factura and \
        not lineas_factura and not emisor:
    return "Falla, datos insuficientes"

  

  cfdi = "[Encabezado]"
  cfdi += "\n" + "serie|" + factura["serie"]
  cfdi += "\n" + "fecha|" + factura["fecha_factura"]
  cfdi += "\n" + "folio|" + factura["folio"]

  cfdi += "\n" + "tipoDeComprobante|ingreso"
  cfdi += "\n" + "formaDePago|" + encabezado["forma_de_pago"]
  cfdi += "\n" + "metodoDePago|" + encabezado["metodo_de_pago"]
  cfdi += "\n" + "condicionesDePago|" + encabezado["condiciones"]
  cfdi += "\n" + "NumCtaPago|" + encabezado["NumCtaPago"]
  cfdi += "\n" + "subTotal|" + encabezado["subtotal"]
  cfdi += "\n" + "descuento|0.00"
  cfdi += "\n" + "total|" + encabezado["total"]
  cfdi += "\n" + "Moneda|MXN"
  cfdi += "\n" + "noCertificado|"
  cfdi += "\n" + "LugarExpedicion|" + encabezado["lugarDeExpedicion"]

  cfdi += "\n" + "[Datos Adicionales]"

  cfdi += "\n" + "tipoDocumento|Factura"
  cfdi += "\n" + "observaciones|"+encabezado["notas"]

  cfdi += "\n" + "[Emisor]"

  cfdi += "\n" + "rfc|" + emisor["emisor_rfc"]
  cfdi += "\n" + "nombre|" + emisor["emisor_nombre"]
  cfdi += "\n" + "RegimenFiscal|" + emisor["regimen_fiscal"]
  
  cfdi += "\n" + "[DomicilioFiscal]"

  cfdi += "\n" + "calle|" + emisor["domicilio_calle"]
  cfdi += "\n" + "noExterior|" + emisor["domicilio_noExterior"]
  cfdi += "\n" + "noInterior|" + emisor["domicilio_noInterior"]
  cfdi += "\n" + "colonia|" + emisor["domicilio_colonia"]
  cfdi += "\n" + "localidad|" + emisor["domicilio_localidad"]
  cfdi += "\n" + "municipio|" + emisor["domicilio_municipio"]
  cfdi += "\n" + "estado|" + emisor["domicilio_estado"]
  cfdi += "\n" + "pais|" + emisor["domicilio_pais"]
  cfdi += "\n" + "codigoPostal|" + emisor["domicilio_cp"]

  cfdi += "\n" + "[ExpedidoEn]"
  cfdi += "\n" + "calle|" + emisor["expedidoen_calle"]
  cfdi += "\n" + "noExterior|" + emisor["expedidoen_noExterior"]
  cfdi += "\n" + "noInterior|" + emisor["expedidoen_noInterior"]
  cfdi += "\n" + "colonia|" + emisor["expedidoen_colonia"]
  cfdi += "\n" + "localidad|" + emisor["expedidoen_localidad"]
  cfdi += "\n" + "municipio|" + emisor["expedidoen_municipio"]
  cfdi += "\n" + "estado|" + emisor["expedidoen_estado"]
  cfdi += "\n" + "pais|" + emisor["expedidoen_pais"]
  cfdi += "\n" + "codigoPostal|" + emisor["expedidoen_cp"]

  cfdi += "\n" + "[Receptor]"
  cfdi += "\n" + "rfc|" + receptor["rfc_receptor"]
  cfdi += "\n" + "nombre|" + receptor["nombre_fiscal"]

  cfdi += "\n" + "[Domicilio]"
  cfdi += "\n" + "calle|" + receptor["calle"]
  cfdi += "\n" + "noExterior|" + receptor["noExterior"]
  cfdi += "\n" + "noInterior|" + receptor["noInterior"]
  cfdi += "\n" + "colonia|" + receptor["colonia"]
  cfdi += "\n" + "localidad|" + receptor["localidad"]
  cfdi += "\n" + "municipio|" + receptor["municipio"]
  cfdi += "\n" + "estado|" + receptor["estado"]
  cfdi += "\n" + "pais|" + receptor["pais"]
  cfdi += "\n" + "codigoPostal|" + receptor["cp"]

  cfdi += "\n" + "[DatosAdicionales]"

  cfdi += "\n" + "noCliente|" + receptor["noCliente"]
  cfdi += "\n" + "email|" + receptor["email"]


  for linea in lineas_factura:
    cfdi += "\n" + "[Concepto]"
    
    cfdi += "\n" + "cantidad| " + str(linea["cantidad"])
    cfdi += "\n" + "unidad| " + linea["unidad"]
    cfdi += "\n" + "noIdentificacion| " + linea["noIdentificacion"]
    cfdi += "\n" + "descripcion| " + linea["descripcion"]
    cfdi += "\n" + "valorUnitario| " + str(linea["valorUnitario"])
    cfdi += "\n" + "importe| " + linea["importe"]
    
  cfdi += "\n" + "[ImpuestoTrasladado] "
    


  cfdi += "\n" + "impuesto| " + str(impuesto["impuesto"])
  cfdi += "\n" + "importe| " + str(impuesto["importe_impuesto"])
  cfdi += "\n" + "tasa| " + str(impuesto["tasa"])



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
        })
  impuesto = {
    
    "impuesto":"IVA",
    "importe_impuesto":"1.60",
    "tasa":"16.00",
    }
  

  print genera_layout(encabezado, receptor, factura, emisor, lineas_factura)

