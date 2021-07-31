# Uses python3
import sys

def optimal_sequence(n):
    sequences = [[]] * (n + 1)
    sequences[1] = [1]
    min_num_ops = [0] * (n + 1)


    for number in range(2, n + 1):
        min_num_ops[number] = n + 1
        if number % 3 == 0:
            prev = number // 3
            current_min = len(sequences[prev]) + 1
            if current_min < min_num_ops[number]:
                min_num_ops[number] = current_min
                sequences[number] = sequences[prev] + [number]

        if number % 2 == 0:
            prev = number // 2
            current_min = len(sequences[prev]) + 1
            if current_min < min_num_ops[number]:
                min_num_ops[number] = current_min
                sequences[number] = sequences[prev] + [number]

        if number - 1 > 0:
            prev = number - 1
            current_min = len(sequences[prev]) + 1
            if current_min < min_num_ops[number]:
                min_num_ops[number] = current_min
                sequences[number] = sequences[prev] + [number]

    return sequences[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
