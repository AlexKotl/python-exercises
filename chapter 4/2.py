guess_me = 7
start = 1

while True:
    if guess_me == start:
        print("Right");
        break
    elif start < guess_me:
        print("Too low");
        start += 1
    else:
        print("oops")
