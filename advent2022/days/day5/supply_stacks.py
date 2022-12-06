from collections import deque

def part_one():
    stacks_input, instructions = open('prompt_stacks.txt').read().split('\n\n')

    print(stacks_input)
    num_stacks = int(stacks_input[-1])
    stacks = [[] for _ in range(num_stacks)]
    indices = [4*i++1 for i in range(num_stacks)]

    for i in reversed(stacks_input.splitlines()[:-1]):
        print(i)
        elements = [i[index] for index in indices]
        for stack, element in enumerate(elements):
            if element != ' ':
                stacks[stack].append(element)

    print(stacks)

part_one()