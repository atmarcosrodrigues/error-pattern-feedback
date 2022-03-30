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
# from app.tests.data.errorpatterns import valid_values, invalid_values

class AuthUserStautsTestCase(BaseUnitTest):
    """This class represents the test case for auth login user"""

    def login_user(self, user):        
        # make a post request in api entry auth/login
        res_post = self.client().post(
            '/auth/login', 
            data=user)
        
        return res_post
        

    # def test_login(self):
    #     """ Test for user login """

    #     # select randomly a user from test dataset
    #     user = BaseUnitTest.select_random_user(self)      
        
    #     # make a login post to selected user data
    #     response = self.login_user(user)
    #     print (response.data)
    #     # data = json.loads(response.data.decode())
        
        
    # def test_login_usernamme_not_registered(self):
    #     """ Test for user login with a user not registered """

    #     # select randomly a user from test dataset
    #     user = BaseUnitTest.select_random_user(self)      
    #     data_login = {'username': user['username'], 'password': user['password']}
    #     # make a login post to selected user data
    #     response = self.login_user(data_login)        
    #     data = json.loads(response.data.decode())
        
    #     # verify if an error of invalid username/password has ocurred        
    #     self.assertEqual(response.status_code, 401)
    #     self.assertTrue(data['status'] == 'fail')
    #     self.assertTrue(
    #         data['message'] == 'The username or password are incorrect.')
    
    # def test_login_email_not_registred(self):        
    #     """ Test for user login with a user email not registered """

    #     # select randomly a user from test dataset
    #     user = BaseUnitTest.select_random_user(self)      
    #     data_login = {'email': user['email'], 'password': user['password']}
    #     # make a login post to selected user data
    #     response = self.login_user(data_login)        
    #     data = json.loads(response.data.decode())

    #     # verify if an error of invalid email/password has ocurred        
    #     self.assertEqual(response.status_code, 401)
    #     self.assertTrue(data['status'] == 'fail')
    #     self.assertTrue(
    #         data['message'] == 'The email or password are incorrect.')



    def test_user_status_malformed_bearer_token(self):
        """ Test for user status with malformed bearer token"""

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

        # get the logged user auth_token
        auth_token = login_data['auth_token']
        # make a user status request passing the token in headers using Bearer
        status_response = self.client().get(
                '/auth/status',
                headers=dict(
                    Authorization='Bearer' + auth_token
                )
            )

        # verify if status request is unauthorized        
        self.assertEqual(status_response.status_code, 401)
        
        # verify if the status return beare malformed message        
        data = json.loads(status_response.data.decode())
        self.assertTrue(data['status'] == 'fail')
        self.assertTrue(data['message'] == 'Bearer token malformed.')


    def test_status_wtih_logged_user(self):
        """ Test user status with already logged email"""

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

        # get the logged user auth_token
        auth_token = login_data['auth_token']
        # make a user status request passing the token in headers using Bearer
        status_response = self.client().get(
                '/auth/status',
                headers=dict(
                    Authorization='Bearer ' + auth_token
                )
            )

        # verify if status request using the token was valid        
        self.assertEqual(status_response.status_code, 200)
        user_status = json.loads(status_response.data.decode())
        
        self.assertTrue(user_status['status'] == 'success')
        # verify if the status return the correct user data
        self.assertTrue(user_status['data'] is not None)
        self.assertTrue(user_status['data']['email'] == user['email'])
        self.assertTrue(user_status['data']['admin'] == (False if user['user_type']=='STUDENT' else True))

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()