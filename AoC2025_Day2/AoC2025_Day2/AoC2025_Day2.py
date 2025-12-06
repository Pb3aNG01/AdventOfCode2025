with open ('testinput.txt', 'r') as file:
    lines = file.read().strip()

ranges = [list(map(int, part.split('-'))) for part in lines.split(',')]
nums = sum((list(range(x, y + 1)) for x, y in ranges), [])

def part1(input) -> int:
    invalid_total = 0

    for num in nums:
        s = str(num)
        if len(s) % 2 == 0 and (s[:len(s)//2] * 2) == s:
            invalid_total += num

    return invalid_total

def part2(input) -> int:
    invalid_total = 0

    for num in nums:
        s = str(num)
        for i in range(2, len(s) + 1):
            if len(s) % i == 0 and (s[:len(s)//i] * i) == s:
                invalid_total += num
                break

    return invalid_total

if __name__ == "__main__":
    print(part1(nums))
    print(part2(nums))