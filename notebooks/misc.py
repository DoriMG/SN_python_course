def answer(n):
    
    print({0:"iris = pd.read_csv('irises.csv', header = 0, index_col = 0)",
           1:"print(iris.columns)",
           2: "use .describe() or alternatively .min() to find  that the min is 1",
           3: "v = set(iris.index)",
           4:"_= iris.plot() - see how the length of the sepals jumps between the three sets",
           5:"""se = iris.loc['setosa']
ve=iris.loc['versicolor']
vi=iris.loc['virginica']
se.plot()
ve.plot()
vi.plot()""",
           6:"""_= iris.hist()
plt.tight_layout()""",
           7:'''def rain_mean(i):
    
    return example.loc[i,'rain'].mean()
    
example['rain_mean']=pd.Series( example.index.map(rain_mean),index = example.index)

example[:12]['rain_mean']''',
           8:'''rain = example ['rain']>example['rain_mean']
rain_months = example.loc[rain]
_= rain_months['yyyy'].value_counts().loc[range(1959,2018)].plot()''',
           9:'''example['rain_ratios'] = example['rain']/example['rain_mean']
max_ratio = example['rain_ratios'].max()
print(max_ratio)
example.loc[example['rain_ratios']==max_ratio]'''
          }[n])
    
def hint(n):
    
    print({0:"replace weather.csv with irises.csv",
           1:"use .columns to get the column titles",
           2: "use .describe() or alternatively .min()",
           3: "convert iris.index into a set to get the three unique values",
           4: "try .plot() of the iris dataframe",
           5:"use iris.loc[type_of_iris] to split up the dataframe" ,
           6:"using .hist()",
           7:"define rain_mean(i) by modifying tmax_mean(i) and then map it onto the rain month",
           8:'''follow the same process that you did for hot substituting the rain column for tmax''',
           9:'''define a new column which is the ratio of rain to rain_mean''',
           
          }[n])