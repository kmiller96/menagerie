"""There is a grid of size NxN. You have Y marbles. Identify a solution that
has no marbles touching each other.

A marble is touching another marble if it is directly adjacent to it (not
diagonally).
"""

import argparse
import itertools

from ortools.sat.python import cp_model

parser = argparse.ArgumentParser(description="Marble array")
parser.add_argument(
    "N",
    metavar="N",
    type=int,
    help="The size of the grid (NxN)",
)
parser.add_argument(
    "Y",
    metavar="Y",
    type=int,
    help="The number of marbles",
)

args = parser.parse_args()

N = args.N
Y = args.Y

# Create the model
model = cp_model.CpModel()

# Create the grid of possible marble positions
grid = {}
for i in range(N):
    for j in range(N):
        grid[(i, j)] = model.NewBoolVar(f"grid_{i}_{j}")

# Add max number of marbles
model.Add(sum(grid.values()) == Y)  # There are Y marbles

# Add no touching marbles constraint
for i, j in itertools.product(range(N), range(N)):
    if i > 0:
        model.AddBoolOr([grid[(i, j)].Not(), grid[(i - 1, j)].Not()])
    if j > 0:
        model.AddBoolOr([grid[(i, j)].Not(), grid[(i, j - 1)].Not()])
    if i < N - 1:
        model.AddBoolOr([grid[(i, j)].Not(), grid[(i + 1, j)].Not()])
    if j < N - 1:
        model.AddBoolOr([grid[(i, j)].Not(), grid[(i, j + 1)].Not()])


# Solve the model
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Print the solution
if status == cp_model.OPTIMAL:
    print("Marbles:")
    for i in range(N):
        print("".join("O" if solver.Value(grid[(i, j)]) else "." for j in range(N)))
else:
    print("No solution found")
