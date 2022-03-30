# -*- coding: utf-8 -*-

# question/get_by_id/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.questions import valid_values
from app.tests.data.invalid_ids import invalid_ids
        
class QuestionGetByIdTestCase(BaseUnitTest):
    """This class represents the test case for get question by id"""


    def list_question_invalid_id(self, invalid_id):
        """Test API can get question passing invalid id (GET request)"""

        # make a query question passing invalid parameter
        res = self.client().get('/questions/'+invalid_id)
        self.assertEqual(res.status_code, 400)
        self.assertIn('The id value is not valid.', str(res.data))      

    def list_question_query(self, question):
        """Test API can get question by id (GET request)"""

        # post the question
        res_post = self.client().post('/questions/', data=question)
        posted_data =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
        
        self.assertEqual(res_post.status_code, 201)
        self.assertIn(question['title'], str(res_post.data.decode('unicode-escape')))

        # make a query question passing the question posted id
        res = self.client().get('/questions/{}'.format(posted_data['id']))
        
        # check if the api can get the new question posted by the id
        self.assertEqual(res.status_code, 200)
        self.assertIn(question['title'], str(res.data))


    def test_list_by_id_with_invalid_parameter(self):
        """Test API can get question passing invalid id (GET request)"""
        
        # Load the test dataset for invalids id       
        for id in invalid_ids:
            self.list_question_invalid_id(id)


    def test_list_by_id_not_existing_question(self):
        """Test API can get question passing a not existent id (GET request)"""

        # make a query question passing invalid parameter id
        res = self.client().get('/questions/78327fc6-080d-4e45-9ead-3862e30160a8')
        self.assertEqual(res.status_code, 404)
        self.assertIn('Question not found.', str(res.data))        


    def test_get_by_id_query(self):
        """Test API can get question by id (GET request)"""

        # post a valid user manager from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)      
        question = valid_values[0]
        
        # Load the test dataset for valid student questions        
        for question in valid_values:
            question['author_id'] = user_manager['id']
            self.list_question_query(question)
        
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()