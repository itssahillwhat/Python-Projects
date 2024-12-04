import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240524.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])

# gray = data[data["Primary Fur Color"] == "Gray"].shape[0]
# black = data[data["Primary Fur Color"] == "Black"].shape[0]
# red = data[data["Primary Fur Color"] == "Cinnamon"].shape[0]

data_dict = {
    "Fur Color": ["gray", "black", "red"],
    "Count": [gray, black, red]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")