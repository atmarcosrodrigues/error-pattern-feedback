# -*- coding: utf-8 -*-

# auth/register/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest

class RegisterUserTestCase(BaseUnitTest):
    """This class represents the test case for auth register user"""

    def register_user(self, user):        
        # make a post request in api entry auth/register
        res_post = self.client().post(
            '/auth/register', 
            data=user)
        
        return res_post
        

    def test_registration(self):
        """ Test for user registration """

        # select randomly a user from test dataset
        user = BaseUnitTest.select_random_user(self)      
        
        # make a register post to selected user data
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        
        # verify if user was registered successfully
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['status'] == 'success')
        self.assertTrue(data['message'] == 'Successfully registered.')
        self.assertTrue(data['auth_token'])
        

    def test_registered_with_already_registered_user(self):
        """ Test registration with already registered email"""

        # select randomly a user from test dataset
        user = BaseUnitTest.select_random_user(self)      
        
        # make a register post to selected user data
        response = self.register_user(user)
        
        # verify if user was registered successfully
        self.assertEqual(response.status_code, 201)
        
        # try post again a already registered user
        invalid_register_response = self.register_user(user)
        invalid_register_data = json.loads(invalid_register_response.data.decode())

        self.assertEqual(invalid_register_response.status_code, 202)
        self.assertTrue(invalid_register_data['status'] == 'fail')
        self.assertTrue(
            invalid_register_data['message'] == 'User already exists. Please Log in.')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()