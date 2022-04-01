mport pandas as pd
import numpy as np

data = pd.read_csv('Data18.csv')
data.fillna(0,inplace=True)
stocks = []


for x in range(1,10):
    for y in data['stock'+str(x)]:
        if y == 0:
            continue
        else:
            stocks.append(y)

stocks = set(stocks)
print(stocks)
stock_tot = {}

#until here we have the shares present

for x in stocks:

    total = 0
    age_score = 0
    for z in range(1,10):
        dtf = data.loc[data['stock'+str(z)] == x]
        valtot = dtf['Nr Shares_Stock'+str(z)]
        totvalscr = dtf[['Nr Shares_Stock'+str(z), 'age']]
        for y in valtot:
            total+=y

    for z in range(1, 10):
        dtf = data.loc[data['stock' + str(z)] == x]
        valtot = dtf['Nr Shares_Stock' + str(z)]
        totvalscr = dtf[['Nr Shares_Stock' + str(z), 'age']]
        for index, row in totvalscr.iterrows():
            values = row.values
            amount = values[0]
            agee = values[1]
            try:
                weight = float(amount)/total
            except ZeroDivisionError:
                weight = 0
            score = agee*weight
            age_score+=score
            print(amount,agee)
    stock_tot[''+str(x)+''] = age_score

#until here we have the total amount of shares per year

for x in stocks:
    for z in range(1,10):
        dtf = data.loc[data['stock'+str(z)] == x]
        age = dtf['age']


print(stock_tot)
