# This program read in a students percentages 
# And prints out the corresponding grade
# author: Tanya San Juan

percentage = float (input ('Enter the percentage: '))
#print (percentage)

if percentage < 0 or percentage > 100: 
    print ('Please enter a number between 0 and 100')
elif percentage < 40: # we it is greatet than 0 
    print ('Fail')
elif percentage < 50: # Between 40 and 49
    print ('Pass')
elif percentage < 60: # Between 50 and 59 
    print ('Meriti')
elif percentage < 70: # Betweeen 60 and 69
    print ('Merit2')
else: # The onlu option left is between 70 and 100 
    print ('Distintion')