import xml.dom.minidom

def traverseTree(document,ftag, depth=0):
  tag = document.tagName
  for child in document.childNodes:
    if child.nodeType == child.TEXT_NODE:
      if document.tagName == ftag:
        print depth*'    ', child.data
    if child.nodeType == xml.dom.Node.ELEMENT_NODE:
      traverseTree(child, depth+1)

filename = 'c:/users/tring/downloads/example.smrf'
dom = xml.dom.minidom.parse(filename)
traverseTree(dom.documentElement,'Name')
