import pandas as pd
import numpy as np

datamaster = pd.read_csv('Dataset_NL.csv')
data_year = pd.read_csv('Final_Data18.csv')
data_year_before = pd.read_csv('Data17.csv')


data_year = data_year.fillna('')
datamaster['date'].astype(str)
year = 2018


data_year['Portfolio value'] = 0
data_year['Yr Return'] = 0
for x in range(1,10):
    data_year['S' + str(x) + '_Value'] = 0
    data_year['S'+str(x)+'_Weight_TotPort'] = 0

for y in range(0, len(data_year)):

    for x in range(1,10):

        if data_year['stock'+str(x)][y][0:2] == 'NL':

            value = datamaster.loc[datamaster['isin']== data_year['stock'+str(x)][y]]
            value = value.loc[value['date']== str(year)+'-12-31']
            value = value['price'].values.astype(float)

            if str(value) == '[]':
                value = 0
            else:
                value = float(value)
                number_stocks=data_year['Nr Shares_Stock'+str(x)][y]
                if number_stocks =='' or number_stocks=="don't know":
                    number_stocks = 0
                else:
                    number_stocks=float(number_stocks)
                valuestock = number_stocks*float(value)
                data_year['S' + str(x) + '_Value'][y] = valuestock

        else:
            continue

for y in range(0, len(data_year)):
    total = 0
    for x in range(1,10):
        if data_year['S' + str(x) + '_Value'][y] == '':
            total += 0
        else:
            total += float(data_year['S' + str(x) + '_Value'][y])

    data_year['Portfolio value'][y] = float(total)

for y in range(0, len(data_year)):
    for x in range(1,10):
        data_year['S'+str(x)+'_Weight_TotPort'][y] = (data_year['S' + str(x) + '_Value'][y])/(data_year['Portfolio value'][y])


datamaster.fillna(0, inplace=True)
data_year.fillna(0, inplace=True)
data_year_before.fillna(0, inplace=True)
n= 0
for x in data_year['nohhold']:
     portval_year_before = data_year_before.loc[data_year_before['nohhold'] == x]
     portval_year_before = portval_year_before['Portfolio value'].values
     portval_year_actual = data_year.loc[data_year['nohhold'] == x]
     portval_year_actual = portval_year_actual['Portfolio value'].values
     portval_year_actual = portval_year_actual[0]

     if portval_year_before.any() != 0:
         portval_year_before = portval_year_before[0]
     portval_year_before = portval_year_before.astype(float)
     portval_year_actual = portval_year_actual.astype(float)



     r_port= ((portval_year_actual)/(portval_year_before)).astype(float)


     #if r_port.astype(float) < float(1.0):
      #   r_port = 1.0-r_port
       #  r_port = -abs(r_port)
    # else:
        # r_port = r_port-1


     if str(r_port) == '[]' or str(r_port) == '[nan]' or str(r_port) == '[inf]' or str(r_port) == '[nan nan]' or str(r_port)=='[inf inf]':
         r_port= 0.0
     else:
         r_port=r_port


     data_year['Yr Return'][n]=r_port
     n+=1

     #data(data_year.loc[data_year['nohhold']==x]['Yr Return']= r_port)


data_year.to_csv('Data18.csv')
