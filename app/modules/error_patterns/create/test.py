# -*- coding: utf-8 -*-

# errorpattern/create/test.py
import unittest

import sys
sys.path.append(".") 
from app.tests.BaseTest import BaseUnitTest
from app.tests.data.errorpatterns import valid_values, invalid_values

class ErrorPatternCreateTestCase(BaseUnitTest):
    """This class represents the test case for creat error patterns"""

    def create_errorpattern(self, errorpattern):
        """Test API can create a user (POST request)"""

        # post the errorpattern
        res_post = self.client().post('/errorpatterns/', data=errorpattern)
        
        # verify if errorpattern- created with success
        self.assertEqual(res_post.status_code, 201)

        # verify with the returned user has the same name/email that initial values
        self.assertIn(errorpattern['title'], str(res_post.data.decode('unicode-escape')))
        self.assertIn(errorpattern['description'], str(res_post.data.decode('unicode-escape')))
        

    def test_create_errorpattern(self):
        """Test API can create a error pattern (POST request)"""
        
        # Load the test dataset for valid values erropatterns        
        for data in valid_values:
            self.create_errorpattern(data)
        
    def errorpattern_creation_invalid_values(self, errorpattern):
        """Test API can create a error pattern (POST request) with invalid values"""
        
        res = self.client().post('/errorpatterns/', data=errorpattern)
        
        # Verify the error code 400 and error message
        self.assertEqual(res.status_code, 400)
        self.assertIn('Invalid', str(res.data))

    def test_create_invalid_errorpattern(self):
        """Test API can create a error pattern (POST request)"""
        
        # Load the test dataset for invalid values erropatterns        
        for data in invalid_values:
            self.errorpattern_creation_invalid_values(data)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()