# -*- coding: utf-8 -*-

# feedback/reportederros/test.py
import unittest
import json
import random

import sys
sys.path.append(".") 

from app.tests.BaseTest import BaseUnitTest
from app.tests.data.feedbacks import valid_values
from app.tests.data.errorpatterns import valid_values as errorpatterns

        
class FeedbackReportedErrorsTestCase(BaseUnitTest):
    """This class represents the test case for feedback reportederros"""

    def generate_errorpatterns(self):
        errorpatterns_list = []

        # Load the test dataset for valid errorpatterns
        for item in errorpatterns:
            res_post = self.client().post('/errorpatterns/', data=item)
            self.assertEqual(res_post.status_code, 201)

            posted_item = json.loads(res_post.data.decode('utf-8').replace("'", "\'"))
            errorpatterns_list.append(posted_item)
        return errorpatterns_list
    
    def generate_feedbacks(self, author_id, submission_id):
        feedbacks_list = []
        
        # Load the test dataset for valid student feedbacks        
        for feedback in valid_values:
            # create a feedback from user manager to generated submission            
            feedback['author_id'] = author_id
            feedback['submission_id'] = submission_id
            
            # post the data
            res_post = self.client().post('/feedbacks/', data=feedback)
            self.assertEqual(res_post.status_code, 201)

            posted_feedback = json.loads(res_post.data.decode('utf-8').replace("'", "\'"))
            feedbacks_list.append(posted_feedback)
        return feedbacks_list


    def insert_reportederros(self):
        """ Generate valid data from tests dataset and create new error reports"""

        # post a valid user manager, student and question from dataset
        user_manager = BaseUnitTest.post_valid_user_manager(self, 0)
        user_student = BaseUnitTest.generate_valid_student(self, 0)
        question = BaseUnitTest.generate_valid_question(self, user_manager['id'], 0)
        
        # create a submission from student to question 
        submission = BaseUnitTest.generate_valid_submission(self, student_id=user_student['id'],
                                        question_id=question['id'], index_submission=0)
        
        self.feedbacks_list = self.generate_feedbacks(author_id=user_manager['id'], 
                                                     submission_id=submission['id'] )
        self.errorpatterns_list = self.generate_errorpatterns()

        # randomly selects error patterns and inserts them in the registred feedbacks
        for feedback in self.feedbacks_list:

            # randomly select a sample of errorpatterns
            sample_size = random.randint(1, len(self.errorpatterns_list))
            selected_errospatterns = random.sample(self.errorpatterns_list, sample_size)    

            for errorpattern in selected_errospatterns:
                reportederror_data = {
                    'errorpattern_id': errorpattern['id']
                }

                res_post = self.client().post('/feedbacks/{}/reportederros/'.format(feedback['id']), data=reportederror_data)
                # verify if reported error was posted successully
                self.assertEqual(res_post.status_code, 201)
                
        

    def test_insert_reportederrors(self):
        """Test API can post error reports using generated feedbacks an erropattern dataset (post request)"""        
        self.insert_reportederros()

    def test_remove_reportederrors(self):
        """Test API can remove error reports after post it (delete request)"""        
        
        # make a post call to insert valid errorpatterns
        self.insert_reportederros()

        for feedback in self.feedbacks_list:
            # make a query reportederros for the current feedback
            get_reports = self.client().get('/feedbacks/{}/reportederros/'.format(feedback['id']))
            # verify the status resulted from query
            self.assertEqual(get_reports.status_code, 200)
            reports = json.loads(get_reports.data.decode('utf-8').replace("'", "\'"))
            
            # remove each errorreport from current feedback
            for item_report in reports:                
                delete_request = self.client().delete('/feedbacks/{}/reportederros/{}'.format(feedback['id'], item_report['report_id']))
                
                # verify if reported error deleted successfully
                self.assertEqual(delete_request.status_code, 200)
                self.assertIn('Reported Error deleted successfully.', str(delete_request.data) )
            

    def test_list_reportederrors(self):
        """Test API can get error reports after post it (get request)"""        

        # make a post call to insert valid errorpatterns
        self.insert_reportederros()

        for feedback in self.feedbacks_list:
            # make a query reportederros for the current feedback
            get_reports = self.client().get('/feedbacks/{}/reportederros/'.format(feedback['id']))
            
            # verify the status resulted from query
            self.assertEqual(get_reports.status_code, 200)
            reports = json.loads(get_reports.data.decode('utf-8').replace("'", "\'"))
            
            # verify if recovered reports from query are valid erropattens values
            for item_report in reports:
                self.assertIn(item_report['title'], str(errorpatterns))
            


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()