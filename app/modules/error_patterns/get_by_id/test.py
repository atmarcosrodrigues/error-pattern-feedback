# -*- coding: utf-8 -*-

# errorpattern/get_by_id/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.errorpatterns import valid_values, invalids_id
        
class ErrorPatternGetByIdTestCase(BaseUnitTest):
    """This class represents the test case for get errorpattern by id"""


    def list_errorpattern_invalid_id(self, invalid_id):
        """Test API can get errorpattern passing invalid id (GET request)"""

        # make a query errorpattern passing invalid parameter
        res = self.client().get('/errorpatterns/'+invalid_id)
        self.assertEqual(res.status_code, 400)
        self.assertIn('The id value is not valid.', str(res.data))      

    def list_errorpattern_query(self, errorpattern):
        """Test API can get errorpattern by id (GET request)"""

        # post the errorpattern
        res_post = self.client().post('/errorpatterns/', data=errorpattern)
        posted_data =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
        
        self.assertEqual(res_post.status_code, 201)
        self.assertIn(errorpattern['title'], str(res_post.data.decode('unicode-escape')))

        # make a query errorpattern passing the errorpattern posted id
        res = self.client().get('/errorpatterns/{}'.format(posted_data['id']))
        
        # check if the api can get the new errorpattern posted by the id
        self.assertEqual(res.status_code, 200)
        self.assertIn(errorpattern['title'], str(res.data))


    def test_list_by_id_with_invalid_parameter(self):
        """Test API can get errorpattern passing invalid id (GET request)"""
        
        # Load the test dataset for invalids id       
        for id in invalids_id:
            self.list_errorpattern_invalid_id(id)


    def test_list_by_id_not_existing_errorpattern(self):
        """Test API can get errorpattern passing a not existent id (GET request)"""

        # make a query errorpattern passing invalid parameter id
        res = self.client().get('/errorpatterns/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('ErrorPattern not found.', str(res.data))        


    def test_get_by_id_query(self):
        """Test API can get errorpattern by id (GET request)"""
                
        # Load the test dataset for valid student errorpatterns        
        for errorpattern in valid_values:
            self.list_errorpattern_query(errorpattern)
        
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()