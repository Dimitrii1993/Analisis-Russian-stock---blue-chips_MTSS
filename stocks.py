print('welcome to my repo')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import plotly.express as px

data = pd.read_csv('mtss_2025.txt', sep = ',')
data.info()

mtss = pd.DataFrame({
    'date': data['<DATE>'],
    'price_open': data['<OPEN>'],
    'price_close': data['<CLOSE>'],
    'volume': data['<VOL>'],
})

mtss['date'] = pd.to_datetime(mtss['date'], format = '%Y%m%d')

mtss['price_open'] = mtss['price_open'].astype('int64')
mtss['price_close'] = mtss['price_close'].astype('int64')
mtss['volume'] = mtss['volume'].astype('int64')
mtss.head()
mtss.tail()

# Линейный график - временная диаграмма - свойства, описать что делает
fig, chart = plt.subplots(nrows = 1, ncols = 1, figsize = (15,6))

chart.plot(
    mtss_2025['date'],
    mtss_2025['price_open'],
    label = 'MTSS',
    marker = 'o',
    markerfacecolor = 'yellow',
    markeredgecolor = 'black',
    markersize = 3,
    linestyle = '-',
    linewidth = 1,
    alpha = .80,
    color = 'black')

chart.legend()

chart.set_title('Mtss 2023-2025y', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight': 'bold'})
chart.set_xlabel('Date', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight': 'normal'})
chart.set_ylabel('Price', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight': 'normal'})

chart.set_yticks(range(150,400,30))

chart.grid(True, axis = 'x', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')
chart.grid(True, axis = 'y', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')

chart.tick_params(axis = 'x', rotation = 50)
chart.tick_params(axis = 'y', rotation = 30)

chart.xaxis.set_major_locator(mdates.YearLocator())
chart.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

chart.xaxis.set_minor_locator(mdates.MonthLocator())
chart.xaxis.set_minor_formatter(mdates.DateFormatter('%m'))

chart.set_facecolor('white')

plt.savefig('mtss_2025.png', dpi = 300)

# Анализ двух графиков динамики вместе на одной координатной
mtss_2025.loc[:,'price_close'] = mtss_2025['price_close'].add(3)

fig, chart = plt.subplots(nrows = 1, ncols =1, figsize = (15,8))

chart.plot(
    mtss_2025['date'],
    mtss_2025['price_open'],
    label = 'price_open',
    marker = 'x',
    markerfacecolor = 'yellow',
    markeredgecolor = 'blue',
    markersize = 2,
    linestyle = '--',
    linewidth = 0.5,
    alpha = .8,
    color = 'black')

chart.plot(
    mtss_2025['date'],
    mtss_2025['price_close'],
    linestyle = '-',
    linewidth = 0.5,
    alpha = .8,
    color = 'red')

chart.legend()

chart.set_title('MTSS 2023-2025', fontdict = {'family': 'times New Roman', 'size': 12, 'weight': 'bold'})
chart.set_xlabel('Дата', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})
chart.set_ylabel('Цена', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})

chart.set_yticks(range(150,500,30))

chart.grid(True, axis = 'x', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')
chart.grid(True, axis ='y', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')

chart.tick_params(axis = 'x', rotation = 50)
chart.tick_params(axis = 'y', rotation = 30)

chart.xaxis.set_major_locator(mdates.YearLocator())
chart.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

chart.xaxis.set_minor_locator(mdates.MonthLocator())
chart.xaxis.set_minor_formatter(mdates.DateFormatter('%m'))

chart.set_facecolor('white')

plt.savefig('mtss_2025.png', dpi = 300)

# График динамики показан с верхними границами цены
fig, chart = plt.subplots(nrows = 1, ncols = 1, figsize = (15,8))

chart.plot(
    mtss_2025['date'],
    mtss_2025['price_open'],
    label = 'МТС 2025',
    linestyle = '-',
    linewidth = 0.5,
    alpha = 0.8,
    color = 'black')

chart.fill_between(
    mtss_2025['date'],
    mtss_2025['price_open'],
    mtss_2025['price_close'],
    alpha = .1,
    linestyle = '-',
    linewidth = 0.2,
    color = 'red')

chart.legend()

chart.set_title('MTC 2023-2025г.', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight': 'bold'})
chart.set_xlabel('Дата', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})
chart.set_ylabel('Цена', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})

chart.set_yticks(range(150,500,50))

chart.grid(True,axis = 'x', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')
chart.grid(True,axis = 'y', linestyle = '-', linewidth = 1, alpha = 0.2, color = 'black')

chart.tick_params(axis = 'x', rotation = 50)
chart.tick_params(axis = 'y', rotation = 30)

chart.xaxis.set_major_locator(mdates.YearLocator())

chart.xaxis.set_minor_locator(mdates.MonthLocator())
chart.xaxis.set_minor_formatter(mdates.DateFormatter('%m'))

chart.set_facecolor('white')

plt.savefig('mtss_2025.png', dpi = 300)

fig, chart = plt.subplots(nrows = 1, ncols = 1, figsize = (10,5))

chart.bar(
    mtss_2025['date'],
    mtss_2025['volume'], 
    width = 2,
    alpha=.1, 
    color = 'skyblue',
    edgecolor = 'black')

chart.xaxis.set_major_locator(mdates.YearLocator())
chart.xaxis.set_minor_locator(mdates.MonthLocator())

plt.savefig('mtss_2025_volume.png', dpi = 300)


name = data['<TICKER>'][0][0:4]
mask_1 = mtss_2025['date'] > '2025-01-01'
mask_2 = mtss_2025['date'] < '2025-12-31'

mtss_2025_m = mtss_2025[mask_1 & mask_2]

mtss_2025['year'] = mtss_2025['date'].dt.year

mtss_2025_m['date'] = mtss_2025_m['date'].dt.month
mtss_2025_m = mtss_2025_m.groupby( by = 'date', as_index = False)['volume'].sum()

fig,chart = plt.subplots(nrows = 1, ncols = 1, figsize = (15,8))

chart.bar(
    mtss_2025_m['date'],
    mtss_2025_m['volume'],
    width = 0.9,
    alpha = .5,
    color = 'red',
    edgecolor = 'black')

chart.set_title(f'Объем акций {name} за 2025г.', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight':'bold'})
chart.set_xlabel('Дата', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})
chart.set_ylabel('Цена', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})

chart.grid(True, axis = 'y', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')

# Установка интервала между метками
chart.set_yticks(range(500000,20000000,2500000))


chart.tick_params(axis='x', 
                 which='major',
                 labelsize=10,
                 pad=1)

chart.tick_params(axis = 'x', rotation = 45)

chart.set_facecolor('white')

plt.savefig('mtss_2025.png', dpi = 300)

mask_1 = mtss_2025['date'] > '2025-01-01'
mask_2 = mtss_2025['date'] < '2025-12-31'
mtss_2025_y = mtss_2025[mask_1 & mask_2]

fig, chart = plt.subplots(nrows =1, ncols = 1, figsize = (15,8))

chart.plot(
    mtss_2025_y['date'],
    mtss_2025_y['price_open'],
    label = 'MTSS_2025',
    marker = 'o',
    markerfacecolor = 'red',
    markeredgecolor = 'black',
    markersize = 3,
    linestyle = '--',
    linewidth = 1,
    alpha = 0.8,
    color = 'black'
)

chart.legend()

chart.set_title(f'Акции {name} за 2025г.', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight': 'normal'})
chart.set_xlabel('Дата', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})
chart.set_ylabel('Цена', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})

chart.set_yticks(range(150,500,50))

chart.grid(True,axis = 'x', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')
chart.grid(True,axis = 'y', linestyle = '-', linewidth = 1, alpha = 0.2, color = 'black')

chart.tick_params(axis = 'x', rotation = 50)
chart.tick_params(axis = 'y', rotation = 30)

chart.xaxis.set_major_locator(mdates.YearLocator())

chart.xaxis.set_minor_locator(mdates.MonthLocator())
chart.xaxis.set_minor_formatter(mdates.DateFormatter('%m'))

chart.set_facecolor('white')

plt.savefig('mtss_2025.png', dpi = 300)

mask_1 = mtss_2025['date'] > '2024-01-01'
mask_2 = mtss_2025['date'] < '2024-12-31'

mtss_2024 = mtss_2025[mask_1 & mask_2]

fig, chart = plt.subplots(nrows = 1, ncols = 1, figsize = (15,8))

chart.bar(
    mtss_2024['date'],
    mtss_2024['volume'],
    width = 0.9,
    alpha = .5,
    edgecolor = 'black',
    color = 'blue')

chart.set_title(f'{name} 2024г.', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight': 'normal'})
chart.set_xlabel('Дата', fontdict = {'family': 'Times New Roman','size': 10, 'weight': 'normal'})
chart.set_ylabel('Цена', fontdict = {'family': 'Times New Roman', 'size': 10, 'weight': 'normal'})

chart.set_yticks(range(100000,3000000,250000))

chart.grid(True, axis = 'y', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')

chart.tick_params(axis = 'x',
                  which='major',
                  labelsize=7) # Уменьшение/увеличение значений x
chart.tick_params(axis = 'y',
                  which='major',
                  labelsize=7) # Уменьшение/увеличение значений y

chart.tick_params(axis = 'x', rotation = 45)

chart.xaxis.set_major_locator(mdates.MonthLocator()) # Редактирует месяцы на каждый 
chart.xaxis.set_major_formatter(mdates.DateFormatter('%m')) # Формат месяцев

chart.set_facecolor('white')

plt.savefig('mtss_2024_volume.png', dpi = 300)

fig, chart = plt.subplots(nrows = 1, ncols = 1, figsize = (15,8))

chart.boxplot(
    mtss_2025['price_open'],
    positions = [2],
    widths = 0.3,
    patch_artist = False,
)
chart.set_title(f'{name} 2024г.', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight': 'normal'})
chart.set_ylabel('Цена', fontdict = {'family': 'Times New Roman','size': 10, 'weight': 'normal'})

chart.grid(True, axis = 'y', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')

chart.tick_params(axis = 'x',
                  which='major',
                  labelsize=7) # Уменьшение/увеличение значений x
chart.tick_params(axis = 'y',
                  which='major',
                  labelsize=7) # Уменьшение/увеличение значений y

chart.tick_params(axis = 'x', rotation = 45)

chart.xaxis.set_major_locator(mdates.MonthLocator()) # Редактирует месяцы на каждый 
chart.xaxis.set_major_formatter(mdates.DateFormatter('%m')) # Формат месяцев

chart.set_facecolor('white')

plt.savefig('mtss_2024_volume.png', dpi = 300)

fig, chart = plt.subplots(nrows = 1, ncols = 1, figsize = (15,8))

chart.hist(
    mtss_2025['price_open'],
    bins = 20, # Деление гистограммы на 20 частей
    color = 'red', # Цвет гистограммы
    linewidth = 0.1, # Обводка гистограммы
    edgecolor = 'black' ) # Цвет обводки гистограммы

chart.set_title(f'{name} 2024г.', fontdict = {'family': 'Times New Roman', 'size': 12, 'weight': 'normal'})
chart.set_ylabel('Цена', fontdict = {'family': 'Times New Roman','size': 10, 'weight': 'normal'})

chart.grid(True, axis = 'y', linestyle = '--', linewidth = 1, alpha = 0.2, color = 'black')

chart.tick_params(axis = 'x',
                  which='major',
                  labelsize=7) # Уменьшение/увеличение значений x
chart.tick_params(axis = 'y',
                  which='major',
                  labelsize=7) # Уменьшение/увеличение значений y

chart.tick_params(axis = 'x', rotation = 45)

chart.xaxis.set_major_locator(mdates.MonthLocator()) # Редактирует месяцы на каждый 
chart.xaxis.set_major_formatter(mdates.DateFormatter('%m')) # Формат месяцев

chart.set_facecolor('white')

plt.savefig('mtss_2024_volume.png', dpi = 300)

# ОБОЗНАЧЕНИЕ УРОВНЕЙ ПОДДЕРЖКИ И СОПРОТИВЛЕНИЯ ЗА 2020-2025 ГОД

mask_1 = mtss_2025['date'] > '2020-01-01'
mask_2 = mtss_2025['date'] < '2025-12-31'

mtss_20_25 = mtss_2025[mask_1 & mask_2]
mtss_20_25.reset_index(drop = True, inplace = True)

mtss_20_25 = mtss_20_25.copy()
mtss_20_25['resistance_2'] = 260
mtss_20_25['support_1'] = 190
mtss_20_25['support_2'] = 180

fig, chart = plt.subplots(nrows = 1, ncols = 1, figsize = (15,6))

chart.plot(
    mtss_20_25['date'],
    mtss_20_25['price_open'],
    label = 'price_mtss',
    marker = 'o',
    markeredgecolor = 'blue',
    markerfacecolor = 'blue',
    markersize = 2,
    linestyle = '--',
    linewidth = 1,
    alpha = 0.5, 
    color = 'black'
)

chart.fill_between(
    mtss_20_25['date'],
    mtss_20_25['resistance_1'],
    mtss_20_25['resistance_2'],
    alpha = 0.2,
    color = 'red'
)

chart.plot(
    mtss_20_25['date'],
    mtss_20_25['resistance_1'],
    linestyle = '--',
    color = 'red'
)

chart.fill_between(
    mtss_20_25['date'],
    mtss_20_25['resistance_1'],
    mtss_20_25['resistance_2'],
    alpha = 0.2,
    color = 'red'
)

chart.fill_between(
    mtss_20_25['date'],
    mtss_20_25['support_1'],
    mtss_20_25['support_2'],
    alpha = 0.5,
    color = 'yellow'
)

chart.plot(
    mtss_20_25['date'],
    mtss_20_25['support_1'],
    linestyle = '--',
    color = 'blue'
)
