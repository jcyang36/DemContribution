import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# process by pandas
df = pd.read_csv('contributionData.zip',index_col=False)
df.head(5)
df.drop('cmte_id', axis=1)
df=df.dropna(axis=1, how='any')
df=df.sort_values(['contb_receipt_dt','tran_id'])
df=df.drop('contbr_nm',axis=1)
df=df[df['cand_nm'].isin(['Sanders, Bernard','Warren, Elizabeth','Buttigieg, Pete','Biden, Joseph R Jr','Gabbard, Tulsi','Steyer, Tom','Klobuchar, Amy J.'])]
df=df.filter()
counts=df["cand_nm"].value_counts()
plt.bar(range(len(counts)),counts)
plt.show()
plt.setlabel
print(counts)