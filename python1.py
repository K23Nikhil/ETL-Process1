import pyodbc 
import xml.etree.ElementTree as ET
import re
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=.;"
                      "Database=qsrxGIGI;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT StoreCd FROM vxstore  where StoreId <5')

Root = ET.Element("Data")
for row in cursor:   
    data = str(row)
    data = re.sub('[('',)]', '', data)
    ET.SubElement(Root, "Row",stcode = data)
tree = ET.ElementTree(Root)
tree.write("nik.xml")