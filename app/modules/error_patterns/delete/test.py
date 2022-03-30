# -*- coding: utf-8 -*-

# errorpattern/delete/test.py
import unittest
import json

import sys
sys.path.append(".") 
from app.tests.BaseTest import BaseUnitTest
from app.tests.data.errorpatterns import valid_values

class ErrorPatterndeleteTestCase(BaseUnitTest):
    """This class represents the test case for delete error patterns"""


    def delete_errorpattern(self, errorpattern):
        """Test API can delete a errorpattern (delete request)"""

        # post the errorpattern
        res_post = self.client().post('/errorpatterns/', data=errorpattern)
        posted_data =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
        # verify if errorpattern was created with success
        self.assertEqual(res_post.status_code, 201)

        # verify with the returned user has the same name/email that initial values
        self.assertIn(errorpattern['title'], str(res_post.data.decode('unicode-escape')))

        # make a query to delete errorpattern passing the posted user id
        res = self.client().delete('/errorpatterns/{}'.format(posted_data['id']))
        
        # # check if the api can get the new user posted by the id
        self.assertEqual(res.status_code, 200)
        self.assertIn('ErrorPattern deleted successfully.', str(res.data))


    def test_delete_not_existing_errorpattern(self):
        """Test API can delete errorpattern passing a not existent id (DELETE request)"""

        #  user passing invalid parameter
        res = self.client().delete('/errorpatterns/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('ErrorPattern not found.', str(res.data))        

        

    def test_delete_errorpattern(self):
        """Test API can delete a error pattern (delete request)"""
        
        # Load the test dataset for valid values erropatterns        
        for data in valid_values:
            self.delete_errorpattern(data)
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()