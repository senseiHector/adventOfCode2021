from numpy import *


def day_two_part_one(file):
    with open(file) as f:
        depth = 0
        hor = 0
        for line in f:
            if 'forward' in line:
                hor += int(line.split()[1].strip())
            if 'up' in line:
                depth -= int(line.split()[1].strip())
            if 'down' in line:
                depth += int(line.split()[1].strip())
        print(depth * hor)


def day_two_part_two(file):
    with open(file) as f:
        depth = 0
        hor = 0
        aim = 0
        for line in f:
            if 'forward' in line:
                hor += int(line.split()[1].strip())
                depth += (int(line.split()[1].strip()) * aim)
            if 'up' in line:
                aim -= int(line.split()[1].strip())
            if 'down' in line:
                aim += int(line.split()[1].strip())
        print(depth * hor)


def day_three_part_one(file):
    gamma = ''
    eps = ''
    with open(file) as f:
        tally = {}
        for line in f:
            i = 0
            for val in line:
                if i not in tally:
                    if val == '0':
                        tally[i] = {'0': 1, '1': 0}
                    elif val == '1':
                        tally[i] = {'0': 0, '1': 1}
                else:
                    if val == '0':
                        tally[i]['0'] += 1
                    elif val == '1':
                        tally[i]['1'] += 1
                i += 1
    for k in tally:
        if tally[k]['0'] > tally[k]['1']:
            gamma += '0'
            eps += '1'
        else:
            gamma += '1'
            eps += '0'
    print(int(gamma, 2) * int(eps, 2))


def day_three_part_two(file):
    nums, oxy, co, oxy_tally, co_tally = [], [], [], {}, {}
    with open(file) as f:
        tally = {}
        for line in f:
            nums.append(line)
            get_tally_per_line(tally, line)

    for i in range(12):
        if i == 0:
            oxy = check_line_oxy(i, tally, nums)
            co = check_line_co(i, tally, nums)
        else:
            oxy = check_line_oxy(i, oxy_tally, oxy)
            co = check_line_co(i, co_tally, co)
        oxy_tally = get_tally(oxy)
        co_tally = get_tally(co)
    print(int(oxy[0], 2) * int(co[0], 2))


def get_tally(arr):
    tally = {}
    for line in arr:
        get_tally_per_line(tally, line)
    return tally


def get_tally_per_line(tally, line):
    i = 0
    for val in line:
        if i not in tally:
            if val == '0':
                tally[i] = {'0': 1, '1': 0}
            elif val == '1':
                tally[i] = {'0': 0, '1': 1}
        else:
            if val == '0':
                tally[i]['0'] += 1
            elif val == '1':
                tally[i]['1'] += 1
        i += 1


def check_line_oxy(i, col, arr):
    oxy = []
    if col[i]['0'] > col[i]['1']:
        for line in arr:
            if line[i] == '0':
                oxy.append(line)
    elif col[i]['0'] < col[i]['1']:
        for line in arr:
            if line[i] == '1':
                oxy.append(line)
    else:
        for line in arr:
            if line[i] == '1':
                oxy.append(line)
    return oxy if len(oxy) > 0 else arr


def check_line_co(i, col, arr):
    co = []
    if col[i]['0'] > col[i]['1']:
        for line in arr:
            if line[i] == '1':
                co.append(line)
    elif col[i]['0'] < col[i]['1']:
        for line in arr:
            if line[i] == '0':
                co.append(line)
    else:
        for line in arr:
            if line[i] == '0':
                co.append(line)
    return co if len(co) > 0 else arr


