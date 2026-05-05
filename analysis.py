import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/dailyActivity.csv")

# Basic info
print("Dataset shape:", df.shape)
print(df.info())

# Correlation between steps and calories
corr = df[["TotalSteps", "Calories"]].corr()
print("\nSteps vs Calories Correlation:\n", corr)

# Scatter plot
plt.scatter(df["TotalSteps"], df["Calories"])
plt.xlabel("Total Steps")
plt.ylabel("Calories Burned")
plt.title("Steps vs Calories")

plt.savefig("steps_vs_calories.png")
plt.show()

# Regression plot
sns.regplot(x="TotalSteps", y="Calories", data=df)
plt.title("Steps vs Calories with Trend Line")

plt.savefig("steps_vs_calories_trend.png")
plt.show()

# Multi-variable correlation
activity_corr = df[
    ["VeryActiveMinutes", "FairlyActiveMinutes", "LightlyActiveMinutes", "SedentaryMinutes", "Calories"]
].corr()

print("\nActivity vs Calories Correlation:\n", activity_corr)