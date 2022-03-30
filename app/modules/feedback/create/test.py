# -*- coding: utf-8 -*-

# feedback/create/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.feedbacks import valid_values

class FeedbackCreateTestCase(BaseUnitTest):
    """This class represents the test case for create feedbacks"""

    def post_feedback(self, feedback):
        """Test API can create a feedback (POST request)"""
        
        # post the feedback
        res_post = self.client().post('/feedbacks/', data=feedback)
        
        posted_data =  json.loads(res_post.data.decode('utf-8').replace("'", "\'"))
        
        # verify if feedback- created with success
        self.assertEqual(res_post.status_code, 201)

        # verify with the returned user has the same name/email that initial values
        self.assertIn(feedback['title'], str(res_post.data.decode('unicode-escape')))
        

    def test_create_feedback(self):
        """Test API can create a feedback (POST request)"""

        # post a valid user manager from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)      
        # post a valid user student from dataset
        user_student = BaseUnitTest.generate_valid_student(self, 0)      
        
        # post a valid question from dataset
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)      
                
        # post a valid submission manager from dataset
        submission = BaseUnitTest.generate_valid_submission(self, student_id=user_student['id'], 
                                                           question_id=question['id'], index_submission=0)      
                
        # Load the test dataset for valid  feedbacks  
        for feedback in valid_values:
            # set the author and submission created to current feedback to be posted
            feedback['author_id'] = user_manager['id']
            feedback['submission_id'] = submission['id']

            self.post_feedback(feedback)
        
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()