
with open('plansza.txt') as f:
    plansza = [list(map(int, line.strip().split())) for line in f]

with open('robot.txt') as f:
    ruchy_graczy = [line.strip() for line in f]

n = len(plansza)
liczba_zdyskwalifikowanych_graczy = 0

for ruchy in ruchy_graczy:
    pozycja_robota = (0, 0)
    liczba_ruchow = 0
    for ruch in ruchy:
        if ruch == 'N':
            nowa_pozycja = (pozycja_robota[0] - 1, pozycja_robota[1])
        elif ruch == 'E':
            nowa_pozycja = (pozycja_robota[0], pozycja_robota[1] + 1)
        elif ruch == 'S':
            nowa_pozycja = (pozycja_robota[0] + 1, pozycja_robota[1])
        elif ruch == 'W':
            nowa_pozycja = (pozycja_robota[0], pozycja_robota[1] - 1)

        if nowa_pozycja[0] < 0 or nowa_pozycja[0] >= n or \
           nowa_pozycja[1] < 0 or nowa_pozycja[1] >= n:
            liczba_zdyskwalifikowanych_graczy += 1
            break

        pozycja_robota = nowa_pozycja
        liczba_ruchow += 1
        if liczba_ruchow >= 5 * n:
            break


print(f'4. Liczba zdyskwalifikowanych graczy: {liczba_zdyskwalifikowanych_graczy}')


############


with open('plansza.txt') as f:
    plansza = [[int(x) for x in line.split()] for line in f]

with open('robot.txt') as f:
    ruchy = [line.strip() for line in f]

n = len(plansza)
punkty_graczy = [0] * len(ruchy)

for i in range(len(ruchy)):
    x, y = 0, 0
    for ruch in ruchy[i]:
        if ruch == 'N' and x > 0:
            x -= 1
        elif ruch == 'E' and y < n-1:
            y += 1
        elif ruch == 'S' and x < n-1:
            x += 1
        elif ruch == 'W' and y > 0:
            y -= 1
        else:
            punkty_graczy[i] = -1
            break
        punkty_graczy[i] += plansza[x][y]

najwyzsze_punkty = max(punkty_graczy)
numer_gracza = punkty_graczy.index(najwyzsze_punkty) + 1

print(f'4.2 {najwyzsze_punkty}')


########


def find_robot_position(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == -1:
                return (row, col)


# Wczytanie planszy
board = []
with open("plansza.txt") as f:
    for line in f:
        row = [int(x) for x in line.split()]
        board.append(row)

# Wczytanie ruchów graczy
moves = []
with open("robot.txt") as f:
    for line in f:
        moves.append(line.strip())

# Znalezienie gracza z największą liczbą ruchów w jednym wierszu planszy
max_count = 0
max_players = []
for player, move_seq in enumerate(moves):
    count = 0
    for i in range(len(move_seq) - 1):
        row, col = find_robot_position(board)
        if move_seq[i] == "W" and move_seq[i+1] == "W":
            if col > 0 and board[row][col-1] != -1:
                count += 1
        elif move_seq[i] == "E" and move_seq[i+1] == "E":
            if col < len(board[0])-1 and board[row][col+1] != -1:
                count += 1
    if count > max_count:
        max_count = count
        max_players = [player]
    elif count == max_count:
        max_players.append(player)

# Zapisanie odpowiedzi do pliku

print("6. " + " ".join(str(p+1) for p in max_players) + " " + str(max_count))

