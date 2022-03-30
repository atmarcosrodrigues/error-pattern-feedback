# -*- coding: utf-8 -*-

import unittest
import json
import random
import string

import sys
sys.path.append(".") 
from app import create_app, db

from app.tests.data.users import valid_users
from app.tests.data.questions import valid_values as questions
from app.tests.data.submissions import valid_values as submissions

class BaseUnitTest(unittest.TestCase):
    """This class represents the base test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        # Clean and restore the database to inicial state
        self.delete_db()
        self.create_db()

    def test_start(self):
        self.assertEqual(self.app.config['TESTING'], True)        
        

    def post_valid_user_manager(self, index=0):
        # post a valid user
        user = valid_users['professor'][index]
        res_post_user = self.client().post('/users/', data=user)
        posted_user =  json.loads(res_post_user.data.decode('utf-8').replace("'", "\""))

        # verify if user created with success
        self.assertEqual(res_post_user.status_code, 201)

        return posted_user


    def generate_valid_student(self, index=0):
        # post a valid user
        user = valid_users['student'][index]
        res_post_user = self.client().post('/users/', data=user)
        posted_user =  json.loads(res_post_user.data.decode('utf-8').replace("'", "\""))

        # verify if user created with success
        self.assertEqual(res_post_user.status_code, 201)

        return posted_user

    def select_random_user(self):
        """ Chose randomly a user from test dataset"""
        user_types = ['professor', 'monitor', 'student']
        type_selected = random.choice(user_types)
        return random.choice(valid_users[type_selected])

    def generate_valid_question(self, author_id, index_question=0):
                
        question = questions[index_question]
        question['author_id'] = author_id
        
        # post the received question
        res_post_question = self.client().post('/questions/', data=question)
        posted_question =  json.loads(res_post_question.data.decode('utf-8').replace("'", "\""))

        # verify if user created with success
        self.assertEqual(res_post_question.status_code, 201)

        return posted_question

    def generate_unique_email(self, username):
        characters = list(string.ascii_letters + string.digits)
        domains = ['@ufcg.edu.br', '@gmail.com', "@uol.com", "@hotmail.com", "@test.com"]

        return username +  ''.join(random.sample(characters, 8)) + random.choice(domains) 


    def generate_valid_submission(self, student_id, question_id, index_submission=0):
                
        submission = submissions[index_submission]
        submission['student_id'] = student_id
        submission['question_id'] = question_id
        
        # post the received submission
        res_post_submission = self.client().post('/submissions/', data=submission)
        posted_submission =  json.loads(res_post_submission.data.decode('utf-8').replace("'", "\""))

        # verify if user created with success
        self.assertEqual(res_post_submission.status_code, 201)

        return posted_submission


    def tearDown(self):        
        # Clean and restore the database to inicial state
        self.delete_db()
        self.create_db()

    def create_db(self):
        with self.app.app_context():
            # create all tables
            db.create_all()
    
    def delete_db(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# # Make the tests conveniently executable
# if __name__ == "__main__":
#     unittest.main()