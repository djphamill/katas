from dataclasses import dataclass
import sys

@dataclass
class Day:
    number: int
    max: int
    min: int

    @property
    def spread(self) -> int:
        return self.max - self.min

def main(lines: list):
    max_day = Day(1, -1, 0) 
    for line in lines:
        number, max, min = line.strip().split()[:3]
        try:
            current_day = Day(int(number), int(max), int(min))
        except:
            continue
        if current_day.spread > max_day.spread:
            max_day = current_day

    return max_day.number

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    print(main(lines[2:]))
