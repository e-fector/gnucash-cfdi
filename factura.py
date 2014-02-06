# encoding: utf-8

class Configuraciones():

    def __init__(self):
        self.archivo = "./gnucash/prueba.gnucash"

        self.encabezado = {
            "lugarDeExpedicion":"Durango, DGO. MX",
            "forma_de_pago":"Pago en una sola exhibicion",
            }
        self.emisor = {
            "emisor_rfc":"ESI920427886",
            "emisor_nombre":"Empresa Emisora de CFDI SA de CV",
            "emisor_regimen_fiscal":"Regimen general de personas morales",
            }
        self.domicilioFiscal = {
            "calle":"Lic. Alberto Terrones Benitez",
            "noExterior":"101 NTE",
            "noInterior":".",
            "colonia":"Centro",
            "localidad":"",
            "municipio":"Durango",
            "estado":"Durango",
            "pais":"Mexico",
            "codigoPostal":"34000",
            }
        self.expedidoEn = {
            "calle":"Lic. Alberto Terrones Benitez",
            "noExterior":"101 NTE",
            "noInterior":".",
            "colonia":"Centro",
            "localidad":"",
            "municipio":"Durango",
            "estado":"Durango",
            "pais":"Mexico",
            "codigoPostal":"34000",
            }

    def return_encabezado(self):
        return self.encabezado

    def return_archivo(self):
        return self.archivo

    def agrega_metodo_de_pago(self, metodo):
        self.encabezado["metodo_de_pago"] = metodo

    def agrega_cta_pago(self,cuenta):
        self.encabezado["NumCtaPago"] = cuenta

    def agrega_fecha_factura(self,fecha):
        self.encabezado["fecha_factura"] = fecha

    def agrega_condiciones_de_pago(self,condiciones):
        self.encabezado["condiciones"] = condiciones
