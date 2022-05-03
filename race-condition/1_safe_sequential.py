import time
import threading
import random

account_1 = 1000
account_2 = 1000

def check_balance(expect_total=2000):
        total = account_1 + account_2
        if total != expect_total:
           print(f"\t======= INVALID AMOUNT: ${total} ======= ")



check_balance()

def move_funds_from_1_to_2():
    global account_1, account_2

    amount = random.randint(0, 10)
    account_1 -= amount
    account_2 += amount
    check_balance()

def move_funds_from_2_to_1():
    global account_1, account_2
     
    amount = random.randint(0, 10)
    account_2 -= amount
    account_1 += amount
    check_balance()

while True:
       move_funds_from_1_to_2()
       move_funds_from_2_to_1()
        

