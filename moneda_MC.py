import pandas as pd
import numpy as np
import random 
#from scipy.stats import norm

cara = 1
sello = 0
num_de_lanzamiento = 10000
cara_sello= []



for i in range(0,num_de_lanzamiento):
    cara_sello.append(random.randint(sello,cara))



df1 = pd.DataFrame ({  'cara/sello' : cara_sello })

print(df1.head())


    
     