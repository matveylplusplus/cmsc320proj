import sqlite3
import pandas as pd


def main():
    xlsx = pd.ExcelFile("Inflation-data.xlsx")
    df = pd.read_excel(xlsx, "hcpi_m")
    print(df[197001])


if __name__ == "__main__":
    main()
