
# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter


#email_address = input("What is your email address?  (format: firstName.lastName@exam.com) ")
email_address = ""
searching="@" 
searching2="."

def is_valid_email(email_address):
    end = email_address.index(searching)
    for i in email_address:
        if searching in email_address:
            return(True)
        elif searching2 in email_address[:end]:
            return(True)
        else:
            return(False)

def name_from_email(email_address):
    if is_valid_email(email_address):
        end1 = email_address.index(searching)
        end2 = email_address.index(searching2)
        print(email_address[end2+1:end1], email_address[:end2] )


print(name_from_email("elek.viz@exam.com"))
