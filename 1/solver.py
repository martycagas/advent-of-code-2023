import re
from re import Pattern


class Solver:
    def __init__(self, file: str) -> None:
        with open(file, "r") as f:
            self.input_lines: list[str] = f.read().splitlines()

    def solve_part_one(self) -> int:
        res: list[int] = []
        for line in self.input_lines:
            matches = re.findall(r"\d", line)
            res.append(int(f"{matches[0]}{matches[-1]}"))
        return sum(res)

    def solve_part_two(self) -> int:
        dmap = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        res: list[int] = []
        for line in self.input_lines:
            matches = re.finditer(rf"(?=({'|'.join(dmap.keys())}))", line)
            results = [match.group(1) for match in matches]
            res.append(int(f"{dmap[results[0]]}{dmap[results[-1]]}"))
        return sum(res)

    def print_solve(self, file: str | None) -> None:
        if file is not None:
            with open(file, "w") as f:
                f.write(f"{self.solve_part_one()}\n")
                f.write(f"{self.solve_part_two()}\n")
        else:
            print(self.solve_part_one())
            print(self.solve_part_two())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-o", "--output", type=str)
    args = parser.parse_args()
    solver = Solver(args.input)
    solver.print_solve(args.output)
