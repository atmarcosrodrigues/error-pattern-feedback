# -*- coding: utf-8 -*-

# question/create/test.py
import unittest
import json
import random

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.users import valid_users
from app.tests.data.questions import valid_values, invalid_values

class QuestionCreateTestCase(BaseUnitTest):
    """This class represents the test case for create questions"""

    def create_question(self, question):
        """Test API can create a question (POST request)"""
        
        # post the question
        res_post = self.client().post('/questions/', data=question)
        
        # verify if question- created with success
        self.assertEqual(res_post.status_code, 201)

        # verify with the returned user has the same name/email that initial values
        self.assertIn(question['title'], str(res_post.data.decode('unicode-escape')))
        self.assertIn(question['description'], str(res_post.data.decode('unicode-escape')))
        

    def test_create_question(self):
        """Test API can create a question (POST request)"""

        # post a valid user
        user = random.choice(valid_users['professor'])
        res_post_user = self.client().post('/users/', data=user)
        posted_user =  json.loads(res_post_user.data.decode('utf-8').replace("'", "\""))

        # verify if user created with success
        self.assertEqual(res_post_user.status_code, 201)

        # Load the test dataset for valid values questionsrns        
        for question in valid_values:

            # set the created user id as author id for the new question
            question['author_id'] = posted_user['id']
            # print (question['title'], question['author_id'])
            self.create_question(question)
        

    def test_create_question_with_invalid_values(self):
        """Test API can create a question with invalid values(POST request)"""
        
        # post a valid user
        user = random.choice(valid_users['professor'])
        res_post_user = self.client().post('/users/', data=user)
        posted_user =  json.loads(res_post_user.data.decode('utf-8').replace("'", "\""))

        # verify if user created with success
        self.assertEqual(res_post_user.status_code, 201)

        # Load the test dataset for valid values questionsrns        
        for question in invalid_values:

            # set the created user id as author id for the new question
            question['author_id'] = posted_user['id']
            res_post = self.client().post('/questions/', data=question)
            
            # verify response error code
            self.assertEqual(res_post.status_code, 400)
            # verify response error message
            self.assertIn("Invalid", str(res_post.data.decode('unicode-escape')))
            
            

        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()