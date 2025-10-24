import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Товар': ['Телефон', 'Ноутбук', 'Планшет', 'Смартфон', 'Монитор'],
    'Цена': [np.nan, 15000, 5000, 10000, 2000],
    'Количество': [-5, 100, 10000, 50, 10]
}

df = pd.DataFrame(data)

median_price = df['Цена'].median(skipna=True)
df['Цена'].fillna(median_price, inplace=True)

df = df[(df['Количество'] > 1) & (df['Количество'] <= 1000)]

df['Общая_стоимость'] = df['Цена'] * df['Количество']

total_revenue = df.groupby('Товар')['Общая_стоимость'].sum()

plt.figure(figsize=(10, 6))
total_revenue.plot(kind='bar', color='skyblue')
plt.title('Суммарная выручка по товарам')
plt.xlabel('Товар')
plt.ylabel('Выручка')
plt.show()