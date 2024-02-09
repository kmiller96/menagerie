"""Solve the typical male problem: minimise the number of people that are
standing next to each other in a row of urinals.

Basically a good excuse to practice more constraint programming.

Usage:

```
# Solve the problem with 5 urinals and 3 people
python optimise.py 5 3
```

"""

# Parse CLI
import argparse

parser = argparse.ArgumentParser(description="Urinal problem")
parser.add_argument(
    "N",
    metavar="N",
    type=int,
    help="The number of urinals",
)
parser.add_argument(
    "Y",
    metavar="Y",
    type=int,
    help="The number of people",
)

args = parser.parse_args()

N_URINALS = args.N
N_PEOPLE = args.Y

# Run solver
from ortools.sat.python import cp_model

# Create the model
model = cp_model.CpModel()

# Make the urinals
urinals = []
for i in range(N_URINALS):
    urinals.append(model.NewIntVar(0, 1, f"urinal_{i}"))

# Add constraints
model.Add(sum(urinals) == N_PEOPLE)

# Add objective function (fewest adjacent people)
objective_terms = []
for i in range(N_URINALS):
    term = model.NewIntVar(0, 1, f"adjacent_{i}")

    LEFT_END = i == 0
    RIGHT_END = i == N_URINALS - 1

    if LEFT_END:
        model.AddMultiplicationEquality(term, [urinals[i], urinals[i + 1]])
    elif RIGHT_END:
        model.AddMultiplicationEquality(term, [urinals[i], urinals[i - 1]])
    else:
        left = model.NewIntVar(0, 1, f"adjacent_{i}_left")
        right = model.NewIntVar(0, 1, f"adjacent_{i}_right")

        model.AddMultiplicationEquality(left, [urinals[i], urinals[i + 1]])
        model.AddMultiplicationEquality(right, [urinals[i], urinals[i - 1]])
        model.AddMaxEquality(term, [left, right])

    objective_terms.append(term)

model.Minimize(sum(objective_terms))

# Solve the model
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Print the solution
print(f"Fewest adjacent people: {solver.ObjectiveValue()}")
print("Urinals:", [int(solver.Value(u)) for u in urinals])
