#! python3
# Remove "-" from phone number

tn = input('Enter TN: ')

tn = tn.split('-')[0] + tn.split('-')[1] + tn.split('-')[2]

print ('\n\n' + tn + '\n\n')
