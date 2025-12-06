with open ("testinput.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def part1(lines) -> int:
    total = 0
    for line in lines:
        batteries = list(line)
        tens = max(batteries[:-1]) # Find the largest digit for tens place excluding the last digit
        tens += (max(batteries[batteries.index(tens) + 1:]))  # Find the largest digit for ones place after the index of the tens place and appends it to the tens

        total += int(tens)

    return total

def part2(lines) -> int:
    total = 0
    for line in lines:
        batteries = list(map(int, line))
        jolts = 0

        for i in range(11):
            biggest_num = (max(batteries[:i - 11])) # gets the first biggest number in the list
            batteries = batteries[batteries.index(biggest_num) + 1:] # removes all numbers up to and including the biggest number found
            jolts = (jolts * 10 ) + int(biggest_num) # adds the biggest number to the jolts variable in the correct place value

        jolts = (jolts * 10 ) + max(batteries) # adds the last remaining biggest digit such that there will be 12 batteries activated
        total += int(jolts)


    return total


if __name__ == "__main__":
    print(part1(lines))
    print(part2(lines))