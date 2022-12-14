from unittest import case

def ageprintOut(yearsLeft, monthsLeft, daysLeft, hoursLeft, minutesLeft, secondsLeft, ageFormat):
    match ageFormat:
        case "1":
            print(f'You have {yearsLeft} years left till 90')

        case "2":
            print(f'You have {monthsLeft} months left till 90')

        case "3":
            print(f'You have {daysLeft} days left till 90')
    
        case "4":
            print(f'You have {hoursLeft} hours left till 90')

        case "5":
            print(f'You have {minutesLeft} minutes left till 90')
        
        case "6":
            print(f'You have {secondsLeft} seconds left till 90')
        
        case "7":
            print(f'You have {yearsLeft} years left till 90, {monthsLeft} months left till 90, {daysLeft} days left till 90, {hoursLeft} hours left till 90, {minutesLeft} minutes left till 90, {secondsLeft} seconds left till 90.')
        case _:
            print('Please select a correct age')

def ageMath(userAge):
    maxAge = 90
    yearsLeft = maxAge - userAge
    monthsLeft = yearsLeft * 12
    daysLeft = monthsLeft * 365
    hoursLeft = daysLeft * 24
    minutesLeft = hoursLeft * 60
    secondsLeft = minutesLeft * 60
    return yearsLeft,monthsLeft,daysLeft,hoursLeft,minutesLeft,secondsLeft

userAge = int(input('\nHow old are you? \n'))
yearsLeft, monthsLeft, daysLeft, hoursLeft, minutesLeft, secondsLeft = ageMath(userAge)

def ageQuestion():
    ageFormat = input('''
What format would you like to view how long you have left till 90?
    1: Years 
    2: months 
    3: days 
    4: Hours
    5: minutes 
    6: seconds    
    7: All 
    Option : ''')
    return ageFormat

ageFormat = ageQuestion()

ageprintOut(yearsLeft, monthsLeft, daysLeft, hoursLeft, minutesLeft, secondsLeft, ageFormat)
        
