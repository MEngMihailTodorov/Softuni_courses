from collections import deque


def math_operations(*args: float, **kwargs):
    kwargs_dict = dict(kwargs)
    args_queue = deque(args[:len(args) + 1:])
    counter = 0

    while args_queue:
        if counter % 4 == 0:
            kwargs_dict["a"] += args_queue.popleft()
            print(kwargs_dict)

        elif counter % 4 == 1:
            kwargs_dict["s"] -= args_queue.popleft()
            print(kwargs_dict)

        elif counter % 4 == 2:
            if args_queue[0] != 0:
                kwargs_dict["d"] = kwargs_dict["d"] / args_queue.popleft()
                print(kwargs_dict)
            else:
                pass
        else:
            kwargs_dict["m"] *= args_queue.popleft()
            print(kwargs_dict)

        counter += 1

    return kwargs_dict


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))