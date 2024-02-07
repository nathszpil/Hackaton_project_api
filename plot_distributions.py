import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("students_data.csv")
num_rows = 4
num_cols = 4
total_plots = num_rows * num_cols

fig, axes = plt.subplots(num_rows, num_cols, figsize=(10, 7))

axes = axes.flatten()

for i, column in enumerate(df.columns):
    if column != "STUDENT ID":
        # Plot a histogram for numerical features
        sns.histplot(df[column], kde=True, color='skyblue', ax=axes[i])
        axes[i].set_title(f'Histogram of {column}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frequency')


plt.tight_layout()
plt.show()