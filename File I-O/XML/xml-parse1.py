from xml.dom import minidom
myxmlfile='sample.xml'
a=minidom.parse(myxmlfile)
print (a.childNodes)
for node  in a.getElementsByTagName('price'):
    print (node.firstChild.data)

