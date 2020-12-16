import re

list_email_users  = ["jenny@gmail.com", "jonny@gmail.com", "kevin@yahoo.com", "lina@yahoo.com", "vic@gmail.com", "leandro@outloo.com"]

#gmail = [email for email in list_email_users if re.match("^gmail^", email)]
#Still trying to figure out
#pattern = "gmail"
#for email in list_email_users:
#    if re.search(pattern, email) is not None: 
#        print(email)

list_gmail = [email for email in list_email_users if re.search("gmail", email) is not None]
print(list_gmail)