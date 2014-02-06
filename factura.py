# encoding: utf-8

from genera_layout import genera_layout

class Factura():

    def __init__(self):
        """ Valores predeterminados """
        
        self.encabezado = {
            "forma_de_pago":"Transferencia",
            "metodo_de_pago":"Pago en una sola exhibicion",
            "condiciones":"Contado",
            "NumCtaPago":"1234",
            "lugarDeExpedicion":"Victoria de Durango",
            }
        self.emisor = {
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
        self.receptor = {
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
        self.factura = {
            "fecha_factura":"10-10-2010",
            "serie":"A",
            "folio":"123"
            }
        self.lineas_factura = []

    def agrega_linea(self,cantidad,unidad,noIdentificacion,descripcion,valorUnitario, \
                         importe,importe_impuesto,tasa):
            self.lineas_factura.append( {
                    "cantidad":cantidad,
                    "unidad":unidad,
                    "noIdentificacion":noIdentificacion,
                    "descripcion":descripcion,
                    "valorUnitario":valorUnitario,
                    "importe":importe,
                    "impuesto":impuesto,
                    "importe_impuesto":importe_impuesto,
                    "tasa":tasa,
                    })


    def edita_rfc_receptor(self, rfc_receptor):
        self.receptor.rfc_receptor = rfc_receptor



    def __str__(self):
        return genera_layout(self.encabezado, self.receptor, self.factura, \
                                 self.lineas_factura, self.emisor)

    def __unicode__(self):
        return genera_layout(self.encabezado, self.receptor, self.factura, \
                                 self.lineas_factura, self.emisor)
