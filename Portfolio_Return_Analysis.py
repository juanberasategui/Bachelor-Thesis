import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import string

portfolios = pd.read_csv('PortfoliosDef.csv')
int_stocks = pd.read_csv('FinalIntStocks.csv')
us_stocks = pd.read_stata('dnednmnmk9wsfgxo.dta')
us_stocks['datadate'] = us_stocks['datadate'].apply(str)
int_stocks['datadate'] = int_stocks['datadate'].apply(str)
us_stocks.datadate = us_stocks.datadate.str[:4]
int_stocks.datadate = int_stocks.datadate.str[:4]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = 2015





return_full_period_port_young = []
return_full_period_port_old = []


def yearstocks(year, type):
    stocks = portfolios.loc[portfolios['Year']== year]
    if type == 'young':
        stocks = stocks['Actual Young Name']
    elif type == 'old':
        stocks = stocks['Actual Old Name']
    return stocks

def stockperfyear(stock, year):
    perf_monthly = ([])
    year = str(year)
    stock = str(stock)
    stock = stock.upper()
    if stock in us_stocks['conm'].values:
        stock_perf = us_stocks.loc[us_stocks['conm'] == stock]
        stock_perf = stock_perf.loc[stock_perf['datadate'] == year]

        for x in stock_perf['prccm']:
            perf_monthly.append(x)

    else:
        stock_perf = int_stocks.loc[int_stocks['conm'] == stock]
        stock_perf = stock_perf.loc[stock_perf['datadate'] == year]

        for x in stock_perf['prccd']:
            perf_monthly.append(x)
    perf_monthly = list(pd.Series(perf_monthly).dropna().unique().tolist())
    if len(perf_monthly) <12:
        pass
    else:

        return perf_monthly[:12]

def returnstock(myList =[], *args):
    returnstock = [0]
    for x in range(0,11):
        try:
            r_stock = myList[x+1]/myList[x]

            r_stock = r_stock-1

            returnstock.append(round(r_stock,3))
        except TypeError:
            pass
    return returnstock
n1=0
n2=0

for year in range(2002,2019):

    oldp = yearstocks(year,'old')

    returnsyearold = []


    for x in oldp:

        value =returnstock(stockperfyear(x,year))
        if len(value) !=12:
            pass
        else:
            returnsyearold.append(value)


    returns_month_port_old = []

    for x in range(0,12):
        valuetot = 0
        for y in range(0,len(returnsyearold)):
            val =returnsyearold[y][x]
            val = round(val/len(returnsyearold), 3)
            valuetot+=val
        returns_month_port_old.append(round(valuetot,3))

    #return_old= dict(zip(months, returns_month_port_old))
    for r in returns_month_port_old:

        return_full_period_port_old.append(r)
        n1+=1


    #Same calculation as above but for the young portfolio

    youngs = yearstocks(year,'young')
    returnsyearyoung = []


    for x in youngs:

        value =returnstock(stockperfyear(x,year))
        if len(value) !=12:
            pass
        else:
            returnsyearyoung.append(value)


    returns_month_port_young = []

    for x in range(0,12):
        valuetot = 0
        for y in range(0,len(returnsyearyoung)):
            val =returnsyearyoung[y][x]
            val = round(val/len(returnsyearyoung), 3)
            valuetot+=val
        returns_month_port_young.append(round(valuetot,3))

    for r in returns_month_port_young:

        return_full_period_port_young.append(r)
        n2+=1

#return_young= dict(zip(months, returns_month_port_young))

#print(return_young)

plt.plot(returns_month_port_old, 'b')
plt.plot(returns_month_port_young, 'g')
plt.legend(['Portfolio Old','Portfolio Young'])
plt.title('Monthly Return - 2007')
plt.xlabel(months)
plt.show()

dataframe = pd.DataFrame(data=(zip(return_full_period_port_old,return_full_period_port_young)),
                         columns=['Portfolio Old','Portfolio Young'])
print(return_full_period_port_young)
print(return_full_period_port_old)
