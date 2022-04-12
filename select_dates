import pandas as pd

data = pd.read_stata('j1gj8adyktip4pot.dta')
data2 = pd.read_stata('dnednmnmk9wsfgxo.dta')
data3 = pd.read_csv('price_data.csv', delimiter=';')
df = pd.DataFrame([['gvkey'],['iid'],['datadate'],['conm'],['prccd'],['isin']])
df = {'gvkey':[],'iid':[],'datadate':[],'conm':[],'prccd':[],'isin':[]}
df = pd.DataFrame(df)
print(df)

data = data.astype(str)

dates = []
stocksindata = []
n = 0
n2 = 0

for x in data['datadate']:
    dates.append(x[:7])
    data['datadate'][n]=x[:7]
    dates.append(x[:7])
    n+=1

for x in data['conm']:
    stocksindata.append(x)

stocksindata = list(set(stocksindata))
dates = set(dates)
dates = sorted(dates)

for x in stocksindata:
    datos = data.loc[data['conm']==x]
    for y in dates:
        dt = datos.loc[datos['datadate']==y]
        dt = dt.tail(1)
        print(dt)
        df = df.append(dt)
        n2+=1

print(df)
df.to_csv('FinalIntStocks.csv')
