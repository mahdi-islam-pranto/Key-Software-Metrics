def example_function(x, y):
    if x > y:
        print("x is greater than y.")
    elif x < y:
        print("x is less than y.")
    else:
        print("x is equal to y.")

    for i in range(x):
        print(i)

    while y > 0:
        y -= 1
        print(y)