import streamlit as st
import seaborn as sns
import altair as alt
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
import matplotlib.pyplot as plt



import pandas as pd
markers = ['x', '*', '.', '|', '_']



st.title("Clustering")
data0 = pd.read_csv("data/Mall_Customers.csv")

data0.rename({'Annual Income (k$)':'Income', \
              'Spending Score (1-100)':'Spend_score'}, axis=1, \
             inplace=True)
st.write(data0.describe())

fig =  alt.Chart(data0).mark_bar().encode(
    alt.X("Income", bin=True),
    y="count()"
)
st.altair_chart(fig, use_container_width=True)






cols_to_scale = ['Age', 'Income', 'Spend_score']
data_scaled = data0.copy()

data_scaled[cols_to_scale] = scaler.fit_transform \
    (data0[cols_to_scale])

data_scaled[cols_to_scale].describe()

sel_cols = ['Income', 'Spend_score']
from scipy.spatial.distance import cdist
cust3 = data_scaled[sel_cols]
cdist(cust3, cust3, metric='euclidean')

from sklearn.cluster import KMeans

cluster_cols = ['Income', 'Spend_score']
# da = data_scaled.plot.scatter(x='Income', y='Spend_score',
#                          color='gray')
#
# st.pyplot(da)

a = alt.Chart(data_scaled).mark_circle().encode(
    alt.X('Income').scale(zero=False),
    alt.Y("Spend_score").scale(zero=False, padding=1)

)
st.altair_chart(a)
from sklearn.cluster import KMeans
model = KMeans(n_clusters=5, random_state=42)
model.fit(data_scaled[cluster_cols])
data_scaled['Cluster'] = model.predict(data_scaled[cluster_cols])
fig = plt.figure()
for clust in range(5):
    temp = data_scaled[data_scaled.Cluster == clust]

    plt.scatter(temp.Income, temp.Spend_score,
            marker=markers[clust],
            color = 'gray',
            label="Cluster "+str(clust))
plt.xlabel('Income')
plt.ylabel('Spend_score')
plt.legend()
st.pyplot(fig)