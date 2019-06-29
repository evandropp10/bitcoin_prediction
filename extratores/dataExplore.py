
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#%%
df = pd.read_csv("data_mining.csv")


#%%
df.head()


#%%
df['value'].plot(figsize=[15,6], grid=True )


#%%
plt.subplots(figsize=(15,6))
plt.hist(df['value'], bins = 40, rwidth=20, )


#%%
fig, ax = plt.subplots(figsize=(15,6))
sns.distplot(df['value'], bins = 20, ax=ax)


#%%
df['value'].mean()


#%%
df['value'].median()


#%%
print(df['value'].quantile(q=0.25))
print(df['value'].quantile(q=0.5))
print(df['value'].quantile(q=0.75))
print(df['value'].quantile(q=1))


#%%
df['value'].mode()


#%%
print(df['value'].min())
print(df['value'].max())


#%%
df['value'].max() - df['value'].min()


#%%
df['value'].var()


#%%
df['value'].std()


#%%



#%%
df.corr()


#%%
fig, ax = plt.subplots(figsize=(15,15))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(df.corr(), cmap=cmap, vmax=1, vmin=-1, center=0, ax=ax,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


#%%
df.hist(layout=(11,3), figsize=(31,31))
plt.show()


#%%
plt.subplots(figsize=(15,6))
plt.hist(df['change'], bins = 40, rwidth=20, )


#%%
df['change'].mean()
#%%
df['change'].median()
#%%
df['change'].std()

#%%
plt.boxplot(df['change'], )

#%%
plt.scatter(df['value_tomorrow'], df['value'])


#%%
plt.scatter(df['value_tomorrow'], df['bitcoin'])


#%%
plt.scatter(df['value_tomorrow'], df['bitcoin_price'])


#%%
plt.scatter(df['value_tomorrow'], df['blockchain'])


#%%
plt.scatter(df['value_tomorrow'], df['revenue'])


#%%
plt.scatter(df['value_tomorrow'], df['trade_volume'])


#%%
plt.scatter(df['value_tomorrow'], df['market_cap'])


#%%



#%%



#%%
def fact_class_change(x):
    if x == "down4":
        return 1
    if x == "down3":
        return 2
    if x == "down2":
        return 3
    if x == "down1":
        return 4
    if x == "up1":
        return 5
    if x == "up2":
        return 6
    if x == "up3":
        return 7
    if x == "up4":
        return 8
    
df['fact'] = df['class_change_tomorrow'].apply(fact_class_change)
    


#%%
plt.subplots(figsize=(15,6))
plt.hist(df['fact'])


#%%



