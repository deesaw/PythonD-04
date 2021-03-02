
#adding a new product to the current xml
import os
import xml.etree.ElementTree as et
base_path=os.path.dirname(os.path.realpath(__file__))
print(base_path)

xml_file=os.path.join(base_path,"prod1.xml")
tree=et.parse(xml_file)
root=tree.getroot()

#To create a new product
new_product=et.SubElement(root,"product",attrib={"id":"6"})
new_prod_name=et.SubElement(new_product,"name")
new_prod_desc=et.SubElement(new_product,"description")
new_prod_cost=et.SubElement(new_product,"cost")
new_prod_ship=et.SubElement(new_product,"shipping")
#Creating new id 4 and appending the data to the xml
new_prod_name.text="Python Pants"
new_prod_desc.text="These pants will help you code like crazy"
new_prod_cost.text="39.95"
new_prod_ship.text="4.00"
#writing to current xml_file
tree.write(xml_file)
for child in root:
    print(child.tag,child.attrib)

