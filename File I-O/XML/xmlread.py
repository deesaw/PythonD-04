#parse an xml document
from xml.etree import ElementTree

document = ElementTree.parse( 'membership.xml' )


users = document.find( 'users')


membership = document.getroot()
users = membership.find( 'users' )
for user in document.findall( 'users/user' ):
    print user.attrib[ 'name' ]
for group in document.findall( 'groups/group' ):
    print group.attrib[ 'name' ]