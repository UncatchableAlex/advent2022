f = open("../inputs/day2.txt").read().splitlines()
games = [[ord(a) - ord('A'), ord(b) - ord('X')] for [a, b] in (ln.split(" ") for ln in f)]


def get_score1(game):
    game_sum = game[0] - game[1]
    bonus = 3 if game_sum == 0 else (6 if (game_sum == -1 or game_sum == 2) else 0)
    return bonus + game[1] + 1


def get_score2(game):
    return (game[1] * 3) + ((game[0] + game[1] - 1) % 3) + 1


part1 = sum([get_score1(game) for game in games])
print(part1)
part2 = sum([get_score2(game) for game in games])
print(part2)
