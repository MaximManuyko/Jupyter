#!/usr/bin/env python
# coding: utf-8

# # Данные о численности населения мира

# https://www.kaggle.com/datasets/sazidthe1/world-population-data?select=world_population_data.csv

# **О наборе данных**
# Контекст
# 
# Население мира претерпело значительный рост, превысив 7,5 миллиарда к середине 2019 года и продолжая расти сверх предыдущих оценок. Примечательно, что Китай и Индия стоят как две самые густонаселенные страны, при этом население Китая потенциально сталкивается с сокращением, в то время как траектория Индии намекает на то, чтобы превзойти ее к 2030 году. Этот значительный демографический сдвиг является лишь одним из аспектов глобального ландшафта, где такие страны, как Соединенные Штаты, Индонезия, Бразилия, Нигерия и другие, каждая из которых имеет население более 100 миллионов человек, играют ключевую роль.
# 
# Однако устойчивое снижение темпов роста изменет прогнозы. В то время как ожидается, что население мира превысит 8 миллиардов к 2030 году, рост заметно замедлится по сравнению с предыдущими десятилетиями. Конкретные страны, такие как Индия, Нигерия и несколько африканских стран, внесут значительный вклад в этот рост, потенциально удвоив свое население до плато ставок.
# 
# **Содержание**
# 
# Этот набор данных предоставляет исчерпывающие исторические данные о численности населения для стран и территорий во всем мире, предлагая представление о различных параметрах, таких как размер площади, континент, темпы роста населения, рейтинги и процент населения мира. С 1970 по 2023 год он включает в себя данные о численности населения за разные годы, что позволяет детально изучить демографические тенденции и изменения с течением времени.
# 
# **Набор данных**
# 
# Этот набор данных, структурированный с тщательной детализацией, предлагает широкий спектр информации в формате, способствующем анализу и исследованию. Благодаря таким параметрам, как население по годам, рейтинг стран, географические детали и темпы роста, он служит ценным ресурсом для исследователей, политиков и аналитиков. Кроме того, включение темпов роста и процентов населения мира дает четкое понимание того, как страны вносят свой вклад в глобальные демографические сдвиги.
# 
# Этот набор данных бесценен для тех, кто заинтересован в понимании исторических тенденций в области народонаселения, прогнозировании будущих демографических моделей и проведении углубленного анализа для информирования политики в различных секторах, таких как экономика, городское планирование, общественное здравоохранение и многое другое.
# 
# **Структура**
# 
# Этот набор данных, охватывающий период с 1970 по 2023 год, включает в себя следующие столбцы:
# 
# **Имя Столбца	описание**
# 
# Rank	Ранг по численности населения
# 
# CCA3	3-значный код страны/территории
# 
# Country	Название страны
# 
# Continent	Название континента
# 
# 2023 Population	Население страны в 2023 году
# 
# 2022 Population	Население страны в 2022 году
# 
# 2020 Population	Население страны в 2020 году
# 
# 2015 Population	Население страны в 2015 году
# 
# 2010 Population	Население страны в 2010 году
# 
# 2000 Population	Население страны в 2000 году
# 
# 1990 Population	Население страны в 1990 году
# 
# 1980 Population	Население страны в 1980 году
# 
# 1970 Population	Население страны в 1970 году
# 
# Area (km²)	Размер территории страны/территории в квадратных километрах
# 
# Density (km²)	Плотность населения на квадратный километр
# 
# Growth Rate	Темпы роста населения по странам
# 
# World Population Percentage	Процент населения по каждой стране
# ________________________________________________________________
# 

# In[116]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[117]:


# переменные для размеров графиков

a = 20


# In[118]:


# Загрузка данных из CSV файла в датафрейм
file_path = "/Users/maxim_manuyko/Documents/GitHub/Jupiter/1_Данные_о_численности_населения_мира.csv"
world_population_data = pd.read_csv(file_path)


world_population_data.head(1000000)


# In[119]:


world_population_data.describe()


# In[120]:


world_population_data_copy = world_population_data.copy(deep=True)

world_population_data_copy['growth rate'] = pd.to_numeric(world_population_data_copy['growth rate'].str.replace('%', ''), errors='coerce')
world_population_data_copy['world percentage'] = pd.to_numeric(world_population_data_copy['world percentage'].str.replace('%', ''), errors='coerce')

# Построение тепловой карты корреляции
correlation_matrix = world_population_data_copy[['area (km²)', 'density (km²)', 'growth rate', 'world percentage', '2023 population']].corr()

plt.figure(figsize=(a * 0.2, a * 0.2))
cmap = sns.color_palette("coolwarm", as_cmap=True)
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap=cmap, vmin=-1, vmax=1, center=0, linewidths=.5, square=True)
plt.title('Тепловая карта корреляции')
plt.show()


# In[121]:


x_columns = ['2023 population', '2022 population', '2020 population', '2015 population', '2010 population', '2000 population', '1990 population', '1980 population', '1970 population']
y_columns = ['2023 population', '2022 population', '2020 population', '2015 population', '2010 population', '2000 population', '1990 population', '1980 population', '1970 population']

