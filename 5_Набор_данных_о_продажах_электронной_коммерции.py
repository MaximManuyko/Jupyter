#!/usr/bin/env python
# coding: utf-8

# # Набор данных о продажах электронной коммерции через Amazon

# https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data

# ![amazon-robot-scaled.jpg](attachment:e4bed548-7fa5-4c6e-991f-8ff5e7d7f8c7.jpg)

# ### Анализ и максимизация эффективности онлайн-бизнеса

# In[160]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
import os

# In[161]:


# Переменные

a = 1000000 # Размер строк для head

b = 20 # Переменная для размера графиков


# In[162]:

# Получаем путь к текущей директории, где находится Python-скрипт
current_directory = os.path.dirname(os.path.realpath(__file__))

# Укажите имя файла
csv_filename = "5_Набор_данных_о_продажах_электронной_коммерции.csv"

# Соберите полный путь к файлу CSV
csv_path = os.path.join(current_directory, csv_filename)


# Загрузите данные из CSV файла в DataFrame
input_raw = pd.read_csv(csv_path)

input_raw.head(a)


# In[163]:


#input_raw.dtypes


# In[164]:


input_raw.describe()


# In[165]:


df = input_raw.copy(deep=True)

plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['Qty'], alpha=0.5)

plt.title('Распределение количества штук в заказе')
plt.xlabel('Индекс')
plt.ylabel('Количество штук в заказе')
plt.grid(True)
plt.show()


# In[166]:


df = input_raw.copy(deep=True)

# Построение гистограммы
plt.figure(figsize=(10, 6))
sns.histplot(df['Qty'], bins=20, kde=False, color='blue')
plt.title('Распределение количества штук в заказе')
plt.xlabel('Количество штук в заказе')
plt.ylabel('Количество')
plt.grid(True)
plt.show()


# In[167]:


df = input_raw.copy(deep=True)
plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['Amount'], alpha=0.5)
plt.title('Точечный график распределения суммы заказа')
plt.xlabel('Индекс')
plt.ylabel('Сумма заказа, $')
plt.grid(True)
plt.show()

# Гистограмма
plt.figure(figsize=(10, 6))
plt.hist(df['Amount'], bins=20, color='blue', edgecolor='black')
plt.title('Гистограмма распределения суммы заказа')
plt.xlabel('Сумма заказа, $')
plt.ylabel('Частота')
plt.grid(True)
plt.show()


# In[168]:


df = input_raw.copy(deep=True)

# Убираем строки, где в колонке 'Status' есть указанные значения
df_filtered = df[df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Подсчет количества строк
count_rows = len(df_filtered)

# Форматирование строки с использованием f-строк
formatted_count_rows = f'{count_rows:,}'

# Вывод результата
print(f"Количество заказов после фильтрации: {formatted_count_rows}")


# In[169]:


DF = input_raw.copy(deep=True)

statuses_to_remove = ['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up']
DF_filtered = DF[DF['Status'].isin(statuses_to_remove)]

total_amount = DF_filtered['Amount'].sum()

# Форматирование строки с использованием f-строк
formatted_total_amount = f'{total_amount:,.2f}'

print(f'Общая сумма продаж: {formatted_total_amount} $')


# In[170]:


DF = input_raw.copy(deep=True)

statuses_to_remove = ['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up']
DF_filtered = DF[DF['Status'].isin(statuses_to_remove)]

# Используйте метод 'mean' для вычисления среднего значения
total_amount = DF_filtered['Amount'].mean()

# Округление до двух знаков после точки
rounded_total_amount = round(total_amount, 2)

print('Средняя сумма продаж: ', rounded_total_amount, ' $')


# In[171]:


df = input_raw.copy(deep=True)

# Словарь соответствия английских и русских статусов
status_translation = {
    'Cancelled': 'Отменено',
    'Pending': 'В ожидании',
    'Pending - Waiting for Pick Up': 'Ожидание – ожидание получения',
    'Shipped': 'Отправленный',
    'Shipped - Damaged': 'Отправлено – повреждено',
    'Shipped - Delivered to Buyer': 'Отгружено – доставлено покупателю',
    'Shipped - Lost in Transit': 'Отправлено – потеряно в пути',
    'Shipped - Out for Delivery': 'Отправлено – отправлено на доставку',
    'Shipped - Picked Up': 'Отправлено – получено',
    'Shipped - Rejected by Buyer': 'Отправлено – отклонено покупателем',
    'Shipped - Returned to Seller': 'Отправлено – возвращено продавцу',
    'Shipped - Returning to Seller': 'Отправлено – возвращается продавцу',
    'Shipping': 'Перевозки'
}

# Преобразование статусов в русские
df['Status_Russian'] = df['Status'].map(status_translation)

# Группировка данных по статусам
status_counts = df['Status_Russian'].value_counts()

# Построение столбчатой диаграммы
plt.figure(figsize=(b, b * 0.3))
bars = status_counts.plot(kind='bar', color='skyblue')

# Добавление аннотаций над столбиками
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width() / 2 , bar.get_height() + 0.1, str(bar.get_height()), ha='center', color='black')

