
while True:
    try:
        text = input()
        times = input()

        output = text * int(times)
        print(output)
    except ValueError:
        print("Variable times must be an integer")