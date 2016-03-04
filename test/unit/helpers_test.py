#!/usr/bin/env python

import sys
import unittest
import unicodecsv
# import csv
from app.helpers import WordUp

class TestWordUp(unittest.TestCase): 	
    # CONSIDER ADDING PYTEST FIXTURES FOR CONSTANTS 
    def setUp( self): 
        self.w = WordUp() 

    def test_html_codes(self):
        body = u'&gt;her kids have to pay the debt i was stuck making &lt;$55k to ship &amp; drive day to&nbsp;day'
        actual = self.w.cleanup(body)
        expected = u'>her kids have to pay the debt i was stuck making <$55k to ship drive day to day'
        self.assertEqual(expected, actual)

    '''def test_remove_deleted(self):
        body = u'[deleted]'
        actual = self.w.cleanup(body)
        expected = u''
        self.assertEqual(expected, actual)
    '''
        
    def test_remove_url(self):
        body = u'test url https://www.reddit.com/r/investing/comments/3pulwr/i_just_won_a_25000_lawsuit_what_do_i_do/'
        actual = self.w.cleanup(body)
        expected = u'test url'
        self.assertEqual(expected, actual)
        
    def test_remove_subreddit_user(self):
        body = u'test remove reddit slashes /r/personalfinance /u/fakeuser'
        actual = self.w.cleanup(body)
        expected = u'test remove reddit slashes'
        self.assertEqual(expected, actual)
    
    def test_remove_control_chars(self):
        body = u'remove control chars \n they would drop you in a \b second'
        actual = self.w.cleanup(body)
        expected = u'remove control chars they would drop you in a second'
        self.assertEqual(expected, actual)
        
    def test_remove_single_quotes(self):
        body = u"remove single quotes it's in it's interest"
        actual = self.w.cleanup(body)
        expected = u'remove single quotes its in its interest'
        self.assertEqual(expected, actual)
    
    def test_remove_punctuation(self):
        body = u'test punctuation!  no really, bullfrogs? such is life:  it is.'
        actual = self.w.cleanup(body)
        expected = u'test punctuation no really bullfrogs such is life it is'
        self.assertEqual(expected, actual) 
        
    def test_remove_multiple_spaces(self):
        body = u'  leading and multiple     spaces       should     be       removed   '
        actual = self.w.cleanup(body)
        expected = u'leading and multiple spaces should be removed'
        self.assertEqual(expected, actual)
        
    def test_lower_case(self):
        body = u'THIS IS ALL UPPERCASE BUT SHOULD BE LOWER'
        actual = self.w.cleanup(body)
        expected = u'this is all uppercase but should be lower'
        self.assertEqual(expected, actual)

    # def __del__(self):
        # close files in destructor method
        # destructors are controversial in Python but while seems awkward in this case
        # IMPORTANT:  avoid circular references with other classes when using destructor.
        # self.f.close()

if __name__ == '__main__':
    unittest.main()

