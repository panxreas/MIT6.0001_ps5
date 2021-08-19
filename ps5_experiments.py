"""
    def is_phrase_in(self, story):
        
        phrase = str(self.PhraseTriggers).lower()
        s = str(story).lower()
        count = 0
        
        for section in range(len(s)):
            for word in phrase.split():
                #print(s[section:section+len(word)])
                if word == s[section:section+len(word)]:
                    count += 1
                    #print(count)
                    if count == len(phrase.split()):
                        return True
        if count == len(phrase.split()):
            return True
        else:
            return False


"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 04:32:18 2021

@author: pank
"""
from datetime import timedelta
from datetime import datetime
import time
import string

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    def get_guid(self):
        return self.guid    
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate
    def __str__(self):
        return f'{str(self.guid)} {str(self.title)} {str(self.description)}' 


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTriggers(Trigger):
        
    def is_phrase_in(self, story):
        
        phrase = str(self.PhraseTriggers).lower().split()
        s = str(story).lower()
        
        clean_s = ''
        for char in s:
            if char not in string.punctuation:
                clean_s += char
            else:
                clean_s += ' '    
        clean_story = clean_s.split()
        
        print(phrase)
        print(clean_story)
        
        if all(word in clean_story for word in phrase) == False:
            return False
        
        frst_index = clean_story.index(phrase[0])
        
        if clean_story[frst_index:frst_index + len(phrase)] == phrase:
            return True
        else:
            return False

# Problem 3
class TitleTrigger(PhraseTriggers):

    def __init__(self, PhraseTriggers):
        self.PhraseTriggers = PhraseTriggers
    
    def evaluate(self, story):
        pass

        
        
        
        
symbols   = NewsStory('', 'The purple cow is soft and cuddly.', '', '', datetime.now())  


s1 = TitleTrigger('PURPLE COW')
s2  = TitleTrigger('purple cow')
        
print(s1.evaluate(symbols))
print(s2.evaluate(symbols))        
        
dateT = "3 Oct 2016 17:00:10"
date_output = datetime.strptime(dateT, "%d %b %Y %H:%M:%S")
print(date_output)
print(type(date_output))



