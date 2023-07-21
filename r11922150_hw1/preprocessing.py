import pandas as pd
train_data = pd.read_csv('./covid_train.csv').values
df = pd.DataFrame(train_data)
corrs = df.corr()
output= []
for idx,corr in enumerate(corrs[88]):
    if abs(corr) > 0.7:
        output.append(idx)
print(output)
