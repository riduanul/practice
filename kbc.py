questions = [
    [
        "which language was used to create facebook?", 'Python', 'French',
        "Javascript", "PHP", 'd'
    ],
    [
        "which language was used to create youtube?", 'Python', 'French',
        "Javascript", "PHP", 'a'
    ],
    [
        "which language was used to create google?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create amazon?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create render?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create x?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create snapchat?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create whatsaap?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create alibaba.com?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create spacex?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create instagram?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create ticktok?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create tweeter?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create bing?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
    [
        "which language was used to create chrome?", 'Python', 'French',
        "Javascript", "PHP", 'c'
    ],
]

levels = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
    1250000, 2500000, 5000000, 10000000
]

money = 0

for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for TK. {levels[i]}\n")
  print(f"{question[0]}\n")
  print(f"a. {question[1]}   b. {question[2]}")
  print(f"c. {question[3]}   d. {question[4]}")

  reply = input("\nEnter your answer or press x to quite:\n ")

  if reply == 'x':
    if i == 0:
      money = 0
    else:
      money = levels[i - 1]
    print(f"\nYou Quit the Game, You have won {money} tk")
    break
  elif reply == question[-1]:
    print("------------")
    print("\nCorrect Answer")
    print(f"\ncongratulations! , You have won TK {levels[i]}")
    print("-----------")
    money = levels[i]
    if (i >= 4 and i <= 8):
      money = 10000
    elif i >= 9 and i <= 13:
      money = 320000
    elif i == 14:
      money == 100000
  else:
    print("------------")
    print("wrong Answer\n")
    print(f"correct answer is {question[-1]}\n")
    print(f"You have won {money} tk")
    print("------------")
    break
