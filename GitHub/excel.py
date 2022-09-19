from operator import index
import string
import pandas as pd
import numpy as np

#https://github.com/drixit/product-issue-reporting/issues/467




colnames=['N° Issue','Status','Tittle','Labels','Date']
dtypes= {'N° Issue':'str','Status':'str','Tittle':'str','Labels':'str','Date':'str'}
read_file = pd.read_csv ('issues.csv',sep='\t',engine='python', names=colnames, header=None, dtype=dtypes)

df = pd.DataFrame(read_file,
    columns = colnames,
    index = None,
    )
print (df.head())
print (df.dtypes)

# Queda pendiente agregar la columna de URL's 
#df['new'] = df['W'] + df['Y']
#columna_url(df)

excel_file = pd.ExcelWriter('issues.xlsx', engine='openpyxl')
df.to_excel(excel_file, index=False,sheet_name='Issues' )
excel_file.save()




