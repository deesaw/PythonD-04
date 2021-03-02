#Program to read current xml file and know its elements
# ElementTree has functions to read and manipulate XMLs 
import xml.etree.ElementTree as et

#takes the xml file
tree=et.parse('prod1.xml')

#gives the root element
root=tree.getroot()

#To iterate over subelements (called "children") in the root using "for" loop.
for child in root:
    print(child.tag,child.attrib)

#To know all the elements in the entire tree, use root.iter()
s=[elem.tag for elem in root.iter()]
print(s)
'''
If you pass the root into the .tostring() method, you can return the
whole document along with ElementTree

Since ElementTree is a powerful library that can interpret more than just XML,
you must specify both the encoding and decoding of the document you are displaying
as the string.
'utf8' - this is the typical document format type for an XML.

'''

print(et.tostring(root, encoding='utf8').decode('utf8'))
for child in root:
    for element in child:
        print(element.tag,":",element.text)
print("*************************")
'''
XPath Expressions
prints the text of description
'''
for description in root.iter('description'):
    print(description.text)