def day_four_part_one(file):
    inputs, boards = [], []
    with open(file) as f:
        count = 0
        board_count = 0
        temp_board = []
        for line in f:
            line = line.strip()
            if count == 0:
                inputs = line.split(',')
                count += 1
            else:
                if line and board_count < 5:
                    temp_line = line.split()
                    temp_line = [{'num': val, 'checked': False} for val in temp_line]
                    temp_board.append(temp_line)
                    board_count += 1
                if board_count == 5:
                    boards.append(temp_board)
                    temp_board = []
                    board_count = 0
    for i, v in enumerate(inputs):
        for board in boards:
            for line in board:
                for n in line:
                    if n['num'] == v:
                        n['checked'] = True
            if i > 5:
                for j in range(5):
                    if all(k['checked'] for k in board[j]) or\
                     all(k['checked'] for k in [board[0][j], board[1][j], board[2][j], board[3][j], board[4][j]]):
                        bingo_sum = 0
                        for row in board:
                            for cell in row:
                                if not cell['checked']:
                                    bingo_sum += int(cell['num'])

                        print(bingo_sum * int(v))
                        return


def day_four_part_two(file):
    inputs, boards = [], []
    with open(file) as f:
        count = 0
        board_count = 0
        temp_board = []
        for line in f:
            line = line.strip()
            if count == 0:
                inputs = line.split(',')
                count += 1
            else:
                if line and board_count < 5:
                    temp_line = line.split()
                    temp_line = [{'num': val, 'checked': False} for val in temp_line]
                    temp_board.append(temp_line)
                    board_count += 1
                if board_count == 5:
                    boards.append(temp_board)
                    temp_board = []
                    board_count = 0
    wins = {}
    for i, v in enumerate(inputs):
        for b_num, board in enumerate(boards):
            if b_num in wins:
                continue
            else:
                for line in board:
                    for n in line:
                        if n['num'] == v:
                            n['checked'] = True
                if i > 5:
                    for j in range(5):
                        if all(k['checked'] for k in board[j]) or\
                         all(k['checked'] for k in [board[0][j], board[1][j], board[2][j], board[3][j], board[4][j]]):
                            if b_num not in wins:
                                wins[b_num] = 1
                            if len(wins) == len(boards):
                                bingo_sum = 0
                                for row in board:
                                    for cell in row:
                                        if not cell['checked']:
                                            bingo_sum += int(cell['num'])

                                print(bingo_sum * int(v))
                                return


def day_five_part_one(file):
    line_tracker = []
    max_x = 0
    max_y = 0
    with open(file) as f:
        for line in f:
            line = line.strip()
            lines = line.split('->')
            x1, y1 = lines[0].split(',')
            x2, y2 = lines[1].split(',')
            x1, y1, x2, y2 = int(x1.strip()), int(y1.strip()), int(x2.strip()), int(y2.strip())
            max_x = max([max_x, x1, x2])
            max_y = max([max_y, y1, y2])
            line_tracker.append([x1, y1, x2, y2])
    line_board = [[0 for j in range(max_y+1)] for i in range(max_x+1)]
    overlaps = 0
    for segment in line_tracker:
        if segment[0] == segment[2]:
            if segment[3] < segment[1]:
                temp = segment[1]
                segment[1] = segment[3]
                segment[3] = temp
            diff = segment[3] - segment[1]

            for i in range(diff+1):
                line_board[segment[0]][segment[1]+i] += 1
                if line_board[segment[0]][segment[1]+i] == 2:
                    overlaps += 1
        elif segment[1] == segment[3]:
            if segment[2] < segment[0]:
                temp = segment[0]
                segment[0] = segment[2]
                segment[2] = temp
            diff = segment[2] - segment[0]
            for i in range(diff+1):
                line_board[segment[0]+i][segment[1]] += 1
                if line_board[segment[0] + i][segment[1]] == 2:
                    overlaps += 1
    print(overlaps)


