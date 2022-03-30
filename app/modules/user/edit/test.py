# user/edit/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.users import valid_users, invalids_id

class UserEditTestCase(BaseUnitTest):
    """This class represents the test case for get user by id"""


    # def create_valid_professor(self):
    #     return {
    #         'username': 'professor_test',
    #         'email': 'professor@test.com',
    #         'name': 'Professor Test',
    #         'info_description': 'Professor Test UFCG',
    #         'password': 'test123#',
    #         'user_type': 'PROFESSOR'
    #     }

    # def create_valid_monitor(self):
    #     return {
    #         'username': 'monitor_test',
    #         'email': 'monitor@test.com',
    #         'name': 'Monitor Test',
    #         'info_description': 'monitor Test UFCG',
    #         'password': 'test123#',
    #         'user_type': 'MONITOR'
    #     }

    # def create_valid_student(self):
    #     return {
    #         'username': 'student_test',
    #         'email': 'student@test.com',
    #         'name': 'Student Test',
    #         'info_description': 'student Test UFCG',
    #         'password': 'test123#',
    #         'user_type': 'STUDENT'
    #     }

    def edit_user_invalid_id(self, invalid_id):
        """Test API can edit user passing invalid id (PUT request)"""

        # make a query user passing invalid parameter id        
        res = self.client().delete('/users/'+invalid_id)
        self.assertEqual(res.status_code, 400)
        self.assertIn('The id value is not valid.', str(res.data))        

    def test_list_by_id_with_invalid_parameter(self):
        """ Test API can delete user passing invalid id (DELETE request)"""
        
        # Load the test dataset for invalids id       
        for id in invalids_id:
            self.edit_user_invalid_id(id)


    def test_edit_not_existing_user(self):
        """Test API can edit user passing a not existent id (PUT request)"""

        # make a put edit user passing invalid parameter
        res = self.client().put('/users/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('User not found.', str(res.data))        


    def edit_user_request(self, user):
        """Test API can edit user by id (PUT request)"""

        # post a user 
        res_post = self.client().post('/users/', data=user)
        posted_user =  json.loads(res_post.data.decode('utf-8').replace("'", "\'"))
        
        self.assertEqual(res_post.status_code, 201)
        self.assertIn(user['username'], str(res_post.data))
        
        user_new_data = {
            'name': user['name']+ ' Silva',
            'email':BaseUnitTest.generate_unique_email(self, user['username'])
        }
        
        # try edit user put method passing the user posted id
        res = self.client().put('/users/{}'.format(posted_user['id']), data=user_new_data)

        # check if the user data changed with new values
        self.assertEqual(res.status_code, 200)
        self.assertIn(user_new_data['name'], str(res.data.decode('unicode-escape')))
        self.assertIn(user_new_data['email'], str(res.data.decode('unicode-escape'))) 
        return user_new_data


    def test_edit_professor(self):
        """Test API can edit user professor (PUT request)"""
        
        # Load the test dataset for professor users        
        for user in valid_users['professor']:
            self.edit_user_request(user)

    def test_edit_student(self):
        """Test API can edit user student (PUT request)"""
        
        # Load the test dataset for professor users        
        for user in valid_users['student']:
            self.edit_user_request(user)

    def test_edit_multiple_users_query(self):
        """Test API can edit multiple users (PUT request)"""

        multiple_users = valid_users['professor'] + valid_users['monitor'] + valid_users['student']

        new_users_values = []
        for user in multiple_users:
            new_users_values.append(self.edit_user_request(user))
        
        #check if the user data changed with new values using get users request
        res = self.client().get('/users/')
        self.assertEqual(res.status_code, 200)
        
        for user in new_users_values:
            self.assertIn(user['name'], str(res.data.decode('unicode-escape')))
            self.assertIn(user['email'], str(res.data.decode('unicode-escape')))



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()