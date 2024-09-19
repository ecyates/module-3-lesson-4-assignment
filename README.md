# Module 3 - Lesson 4 - Regular Expressions
Author: Elizabeth Yates

In this repository, I am completing the following assignment:

## 1. Python Regular Expressions Deep Dive 

Objective: The aim of this assignment is to deepen your practical skills in Python's regular expressions, enhancing your ability to process and manipulate text data. You will tackle a variety of real-world scenarios, applying regex to extract, validate, and transform text effectively.

### Task 1: Email Extraction Enhancement (email_extraction_enhancement.py)

Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains 
(e.g., '[exclude.com](http://exclude.com/)'). 

Modify the script to extract all email addresses except those from the specified domain.

Code Example:

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.

Ensure the script still extracts all other valid email addresses. 