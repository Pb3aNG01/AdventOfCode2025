with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

ranges, nums = [], []
count, mid = 0, 0 # answer variable and index of the empty line separating ranges and numbers respectively

for i in range(len(lines)):
    if lines[i] == "":
        mid = i
        break
    ranges.append(lines[i])

for i in range(mid + 1, len(lines)):
    nums.append(int(lines[i]))

ranges = [list(map(int, r.split("-"))) for r in ranges]
ranges.sort()

def part1(c):

    for x in nums:
        for y in ranges:
            if y[0] <= x <= y[1]:
                c+=1
                break

    return c

def part2(c):
    prev = None

    for x, y in ranges:
        if prev is None:
            prev = (x, y)
        elif prev[1] < x:
            c += prev[1] - prev[0] + 1
            prev = (x, y)
        else:
            prev = (prev[0], max(prev[1],y))

    c += prev[1] - prev[0] + 1

    return c

if __name__ == "__main__":
    print(part1(count))
    print(part2(count))
