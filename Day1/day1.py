with open("input", "r") as puzzle_input:
    input_list = puzzle_input.readlines()

print(input_list)

def counter(iterable):
    n = 0
    for i in range(1, len(iterable)):
        print(iterable[i])
        if int(iterable[i].rstrip()) > int(iterable[i - 1].rstrip()):
            n += 1
    return n



print(counter(input_list))