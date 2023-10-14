import pandas as pd
import tabulate  # HACK: Needed for the compile to work. If omitted it will fail.


df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

print(df.to_markdown())
