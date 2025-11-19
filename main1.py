#  let's assume these are the conditions for strong password
# 8 characters minimum
# at least one lowercase character
# at least one uppercase chaarcter
# at least one special symbol
# at least one number

import string

lower= string.ascii_lowercase   #not (), cuz they're not functions but constants
upper= string.ascii_uppercase
num=string.digits
punct=string.punctuation

def pwchecker(word):

    # isnum() and ispunct() do not exist
    # 'any' returns True or False
    has_lower = any(c.islower() for c in word)
    has_upper = any(c.isupper() for c in word)
    has_num   = any(c.isdigit() for c in word)
    has_punct = any(c in punct for c in word)

    if len(word)>8 and has_lower and has_upper and has_num and has_punct:
        return 1
    else:
        return 0

password=input("Enter your password to check its strength ")
ans=pwchecker(password)

if(ans==1):
    print("congrats queen, your password is strong")
else:
    print("my condolences. your pw ain't strong. go to my password generator repository to get a strong one")
