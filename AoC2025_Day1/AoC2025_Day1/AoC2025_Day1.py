with open ('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1(nums) -> int:
    dial, counter = 50, 0

    for num in nums:
        direction, rotations = num[0], int(num[1:])

        if direction == 'L':
            dial -= rotations
        else:
            dial += rotations
        dial %= 100

        if dial == 0:
            counter += 1

    return counter

def part2(nums) -> int:
    dial, counter = 50, 0

    for num in nums:
        direction, rotations = num[0], int(num[1:])
        if direction == 'L':
            div = rotations // 100
            mod = rotations % 100
            counter += div
            if (dial - mod) < 0 and dial != 0:
                counter += 1
            dial -= rotations
        else:
            div = rotations // 100
            mod = rotations % 100
            counter += div
            if (dial + mod) > 100:
                counter += 1
            dial += rotations
        dial %= 100

        if dial == 0:
            counter += 1

    return counter

if __name__ == "__main__":
    #print(part1(lines))
    print(part2(lines))

