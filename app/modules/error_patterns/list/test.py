# create_errorpattern/test.py
import unittest

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.errorpatterns import valid_values

class ErrorPatternListTestCase(BaseUnitTest):
    """This class represents the test case for errorpatterns list"""


    def test_list_errorpatterns_query(self):
        """Test API can list errorpatterns (GET request)"""
        errorpattern = valid_values[0]
        
        # post the data
        res_post = self.client().post('/errorpatterns/', data=errorpattern)
        
        self.assertEqual(res_post.status_code, 201)
        self.assertIn(errorpattern['title'], str(res_post.data))

        # make the get request list
        res = self.client().get('/errorpatterns/')
        
        # verify if posted data is on query response
        self.assertEqual(res.status_code, 200)
        self.assertIn(errorpattern['title'], str(res.data))

    def test_list_multiple_errorpatterns_query(self):
        """Test API can list multiple errorpatterns (GET request)"""

        for errorpattern in valid_values:
            # post the data
            res_post = self.client().post('/errorpatterns/', data=errorpattern)
        
            self.assertEqual(res_post.status_code, 201)
            self.assertIn(errorpattern['title'], str(res_post.data))

        # make get request list errorpatterns
        res = self.client().get('/errorpatterns/')
    
        # verify if the posted multiple errorpatterns are on request list
        self.assertEqual(res.status_code, 200)
        for errorpattern in valid_values:
            self.assertIn(errorpattern['title'], str(res.data))
        
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()