# Инвертируйте порядок колонок
x_columns = x_columns[::-1]
y_columns = y_columns[::-1]

# Создайте новый датафрейм с суммарными значениями по выбранным колонкам
sum_df = world_population_data[y_columns].sum()

# Постройте линейный график
plt.figure(figsize=(a, a * 0.3))
plt.plot(x_columns, sum_df, marker='o', linestyle='-', color='b')
plt.title('Суммарная популяция по годам')
plt.xlabel('Год')
plt.ylabel('Суммарная популяция, млн. чел.')
plt.grid(True)
plt.show()


# In[122]:


# Установка размера графика
plt.figure(figsize=(a, a * 0.3))

# Выбор только первых 10 стран
top_10_countries = world_population_data.head(10)

# Построение горизонтального столбчатого графика
plot = sns.barplot(x='2023 population', y='country', data=top_10_countries)

# Добавление значений над столбцами
for index, value in enumerate(top_10_countries['2023 population']):
    plot.text(value, index, f'{value:,}', ha='left', va='center', fontsize=10)

# Настройка заголовка и меток осей
plt.title('График населения Топ 10 странв в 2023 году')
plt.xlabel('2023 год Население')
plt.ylabel('Страна')

# Отображение графика
plt.show()


# In[123]:


# Установка размера графика
plt.figure(figsize=(a, a * 0.3))

# Выбор только последних 10 стран
bottom_10_countries = world_population_data.tail(10)

# Построение горизонтального столбчатого графика
plot = sns.barplot(x='2023 population', y='country', data=bottom_10_countries)

# Добавление значений над столбцами
for index, value in enumerate(bottom_10_countries['2023 population']):
    plot.text(value, index, f'{value:,}', ha='left', va='center', fontsize=10)

# Настройка заголовка и меток осей
plt.title('График населения FLOP 10 странв в 2023 году')
plt.xlabel('2023 год Население')
plt.ylabel('Страна')

# Отображение графика
plt.show()


# In[124]:


# Группировка данных по континентам и суммирование населения для 2023 года
continent_population = world_population_data.groupby('continent')['2023 population'].sum()

# Создание круговой диаграммы
plt.figure(figsize=(a * 0.5, a * 0.4))
patches, texts, autotexts = plt.pie(continent_population, labels=continent_population.index, autopct='%1.1f%%', startangle=140)

# Добавление аннотаций (количество жителей) на круговую диаграмму
for text, autotext, value in zip(texts, autotexts, continent_population):
    text.set_text(f'{text.get_text()} ({value:,} чел.)')

# Настройка заголовка
plt.title('Распределение населения по континентам в 2023 году')

# Отображение круговой диаграммы
plt.show()


# In[125]:


# Выбираем первые 10 стран
top_10_countries = world_population_data.head(10)

# Отсортируем столбцы с годами
sorted_columns = sorted(['2023 population', '2022 population', '2020 population', '2015 population',
                          '2010 population', '2000 population', '1990 population', '1980 population', '1970 population'])

# Строим линейные графики для каждой страны
plt.figure(figsize=(a, a * 0.3))

for index, row in top_10_countries.iterrows():
    country_name = row['country']
    population_data = row[sorted_columns]
    
    plt.plot(population_data, label=country_name)

# Настройка осей и легенды
plt.xlabel('Год')
plt.ylabel('Население, млн. чел')
plt.title('Население топ-10 стран по годам')
plt.legend()
plt.xticks(rotation=45)  # Поворот названий годов для лучшей читаемости

# Отображение графика
plt.show()


# In[126]:


# Создаем DataFrame down_Population
down_Population = world_population_data[['rank', 'cca3', 'country', 'continent', '2023 population', '1970 population']].copy()

# Добавляем колонку down_Population как разницу между 2023 population и 1970 population
down_Population['down_Population'] = down_Population['2023 population'] - down_Population['1970 population']

# Сортируем по возрастанию по колонке down_Population
down_Population = down_Population.sort_values(by='down_Population')

# Отфильтровываем значения меньше или равно нулю
down_Population = down_Population[down_Population['down_Population'] <= 0]

# Выводим результат
down_Population.head(1000000)


# In[127]:


# Создаем DataFrame down_Population
down_Population = world_population_data.copy()

# Добавляем колонку down_Population как разницу между 2023 population и 1970 population
down_Population['down_Population'] = down_Population['2023 population'] - down_Population['1970 population']

# Сортируем по возрастанию по колонке down_Population
down_Population = down_Population.sort_values(by='down_Population')

# Отфильтровываем значения меньше или равно нулю
down_Population = down_Population[down_Population['down_Population'] <= 0]

# Определение списка колонок с данными о населении
population_columns = ['2023 population', '2022 population', '2020 population', 
                      '2015 population', '2010 population', '2000 population', 
                      '1990 population', '1980 population', '1970 population']

# Переворачивание порядка колонок по оси x
population_columns.reverse()

