# -*- coding: utf-8 -*-

# feedback/delete/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.feedbacks import valid_values

class FeedbackDeleteTestCase(BaseUnitTest):
    """This class represents the test case for creat error patterns"""


    def delete_feedback(self, id):
        """Test API can delete a user (delete request)"""

        # make a query to delete feedback passing the posted user id
        res = self.client().delete('/feedbacks/{}'.format(id))
        
        # # check if the feedback was deleted
        self.assertEqual(res.status_code, 200)
        self.assertIn('Feedback deleted successfully.', str(res.data))


    def test_delete_not_existing_feedback(self):
        """Test API can delete feedback passing a not existent id (DELETE request)"""

        # user passing not existing feedback id
        res = self.client().delete('/feedbacks/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('Feedback not found.', str(res.data))        

    

    def test_delete_feedbacks(self):
        """Test API can create feedbacks to be deleted"""
        
        # post a valid user manager from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)      
        # post a valid user student from dataset
        user_student = BaseUnitTest.generate_valid_student(self, 0)      
        
        # post a valid user manager from dataset
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)      

        # post a valid submission manager from dataset
        submission = BaseUnitTest.generate_valid_submission(self, student_id=user_student['id'], 
                                                           question_id=question['id'], index_submission=0)      
                
        self.feedbacks_list = []        
        # Load the test dataset for valid  feedbacks  
        for feedback in valid_values:
            # set the author and submission created to current feedback to be posted
            feedback['author_id'] = user_manager['id']
            feedback['submission_id'] = submission['id']

            # post the feedback
            res_post = self.client().post('/feedbacks/', data=feedback)
        
            # verify if feedback- created with success
            self.assertEqual(res_post.status_code, 201)

            posted_feedback =  json.loads(res_post.data.decode('utf-8').replace("'", "\'"))
            self.feedbacks_list.append(posted_feedback)

        
        for feedback_created in self.feedbacks_list:
            self.delete_feedback(feedback_created['id'])
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()