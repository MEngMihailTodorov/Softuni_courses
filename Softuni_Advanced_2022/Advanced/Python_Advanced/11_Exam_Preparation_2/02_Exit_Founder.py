from collections import deque

players_name_queue = deque(map(str, input().split(", ")))

board = [[str(i) for i in input().split()] for row in range(6)]

players_resting_data = {player: 0 for player in players_name_queue}

while True:
    row, col = [int(x) for x in input().strip("()").split(", ")]

    if players_resting_data[players_name_queue[0]]:
        players_resting_data[players_name_queue[0]] -= 1
        players_name_queue.append(players_name_queue.popleft())
        continue

    position = board[row][col]

    if position == "E":
        print(f"{players_name_queue[0]} found the Exit and wins the game!")
        break
    elif position == "T":
        print(f"{players_name_queue[0]} is out of the game! The winner is {players_name_queue[1]}.")
        break
    elif position == "W":
        print(f"{players_name_queue[0]} hits a wall and needs to rest.")
        players_resting_data[players_name_queue[0]] += 1

    players_name_queue.append(players_name_queue.popleft())