# Построение графиков для каждой страны
for country in down_Population['country'].unique():
    country_data = down_Population[down_Population['country'] == country]
    
    # Сортировка данных по выбранным годам
    sorted_data = country_data[population_columns]
    
    # Построение линейного графика
    plt.figure(figsize=(a, a * 0.3))
    plt.plot(sorted_data.columns, sorted_data.iloc[0], marker='o', label=country)
    
    # Добавление значений к точкам на графике
    for i, txt in enumerate(sorted_data.iloc[0]):
        plt.annotate(txt, (sorted_data.columns[i], sorted_data.iloc[0, i]), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.title(f'Изменение населения по годам в {country}')
    plt.xlabel('Год')
    plt.ylabel('Население млн. чел.')
    
    # Добавление горизонтальных линий сетки
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()


# In[128]:


# Сортировка по убыванию density (km²)
sorted_data = world_population_data.sort_values(by='density (km²)', ascending=False).copy()

# Построение горизонтальных столбчатых диаграмм для первых 10 стран
plt.figure(figsize=(a, a * 0.3))
bars = plt.barh(sorted_data['country'].head(10), sorted_data['density (km²)'].head(10), color='skyblue')
plt.xlabel('Плотность населения чел на km²')
plt.title('Top 10 стран по плотности населения')
plt.gca().invert_yaxis()  # чтобы страны были в порядке убывания

# Добавление значений на столбцы
for bar in bars:
    yval = bar.get_width()  # теперь берем значение из ширины столбца
    plt.text(yval, bar.get_y() + bar.get_height()/2, round(yval, 2), ha='left', va='center')

plt.show()

# Построение горизонтальных столбчатых диаграмм для последних 10 стран
plt.figure(figsize=(a, a * 0.3))
bars_bottom = plt.barh(sorted_data['country'].tail(10), sorted_data['density (km²)'].tail(10), color='skyblue')
plt.xlabel('Плотность населения чел на km²')
plt.title('FLOP 10 стран по плотности населения')
plt.gca().invert_yaxis()  # чтобы страны были в порядке убывания

# Добавление значений на столбцы
for bar in bars_bottom:
    yval = bar.get_width()  # теперь берем значение из ширины столбца
    plt.text(yval, bar.get_y() + bar.get_height()/2, round(yval, 2), ha='left', va='center')

plt.show()


# In[129]:


continent_metriks = world_population_data.copy(deep=True)

pivot_table = pd.pivot_table(continent_metriks, values=['2023 population', 'area (km²)'], index='continent', aggfunc='sum')

pivot_table['density (km²)'] = pivot_table['2023 population'] / pivot_table['area (km²)']

pivot_table = pivot_table.reset_index()

# Сортировка по увеличению '2023 population'
pivot_table = pivot_table.sort_values(by='2023 population', ascending=True)

# Выводим DataFrame
pivot_table.head(1000000)


# In[132]:


# Сортируем DataFrame по каждому столбцу
sorted_by_population = pivot_table.sort_values(by='2023 population', ascending=False)
sorted_by_area = pivot_table.sort_values(by='area (km²)', ascending=False)
sorted_by_density = pivot_table.sort_values(by='density (km²)', ascending=False)

# Создаем три горизонтальных столбчатых графика
plt.figure(figsize=(a , a * 0.5))

# График для '2023 population'
plt.subplot(3, 1, 1)
bars_population = plt.barh(sorted_by_population['continent'], sorted_by_population['2023 population'], color='blue')
plt.xlabel('2023 Население, млрд. чел.')
plt.title('2023 Распределение населения по континентам')

# Добавляем значения внутри столбцов
for bar in bars_population:
    yval = bar.get_width()
    plt.text(yval, bar.get_y() + bar.get_height()/2, round(yval, 2), ha='left', va='center')

# Добавляем вертикальные линии сетки
plt.grid(axis='x', linestyle='--', alpha=0.6)

# График для 'area (km²)'
plt.subplot(3, 1, 2)
bars_area = plt.barh(sorted_by_area['continent'], sorted_by_area['area (km²)'], color='green')
plt.xlabel('Площадь km²')
plt.title('Площадь континента km²')

# Добавляем значения внутри столбцов
for bar in bars_area:
    yval = bar.get_width()
    plt.text(yval, bar.get_y() + bar.get_height()/2, round(yval, 2), ha='left', va='center')

# Добавляем вертикальные линии сетки
plt.grid(axis='x', linestyle='--', alpha=0.6)

# График для 'density (km²)'
plt.subplot(3, 1, 3)
bars_density = plt.barh(sorted_by_density['continent'], sorted_by_density['density (km²)'], color='orange')
plt.xlabel('Плотность населения чел./km²')
plt.title('Плотность населения по континентам чел./km²')

# Добавляем значения внутри столбцов
for bar in bars_density:
    yval = bar.get_width()
    plt.text(yval, bar.get_y() + bar.get_height()/2, round(yval, 2), ha='left', va='center')

# Добавляем вертикальные линии сетки
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

