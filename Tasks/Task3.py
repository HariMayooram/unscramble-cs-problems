"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def bangalore_number(number):
  if number[0][0:5] == '(080)':
    return True

def find_codes(codes, number):
  codes['count'] += 1

  if number[0] == '(':
    code = number[number.find('(') + 1:number.rfind(')')]
    if code == '080':
      codes['fixed_line_count'] += 1
  elif number[0:3] == '140':
    code = '140'
  else:
    code = number[0:4]
  
  if code in codes:
    codes[code] += 1
  else:
    codes[code] = 1
  
  return codes

def calls_from_bangalore_numbers():
  codes = {}
  codes['count'] = 0
  codes['fixed_line_count'] = 0

  for call in calls:
    if bangalore_number(call):
      codes = find_codes(codes, call[1])
  
  return codes

if __name__ == "__main__":
  codes = calls_from_bangalore_numbers()

  keycodes = list(codes.keys())
  keycodes.remove('count')
  keycodes.remove('fixed_line_count')
  keycodes.sort()
  
  fl_to_fl_ratio = codes['fixed_line_count'] / codes['count'] * 100

  print('The numbers called by people in Bangalore have codes:')
  print('\n'.join(keycodes))
  print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(fl_to_fl_ratio))