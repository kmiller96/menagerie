# Running Total

Calculates a running total from STDIN streamed in.

Bit like a calculator where you can rapidly add/subtract numbers and see the total change in real time.

## Vision

I want it to not be as dumb as just reading stdin but, rather, be a bit more
interactive. I want it that the user can specify a number and an operation (add/subtract) and the running total will be updated accordingly.

```bash
# Screen 1
101
+

# Screen 2
101
+ 5

# Screen 3
106
+

# Screen 4
106
- 3

# Screen 5
103
+
```

Note that this approach relies on us using a crate like `crossterm`. So, as a starting point, we will just read line-by-line which is more easily suppored with the standard library.
