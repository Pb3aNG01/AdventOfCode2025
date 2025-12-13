with open ("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def part1(lines):
    total = 0
    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if char != "@": continue # only process "@" cells
            neighborcount = 0
            for offsetr in [-1, 0, 1]:
                for offsetc in [-1, 0, 1]:
                    if offsetr == 0 and offsetc == 0: continue # skips itself
                    nr, nc = r + offsetr, c + offsetc # sets neighbor row and col
                    if 0 <= nr < len(lines) and 0 <= nc < len(row): # boundary check
                        if lines[nr][nc] == "@":
                            neighborcount += 1
            if neighborcount < 4:
                total += 1
    
    return total
            
def part2(lines):
    total = 0
    while True:
        copy = [list(row) for row in lines]
        opcount = 0
        for r, row in enumerate(lines):
            for c, char in enumerate(row):
                if char != "@": continue # only process "@" cells
                neighborcount = 0
                for offsetr in [-1, 0, 1]:
                    for offsetc in [-1, 0, 1]:
                        if offsetr == 0 and offsetc == 0: continue # skips itself
                        nr, nc = r + offsetr, c + offsetc # sets neighbor row and col
                        if 0 <= nr < len(lines) and 0 <= nc < len(row): # boundary check
                            if lines[nr][nc] == "@":
                                neighborcount += 1
                if neighborcount < 4:
                    copy[r][c] = "x"
                    opcount += 1
        if opcount == 0: break
        total += opcount
        lines = copy

    return total

if __name__ == "__main__":
    #print(part1(lines))
    print(part2(lines))