def day_five_part_two(file):
    line_tracker = []
    max_x = 0
    max_y = 0
    with open(file) as f:
        for line in f:
            line = line.strip()
            lines = line.split('->')
            x1, y1 = lines[0].split(',')
            x2, y2 = lines[1].split(',')
            x1, y1, x2, y2 = int(x1.strip()), int(y1.strip()), int(x2.strip()), int(y2.strip())
            max_x = max([max_x, x1, x2])
            max_y = max([max_y, y1, y2])
            line_tracker.append([x1, y1, x2, y2])
    line_board = [[0 for j in range(max_y+1)] for i in range(max_x+1)]
    overlaps = 0
    for segment in line_tracker:
        if segment[0] == segment[2]:
            if segment[3] < segment[1]:
                temp = segment[1]
                segment[1] = segment[3]
                segment[3] = temp
            diff = segment[3] - segment[1]

            for i in range(diff+1):
                line_board[segment[0]][segment[1]+i] += 1
                if line_board[segment[0]][segment[1]+i] == 2:
                    overlaps += 1
        elif segment[1] == segment[3]:
            if segment[2] < segment[0]:
                temp = segment[0]
                segment[0] = segment[2]
                segment[2] = temp
            diff = segment[2] - segment[0]
            for i in range(diff+1):
                line_board[segment[0]+i][segment[1]] += 1
                if line_board[segment[0] + i][segment[1]] == 2:
                    overlaps += 1
        elif segment[0] < segment[2] and segment[1] < segment[3]:
            x_diff = segment[2] - segment[0]
            for i in range(x_diff+1):
                line_board[segment[0]+i][segment[1]+i] += 1
                if line_board[segment[0] + i][segment[1]+i] == 2:
                    overlaps += 1
        elif segment[2] < segment[0] and segment[1] < segment[3]:
            x_diff = abs(segment[2] - segment[0])
            for i in range(x_diff+1):
                line_board[segment[0] - i][segment[1] + i] += 1
                if line_board[segment[0] - i][segment[1] + i] == 2:
                    overlaps += 1
        elif segment[2] < segment[0] and segment[3] < segment[1]:
            x_diff = abs(segment[2] - segment[0])
            for i in range(x_diff+1):
                line_board[segment[0]-i][segment[1]-i] += 1
                if line_board[segment[0] - i][segment[1]-i] == 2:
                    overlaps += 1
        elif segment[0] < segment[2] and segment[3] < segment[1]:
            x_diff = segment[2] - segment[0]
            for i in range(x_diff+1):
                line_board[segment[0] + i][segment[1] - i] += 1
                if line_board[segment[0] + i][segment[1] - i] == 2:
                    overlaps += 1
    print(overlaps)


def day_six_part_one(file):
    fishes = []
    fish_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
    with open(file) as f:
        for line in f:
            fishes = [x for x in line.strip().split(',')]
    for fish in fishes:
        fish_dict[fish] += 1

    for i in range(80):
        temp_dict = fish_dict.copy()
        fish_dict['8'] = temp_dict['0']
        if fish_dict['7'] != 0:
            fish_dict['6'] = temp_dict['0'] + temp_dict['7']
        else:
            fish_dict['6'] = temp_dict['0']
        fish_dict['0'] = temp_dict['1']
        fish_dict['1'] = temp_dict['2']
        fish_dict['2'] = temp_dict['3']
        fish_dict['3'] = temp_dict['4']
        fish_dict['4'] = temp_dict['5']
        fish_dict['5'] = temp_dict['6']
        fish_dict['7'] = temp_dict['8']
    print(fish_dict)
    print(sum(fish_dict.values()))


def day_six_part_two(file):
    fishes = []
    fish_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
    with open(file) as f:
        for line in f:
            fishes = [x for x in line.strip().split(',')]
    for fish in fishes:
        fish_dict[fish] += 1

    for i in range(256):
        temp_dict = fish_dict.copy()
        fish_dict['8'] = temp_dict['0']
        if fish_dict['7'] != 0:
            fish_dict['6'] = temp_dict['0'] + temp_dict['7']
        else:
            fish_dict['6'] = temp_dict['0']
        fish_dict['0'] = temp_dict['1']
        fish_dict['1'] = temp_dict['2']
        fish_dict['2'] = temp_dict['3']
        fish_dict['3'] = temp_dict['4']
        fish_dict['4'] = temp_dict['5']
        fish_dict['5'] = temp_dict['6']
        fish_dict['7'] = temp_dict['8']
    print(fish_dict)
    print(sum(fish_dict.values()))


