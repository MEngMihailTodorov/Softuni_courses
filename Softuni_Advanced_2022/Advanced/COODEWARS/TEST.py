import math
name_show = input()
show_length = float(input())
break_length = float(input())

break_true = 0.625 * break_length

if break_true >= show_length:
    break_true = math.ceil(break_true)
    # print(break_true)
    # print(show_length)
    print(f"You have enough time to watch {name_show} and left with {abs(break_true - show_length):.0f} minutes free time.")
else:
    break_true = math.floor(break_true)
    # print(break_true)
    # print(show_length)
    print(f"You don't have enough time to watch {name_show}, you need {abs(break_true - show_length):.0f} more minutes.")