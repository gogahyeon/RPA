import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager

w = pd.read_csv('moving_keyword.csv')
print(w, end="\n\n")
print(w.head(10), end="\n\n")

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

w_n = w.iloc[:, 1:5]
print(w_n, end='\n\n')

w_cor = w_n.corr(method='pearson')
print(w_cor, end='\n\n')

sns.pairplot(w_n)
plt.show() 

plt.figure(figsize=(10, 7))
sns.heatmap(w_cor, annot=True, cmap='Blues')
plt.show()  
