import re
from email.utils import parseaddr

class EmailAddressParser:
    def __init__(self, text):
        self.text = text
        # Regex for validating email addresses:
        self.email_regex = re.compile(r"^[A-Za-z][\w\.-]*@[A-Za-z0-9.-]+\.\w{2,}$")
    
    def parse(self):
        # Split input by commas or whitespace:
        candidates = re.split(r'[,\s]+', self.text)
        
        valid_emails = set()
        for candidate in candidates:
            # parseaddr extracts email part if candidate has name + email:
            _, email = parseaddr(candidate)
            if email and self.email_regex.fullmatch(email):
                valid_emails.add(email.lower())  # normalize case
        
        # Return sorted list
        return sorted(valid_emails)
