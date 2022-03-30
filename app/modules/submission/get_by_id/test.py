# -*- coding: utf-8 -*-

# submission/get_by_id/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.submissions import valid_values
from app.tests.data.invalid_ids import invalid_ids
        
class SubmissionGetByIdTestCase(BaseUnitTest):
    """This class represents the test case for get submission by id"""


    def list_submission_invalid_id(self, invalid_id):
        """Test API can get submission passing invalid id (GET request)"""

        # make a query submission passing invalid parameter
        res = self.client().get('/submissions/'+invalid_id)
        self.assertEqual(res.status_code, 400)
        self.assertIn('The id value is not valid.', str(res.data))      

    def list_submission_query(self, submission):
        """Test API can get submission by id (GET request)"""

        # make a query submission passing the submission posted id
        res = self.client().get('/submissions/{}'.format(submission['id']))
        
        # check if the api can get the new submission posted by the id
        self.assertEqual(res.status_code, 200)
        self.assertIn(submission['title'], str(res.data))


    def test_list_by_id_with_invalid_parameter(self):
        """Test API can get submission passing invalid id (GET request)"""
        
        # Load the test dataset for invalids id       
        for id in invalid_ids:
            self.list_submission_invalid_id(id)


    def test_list_by_id_not_existing_submission(self):
        """Test API can get submission passing a not existent id (GET request)"""

        # make a query submission passing not existing id submission
        res = self.client().get('/submissions/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('Submission not found.', str(res.data))        


    def test_get_by_id_query(self):
        """Test API can get submission by id (GET request)"""

        # post a valid user manager, student and question from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        user_student = BaseUnitTest.generate_valid_student(self, 0)
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)

        self.submissions_list = []
        
        # Load the test dataset for valid student submissions        
        for submission in valid_values:
            submission['student_id'] = user_student['id']
            submission['question_id'] = question['id']
            
            # post the data
            res_post = self.client().post('/submissions/', data=submission)
            posted_submission =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
            self.assertEqual(res_post.status_code, 201)
            self.assertIn(submission['title'], str(res_post.data))

            self.submissions_list.append(posted_submission)
        
        for submission in self.submissions_list:
            self.list_submission_query(submission)
        
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()