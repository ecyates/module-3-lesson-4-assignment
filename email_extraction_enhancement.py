# Task 1: Email Extraction Enhancement

# Problem Statement: You have a script that extracts email addresses from a text 
# but needs to be refined to exclude certain domains 
# (e.g., '[exclude.com](http://exclude.com/)'). 

# Modify the script to extract all email addresses except those from the specified domain.

# Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.

# Ensure the script still extracts all other valid email addresses. 

import re

def extract_valid_emails(text):
    '''This function takes the original string and extracts valid emails, removing any invalid domains (i.e., exclude.com)'''
    valid_emails = []
    try: 
        # First extracts the valid emails from the text in a list.
        emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
        # Then iterates over the emails
        for email in emails:
            # If the email uses the invalid domain name (exclude.com), it's not included in the new list
            if not re.search(r"[A-Za-z0-9._%+-]+@exclude.com", email):
                valid_emails.append(email)
    # Catch any errors
    except Exception as e:
        print(f"There was an error: {e}.")
    finally:
        # Returns valid emails.
        return valid_emails

def main():
    # Defines a text with emails in it. 
    text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
    # Extracts the valid emails from the text in a list.
    valid_emails = extract_valid_emails(text)
    print("Here are the valid emails:")
    for email in valid_emails:
        print(email)
    
    # Testing what happens if there's an error
    valid_emails = extract_valid_emails(123)
    print(valid_emails)

if __name__ == "__main__":
    main()