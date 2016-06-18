from suds.client import Client
import logging
import base64
 
#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)
#logging.getLogger('suds.transport').setLevel(logging.DEBUG)
#logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
#logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
 
# Username and Password, assigned by FINKOK
username = 'ruths.hidalgo@gmail.com'
password = 'Bra3000universo/'
 
# Read the xml file and encode it on base64
invoice_path = "invoice.xml"
file = open("/Users/braulioalejandroramirez/Desktop/NFC/Factura3.xml")
lines = "".join(file.readlines())
xml = base64.encodestring(lines)
 
# Consuming the stamp service
url = "http://demo-facturacion.finkok.com/servicios/soap/stamp.wsdl"
client = Client(url,cache=None)
x=client.service.stamp(xml,username,password)
print(x)
