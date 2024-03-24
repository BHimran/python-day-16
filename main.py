import time


name = input('Enter your name: ')
recenttime = time.strftime('%H:%M:%S')
Recenttime = int(time.strftime('%H'))
if(4<=Recenttime<12):
    print('GOOD MORNING','its',recenttime)
elif(12<=Recenttime<17):
    print('GOOD EVENING','its',recenttime)
else:
    print('GOOD NIGHT','its',recenttime)