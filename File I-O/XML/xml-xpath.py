from lxml import etree
f=open('sample.xml','r')
tree=etree.parse(f)
r = tree.xpath('//breakfast-menu/food/name')
for node in r:
    print(node.tag,node.attrib,node.text)
    
f.close()