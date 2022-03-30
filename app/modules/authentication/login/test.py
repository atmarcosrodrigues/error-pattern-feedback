# -*- coding: utf-8 -*-

# auth/login/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest


class LoginUserTestCase(BaseUnitTest):
    """This class represents the test case for auth login user"""

    def login_user(self, user):        
        # make a post request in api entry auth/login
        res_post = self.client().post(
            '/auth/login', 
            data=user)
        
        return res_post       
       
        
    def test_login_usernamme_not_registered(self):
        """ Test for user login with a user not registered """

        # select randomly a user from test dataset
        user = BaseUnitTest.select_random_user(self)      
        data_login = {'username': user['username'], 'password': user['password']}
        # make a login post to selected user data
        response = self.login_user(data_login)        
        data = json.loads(response.data.decode())
        
        # verify if an error of invalid username/password has ocurred        
        self.assertEqual(response.status_code, 401)
        self.assertTrue(data['status'] == 'fail')
        self.assertTrue(
            data['message'] == 'The username or password are incorrect.')
    
    def test_login_email_not_registred(self):        
        """ Test for user login with a user email not registered """

        # select randomly a user from test dataset
        user = BaseUnitTest.select_random_user(self)      
        data_login = {'email': user['email'], 'password': user['password']}
        # make a login post to selected user data
        response = self.login_user(data_login)        
        data = json.loads(response.data.decode())

        # verify if an error of invalid email/password has ocurred        
        self.assertEqual(response.status_code, 401)
        self.assertTrue(data['status'] == 'fail')
        self.assertTrue(
            data['message'] == 'The email or password are incorrect.')

    def test_login_with_registered_user(self):
        """ Test login with registered user"""

        # select randomly a user from test dataset
        user = BaseUnitTest.select_random_user(self)      
        # make a register post to selected user data        
        register_response = self.client().post('/auth/register', 
                                        data=user)
                
        # verify if user was registered successfully
        self.assertEqual(register_response.status_code, 201)

        # make a request login with the registered user
        data_login = {'username': user['username'], 'password': user['password']}        
        login_response = self.login_user(data_login)        
        login_data = json.loads(login_response.data.decode())
        
        # verify if user was logged successfully
        self.assertEqual(login_response.status_code, 200)    
        self.assertTrue(login_data['status'] == 'success')
        self.assertTrue(login_data['message'] == 'Successfully logged in.')
        self.assertTrue(login_data['auth_token'])    
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()