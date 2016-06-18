anurag="Braulio Rammirez"
MiCasa="Tlaxcala"



xmlTemplate = """<root>
    <person>
        <name>%(name)s</name>
        <address>%(address)s</address>
     </person>
</root>"""

data = {'name':anurag, 'address':MiCasa}
archivo=xmlTemplate%data


f =  open("Factura", "wb")
f.write(str(archivo))
f.close()