import csv
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

questions = []
with open('questions.csv') as f:
    rows = csv.DictReader(f)
    for row in rows:
        questions.append(row)
       
lecNum = raw_input('Which lecture would you like to practice? ')
if int(lecNum) < 1 or int(lecNum) > 9:
    print('There were only 9 lectures, you silly')
    exit()

clear()

done = []
for i in range(0,len(questions)):
    r = random.randint(0, len(questions)-1)
    row = questions[r]

    if r in done:
        continue

    done.append(r)
 
    if row['lecNo'] == str(lecNum):
        
        print('Question ' + str(r+2))
        print('')
    
        for i in range(1,3):
            print(row['MCQ' + str(i)])
            print('A. ' + row[str(i) + '_A'])
            print('B. ' + row[str(i) + '_B'])
            print('C. ' + row[str(i) + '_C'])
            print('D. ' + row[str(i) + '_D'])
            
            comment = row[str(i) + '_Comments']
            
            if comment:
                print('')
                print('Comment: ' + comment)
            
            print('')
            ans = raw_input('Answer: ')
            actual_ans = row[str(i) + '_Answer']
            
            print('')
            if ans and ans in actual_ans:
                print('True')
            else:
                print('False')
                print('The correct answer was supposedly: ' + str(actual_ans))
            
            print('')
            raw_input('Next question? ')
            clear()

print('Done')   
            
