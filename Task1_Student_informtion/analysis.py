import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV dataset
df = pd.read_csv("StudentsPerformance.csv")

# Display first rows
print(df.head())

# Dataset Info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate average of Math Score
avg_math = df["math score"].mean()
print("\nAverage Math Score:", avg_math)

# BAR CHART
df["gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# SCATTER PLOT
plt.scatter(df["math score"], df["reading score"])
plt.title("Math vs Reading Score")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.show()

# HEATMAP
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
