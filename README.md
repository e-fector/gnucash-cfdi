gnucash-cfdi
============

Proyecto que timbra facturas de gnucash por medio de facturacion moderna.

Solo hay que ejecutar el timbrador.py y escribir el ID de la factura a timbrar. y listo

Es una aplicacón sencilla que extrae una factura de gnucash por medio de los bindings de python. La timbra, y la manda por correo electrónico. 

Es todo.

(Usa facturacionmoderna.com como PAC)

El siguiente codigo descarga la aplicacion, y timbra la factura con el id 200 en gnucash/prueba.gnucash

    wget https://codeload.github.com/sebastianavina/gnucash-cfdi/zip/master -O gnucash-cfdi-master.zip
    unzip gnucash-cfdi-master.zip -d ./
    cd ./gnucash-cfdi-master/
    echo "200" | python timbrador.py

Hay que editar el archivo timbrador.py para cambiar la ubicacion del archivo (o la url de conexion) que usen para su sitema gnucash y hay que editar factura.py para alimentar los datos de su empresa. Tambien pueden editar mail.py con los datos de su correo para no estarlos alimentando cada vez que timbren una factura para que la envie el cliente.

El sistema debería de funcionar con MySQL y en Windows, mas no he hecho las pruebas necesarias. Reporten y hagan un pull request si hay que hacer algun cambio.

Abran el archivo gnucash y vean la estructura del cliente "Empresa ficticia", Se uso la cuarta linea del Address para guardar el RFC, el Fax para guardar el pago y el telefono para guarda el numero de cuenta.

OJO !
Tienen que cerrar el timbrador si quieren que en las notas les guarde la informacion de la factura.

Todos los comprobantes se van a guardar en el folder ./comprobantes.

Éxito!


