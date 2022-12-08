# -*- coding: utf-8 -*-

import numpy as np
import statistics as stt

mxCustomer = 20000
casherTime = 0

IAT       = np.random.normal ( 1.0 , 0.2 , mxCustomer )
ST_casher = np.random.normal ( 4/6 , 1/6 , mxCustomer )
ST_Salad  = np.random.normal ( 2   , 1/3 , mxCustomer )
SoupDist  = np.random.uniform( 0   , 1   , mxCustomer )

AT        = list()
CT_casher = list()
TC_casher = list()

AT.append(0)

for i in range ( 1 , mxCustomer+1 ):
    AT.append( IAT[i - 1] + AT[i - 1] )
    startTime = max( AT[-1] , casherTime )
    CT_casher.append( startTime + ST_casher[i - 1] )
    TC_casher.append( CT_casher[-1] - AT[-1] )
    casherTime = CT_casher[-1]
AVG_T_C = stt.mean( TC_casher )
CT_casher.sort()

saladArray = CT_casher
saladTimeArray = [0,0,0,0]
CT_salad = list()
TS_Salad = list()

for i in range ( 1 , mxCustomer+1 ):
    
    index = np.argmin( saladTimeArray )
    startTime = max( saladArray[i - 1] , min(saladTimeArray) )
    CT_salad.append( startTime + ST_Salad[i - 1] )
    saladTimeArray[ index ] = startTime + ST_Salad[i - 1]
    TS_Salad.append( saladTimeArray[ index ] - saladArray[i - 1] ) 
AVG_T_S = stt.mean( TS_Salad )  
CT_salad.sort()
    

nSoup = 0
soupArray = list()
for i in range ( mxCustomer ):
    if ( SoupDist[i] < 0.6 ):
        nSoup = nSoup + 1
        soupArray.append( CT_salad[i] )

soupTimeArray = [0,0]
ST_Soup = np.random.normal( 1 , 1/4 , nSoup )
CT_soup = list()
TS_soup = list()

for i in range ( 1 , nSoup+1 ):
    index = np.argmin( soupTimeArray )
    startTime = max( soupArray[i - 1] , min(soupTimeArray) )
    CT_soup.append( startTime + ST_Soup[i - 1] )
    soupTimeArray[ index ] = startTime + ST_Soup[i - 1]
    TS_soup.append( soupTimeArray[ index ] - soupArray[i - 1] )
AVG_T_Soup = stt.mean( TS_soup ) 

print('Average time a customer spends paying & getting food')
print('if getting salad only is : ' , AVG_T_C + AVG_T_S )
print('if getting both is       : ' , AVG_T_C + AVG_T_S + AVG_T_Soup )



    
    