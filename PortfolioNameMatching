import pandas as pd
from fuzzywuzzy import fuzz, process
import Levenshtein
data_int = pd.read_csv('FinalIntStocks.csv')
data_us = pd.read_stata('dnednmnmk9wsfgxo.dta')
portfolios = pd.read_csv('DataPortfoliosIsin&Name.csv')
portfolios['Actual Young Name']=''
portfolios['Actual Old Name']=''

USAstocks = []
INTstocks = []


for x in data_int['conm']:
    INTstocks.append(x)

INTstocks= set(INTstocks)

for x in data_us['conm']:
    USAstocks.append(x)

USAstocks = set(USAstocks)

ALLstocks = INTstocks.union(USAstocks)
print(ALLstocks)

n1=0
n2=0

for x in portfolios['Name Young']:
    stock = process.extract(str(x), ALLstocks, limit=1)
    stock = stock[0]
    stock = stock[0]
    portfolios['Actual Young Name'][n1] = stock
    n1+=1

for x in portfolios['Name Old']:
    stock = process.extract(str(x), ALLstocks, limit=1)
    stock = stock[0]
    stock = stock[0]
    portfolios['Actual Old Name'][n2] = stock
    n2+=1

portfolios.to_csv('PortfoliosDef.csv')
