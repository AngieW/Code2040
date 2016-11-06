import requests
import json
import datetime


print("#####################  initial API connection  #############################")

headers = {'content-type': 'application/json'}

token = '161fdc48632480b96fa68fe9abf8c8cd'
github = 'https://github.com/AngieW/Code2040'

JSON = {'token': token, 'github': github}

request = requests.post('http://challenge.code2040.org/api/register', params=JSON, headers=headers)

print(request.text)



tokenJSON = {'token': token}

print("#####################  reverse a string  #############################")

string = requests.post('http://challenge.code2040.org/api/reverse', params=tokenJSON, headers=headers)

print('String to reverse:'+string.text)

reverseString = string.text[::-1]

print('Reversed String:'+reverseString)


reverseStringJSON = {'token': token, 'string': reverseString}
validation = requests.post('http://challenge.code2040.org/api/reverse/validate', params=reverseStringJSON, headers=headers)

print((validation).text)


print('#####################  Needle in a Haystack  #############################')
#find a string in an array of strings

response = requests.post('http://challenge.code2040.org/api/haystack', params=tokenJSON, headers=headers)
haystackInfo= json.loads(response.text)
needle = haystackInfo['needle'] 
haystack = haystackInfo['haystack'] 

print("Needle", needle)
print("Haystack", haystack)

needleIndex = []

for i in range(len(haystack)):
    if haystack[i] == needle:
        print('Needle Found')
        needleIndex = i
    else:
        print('Searching...')
print()
print('Needle index:', needleIndex)
print()

answer = {'token': token, 'needle': needleIndex}
validation = requests.post('http://challenge.code2040.org/api/haystack/validate', params=answer, headers=headers)
print((validation).text)




print('#####################  Prefix   #############################')

#remove strings with a given prefix from an array

response = requests.post('http://challenge.code2040.org/api/prefix', params=tokenJSON, headers=headers)
prefixData = json.loads(response.text)

prefix = prefixData['prefix'] 
array = prefixData['array'] 

print()
print("Prefix:", prefix)
print()
print("Array:", array)
print()

arrayNew = []

# Compare the prefix with each string in the list
for i in range(len(array)):
    if (prefix in array[i]) == False:
        arrayNew.append(array[i])

print("New array:", arrayNew)

answer2 = {'token': token, 'array': arrayNew}

validate = requests.post('http://challenge.code2040.org/api/prefix/validate', json=answer2, headers=headers)



print(validate.text)
print('#####################  Date Challenge   #############################')

#Add seconds to given date

response = requests.post('http://challenge.code2040.org/api/dating', params=tokenJSON, headers=headers)
dateInfo = json.loads(response.text)

date_stamp = dateInfo['datestamp']
interval = dateInfo['interval']

print('Date Stamp String: ', date_stamp)
print('Interval str in seconds: ', interval)

print("Info from 'date_stamp': ")
date_year = int(date_stamp[0:4])
print('date_year = ', date_year)

date_month = int(date_stamp[5:7])
print('date_month = ', date_month)

date_day = int(date_stamp[8:10])
print('date_day = ', date_day)

date_hrs = int(date_stamp[11:13])
print('date_hrs = ', date_hrs)

date_mins = int(date_stamp[14:16])
print('date_mins = ', date_mins)

date_seconds = int(date_stamp[17:19])
print('date_seconds = ', date_seconds)



a = datetime.datetime(date_year,date_month,date_day,date_hrs,date_mins,date_seconds) # create datetime
b = a + datetime.timedelta(0,int(interval)) # days, seconds (add more seconds)
print a.isoformat()
newDate = b.isoformat() + 'Z'
print newDate


dateJSON = {'token': token, 'datestamp': newDate}
validate = requests.post('http://challenge.code2040.org/api/dating/validate',json=dateJSON, headers=headers)

print(validate.text)

print('#####################  Done!!   #############################')