def day_seven_part_one(file):
    lines = []
    crabs = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            lines = line.split(',')
    for line in lines:
        crabs.append(int(line))
    crabs.sort()
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - crabs[len(crabs)//2])
    print(fuel)


def day_seven_part_two(file):
    lines = []
    crabs = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            lines = line.split(',')
    for line in lines:
        crabs.append(int(line))
    crabs.sort()
    fuel = 0
    crab_average = int(sum(crabs) / len(crabs))
    for crab in crabs:
        fuel += fuel_expense(abs(crab - crab_average))
    print(fuel)


def fuel_expense(steps):
    fuel = 0
    for step in range(steps+1):
        fuel += step
    return fuel


def day_eight_part_one(file):
    count = 0
    with open(file) as f:
        for line in f:
            output = line.strip().split('|')[1].split()
            for digit in output:
                if len(digit) != 5 and len(digit) != 6:
                    count += 1
    print(count)


def day_eight_part_two(file):
    sum_output = 0
    with open(file) as f:
        for line in f:
            reverse_key = {'1': '', '4': '', '7': '', '8': ''}
            forward_key = {}
            six_digits = set()
            five_digits = set()
            line = line.strip().split('|')
            inp = line[0].split()
            output = line[1].split()
            for digit in inp:
                if len(digit) == 2:
                    if not reverse_key['1']:
                        reverse_key['1'] = digit
                        forward_key[digit] = '1'
                elif len(digit) == 3:
                    if not reverse_key['7']:
                        reverse_key['7'] = digit
                        forward_key[digit] = '7'
                elif len(digit) == 4:
                    if not reverse_key['4']:
                        reverse_key['4'] = digit
                        forward_key[digit] = '4'
                elif len(digit) == 7:
                    if not reverse_key['8']:
                        reverse_key['8'] = digit
                        forward_key[digit] = '8'
                elif len(digit) == 6:
                    six_digits.add(digit)
                else:
                    five_digits.add(digit)
            for digit in six_digits:
                if set(reverse_key['4']) <= set(digit):
                    forward_key[digit] = '9'
                    six_digits.discard(digit)
                    break
            for digit in six_digits:
                if set(reverse_key['1']) <= set(digit):
                    forward_key[digit] = '0'
                else:
                    forward_key[digit] = '6'
                    reverse_key['6'] = digit
            for digit in five_digits:
                if set(reverse_key['1']) <= set(digit):
                    forward_key[digit] = '3'
                    five_digits.discard(digit)
                    break
            for digit in five_digits:
                if set(digit) <= set(reverse_key['6']):
                    forward_key[digit] = '5'
                else:
                    forward_key[digit] = '2'
            output_num = ''
            for digit in output:
                for k in forward_key:
                    if set(k) == set(digit):
                        output_num += forward_key[k]
                        break
            output_num = int(output_num)
            sum_output += output_num
    print(sum_output)


def day_nine_part_one(file):
    with open(file) as f:
        count = 0
        low_sum = 0
        last_one = ''
        last_two = ''
        for line in f:
            line = line.strip()
            count += 1
            if count >= 3:
                for i in range(len(line)):
                    if i == 0:
                        if line[i] > last_one[i] and last_two[i] > last_one[i] and last_one[i+1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                    elif i == len(line) - 1:
                        if line[i] > last_one[i] and last_two[i] > last_one[i] and last_one[i - 1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                    else:
                        if line[i] > last_one[i] and last_two[i] > last_one[i] and last_one[i - 1] > last_one[i] and last_one[i+1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                last_two = last_one
                last_one = line
            if count == 2:
                for i in range(len(line)):
                    if i == 0:
                        if line[i] > last_one[i] and last_one[i+1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                    elif i == len(line) - 1:
                        if line[i] > last_one[i] and last_one[i - 1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                    else:
                        if line[i] > last_one[i] and last_one[i - 1] > last_one[i] and last_one[i+1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                last_two = last_one
                last_one = line
            if count == 1:
                last_one = line
        for i in range(len(last_one)):
            if i == 0:
                if last_two[i] > last_one[i] and last_one[i + 1] > last_one[i]:
                    low_sum += int(last_one[i]) + 1
            elif i == len(last_one) - 1:
                if last_two[i] > last_one[i] and last_one[i - 1] > last_one[i]:
                    low_sum += int(last_one[i]) + 1
            else:
                if last_two[i] > last_one[i] and last_one[i - 1] > last_one[i] and last_one[i + 1] > last_one[i]:
                    low_sum += int(last_one[i]) + 1
        print(low_sum)


def day_nine_part_two(file):
    with open(file) as f:
        count = 0
        low_sum = 0
        last_one = ''
        last_two = ''
        for line in f:
            line = line.strip()
            count += 1
            if count >= 3:
                for i in range(len(line)):
                    if i == 0:
                        if line[i] > last_one[i] and last_two[i] > last_one[i] and last_one[i + 1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                    elif i == len(line) - 1:
                        if line[i] > last_one[i] and last_two[i] > last_one[i] and last_one[i - 1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                    else:
                        if line[i] > last_one[i] and last_two[i] > last_one[i] and last_one[i - 1] > last_one[i] and \
                                last_one[i + 1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                last_two = last_one
                last_one = line
            if count == 2:
                for i in range(len(line)):
                    if i == 0:
                        if line[i] > last_one[i] and last_one[i + 1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                    elif i == len(line) - 1:
                        if line[i] > last_one[i] and last_one[i - 1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                    else:
                        if line[i] > last_one[i] and last_one[i - 1] > last_one[i] and last_one[i + 1] > last_one[i]:
                            low_sum += int(last_one[i]) + 1
                last_two = last_one
                last_one = line
            if count == 1:
                last_one = line
        for i in range(len(last_one)):
            if i == 0:
                if last_two[i] > last_one[i] and last_one[i + 1] > last_one[i]:
                    low_sum += int(last_one[i]) + 1
            elif i == len(last_one) - 1:
                if last_two[i] > last_one[i] and last_one[i - 1] > last_one[i]:
                    low_sum += int(last_one[i]) + 1
            else:
                if last_two[i] > last_one[i] and last_one[i - 1] > last_one[i] and last_one[i + 1] > last_one[i]:
                    low_sum += int(last_one[i]) + 1
        print(low_sum)


def day_ten_part_one(file):
    cypher = {')': '(', '}': '{', ']': '[', '>': '<'}
    error_scores = {')': 3, '}': 1197, ']': 57, '>': 25137}
    score = 0
    with open(file) as f:
        for line in f:
            line = line.strip()
            tracker = []
            for c in line:
                if c in ['(', '{', '[', '<']:
                    tracker.append(c)
                if c in [')', '}', ']', '>']:
                    check = tracker.pop()
                    if check != cypher[c]:
                        score += error_scores[c]
                        break
    print(score)


def day_ten_part_two(file):
    cypher = {')': '(', '}': '{', ']': '[', '>': '<'}
    autocomplete_scores = {'(': 1, '{': 3, '[': 2, '<': 4}
    score = []
    with open(file) as f:
        for line in f:
            line_score = 0
            corrupted = False
            line = line.strip()
            tracker = []
            for c in line:
                if c in ['(', '{', '[', '<']:
                    tracker.append(c)
                if c in [')', '}', ']', '>']:
                    check = tracker.pop()
                    if check != cypher[c]:
                        corrupted = True
                        break
            if not corrupted and len(tracker) > 0:
                remainder = len(tracker)
                for i in range(remainder):
                    cur = tracker.pop()
                    line_score *= 5
                    line_score += autocomplete_scores[cur]
                score.append(line_score)
    score.sort()
    print(score[26])


def day_eleven_part_one(file):
    dumbos = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            dumbos.append([int(c) for c in line])
    for d in dumbos:
        print(d)
    print()
    flashes = 0
    for i in range(2):
        for j in range(len(dumbos)):
            for k in range(len(dumbos[j])):
                flash(dumbos, j, k)
        for d in dumbos:
            print(d)
        print()


def flash(dumbos, j, k):
    if dumbos[j][k] != 9:
        dumbos[j][k] += 1
    else:
        dumbos[j][k] = 0
        if j == 0 and k == 0:
            flash(dumbos, 0, 1)
            flash(dumbos, 1, 0)
            flash(dumbos, 1, 1)
        elif j == 0 and k == (len(dumbos[j]) - 1):
            flash(dumbos, 0, k-1)
            flash(dumbos, 1, k)
            flash(dumbos, 1, k - 1)
        elif j == 0:
            flash(dumbos, 0, k-1)
            flash(dumbos, 0, k + 1)
            flash(dumbos, 1, k)
            flash(dumbos, 1, k - 1)
            flash(dumbos, 1, k + 1)
        elif j == (len(dumbos) - 1) and k == 0:
            flash(dumbos, j, 1)
            flash(dumbos, j - 1, 0)
            flash(dumbos, j - 1, 1)
        elif j == (len(dumbos) - 1) and k == (len(dumbos[j]) - 1):
            flash(dumbos, j, k - 1)
            flash(dumbos, j - 1, k)
            flash(dumbos, j - 1, k - 1)
        elif j == (len(dumbos) - 1):
            flash(dumbos, j, k - 1)
            flash(dumbos, j, k + 1)
            flash(dumbos, j - 1, k)
            flash(dumbos, j - 1, k - 1)
            flash(dumbos, j - 1, k + 1)
        elif k == 0:
            flash(dumbos, j, 1)
            flash(dumbos, j - 1, 0)
            flash(dumbos, j + 1, 0)
            flash(dumbos, j - 1, 1)
            flash(dumbos, j + 1, 1)
        elif k == (len(dumbos[j]) - 1):
            flash(dumbos, j, k - 1)
            flash(dumbos, j - 1, k)
            flash(dumbos, j + 1, k)
            flash(dumbos, j - 1, k - 1)
            flash(dumbos, j + 1, k - 1)
        else:
            flash(dumbos, j, k - 1)
            flash(dumbos, j, k + 1)
            flash(dumbos, j - 1, k)
            flash(dumbos, j + 1, k)
            flash(dumbos, j - 1, k - 1)
            flash(dumbos, j - 1, k + 1)
            flash(dumbos, j + 1, k - 1)
            flash(dumbos, j + 1, k + 1)


def day_eleven_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twelve_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twelve_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_thirteen_part_one(file):
    commands = []
    coordinates = []
    max_coordinates = {'x': 0, 'y': 0}
    with open(file) as f:
        for line in f:
            line = line.strip()
            if 'fold' in line:
                commands.append(line.split()[2])
            elif line:
                coordinates.append((int(line.split(',')[0]), int(line.split(',')[1])))
                max_coordinates['x'] = max(max_coordinates['x'], int(line.split(',')[0]))
                max_coordinates['y'] = max(max_coordinates['y'], int(line.split(',')[1]))

    board = [[0 for _ in range(max_coordinates['x'] + 1)] for _ in range(max_coordinates['y'] + 1)]
    for coordinate in coordinates:
        board[coordinate[1]][coordinate[0]] = 1
    count = 0
    for command in commands:
        if count  == 0:
            new_board = []
            board = array(board)
            plane, turning_point = command.split('=')
            if plane == 'x':
                new_board = board[:, :int(turning_point)]
                for i in range(len(new_board)):
                    for j in range((int(turning_point) + 1), len(board[0])):
                        if board[i][j] == 1:
                            new_board[i][int(turning_point) - (j - int(turning_point))] = 1
                board = new_board
            if plane == 'y':
                new_board = board[:int(turning_point), :]
                for i in range((int(turning_point) + 1), len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] == 1:
                            new_board[int(turning_point) - (i - int(turning_point))][j] = 1
                board = new_board
            count += 1
        else:
            break
    print(sum([sum(b) for b in board]))


def day_thirteen_part_two(file):
    commands = []
    coordinates = []
    max_coordinates = {'x': 0, 'y': 0}
    with open(file) as f:
        for line in f:
            line = line.strip()
            if 'fold' in line:
                commands.append(line.split()[2])
            elif line:
                coordinates.append((int(line.split(',')[0]), int(line.split(',')[1])))
                max_coordinates['x'] = max(max_coordinates['x'], int(line.split(',')[0]))
                max_coordinates['y'] = max(max_coordinates['y'], int(line.split(',')[1]))

    board = [[0 for _ in range(max_coordinates['x'] + 1)] for _ in range(max_coordinates['y'] + 1)]
    for coordinate in coordinates:
        board[coordinate[1]][coordinate[0]] = 1

    for command in commands:
        new_board = []
        board = array(board)
        plane, turning_point = command.split('=')
        if plane == 'x':
            new_board = board[:, :int(turning_point)]
            for i in range(len(new_board)):
                for j in range((int(turning_point) + 1), len(board[0])):
                    if board[i][j] == 1:
                        new_board[i][int(turning_point) - (j - int(turning_point))] = 1
            board = new_board
        if plane == 'y':
            new_board = board[:int(turning_point), :]
            for i in range((int(turning_point) + 1), len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 1:
                        new_board[int(turning_point) - (i - int(turning_point))][j] = 1
            board = new_board
    for b in board:
        print(b)


def day_fourteen_part_one(file):
    polymer = ''
    insertions = {}
    with open(file) as f:
        for line in f:
            line = line.strip()
            if '->' in line:
                insertions[line.split('->')[0].strip()] = line.split('->')[1].strip()
            elif line:
                polymer = line

    for i in range(10):
        cur_dict = {}
        for j in range(len(polymer)):
            if j < (len(polymer) - 1):
                cur_pair = '{}{}'.format(polymer[j], polymer[j + 1])
                if cur_pair in insertions:
                    if j+1 not in cur_dict:
                        cur_dict[j + 1] = insertions[cur_pair]
        for insertion in cur_dict:
            polymer = polymer[:int(insertion.split('-')[0])] + insertion.split('-')[1] + polymer[int(insertion.split('-')[0]):]
    # count_tracker = {}
    # for i in range(len(polymer)):
    #     if polymer[i] in count_tracker:
    #         count_tracker[polymer[i]] += 1
    #     else:
    #         count_tracker[polymer[i]] = 1
    # key_max = max(count_tracker.keys(), key=(lambda k: count_tracker[k]))
    # key_min = min(count_tracker.keys(), key=(lambda k: count_tracker[k]))
    # # print(count_tracker[key_max] - count_tracker[key_min])
    # print(count_tracker)


if __name__ == '__main__':
    day_fourteen_part_one('14.txt')


def day_fourteen_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_fifteen_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_fifteen_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_sixteen_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_sixteen_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_seventeen_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_seventeen_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_eighteen_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_eighteen_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_nineteen_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_nineteen_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_one_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_one_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_two_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_two_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_three_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_three_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_four_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_four_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_five_part_one(file):
    with open(file) as f:
        for line in f:
            line = line.strip()


def day_twenty_five_part_two(file):
    with open(file) as f:
        for line in f:
            line = line.strip()
