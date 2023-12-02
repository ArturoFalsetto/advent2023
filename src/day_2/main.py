MAX_CONF = {"red": 12, "green": 13, "blue": 14}


def read_input_lazily(path):
    with open(path, "r") as f:
        for n, line in enumerate(f, start=1):
            string = line.strip("\n")
            yield n, string


def read_input(path):
    with open(path, "r") as f:
        strings = f.read().splitlines()
    return strings


def parse_line(game, line):
    _, rounds = line.split(":")
    for round in rounds.split(";"):
        scores = {
            v: int(k) for k, v in (data.split() for data in round.lstrip().split(", "))
        }
        for k, v in scores.items():
            if MAX_CONF[k] < v:
                return 0
    return game


def parse_line_min(game, line):
    _, rounds = line.split(":")
    min_conf = {"red": 0, "blue": 0, "green": 0}
    for round in rounds.split(";"):
        scores = {
            v: int(k) for k, v in (data.split() for data in round.lstrip().split(", "))
        }
        for k, v in scores.items():
            if min_conf[k] < v:
                min_conf[k] = v
    total = 1
    for val in min_conf.values():
        total *= val
    return total


def parse_colour(round):
    pass


if __name__ == "__main__":
    total = 0
    for game, rounds in read_input_lazily("input_data.txt"):
        total += parse_line(game, rounds)
    print(total)

    total = 0
    for game, rounds in read_input_lazily("input_data.txt"):
        total += parse_line_min(game, rounds)
    print(total)
