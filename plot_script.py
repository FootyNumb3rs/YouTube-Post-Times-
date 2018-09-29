#%matplotlib inline
#%config InlineBackend.figure_format = 'svg'
import pandas as pd
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import style
from itertools import cycle
cycol = cycle('bgrcmk')


df = pd.concat([pd.read_csv('USvideos.csv',header=0).assign(country='US'),
                pd.read_csv('FRvideos.csv',header=0).assign(country='FR')])
df['WeekDay'] = pd.DatetimeIndex(df['publish_time']).weekday
df['Hour'] = pd.DatetimeIndex(df['publish_time']).hour

hfont = {'fontname':'Arial'}

#Creating Sub-plots
fig,ax = plt.subplots(figsize=(12,3))
times = [str(i+1)+'am' if (i<12) else str((i)%12+1)+'pm' for i in range(24)]

# United States 
hdata = df.query('country=="US"')
hdata = hdata.groupby(['WeekDay','Hour']).count().unstack()['video_id'].as_matrix()/len(hdata)
plt.imshow(hdata)
plt.xticks(range(0,24),times,rotation=45,fontname='Arial',fontsize=11.5)
plt.yticks(range(0,7),['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],fontname='Arial',fontsize=12)
plt.title('Post Time',**hfont)


# France
'''
hdata = df.query('country==US').groupby(['WeekDay','Hour']).count().unstack()['video_id'].as_matrix()/len(df)
.imshow(hdata)
times = [str(i+1)+'AM' if (i<12) else str((i)%12+1)+'PM' for i in range(24)]
plt.xticks(range(0,24),times,rotation=45,fontname='Arial')
plt.yticks(range(0,7),['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],fontname='Arial')
plt.title('Post Time',**hfont)
'''

plt.show()