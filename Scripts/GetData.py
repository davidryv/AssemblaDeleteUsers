'''
Created on Apr 21, 2017

@author: davidryv
'''

from assembla import API
from DeleteMethods import Delete

class GetData():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def getSpaces (self):
        
        self.assembla = API(
            key='69d28d064554d5316c04',
            secret='9d44b1e5082c9fb41c4012065384942cdb7c3116',
            # Use your API key/secret from https://www.assembla.com/user/edit/manage_clients
            )
        
        spaces = self.assembla.spaces()
        
        return spaces
        
    def getUsers (self,space_name=''):
    
        
        my_space = self.assembla.spaces(name=space_name)[0]
        
        print "Space ID " + my_space.data["id"]

        users = my_space.users()
        roles = my_space.roles()
                     
        print roles
        
        for user in users:
            
            login_user = user.data['login']
            
            id_user= user.data['id']

            print("User LogIn: " + login_user +" With ID: " + id_user)
        
        return users,roles,id
        
    def getUserList (self):
        
        filename = '/home/davidryv/workspace/DeleteUsers_2/Scripts/userlist.txt'
        data_chomp = []
        # Using the newer with construct to close the file automatically.
        with open(filename) as f:
            data = f.readlines()
            
        for username in data:
             data_chomp.append(username.rstrip())
        
        return data_chomp
    
    def DeleteUsersList(self,userID,UserName,roles,space_name):
        
        
        Delete_user= Delete()
        
        for roles_id in roles:
            if roles_id['user_id'] == userID:
                role_number=roles_id['id']
                    
                Delete_user.delete_users(id_role=role_number , wiki_name=space_name)
            
                break
            else:
                
                print "ID not found in the list"



        