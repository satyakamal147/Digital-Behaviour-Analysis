import pandas as pd
from pathlib import Path

# DataFrame = table of data
# Series = a column of data
# Index = row labels

csv_path = Path(r"C:\Users\satya\OneDrive\Desktop\ML Training\Projects\digital_behaviour_analysis\digital_behaviour.csv")

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")

df = pd.read_csv(csv_path)

print("First 5 rows:")
print(df.head(5))

print("\nLast 5 rows:")
print(df.tail(5))

print("\nDataFrame info:")
print(df.info())

print("\nShape:")
print(df.shape)

print("\nInstagram_Minutes column:")
print(df["Instagram_Minutes"])

print("\nStudy_Minutes column:")
print(df["Study_Minutes"])

selected_columns = df[["Instagram_Minutes", "Study_Minutes"]]
print("\nSelected columns:")
print(selected_columns.head())

print("\nDate + selected columns:")
print(df[["Date", "Instagram_Minutes", "Study_Minutes"]].head())

print("\nInstagram total:")
print(df["Instagram_Minutes"].sum())

print("\nInstagram mean:")
print(df["Instagram_Minutes"].mean())

print("\nInstagram mean rounded to 2 decimals:")
print(round(df["Instagram_Minutes"].mean(), 2))

print("\nMaximum YouTube_Minutes:")
print(df["YouTube_Minutes"].max())

filtered_data = df[df["Instagram_Minutes"] > 100]
print("\nRows where Instagram_Minutes > 100:")
print(filtered_data.head())

stu = df[df["Study_Minutes"]>180]
print("\nRows with Study Minutes > 180:")
print(stu.head())

Insta_morethan_Study = df[df["Instagram_Minutes"]>df["Study_Minutes"]]
print("\nROws where Instagram was high and Study was low:")
print(Insta_morethan_Study.head())

Heavy_Insta = df[df["Instagram_Minutes"]>df["Instagram_Minutes"].mean()]
print("\nRows with Heavy Instagram days and average is ")
print(df["Instagram_Minutes"].mean())
print(Heavy_Insta)


kf=df.sort_values("Instagram_Minutes",ascending=False)
print("\nArranging the table from highest Instagram usage to the lowest:")
print(kf)

print("\nTop 5 Instagram Days")
print(kf["Instagram_Minutes"].head(5))

sf=df.sort_values("Study_Minutes",ascending=False)
print("\nTop 5 Best Study Days")
print(sf["Study_Minutes"].head(5))

df["Total_Screen_Time"]= df["Instagram_Minutes"]+df["YouTube_Minutes"]+df["WhatsApp_Minutes"]+df["LinkedIn_Minutes"]
print("\nTotal_Screen_Time by adding Instagram, YouTube, WhatsApp and LinkedIn minutes together.")
print(df["Total_Screen_Time"])

df["Screen_Hours"] = df["Total_Screen_Time"]/60
print("\nScreen Hours:")
print(df["Screen_Hours"])

df["Digital_Balance"]= df["Study_Minutes"]/df["Total_Screen_Time"]
print("\n Digital Balance by dividing study minutes by total screen time.")
print(df["Digital_Balance"])

df["Day_Type"]="Normal"
df.loc[df["Total_Screen_Time"]>300,"Day_Type"]="Heavy"
print("\n Create a new column called Day_Type. If total screen time is above 300 minutes, call it Heavy. Otherwise call it Normal.")
print(df["Day_Type"])

apps_total ={
    "Instagram":df["Instagram_Minutes"].sum(),
    "Whatsapp":df["WhatsApp_Minutes"].sum(),
    "LinkedIn":df["LinkedIn_Minutes"].sum(),
    "Youtube":df["YouTube_Minutes"].sum()
}
print("\nTotal minutes on each of the four apps:")
print(apps_total)

high=max(apps_total,key=apps_total.get)
print("\nWhich app consumed the most time")
print(high)

heavy_days = len(df[df["Day_Type"]=="Heavy"])
print("\n No of Heavy Days:")
print(heavy_days)

best_study_day = df["Study_Minutes"].max()
print("\nBest Study Day :")
print(best_study_day)

heaviest_screen_day_study_time = df.loc[df["Total_Screen_Time"].idxmax(),"Study_Minutes"]
print("\nHeaviest screen day, how much did you study:")
print(heaviest_screen_day_study_time)

avg_digital_balance = df["Digital_Balance"].mean()
print("Average Digital Balance:")
print(avg_digital_balance)

df.to_csv("digital_behaviour_panda.csv")
