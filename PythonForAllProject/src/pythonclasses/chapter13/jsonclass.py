import json
from pythonclasses.functions import functions as fc

data = '''
    {
    "application": {
        "users": {
            "user": [{
                    "id": "001",
                    "name": "User1"
                },
                {
                    "id": "002",
                    "name": "ApplicationUser1"
                }
            ]
        }
    }
}'''
#fc.functions.restartPython('self')

print('json string format:', data)
jsonData = json.loads(data)
print('Json loaded:', jsonData)
print('Json indented', json.dumps(jsonData,indent=1))
print('application', jsonData.get('application'))
print('users', (jsonData.get('application')).get('users'))
print('user', ((jsonData.get('application')).get('users')).get('user'))
print('User lenght:', len(((jsonData.get('application')).get('users')).get('user')))
print('User like a tuples:', ((jsonData.get('application')).get('users')).items())

for user in ((jsonData.get('application')).get('users')).get('user'):
    print('User name:', user['name'] )
    print('User id:',user['id'])
