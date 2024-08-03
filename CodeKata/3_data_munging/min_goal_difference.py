from dataclasses import dataclass
from math import inf
import sys

@dataclass
class Team:
    name: str
    goals_for: int
    goals_against: int

    @property
    def goal_difference(self) -> int:
        return abs(self.goals_for - self.goals_against)

def main(lines: list):
    min_team = Team('intial', inf, 0) 
    for line in lines:
        args = line.strip().replace('.', '').replace('-', '').split()
        try:
            current_team = Team(args[1], int(args[6]), int(args[7]))
        except:
            continue
        if current_team.goal_difference < min_team.goal_difference:
            min_team = current_team
    return min_team.name

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    print(main(lines[1:]))

