# create_question/test.py
import unittest
import json

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.errorpatterns import valid_values

class QuestionListTestCase(BaseUnitTest):
    """This class represents the test case for question list"""


    def test_list_questions_query(self):
        """Test API can list questions (GET request)"""

        # post a valid user manager from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        
        question = valid_values[0]
        question['author_id'] = user_manager['id']
        # post the data
        res_post = self.client().post('/questions/', data=question)
        
        self.assertEqual(res_post.status_code, 201)
        self.assertIn(question['title'], str(res_post.data))

        # make the get request list
        res = self.client().get('/questions/')
        
        # verify if posted data is on query response
        self.assertEqual(res.status_code, 200)
        self.assertIn(question['title'], str(res.data))

    def test_list_multiple_questions_query(self):
        """Test API can list multiple questions (GET request)"""

        # post a valid user manager from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        
        self.questions_list = []
        for question in valid_values:
            question['author_id'] = user_manager['id']

            # post the data
            res_post = self.client().post('/questions/', data=question)
            posted_question =  json.loads(res_post.data.decode('utf-8').replace("'", "\""))
            self.questions_list.append(posted_question)

            self.assertEqual(res_post.status_code, 201)
            self.assertIn(question['title'], str(res_post.data))

        # make get request list questions
        res = self.client().get('/questions/')
    
        # verify if the posted multiple questions are on request list
        self.assertEqual(res.status_code, 200)
        for question in self.questions_list:
            self.assertIn(question['title'], str(res.data))
        
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()