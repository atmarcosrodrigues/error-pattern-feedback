# -*- coding: utf-8 -*-

# feedback/edit/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.feedbacks import valid_values
from app.tests.data.invalid_ids import invalid_ids
        
class FeedbackEditTestCase(BaseUnitTest):
    """This class represents the test case for edit feedback by id"""

    def edit_feedback_invalid_id(self, invalid_id):
        """Test API can put feedback passing invalid id (put request)"""

        # make a edit feedback passing invalid parameter
        res = self.client().put('/feedbacks/'+invalid_id)
        self.assertEqual(res.status_code, 400)
        self.assertIn('The id value is not valid.', str(res.data))      

    def edit_feedback_query(self, feedback):
        """Test API can put feedback by id (put request)"""

        feedback_data = {
            'title' : 'Update to your feedback',
            'message' : 'This submission have a review contact your programming professor for more information.'
        }
        # make a edition to feedback passing the id
        res = self.client().put('/feedbacks/{}'.format(feedback['id']), data=feedback_data)
        
        # check if the api can put the new feedback posted by the id
        self.assertEqual(res.status_code, 200)
        self.assertIn(feedback_data['title'], str(res.data))


    def test_edit_id_with_invalid_parameter(self):
        """Test API can put feedback passing invalid id (put request)"""
        
        # Load the test dataset for invalids id       
        for id in invalid_ids:
            self.edit_feedback_invalid_id(id)


    def test_edit_not_existing_feedback(self):
        """Test API can edit feedback passing a not existent id (put request)"""

        feedback_data = { 'title' : 'Feedback Update', 'message' : 'This submission have a review contact your programming professor for more information.'}        # make a query feedback passing not existing id feedback
        res = self.client().put('/feedbacks/78327fc6-080d-4e45-9ead-3862e30160a8', data=feedback_data)
        
        self.assertEqual(res.status_code, 404)
        self.assertIn('Feedback not found.', str(res.data))        


    def test_edit_query(self):
        """Test API can put feedback by id (put request)"""

        # post a valid user manager, student and question from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        user_student = BaseUnitTest.generate_valid_student(self, 0)
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)
        
        # create a submission from student to question 
        submission = BaseUnitTest.generate_valid_submission(self, student_id=user_student['id'],
                                        question_id=question['id'], index_submission=0)
        
        self.feedbacks_list = []
        
        # Load the test dataset for valid student feedbacks        
        for feedback in valid_values:
            # create a feedback from user manager to generated submission
            feedback = valid_values[0]
            feedback['author_id'] = user_manager['id']
            feedback['submission_id'] = submission['id']
            
            # post the data
            res_post = self.client().post('/feedbacks/', data=feedback)
            posted_feedback =  json.loads(res_post.data.decode('utf-8').replace("'", "\'"))
            self.feedbacks_list.append(posted_feedback)

        # Edit all created feedbacks
        for feedback in self.feedbacks_list:
            self.edit_feedback_query(feedback)
        
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()