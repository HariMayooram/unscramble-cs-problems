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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def countNumbers(recordList1, recordList2):
    count_set1 = set()
    count_set2 = set()

    for record in recordList1:
        count_set1.add(record[0])
        count_set1.add(record[1])
    
    for record in recordList2:
        count_set2.add(record[0])
        count_set2.add(record[1])

    count_set = count_set1.union(count_set2)
    
    return len(count_set)

print('There are {} different telephone numbers in the records'.format(countNumbers(texts, calls)))