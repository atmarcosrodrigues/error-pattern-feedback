# create_user/test.py
import unittest
import os
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.users import valid_users, invalids_id


class DeleteUserTestCase(BaseUnitTest):
    """This class represents the test case for delete user resource"""

    def delete_user_invalid_id(self, invalid_id):
        """ Delete user passing invalid id (DELETE request)"""

        # make a query user passing invalid parameter
        res = self.client().delete('/users/'+invalid_id)
        self.assertEqual(res.status_code, 400)
        self.assertIn('The id value is not valid.', str(res.data))        

    def delete_user_query(self, user):
        """ Delete user passing valid id (GET request)"""

        # post the user
        res_post = self.client().post('/users/', data=user)
        posted_user =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
        
        # verify if user was created successfully
        self.assertEqual(res_post.status_code, 201)
        self.assertIn(user['name'], str(res_post.data.decode('unicode-escape')))

        # make a query to delete user passing the posted user id
        res = self.client().delete('/users/{}'.format(posted_user['id']))
        
        # check if the api can get the new user posted by the id
        self.assertEqual(res.status_code, 200)
        self.assertIn('User deleted successfully.', str(res.data))


    def test_list_by_id_with_invalid_parameter(self):
        """ Test API can delete user passing invalid id (DELETE request)"""
        
        # Load the test dataset for invalids id       
        for id in invalids_id:
            self.delete_user_invalid_id(id)


    def test_delete_not_existing_user(self):
        """Test API can get user passing a not existent id (GET request)"""

        # make a query user passing invalid parameter
        res = self.client().delete('/users/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('User not found.', str(res.data))        


    def test_delete_professor(self):
        """Test API can delete user (DELETE request)"""
        
        # Load the test dataset for professor users        
        for user in valid_users['professor']:
            self.delete_user_query(user)
        
    
    def test_delete_monitor(self):
        """Test API can delete user (DELETE request)"""
        
        # Load the test dataset for monitor users        
        for user in valid_users['monitor']:
            self.delete_user_query(user)
        

    def test_delete_student(self):
        """Test API can delete user (DELETE request)"""
                
        # Load the test dataset for valid student users        
        for user in valid_users['student']:
            self.delete_user_query(user)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()