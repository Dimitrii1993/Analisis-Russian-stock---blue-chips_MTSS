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

# Анализ двух графиков динамики 
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


