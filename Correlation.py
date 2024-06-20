import pandas as pd
import matplotlib.pyplot as plt

# Paths to the different CSV files
length_area_csv = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\a\a-l-a.csv"
length_compactness_csv = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\a\a-l-c.csv"
area_compactness_csv = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\a\a-a-c.csv"
curvature_compactness_csv = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\a\c_c.csv"
# Load data from CSV files specifying UTF-8 encoding
df_length_area = pd.read_csv(length_area_csv, encoding='utf-8')
df_length_compactness = pd.read_csv(length_compactness_csv, encoding='utf-8')
df_area_compactness = pd.read_csv(area_compactness_csv, encoding='utf-8')
df_curvature_compactness = pd.read_csv(curvature_compactness_csv, encoding='utf-8')

# Clean the data by dropping rows with any missing values
df_length_area = df_length_area.dropna(subset=['Length', 'Area'])
df_length_compactness = df_length_compactness.dropna(subset=['Length', 'Compactness'])
df_area_compactness = df_area_compactness.dropna(subset=['Area', 'Compactness'])
df_curvature_compactness = df_curvature_compactness.dropna(subset=['Curvature', 'Compactness'])

# Plotting Length vs Size
plt.figure(figsize=(10, 6))
plt.plot(df_length_area['Length'], df_length_area['Area'], color='blue')
plt.title('Length vs Size')
plt.xlabel('Length')
plt.ylabel('Size')
plt.grid(True)
plt.show()

# Plotting Length vs Compactness
plt.figure(figsize=(10, 6))
plt.plot(df_length_compactness['Length'], df_length_compactness['Compactness'], color='green')
plt.title('Length vs Compactness')
plt.xlabel('Length')
plt.ylabel('Compactness')
plt.grid(True)
plt.show()

# Plotting Size vs Compactness
plt.figure(figsize=(10, 6))
plt.plot(df_area_compactness['Area'], df_area_compactness['Compactness'], color='red')
plt.title('Size vs Compactness')
plt.xlabel('Size')
plt.ylabel('Compactness')
plt.grid(True)
plt.show()

#plotting Curvature vs Compactness
plt.figure(figsize=(10,6))
plt.plot(df_curvature_compactness['Curvature'],df_curvature_compactness['Compactness'], color='red')
plt.title('Average Curvature vs Compactness')
plt.xlabel('Average Curvature')
plt.ylabel('Compactness')
plt.grid(True)
plt.show()