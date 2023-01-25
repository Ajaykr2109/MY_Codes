import pandas as pd

df = pd.read_csv("D:\\LPU\\auto.csv")
# print(df)
headers = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price",
]

df["price"] = df["price"].astype("float")
df.describe()
df.isnull().sum()
df["normalized-losses"].value_counts()


df = df.dropna(subset=["price"], axis=0)
