#Question 5
#The convert_phone_number function checks for a U.S. 
#phone number format: XXX-XXX-XXXX (3 digits followed by a dash,
#3 more digits followed by a dash, and 4 digits), 
#and converts it to a more formal format that looks like this: (XXX) XXX-XXXX.
# Fill in the regular expression to complete this function.


import re
def convert_phone_number(phone):
  result =re.sub(r'\b(\s)(\d{3})-(\d{3})-(\d{4})\b', r' (\2) \3-\4', phone)
  #result =re.sub(r'(?<!\S)(\d{3})-', r'(\1) ', phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


# x = "this is the phone number 1111-2222-3333"
# test = re.sub(r'(\d{4})-(\d{4})-(\d{4})', r'(\1)\2\3', x)
# print(test)