'''
Created on Apr 23, 2017

@author: davidryv
'''
import urllib
import requests
import json
import time 

class Delete():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def delete_users (self, id_role='',wiki_name=''):
        
        url = "https://api.assembla.com/v1/spaces/"+wiki_name+"/user_roles/"+str(id_role)+".json"

        response = requests.delete(
            url=url,
            headers={
                'X-Api-Key': '69d28d064554d5316c04',
                'X-Api-Secret': '9d44b1e5082c9fb41c4012065384942cdb7c3116',
                'Content-type': "application/json",
            },
        )
        
        time.sleep(10)
        
        if response.status_code == 204:  # OK
            
            print "Succesfully deleted"
            
            pass
        else:  # Most likely a 404 Not Found
            raise Exception(
                'Code {0} returned from `{1}`. Response text: "{2}".'.format(
                    response.status_code,
                    url,
                    response.text
                )
            )