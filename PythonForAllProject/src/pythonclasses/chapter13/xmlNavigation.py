import xml.etree.ElementTree as et

input = '''
    <application>
        <users>
            <user type="human">
                <id>001</id>
                <name>User1</name>
            </user>
            <user type="application">
                <id>002</id>
                <name>ApplicationUser1</name>
            </user>
        </users>
    </application>'''
    
application = et.fromstring(input)
userList = application.findall('users/user')
print('Number of users:', len(userList))

print('Printing users list:', userList,'\n')

for user in userList:
    print('Name:', user.find('name').text)
    print('Id:', user.find('id').text)
    print('Type of user:', user.get('type'), '\n')