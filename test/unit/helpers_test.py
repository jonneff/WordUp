#!/usr/bin/env python

import sys
import unittest
import unicodecsv
from app.helpers import WordUp

class TestWordUp(unittest.TestCase): 	
    # CONSIDER ADDING PYTEST FIXTURES FOR CONSTANTS 
    def setUp( self): 
        self.w = WordUp() 
        self.f = open('data/test.csv', 'rb')
        self.reader = unicodecsv.reader(f, encoding='utf-8')

    def test_cleanup_handles_gt(self):
        row = next(self.reader)
        body = map(lambda line: line[0], row)
        actual = self.w.cleanup(body)
        expected = u'
        self.assertIsNone(result)

    def test_parse_line_method_returns_correct_result(self):
        line = self.goodlog.readline()
        actual = self.parse.parse_line(line) 
        expected = [1389721010,'/svds.com','http://www.svds.com/rockandroll/','198.0.200.105','SILICON VALLEY DATA SCIENC', 
                    37.8858, -122.118, 'Comcast Business Communications, LLC']
        self.assertEqual(expected, actual)
        

    def __del__(self):
        # close files in destructor method
        # destructors are controversial in Python but while seems awkward in this case
        # IMPORTANT:  avoid circular references with other classes when using destructor.
        self.f.close()

if __name__ == '__main__':
    unittest.main()

