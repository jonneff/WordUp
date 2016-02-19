"""
This module contains helper functions for classification on selected subreddit comments
within the Reddit corpus.

Functions in this module:
    cleanup:  use regular expressions to clean up comment text, e.g., punctuation etc.
"""

import re

class WordUp(object): 
    def cleanup(body):
        """
        use regular expressions to clean up comment text, e.g., punctuation etc.
        :type body:  unicode str
        :rtype: unicode str
        """
        body = re.sub("&gt;", ">", body) # Recode HTML codes
        body = re.sub("&lt;", "<", body)
        body = re.sub("&amp;", "&", body)
        body = re.sub("&nbsp;", " ", body)
        body = re.sub("^[deleted]$", "", body) # Remove deleted
        body = re.sub("http[[:alnum:][:punct:]]*", " ", body) # Remove URL
        body = re.sub("/r/[[:alnum:]]+|/u/[[:alnum:]]+", " ", body) # Remove /r/subreddit, /u/user
        # body = re.sub("(>.*?\\n\\n)+", " ", body) # Remove quoted comments
        body = re.sub("[[:cntrl:]]", " ", body) # Remove control characters (\n, \b)
        body = re.sub("'", "", body) # Remove single quotation marks (contractions)
        body = re.sub("[[:punct:]]", " ", body) # Remove punctuation
        body = re.sub("\\s+", " ", body) # Replace multiple spaces with single space
        body = body.strip()
        body = body.lower() # Lower case
        return body # Return body (cleaned up text)

    def label(score):
        if int(score) <= -1: 
            return 'neg'
        else: 
            return 'pos'