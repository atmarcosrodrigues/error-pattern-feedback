# create_submission/test.py

import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.submissions import valid_values

class SubmissionListTestCase(BaseUnitTest):
    """This class represents the test case for submissions list"""


    def test_list_submissions_query(self):
        """Test API can list submissions (GET request)"""

        # post a valid user manager, student and question from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        user_student = BaseUnitTest.generate_valid_student(self, 0)
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)
        submission = valid_values[0]
        
        submission['student_id'] = user_student['id']
        submission['question_id'] = question['id']

        res_post = self.client().post('/submissions/', data=submission)
        
        self.assertEqual(res_post.status_code, 201)
        self.assertIn(submission['title'], str(res_post.data))

        # make the get request list
        res = self.client().get('/submissions/')
        
        # verify if posted data is on query response
        self.assertEqual(res.status_code, 200)
        self.assertIn(submission['title'], str(res.data))

    def test_list_multiple_submissions_query(self):
        """Test API can list multiple submissions (GET request)"""

        # post a valid user manager, student and question from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        user_student = BaseUnitTest.generate_valid_student(self, 0)
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)
 
        self.submissions_list = []
        
        for submission in valid_values:
            submission['student_id'] = user_student['id']
            submission['question_id'] = question['id']
            
            # post the data
            res_post = self.client().post('/submissions/', data=submission)
            posted_submission =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
            self.submissions_list.append(posted_submission)

            self.assertEqual(res_post.status_code, 201)
            self.assertIn(submission['title'], str(res_post.data))

        # make get request list submissions
        res = self.client().get('/submissions/')
    
        # verify if the posted multiple submissions are on request list
        self.assertEqual(res.status_code, 200)
        for submission in self.submissions_list:
            self.assertIn(submission['title'], str(res.data))
        
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()