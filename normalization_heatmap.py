# %%
#to create a numpy with area ratio
from math import pi
def arearatio(n):
    arealist = []
    for i in range(0,1025-n,2):
        radius1=1024-i
        radius2=1024-n-i
        area = pi*(radius1*radius1-radius2*radius2)
        arealist.append(area)
    return arealist
area2 = arearatio(2)
area4 = arearatio(4)
area8 = arearatio(8)
# %%
import pandas as pd
ds = pd.read_csv('/home/zxu4/CSE_MSE_RXF131/cradle-members/mdle/zxu4/pix_2_v_4.csv')
#%%
ds.loc[:, ~(ds == 'NaN').any()]
for i in range(len(ds.columns)):
    ds[str(i)] = pd.to_numeric(ds[str(i)])
#%%
ds['total'] = ds. sum(axis=1)
#%%
#this is the correct code for plots
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(512, 0, 512)
ax = plt.axes()
# Setting the background color of the plot 
# using set_facecolor() method
ax.set_facecolor("white")

plt.plot(x,ds['total'],color='black')
#plt.gca().invert_xaxis()
plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left=True,      # ticks along the bottom edge are off
    right=False,         # ticks along the top edge are off
    labelleft=True,       # changes apply to the x-axis
    bottom=True,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=True) # labels along the bottom edge are off
# labels along the bottom edge are off
plt.grid(False)
plt.xlabel("Radius, pixels",fontsize=16)
plt.ylabel("Intensity, a.u",fontsize=16)
ax.set_frame_on(True)
plt.show()
# %%
def ratio_data(data,ratio):
    return (data/ratio)
def ratio_table(df,ratiolist):
    for i in range(len(df. index)):
        df.loc[i] = ratio_data(df.loc[i],ratiolist[i])
ratio_table(ds,area2)

# %%
import seaborn as sns; sns.set_theme()
import numpy as np; np.random.seed(0)
ax = sns.heatmap(ds,cmap='bwr')
ax.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left=False,      # ticks along the bottom edge are off
    right=False,         # ticks along the top edge are off
    labelleft=True,       # changes apply to the x-axis
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=True) # labels along the bottom edge are off
ax.set_xlabel('Sequence number', fontsize =14)
ax.set_ylabel("Radius",fontsize=14)   
# labels along the bottom edge are off

# %%
ds.to_csv('/home/zxu4/CSE_MSE_RXF131/cradle-members/mdle/zxu4/2,4,8_csv_norm/WR2_2.csv',index=False,header = True)

# %%
import pandas as pd
ds = pd.read_csv('/home/zxu4/CSE_MSE_RXF131/cradle-members/mdle/zxu4/PB3_2_raw.csv',index_col=0)
ds = ds[(ds != 'error').all(axis=1)]
ds.index = range(len(ds))
#%%
for i in range(len(ds.columns)):
    ds['ss1'] = pd.to_numeric(ds['ss2'])
    ds['ss2'] = pd.to_numeric(ds['ss2'])
    ds['ss3'] = pd.to_numeric(ds['ss3'])
# %%
import seaborn as sns
g= sns.violinplot(order=["ss1","ss2","ss3"],data = ds,palette=['red','blue','black'])
g.set(xlabel='Stainless steel rings', ylabel='Intensity, a.u')
g.set(ylim=(0, 20000000))# %%
g.set()

# %%
