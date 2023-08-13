import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('feeds.csv')

df = df.dropna(axis=0)

df = df.astype({'humidity':'int', 'vibration' : 'int','voltage' : 'int'})

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'random', random_state = 0) 

kmeans.fit(df)

y_predicted = kmeans.predict(df)
print(y_predicted)


def give_pred(current,voltage,temperature,humidity,vibration):
    pred=kmeans.predict([[current,voltage,temperature,humidity,vibration]])
    if pred == 1:
        return "Error"

    else:
        return "No Error"


print(give_pred(5.8 ,232.0 ,59.22 ,68.0 ,0.0))