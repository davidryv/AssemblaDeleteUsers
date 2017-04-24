'''
Created on Apr 22, 2017

@author: davidryv
'''
from GetData import GetData as ReadData

if __name__ == '__main__':
    
    
    
    GetUsers = ReadData()
    
    userList = GetUsers.getUserList()
    
    spaces= GetUsers.getSpaces()
    
    for space in spaces:
        print 'Deleting' + space['wiki_name']
        users,role,id = GetUsers.getUsers(space['name'])
        for user in users:
            if user['login'].encode('utf-8') in userList:
                
                print user['login'].encode('utf-8')  + " , Deleted from " + space['wiki_name'].encode('utf-8')
                GetUsers.DeleteUsersList(user['id'].encode('utf-8'),user['login'].encode('utf-8'),role,space['wiki_name'].encode('utf-8'))
                
            else:
                print '-----------Not deleted-----------'
                print user['login'].encode('utf-8')  + " , Not found, delete it manually"
    