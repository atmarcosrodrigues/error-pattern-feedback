# create_feedback/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.feedbacks import valid_values

class FeedbackListTestCase(BaseUnitTest):
    """This class represents the test case for feedback list"""


    def test_list_feedbacks_query(self):
        """Test API can list feedbacks (GET request)"""

        # post a valid user manager, student and question from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        user_student = BaseUnitTest.generate_valid_student(self, 0)
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)
        
        # create a submission from student to question 
        submission = BaseUnitTest.generate_valid_submission(self, student_id=user_student['id'],
                                        question_id=question['id'], index_submission=0)
        
        # create a feedback from user manager to generated submission
        feedback = valid_values[0]
        feedback['author_id'] = user_manager['id']
        feedback['submission_id'] = submission['id']

        res_post = self.client().post('/feedbacks/', data=feedback)
        
        self.assertEqual(res_post.status_code, 201)
        self.assertIn(feedback['title'], str(res_post.data))

        # make the get request list
        res = self.client().get('/feedbacks/')
        
        # verify if posted data is on query response
        self.assertEqual(res.status_code, 200)
        self.assertIn(feedback['title'], str(res.data))

    def test_list_multiple_feedbacks_query(self):
        """Test API can list multiple feedbacks (GET request)"""

        # post a valid user manager, student and question from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        user_student = BaseUnitTest.generate_valid_student(self, 0)
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)
        
        # create a submission from student to question 
        submission = BaseUnitTest.generate_valid_submission(self, student_id=user_student['id'],
                                        question_id=question['id'], index_submission=0)
        

        self.feedbacks_list = []
        
        for feedback in valid_values:
            # create a feedback from user manager to generated submission
            feedback = valid_values[0]
            feedback['author_id'] = user_manager['id']
            feedback['submission_id'] = submission['id']
            
            # post the data
            res_post = self.client().post('/feedbacks/', data=feedback)
            posted_feedback =  json.loads(res_post.data.decode('utf-8').replace("'", "\'"))
            self.feedbacks_list.append(posted_feedback)

            self.assertEqual(res_post.status_code, 201)
            self.assertIn(feedback['title'], str(res_post.data))

        # make get request list feedbacks
        res = self.client().get('/feedbacks/')
            
        # verify if the posted multiple feedbacks are on request list
        self.assertEqual(res.status_code, 200)
        for feedback in self.feedbacks_list:
            self.assertIn(feedback['title'], str(res.data))
        
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()