import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf  

w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:, 1:5]  

model_lm_food = smf.ols(formula='weight ~ food', data=w_n)
result_lm_food = model_lm_food.fit()
result_lm_food.summary()

print(result_lm_food.summary())

plt.figure(figsize=(10, 7))
plt.scatter(w.food, w.weight, alpha=0.5) 
plt.plot(w.food, w.food * 78.1551 - 4.6684, color='red')  
plt.text(66, 132, 'weight = 78.1551 * food - 4.6684', fontsize=12)  
plt.title('Scatter Plot Food')
plt.xlabel('food')
plt.ylabel('weight')
plt.show()
