"""
Mini Project: Number Analyzer
Features:
- User login with 3 attemts
- Collect numbers until user enters 0
- Calculate total, count, average, min, max

Author: Mohammed Arif Hussain

Read Me: Password masking works in standard terminals.
IDLE may display password due to environment limitaion.
"""

import getpass


def login():
    attempts = 0
    
    while attempts < 3:
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if username == "admin" and password == "python123":
            print("Login Successful")
            return True
        else:
            attempts += 1
            print("Wrong credentials X Attempts left: ", 3 - attempts)
    print("Too many attempts, Access Denied")
    return False


def collect_numbers():
    numbers = []
    while True:
        number = int(input("Please enter a number '0 to STOP': "))
        if number == 0:
            break
        numbers.append(number)
    return numbers

def number_analyzer(num):
    total = 0
    count = 0
    if len(num) == 0:
        return 0, 0, 0, None, None
    min_num = num[0]
    max_num = num[0]
    for n in num:
        total += n
        count += 1
        if n < min_num:
            min_num = n
        if n > max_num:
            max_num = n
        average = total/count
    return total, count, average, min_num,  max_num

def main():
    if not login():
        return #stop if login fails
    
    num = collect_numbers()
    total, count, average, min_num, max_num = number_analyzer(num)
    print('Numbers: ', num)
    print('Total: ', total)
    print('Count: ', count)
    print('Average: ', average)
    print('Minimum Number: ', min_num)
    print('Maximum Number: ', max_num)


main()





