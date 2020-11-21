"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
import operator 

time = {}
for call in calls:
    if call[0] not in time:
        time[call[0]] = 0
    if call[1] not in time:
        time[call[1]] = 0
    time[call[0]] += int(call[3])
    time[call[1]] += int(call[3])

longest_time_key = max(time.items(), key=operator.itemgetter(1))[0]
longest_time_value = time[longest_time_key]

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(longest_time_key, longest_time_value))