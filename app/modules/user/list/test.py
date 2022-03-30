# create_user/test.py
import unittest

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.users import valid_users


class UserListTestCase(BaseUnitTest):
    """This class represents the test case for user list"""


    def test_list_users_professors_query(self):
        """Test API can list users professors (GET request)"""
        for user in valid_users['professor']:
            res_post = self.client().post('/users/', data=user)
            self.assertEqual(res_post.status_code, 201)
            self.assertIn(user['username'], str(res_post.data))

        get_users = self.client().get('/users/')        
        self.assertEqual(get_users.status_code, 200)
        
        for user in valid_users['professor']:
            self.assertIn(user['username'], str(get_users.data))

    def test_list_users_students_query(self):
        """Test API can list users students (GET request)"""
        for user in valid_users['student']:
            res_post = self.client().post('/users/', data=user)
            self.assertEqual(res_post.status_code, 201)
            self.assertIn(user['username'], str(res_post.data))

        get_users = self.client().get('/users/')        
        self.assertEqual(get_users.status_code, 200)
        
        for user in valid_users['student']:
            self.assertIn(user['username'], str(get_users.data))

    def test_list_multiple_users_query(self):
        """Test API can list multiple users (GET request)"""

        multiple_users = valid_users['professor'] + valid_users['monitor'] + valid_users['student']

        for user in multiple_users:
            res_post = self.client().post('/users/', data=user)
            self.assertEqual(res_post.status_code, 201)
            self.assertIn(user['username'], str(res_post.data))

        get_users = self.client().get('/users/')        
        self.assertEqual(get_users.status_code, 200)
        
        for user in multiple_users:
            self.assertIn(user['username'], str(get_users.data))




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()