# -*- coding: utf-8 -*-

# submission/create/test.py
import unittest

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.submissions import valid_values

class SubmissionCreateTestCase(BaseUnitTest):
    """This class represents the test case for create submissions"""

    def post_submission(self, submission):
        """Test API can create a submission (POST request)"""
        
        # post the submission
        res_post = self.client().post('/submissions/', data=submission)
        
        # verify if submission- created with success
        self.assertEqual(res_post.status_code, 201)

        # verify with the returned user has the same name/email that initial values
        self.assertIn(submission['title'], str(res_post.data.decode('unicode-escape')))
        

    def test_create_submission(self):
        """Test API can create a submission (POST request)"""

        # post a valid user manager from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)      
        # post a valid user student from dataset
        user_student = BaseUnitTest.generate_valid_student(self, 0)      
        
        # post a valid user manager from dataset
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)      
                
        # Load the test dataset for valid  submissions  
        for submission in valid_values:
            # set the student and question created to current submission to be posted
            submission['student_id'] = user_student['id']
            submission['question_id'] = question['id']

            self.post_submission(submission)
        
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()