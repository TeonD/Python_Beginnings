#Explanation The SUSU is all about holding one another accountable
#
#
#
#  Add SuSu Users
print("Who are the members of the SuSu?")

#Declarations/Calls
import calendar
import datetime
import random
from collections import deque #rotate list

# Add Members
users = input("Welcome to your SuSu Admin! Please name your users: ").split()
print("Ok so thats " + str(users) + " correct? For a total of " + str(len(users)) + " savers?")


# Pay In
print("Great! How much is each member willing to put towards their goal?")
payIn = input()
suSuTax = 1   # Declare ...Later

# BiWeekly/Monthly?
print("Awesome! Each member is responsible for $" + str(payIn) + " a payment!")

print("So are we doing BiWeekly or Monthly payments? ")
print("leave in mind both contracts require a min. of 12 months investment.")
paymentplan = input()

# Calculate Monthly Payment and Pot
biwi =['biwieekly', 'biweekl', 'biweek', 'twice', '2', 'bi', 'Biweekly']
if paymentplan in biwi:
    TotalPayments = 24
    print("Right so biweekly payments? Great choice!")
    eachmemrespmthly = 2 * int(payIn) * suSuTax
    paymentpotmthly = int(eachmemrespmthly) * len(users) * int(suSuTax)
else:
    TotalPayments = 12
    print("Alright... You chose Monthly payments! Great choice!")
    eachmemrespmthly = 1 * int(payIn) * suSuTax
    paymentpotmthly = int(eachmemrespmthly) * len(users) * int(suSuTax)

eachmemrespyrly = int(eachmemrespmthly) * 12
print("Each member is responsible for $" + str(eachmemrespmthly) +
      " a month. Thats $" + str(eachmemrespyrly) + " yearly")

print("\nThe monthly payout is $" + str(paymentpotmthly) + " and will be released on the 6th of every month.\n")

# PaymentOrder/Shuffling (random)
print("With that being said, do you want to randomize or leave the members order as is?")
print("You submitted: " + str(users) + "....")
userorder_prompt = input() or "testme"
uoprompt = ['random','randomize','rando','rand', 'ran', 'yes', 'yess', 'yeah', 'ok', 'ye', 'y']
if userorder_prompt.lower() in uoprompt:
    random.shuffle(users)
    print("Alright, then lets mix it up. The new order has been set to ")
    print(str(users))
else:  # Let admin choose user order
    print("Hmm, alright. Sure you want to leave it as is? Last chance.")
    print("You submitted: " + str(users) + "....")
    userorder_change_prompt = input() or "no"
    uocprompt = ['leave', 'leav', 'lea', 'leave i', 'dont change', 'leave it', 'leaveit', 'yes', 'yess', 'yeah', 'y']
    if userorder_change_prompt.lower() not in uocprompt:
        # WRITE ORDER CHANGE SCRIPT
        print("So the current order is: " + str(users))
        print()
    else:
        print("Alright, then lets wrap it up. The order has been set to " + str(users))
        print()
# Who wins this month
print("This months pot is $" + str(paymentpotmthly) + " and goes to: " + users[0] + ".")

# Print Calendar
month = ['Jan.','Feb.','Mar.','Apr.','May','Jun.','Jul.','Aug','Sept.','Oct.','Nov.','Dec.']
year = 2016



count = 12 #One payout a month
while count > 0:
    # Before rotation  print(users[0], month[0])
    x = deque(users)
    x.rotate(-1)
    y = deque(month)
    y.rotate(-1)
    users = x
    month = y
    # After rotation  print(users[0], month[0])
print("Payment: " + str(count) + "   |  " + users[0] + " will recieve $" + str(paymentpotmthly) + " in " + month[0], year)
    count -= 1

# Show schedule script
print("All done, see the tentative payout schedule below.")
print()
print("END")

print("All done, see the tentative payout schedule below.")
print()
print("END")
