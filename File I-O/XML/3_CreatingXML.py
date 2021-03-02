#Program to create an xml document 
import xml.etree.ElementTree as et

# <membership/>
membership = et.Element( 'membership' )

# <membership><users/>
users = et.SubElement( membership, 'users' )

# <membership><users><user/>
et.SubElement( users, 'user', name='Ujwal' )
et.SubElement( users, 'user', name='Vishal' )
et.SubElement( users, 'user', name='Lahari' )

# <membership><groups/>
groups = et.SubElement( membership, 'groups' )

# <membership><groups><group/>
group = et.SubElement( groups, 'group', name='users' )

# <membership><groups><group><user/>
et.SubElement( group, 'user', name='Lalitha' )
et.SubElement( group, 'user', name='Shilpa' )

# <membership><groups><group/>
group = et.SubElement( groups, 'group', name='administrators' )

# <membership><groups><group><user/>
et.SubElement( group, 'user', name='Sasi' )

tree=et.ElementTree(membership)
tree.write("items1.xml")
