# -*- coding: utf-8 -*-

# user/create/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.users import valid_users, invalid_users
        
class UserCreateTestCase(BaseUnitTest):
    """This class represents the test case for create user resource"""

    def create_user(self, user):
        """Test API can create a user (POST request)"""

        # post the user
        res_post = self.client().post('/users/', data=user)
        posted_user =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
        
        # verify with user was created with success
        self.assertEqual(res_post.status_code, 201)

        # verify with the returned user has the same name/email that initial values
        self.assertIn(user['name'], str(res_post.data.decode('unicode-escape')))
        self.assertIn(user['email'], str(res_post.data.decode('unicode-escape')))


    def user_creation_invalid_username(self, user):
        """Test API can create a user (POST request) with invalid username"""
        
        res = self.client().post('/users/', data=user)
        
        # Verify the error code 400 and error message (Invalid Username)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Invalid Username', str(res.data))

    def user_creation_invalid_email(self, user):
        """Test API can create a user (POST request) with invalid email"""
        
        res = self.client().post('/users/', data=user)
        
        # Verify the error code 400 and error message (Invalid Email)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Invalid Email', str(res.data))

    def user_creation_invalid_type(self, user):
        """Test API can create a user (POST request) with invalid type"""
        
        res = self.client().post('/users/', data=user)
        
        # Verify the error code 400 and error message (Invalid User Type)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Invalid User Type', str(res.data))

    def user_creation_invalid_password(self, user):
        """Test API can create a user (POST request) with invalid password"""
        
        res = self.client().post('/users/', data=user)
        
        # Verify the error code 400 and error message (Invalid Password)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Invalid Password', str(res.data))


    def test_create_user_with_invalid_username(self):
        """Test API can create a user with invalid username(POST request)"""
        
        # Load the test dataset for professor users        
        for user in invalid_users['invalid-username']:
            self.user_creation_invalid_username(user)
        
    def test_create_user_with_invalid_email(self):
        """Test API can create a user with invalid email(POST request)"""
        
        # Load the test dataset for professor users        
        for user in invalid_users['invalid-email']:
            self.user_creation_invalid_email(user)
        
    def test_create_user_with_invalid_type(self):
        """Test API can create a user with invalid type(POST request)"""
        
        # Load the test dataset for professor users        
        for user in invalid_users['invalid-type']:
            self.user_creation_invalid_type(user)
        
    def test_create_user_with_invalid_password(self):
        """Test API can create a user with invalid password(POST request)"""
        
        # Load the test dataset for professor users        
        for user in invalid_users['invalid-password']:
            self.user_creation_invalid_password(user)
        

    def test_create_professor_user(self):
        """Test API can create a user professor (POST request)"""
        
        # Load the test dataset for professor users        
        for user in valid_users['professor']:
            self.create_user(user)
        
    
    def test_create_monitor_user(self):
        """Test API can create a user monitor (POST request)"""
        
        # Load the test dataset for monitor users        
        for user in valid_users['monitor']:
            self.create_user(user)
        

    def test_create_student_user(self):
        """Test API can create a user student (POST request)"""
                
        # Load the test dataset for valid student users        
        for user in valid_users['student']:
            self.create_user(user)      
      

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()