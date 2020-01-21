import pandas as pd
#df = pd.DataFrame( [ [1, 1, 1], [2, 2, 2] ], columns=['a', 'b', 'c'])
import s3fs


from sklearn.datasets import make_blobs
import pandas as pd
needsamples=200000000*2
synthd = make_blobs(n_samples=needsamples, n_features=10)
df = pd.DataFrame(synthd[0])
df.to_csv("datagen60gb.csv",index=False)



# No multipart config
#s3 = s3fs.S3FileSystem(anon=False)

# Use 'w' for py3, 'wb' for py2
#with s3.open('harshalpatil-s3/datagen2.csv','w') as f:
#    df.to_csv(f)



