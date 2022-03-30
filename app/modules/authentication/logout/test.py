# -*- coding: utf-8 -*-

# auth/login/test.py
from atexit import register
import unittest
import json

import sys

sys.path.append(".") 

from app import create_app, db
from app.tests.BaseTest import BaseUnitTest
from app.models.User import User
from app.tests.data.users import valid_users
import random

class LogoutUserTestCase(BaseUnitTest):
    """This class represents the test case for auth login user"""

    def login_user(self, user):        
        # make a post request in api entry auth/login
        res_post = self.client().post(
            '/auth/login', 
            data=user)
        
        return res_post
        

    def register_and_log_user(self):
        """ Regiter a user and make login """

        # Register user #

        ## select randomly a user from test dataset
        user = BaseUnitTest.select_random_user(self)      
        ## make a register post to selected user data        
        register_response = self.client().post('/auth/register', 
                                        data=user)                
        ## verify if user was registered successfully
        self.assertEqual(register_response.status_code, 201)

        # Login user #

        ## make a request login with the registered user
        data_login = {'username': user['username'], 'password': user['password']}        
        login_response = self.login_user(data_login)        
        login_data = json.loads(login_response.data.decode())
        
        ## verify if user was logged successfully
        self.assertEqual(login_response.status_code, 200)    
        self.assertTrue(login_data['status'] == 'success')
        self.assertTrue(login_data['message'] == 'Successfully logged in.')
        self.assertTrue(login_data['auth_token'])    

        return login_data['auth_token']

        

    def test_valid_logout_user(self):
        """ Test logout with registered and logged in user"""

        # register and log user and receive the auth token
        auth_token = self.register_and_log_user()

        # Logout #
               
        ## make a logout request passing the token in headers using Bearer
        logout_response = self.client().post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + auth_token
                )
            )

        self.assertEqual(logout_response.status_code, 200)
        logout_data = json.loads(logout_response.data.decode())
        self.assertTrue(logout_data['status'] == 'success')
        self.assertTrue(logout_data['message'] == 'Successfully logged out.')


    def test_logout_user_using_blacklisted_token(self):
        """ Test logout with one already logged off user/blacklisted token"""

        # register and log user and receive the auth token
        auth_token = self.register_and_log_user()

        # Logout #               
        ## make a logout request passing the token in headers using Bearer
        logout_response = self.client().post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + auth_token
                )
            )
        ## verify logout result
        self.assertEqual(logout_response.status_code, 200)
        logout_data = json.loads(logout_response.data.decode())
        self.assertTrue(logout_data['status'] == 'success')
        self.assertTrue(logout_data['message'] == 'Successfully logged out.')

        ## Try logout again using the blacklisted token
        invalid_logout = self.client().post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + auth_token
                )
            )
        ## verify if the logout fail
        self.assertEqual(invalid_logout.status_code, 401)
        expired_logout_data = json.loads(invalid_logout.data.decode())
        self.assertTrue(expired_logout_data['status'] == 'fail')
        self.assertTrue(expired_logout_data['message'] == 'Token expired. Please log in again.')

        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()