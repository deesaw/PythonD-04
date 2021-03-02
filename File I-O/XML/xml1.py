import xml.etree.ElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "color", name="blue").text = "Ocean"
ET.SubElement(doc, "color", name="green").text = "Tree"

tree = ET.ElementTree(root)
tree.write("1.xml")