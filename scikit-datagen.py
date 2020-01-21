from sklearn.datasets import make_blobs
import pandas as pd
synthd = make_blobs(n_samples=166000000, n_features=10)
pd.DataFrame(synthd[0]).to_csv("datagen.csv",index=False)

test = pd.read_csv("datagen.csv")
test.head()