
import random
print("Lets play dice")
print("Hit enter to roll")
input()
leaveprogram = 0
while leaveprogram != "q":
    number=random.randint(1,6)
    if number == 1:
        print("[-------------]")
        print("[             ]")
        print("[      O      ]")
        print("[             ]")
        print("[-------------]")
        print("To leave program type 'q'")
        leaveprogram = input()
    if number == 2:
        print("[-------------]")
        print("[             ]")
        print("[   O     O   ]")
        print("[             ]")
        print("[-------------]")
        print("To leave program type 'q'")
        leaveprogram = input()
    if number == 3:
        print("[-------------]")
        print("[      O      ]")
        print("[      O      ]")
        print("[      O      ]")
        print("[-------------]")
        print("To leave program type 'q'")
        leaveprogram = input()
    if number == 4:
        print("[-------------]")
        print("[   O    O    ]")
        print("[             ]")
        print("[   O    O    ]")
        print("[-------------]")
        print("To leave program type 'q'")
        leaveprogram = input()
    if number == 5:
        print("[-------------]")
        print("[   O     O   ]")
        print("[      O      ]")
        print("[   O     O   ]")
        print("[-------------]")
        print("To leave program type 'q'")
        leaveprogram = input()
    if number == 6:
        print("[-------------]")
        print("[  O       O  ]")
        print("[  O       O  ]")
        print("[  O       O  ]")
        print("[-------------]")
        print("To leave program type 'q'")
        leaveprogram = input()
