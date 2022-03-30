# -*- coding: utf-8 -*-

# question/delete/test.py
import unittest
import random

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.users import valid_users
from app.tests.data.errorpatterns import valid_values
import json

class QuestionDeleteTestCase(BaseUnitTest):
    """This class represents the test case for delete questions"""


    def delete_question(self, id):
        """Test API can delete a question (delete request)"""

        # make a query to delete question passing the posted user id
        res = self.client().delete('/questions/{}'.format(id))
        
        # # check if the api can get the new user posted by the id
        self.assertEqual(res.status_code, 200)
        self.assertIn('Question deleted successfully.', str(res.data))


    def test_delete_not_existing_question(self):
        """Test API can delete question passing a not existent id (DELETE request)"""

        #  user passing invalid parameter
        res = self.client().delete('/questions/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('Question not found.', str(res.data))        
 

    def test_delete_questions(self):
        """Test API can create questions to be deleted"""
        
        # post a valid user
        user = random.choice(valid_users['professor'])
        res_post_user = self.client().post('/users/', data=user)
        posted_user =  json.loads(res_post_user.data.decode('utf-8').replace("'", "\""))

        # verify if user created with success
        self.assertEqual(res_post_user.status_code, 201)

        # List to store in this test session the created questions
        self.questions_list = []

        # Load the test dataset for valid values questionsrns        
        for question in valid_values:

            # set the created user id as author id for the new question
            question['author_id'] = posted_user['id']        

            # post the question and store on list
            res_post = self.client().post('/questions/', data=question)
            posted_question =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
            self.questions_list.append(posted_question)

            # verify if question- created with success
            self.assertEqual(res_post.status_code, 201)
            # verify with the returned user has the same name/email that initial values
            self.assertIn(question['title'], str(res_post.data.decode('unicode-escape')))
        
        for question_created in self.questions_list:
            self.delete_question(question_created['id'])
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()