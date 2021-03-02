from xml.etree import ElementTree

f=open('sample.xml')
tree=ElementTree.parse(f)
for node in tree.iter():
    print node.tag,node.attrib,node.text