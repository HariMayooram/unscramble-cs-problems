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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def list_of_telemarketers():
    o_c = set()
    i_c = set()
    i_t = set()
    o_t = set()

    for call in calls:
        o_c.add(call[0])
        i_c.add(call[1])
        
    for text in texts:
        o_t.add(text[0])
        i_t.add(text[1])

    return o_c - i_c & o_c - i_t & o_c - i_c

if __name__ == "__main__":
    possible_telemarketers = set()

    possible_telemarketers = list_of_telemarketers()
    
    print('These numbers could be telemarketers: ')
    print('\n'.join(sorted(possible_telemarketers)))