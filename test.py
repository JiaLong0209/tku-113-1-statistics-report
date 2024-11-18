import pandas as pd
import os

def read_csv_to_df(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV file loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = "Sleep_health_and_lifestyle_dataset.csv"
df = read_csv_to_df(file_name)

print("Columns:")
# columns = ["Person ID", "Gender", "Age", "Occupation", "Sleep Duration", "Quality of Sleep", "Physical Activity Level", "Stress Level", "BMI Category", "Blood Pressure", "Heart Rate", "Daily Steps", "Sleep Disorder"]
columns = [column for column in df]

print(columns)

print(df.head())

print(df.describe())

print(df["BMI Category"].unique())



