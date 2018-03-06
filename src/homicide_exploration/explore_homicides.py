import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calendar as cal
from explore_helpers import yPerX_numeric, yPerX_cat 

def readInData():
    data = pd.read_csv("../data/RochesterNY_Homicides.csv")
    
    # Handle NAs
    colsWithNA = data.columns[data.isna().any()].tolist()
    print("Columns with NA values: %s"%(", ".join(colsWithNA)))
    print(">>> Filling NAs with 0")
    data.fillna(0)

    # Change Occurred Data format
    ymd = data.pop("OccurredDate")\
            .apply(lambda x: x.split("T")[0])\
            .str.split("-", expand=True).astype(int)
    ymd.columns = ["OccuredYear", "OccuredMonth", "OccuredDay"]
    weekDay = ymd.apply(lambda x: cal.day_abbr[cal.weekday(*x)], axis=1)
    data = pd.concat([data, ymd], axis=1)
    data["OccurredDayName"] = weekDay
    return data

def run():
    data = readInData()
    """
    yPerX_numeric(
            "Weapon Category", data["WeaponCategory"], 
            "Victims", data["VictimCount"]
            )
    yPerX_numeric(
            "Weapon Category", data["WeaponCategory"], 
            "Arrestees", data["ArresteeCount"]
            )
    """
    print(data["OccurredYear"].max(), data["OccurredYear"].min())
    data["OccurredDayName"].value_counts().plot(kind="bar")
    plt.show()
if __name__ == "__main__":
    run()
