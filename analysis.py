import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as pyplt

full_dataset = pd.read_excel('PitchforkOutput.xlsx', 'Sheet1', index_col=0, na_values=['NA'])
no_reissues = pd.read_excel('PitchforkOutput_noreissues6-27.xlsx', 'Sheet1', index_col=0, na_values=['NA'])
no_accolades = pd.read_excel('PitchforkOutput_noaccolades6-27.xlsx', 'Sheet1', index_col=0, na_values=['NA'])
reissues_only = pd.read_excel('Pitchfork_reissues_only6-27.xlsx', 'Sheet1', index_col=0, na_values=['NA'])
bnm_only = pd.read_excel('Pitchfork_bnm_only6-27.xlsx', 'Sheet1', index_col=0, na_values=['NA'])

#print data.head()

print('------------')

print('ROCK')
print no_accolades[no_accolades.Genre_1 == 'Rock'].describe()
print('-----')
print('RAP')
print no_accolades[no_accolades.Genre_1 == 'Rap'].describe()
print('-----')
print('METAL')
print no_accolades[no_accolades.Genre_1 == 'Metal'].describe()
print('-----')
print('ELECTRONIC')
print no_accolades[no_accolades.Genre_1 == 'Electronic'].describe()
print('-----')
print('POP/R&B')
print no_accolades[no_accolades.Genre_1 == 'Pop/R&B'].describe()
print('-----')
print('EXPERIMENTAL')
print no_accolades[no_accolades.Genre_1 == 'Experimental'].describe()
print('-----')
print('FOLK/COUNTRY')
print no_accolades[no_accolades.Genre_1 == 'Folk/Country'].describe()
print('-----')
print('JAZZ')
print no_accolades[no_accolades.Genre_1 == 'Jazz'].describe()
print('-----')
print('GLOBAL')
print no_accolades[no_accolades.Genre_1 == 'Global'].describe()
print('-----')
print('NONE')
print no_accolades[no_accolades.Genre_1 == 'none'].describe()
print('-----')

print('------------')

#print data[data.Accolades == 'Best new music'].describe()

print('------------')

#print data[data.Accolades == 'Best new music'].sort_values(by='Score').head()

print('------------')

#print data[data.Accolades == 'Best new music'].sort_values(by='Score').tail()

print('------------')

#histogram = pyplt.hist(data['Score'], bins=100)
#pyplt.show()

print('------------')
