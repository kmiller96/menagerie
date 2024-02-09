# Linear Programming

Prototype showcasing how you can solve a series of linear equations 
programmatically using Google's ORTools library.

## Problem 
You are a manager trying to determine how to staff your organisation.

You have some expected max volume of work (let's call it V) that you need to be
able to satisfy. For example, it might be producing 1000 widgets per day. You
can hire the following staff:

- A manager, that costs $50 per hour that generates no widgets per hour.
- A senior worker, that costs $40 per hour and generates 20 widgets an hour.
- A junior worker, that costs $15 per hour and generates 10 widgets an hour.

There are the following constraints to your problem.

- You must have at least one manager.
- You need one manager per 5 junior workers.
- You need one manager per 7 senior workers.

Your objective is to minimise the total spend on staff.

## Usage

```bash
python optimise.py 1000
```