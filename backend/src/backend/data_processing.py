import pandas as pd
from backend.constants import DATA_PATH

df1 = pd.read_csv(DATA_PATH / "lunar.csv")
df2 = pd.read_csv(DATA_PATH / "solar.csv")

# Replace the "-" values to None in Solar data
df2 = df2.astype(object).where(pd.notnull(df2), None)