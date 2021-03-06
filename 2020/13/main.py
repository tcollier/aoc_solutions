import math
import os
import sys

from aoc_executor import AocExecutor


CWD = os.path.dirname(os.path.abspath(__file__))


def part1_solution(input):
    timestamp = int(input[0])
    bus_ids = [int(n) for n in input[1].split(",") if n != "x"]
    min_wait = math.inf
    min_wait_id = None
    for bus_id in bus_ids:
        wait_time = bus_id - timestamp % bus_id
        if wait_time < min_wait:
            min_wait = wait_time
            min_wait_id = bus_id
    return min_wait_id * min_wait


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def part2_solution(input):
    bus_ids = {i: int(n) for i, n in enumerate(input[1].split(",")) if n != "x"}
    first_bus_id = bus_ids.pop(0)
    incrementer = timestamp = first_bus_id
    for offset, bus_id in bus_ids.items():
        while (timestamp + offset) % bus_id != 0:
            timestamp += incrementer
        incrementer = lcm(incrementer, bus_id)
    return timestamp


executor = AocExecutor(
    [l.rstrip() for l in open(f"{CWD}/input.txt", "r").readlines()],
    part1_solution,
    part2_solution,
)
executor(sys.argv)