plt.title('Распределение по статусам')
plt.xlabel('Статус')
plt.ylabel('Количество заказов, шт.')
plt.xticks(rotation=45, ha='right')  # Поворот подписей оси x для лучшей читаемости
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[172]:


DF = input_raw.copy(deep=True)

DF['Month'] = DF['Date'].dt.to_period('M')
monthly_orders = DF.groupby('Month').size()

# Фильтр для столбца 'Status'
allowed_statuses = ['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up']
filtered_DF = DF[DF['Status'].isin(allowed_statuses)]

# Постройте столбчатую диаграмму для отфильтрованных данных
plt.figure(figsize=(b, b * 0.3))
bar_plot = filtered_DF.groupby('Month').size().plot(kind='bar', color='skyblue')
plt.title('Количество заказов по месяцам (фильтр по статусу)')
plt.xlabel('Месяц')
plt.ylabel('Количество заказов, шт.')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Добавьте аннотации (количество заказов) над каждым столбиком
for i, value in enumerate(filtered_DF.groupby('Month').size()):
    bar_plot.text(i, value + 0.1, str(value), ha='center', va='bottom')

plt.show()


# In[173]:


DF = input_raw.copy(deep=True)

# Фильтрация данных по значениям в колонке 'Status'
DF = DF[DF['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Создание нового столбца 'Month' с месяцем
DF['Month'] = DF['Date'].dt.to_period('M')

# Группировка данных по месяцам и суммирование количества заказов
monthly_orders = DF.groupby('Month')['Qty'].sum()

# Построение столбчатой диаграммы с добавлением значений над столбиками
plt.figure(figsize=(b, b * 0.3))
ax = monthly_orders.plot(kind='bar', color='skyblue')

# Добавление значений над столбиками
for i, v in enumerate(monthly_orders):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Количество заказанных единиц товара по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество заказанных единиц товара, шт.')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[174]:


df = input_raw.copy(deep=True)

# Фильтрация данных по значениям в колонке 'Status'
filtered_df = df[df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])].copy()

# Добавление нового столбца 'Month' для хранения месяца из столбца 'Date'
filtered_df['Month'] = filtered_df['Date'].dt.to_period('M')

# Группировка данных по месяцам и суммирование стоимости заказов
monthly_sum = filtered_df.groupby('Month')['Amount'].sum()

# Построение столбчатой диаграммы
plt.figure(figsize=(b, b * 0.3))
ax = monthly_sum.plot(kind='bar', color='skyblue')

# Добавление значений суммы заказов над столбиками
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.title('Столбчатая диаграмма стоимостей заказов по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Сумма заказов, 10 млн.$')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[175]:


df = input_raw.copy(deep=True)

