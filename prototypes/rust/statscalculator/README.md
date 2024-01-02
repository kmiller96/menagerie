# Stats Calculator

Given a series of numbers (in stdin), compute the mean and standard deviation.

## CLI Mode

```bash
$ statscalculator -- 1 3 2 1 2 2 1 5 3
2.2 1.23  # mean, stddev
```

## Interactive STDIN Mode

```bash
$ statscalculator
1 3 2 1 2 2 1 5 3
<CTRL+D>
2.2 1.23  # mean, stddev
```

## Script Mode

```bash
$ cat 1 3 2 1 2 2 1 5 3 | statscalculator
2.2 1.23  # mean, stddev
```