# -*- coding: utf-8 -*-

# submission/delete/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.errorpatterns import valid_values

class SubmissionDeleteTestCase(BaseUnitTest):
    """This class represents the test case for delete submissions"""


    def delete_submission(self, id):
        """Test API can delete a submission (delete request)"""

        # make a query to delete submission passing the posted user id
        res = self.client().delete('/submissions/{}'.format(id))
        
        # # check if the submission was deleted
        self.assertEqual(res.status_code, 200)
        self.assertIn('Submission deleted successfully.', str(res.data))


    def test_delete_not_existing_submission(self):
        """Test API can delete submission passing a not existent id (DELETE request)"""

        # user passing not existing submission id
        res = self.client().delete('/submissions/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('Submission not found.', str(res.data))        

    

    def test_delete_submissions(self):
        """Test API can create submissions to be deleted"""
        
        # post a valid user manager from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)      
        # post a valid user student from dataset
        user_student = BaseUnitTest.generate_valid_student(self, 0)      
        
        # post a valid user manager from dataset
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)      

        self.submissions_list = []        
        # Load the test dataset for valid  submissions  
        for submission in valid_values:
            # set the student and question created to current submission to be posted
            submission['student_id'] = user_student['id']
            submission['question_id'] = question['id']
    
            # post the submission
            res_post = self.client().post('/submissions/', data=submission)
            posted_submission =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
        
            # verify if submission was created with success
            self.assertEqual(res_post.status_code, 201)
            self.submissions_list.append(posted_submission)

        
        for submission_created in self.submissions_list:
            self.delete_submission(submission_created['id'])
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()