# Фильтрация строк по условию в колонке Status
filtered_df = df[~df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Группировка по категориям и суммирование по колонке Amount
grouped_df = filtered_df.groupby('Category')['Amount'].sum().reset_index()

# Сортировка по убыванию суммы
grouped_df = grouped_df.sort_values(by='Amount', ascending=False)

# Построение столбчатого графика
plt.figure(figsize=(b, b * 0.3))
plt.bar(grouped_df['Category'], grouped_df['Amount'])
plt.xlabel('Категория')
plt.ylabel('Сумма продаж, млн.')
plt.title('График суммы продаж по категориям')
plt.xticks(rotation=45, ha='right')  # Подписи оси x под углом 45 градусов
plt.grid(axis='y')  # Включаем горизонтальную сетку

# Добавляем значения суммы над столбиками
for i, value in enumerate(grouped_df['Amount']):
    plt.text(i, value + 5, str(value), ha='center', va='bottom')

plt.show()


# In[176]:


df = input_raw.copy(deep=True)

# Фильтруем строки по условию в колонке Status
filtered_df = df[df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Создаем область для двух диаграмм
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Первая круговая диаграмма (по количеству)
fulfilment_count = filtered_df['Fulfilment'].value_counts()
fulfilment_count.plot.pie(autopct='%1.1f%%', startangle=90, ax=axes[0])
axes[0].set_title('Распределение по количеству заказов')

# Вторая круговая диаграмма (по сумме в колонке Amount)
fulfilment_sum = filtered_df.groupby('Fulfilment')['Amount'].sum()
fulfilment_sum.plot.pie(autopct='%1.1f%%', startangle=90, ax=axes[1])
axes[1].set_title('Распределение по сумме заказов')

# Отображение диаграмм
plt.show()


# In[177]:


df = input_raw.copy(deep=True)

df['Date'] = pd.to_datetime(df['Date'])

# Фильтрация строк по условиям
filtered_df = df[df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Построение столбчатой диаграммы
fig, ax = plt.subplots(figsize=(b, b * 0.3))

# Создание уникального списка месяцев
months = filtered_df['Date'].dt.to_period("M").unique()

# Ширина столбиков
bar_width = 0.35

for i, fulfillment in enumerate(filtered_df['Fulfilment'].unique()):
    subset = filtered_df[filtered_df['Fulfilment'] == fulfillment]
    subset_grouped = subset.groupby(subset['Date'].dt.to_period("M"))['Amount'].sum()

    # Перемещение каждого столбика по x на ширину столбика
    x_pos = [pos + i * bar_width for pos in range(len(months))]
    
    bars = ax.bar(x_pos, subset_grouped, width=bar_width, label=fulfillment, alpha=0.7)

    # Добавление значений над столбиками
    for bar, value in zip(bars, subset_grouped):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(value, 2),
                ha='center', va='bottom', fontsize=8, color='black')

# Настройка внешнего вида диаграммы
ax.set_title('Сумма продаж по месяцам и типу Fulfilment')
ax.set_xlabel('Месяц')
ax.set_ylabel('Сумма продаж, млн.$')
ax.grid(True)
ax.legend(title='Fulfilment')

# Форматирование дат на оси x
date_form = DateFormatter("%Y-%m")
ax.xaxis.set_major_formatter(date_form)

# Расстановка меток по x и их названия (месяцы)
ax.set_xticks([pos + bar_width for pos in range(len(months))])
ax.set_xticklabels(months)

# Отображение диаграммы
plt.show()


# In[178]:


df = input_raw.copy(deep=True)

df['Date'] = pd.to_datetime(df['Date'])

# Фильтрация строк по условиям
filtered_df = df[df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Построение столбчатой диаграммы
fig, ax = plt.subplots(figsize=(b, b * 0.3))

# Создание уникального списка месяцев и сортировка их по возрастанию
months = sorted(filtered_df['Date'].dt.to_period("M").unique())

# Ширина столбиков
bar_width = 0.35

for i, channel in enumerate(filtered_df['Sales Channel '].unique()):
    subset = filtered_df[filtered_df['Sales Channel '] == channel]
    subset_grouped = subset.groupby(subset['Date'].dt.to_period("M"))['Qty'].size()

    # Перемещение каждого столбика по x на ширину столбика
    x_pos = [pos + i * bar_width for pos in range(len(months))]
    
    bars = ax.bar(x_pos, subset_grouped.reindex(months, fill_value=0), width=bar_width, label=channel, alpha=0.7)

    # Добавление значений над столбиками
    for bar, value in zip(bars, subset_grouped.reindex(months, fill_value=0)):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(value, 2),
                ha='center', va='bottom', fontsize=8, color='black')

# Настройка внешнего вида диаграммы
ax.set_title('Количество заказов по месяцам и типу Sales Channel')
ax.set_xlabel('Месяц')
ax.set_ylabel('Количество заказов')
ax.grid(True)
ax.legend(title='Sales Channel ')

# Форматирование дат на оси x
date_form = DateFormatter("%Y-%m")
ax.xaxis.set_major_formatter(date_form)

# Расстановка меток по x и их названия (месяцы)
ax.set_xticks([pos + bar_width for pos in range(len(months))])
ax.set_xticklabels(months)

# Отображение диаграммы
plt.show()


# In[179]:


df = input_raw.copy(deep=True)

# Фильтрация строк по значению в колонке 'Status'
filtered_df = df[df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Группировка по 'ship-state' и суммирование 'Amount' для каждой группы
grouped_df = filtered_df.groupby('ship-state')['Amount'].sum().reset_index()

# Сортировка по уменьшению 'Amount'
grouped_df = grouped_df.sort_values(by='Amount', ascending=False)

# Построение столбчатой диаграммы
fig, ax = plt.subplots(figsize=(b, b * 0.3))
bars = ax.bar(grouped_df['ship-state'], grouped_df['Amount'], color='blue')

# Добавление названий и подписей на русском языке
plt.title('Сумма по ship-state', fontsize=16)
plt.xlabel('ship-state', fontsize=14)
plt.ylabel('Сумма продаж, млн.$', fontsize=14)

# Добавление сетки
plt.grid(True, linestyle='--', alpha=0.7)

# Добавление подписей к столбцам
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', rotation=45)

# Поворот подписей оси x на 45 градусов
plt.xticks(rotation=45, ha='right')

# Отображение графика
plt.show()


# In[180]:


df = input_raw.copy(deep=True)

# Отфильтруем строки по заданным значениям в колонке Status
filtered_df = df[df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Построим столбчатую диаграмму для колонки Size
plt.figure(figsize=(b, b * 0.3))
size_counts = filtered_df['Size'].value_counts().sort_values(ascending=False)
size_counts.plot(kind='bar', color='skyblue', edgecolor='black')

# Настройка графика
plt.title('Количество заказов по размерам', fontsize=16)
plt.xlabel('Размер', fontsize=14)
plt.ylabel('Количество, шт.', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')

# Добавление значений над столбиками
for i, v in enumerate(size_counts):
    plt.text(i, v + 0.2, str(v), ha='center', va='bottom', fontsize=10)

plt.show()


# In[181]:


df = input_raw.copy(deep=True)

df['Date'] = pd.to_datetime(df['Date'])

# Фильтруем строки
filtered_df = df[df['Status'].isin(['Shipped', 'Shipped - Delivered to Buyer', 'Shipped - Picked Up'])]

# Строим круговую диаграмму
b2b_sum = filtered_df.groupby('B2B')['Amount'].sum()
b2b_sum.plot(kind='pie', autopct='%1.1f%%', labels=['B2B', 'Non-B2B'], colors=['lightblue', 'lightcoral'])
plt.title('Продажи B2B по сумме')
plt.show()

