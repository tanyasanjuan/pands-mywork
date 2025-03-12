# # This program puts 10 random numbers into a queue (list), 
# the program should then output all the values in the queue, 
# then take the numbers from the queue one at a time, 
# print it and the current numbers still in the queue. 
# (the command pop(0) takes the first element out of a list)

# import random randint information: https://docs.python.org/3/reference/import.html
import random

# create an empty list
queue = []
numberofNumbers = 10
# populate the queue
rangeTo = 100

for n in range (0, numberofNumbers):
    queue.append(random.randint(0, rangeTo))
print (f'queue is {queue}')

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print (f'Current Number is {currentNumber} and the queue is {queue}')
# we need to add the f string to print the current number and the queue
# the queue is a list and we need to print it as a list
print ('The queue is now empty')