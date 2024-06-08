import sqlite3
import pandas as pd


def main():
    xlsx = pd.ExcelFile("datasets/wdi/src/WDIEXCEL.xlsx")
    df1 = pd.read_excel(xlsx, "Data")
    print(
        df1[df1["Indicator Name"] == "Gini index"].drop(
            ["Country Name", "Indicator Code"], axis=1
        )
    )

    """
    df2 = pd.read_csv("datasets/ihme/src/ihme.csv")
    print(
        df2[
            (df2["location_name"] == "United States of America")
            & (df2["cause_name"] == "Mental disorders")
        ][["cause_name", "year", "val", "upper", "lower"]]
    )
    """


if __name__ == "__main__":
    main()
