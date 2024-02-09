import argparse

from ortools.linear_solver import pywraplp

parser = argparse.ArgumentParser(description="Optimise staff allocation")
parser.add_argument("volume", type=int, help="The volume of work to be done")

args = parser.parse_args()
work_volume = args.volume

# Create the model
model: pywraplp.Solver = pywraplp.Solver.CreateSolver("SCIP")

# Create the variables
manager = model.IntVar(0, model.infinity(), "manager")
senior = model.IntVar(0, model.infinity(), "senior")
junior = model.IntVar(0, model.infinity(), "junior")

# Set the objective function
model.Minimize(50 * manager + 40 * senior + 15 * junior)

# Add the constraints
model.Add(manager >= 1)  # You must have at least one manager
model.Add(manager >= (junior / 5))  # You need one manager per 5 junior workers
model.Add(manager >= (senior / 7))  # You need one manager per 7 senior workers
model.Add(
    20 * senior + 10 * junior >= work_volume
)  # You have some expected max volume of work

# Solve
status = model.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print(f"Volume: {work_volume}")
    print()
    print(f"No. Managers: {manager.solution_value()}")
    print(f"No. Seniors: {senior.solution_value()}")
    print(f"No. Juniors: {junior.solution_value()}")
    print(f"Total hourly cost: {model.Objective().Value()}")
