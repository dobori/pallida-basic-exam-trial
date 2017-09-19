
# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter


#email_address = input("What is your email address?  (format: firstName.lastName@exam.com) ")
email_address = ""

# def is_valid_email(email_address):
#     if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email_address) != None:)
#         return True
#         print("This is a valid email address")
#     else:
#         return False
#         print("This is not a valid email address")

# def name_from_email():
#     pass

# is_valid_email("elek.vizexam.com")

searching="@" 
searching2="."

def name_from_email(email_address):
    end1 = email_address.index(searching)
    end2 = email_address.index(searching2)
    print(email_address[end2+1:end1], email_address[:end2] )

print(name_from_email("elek.viz@exam.com"))
