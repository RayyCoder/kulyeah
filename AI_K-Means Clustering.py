# 4 CLUSTER
#1. import library
from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt

#2. membaca dataset
path = r'D:\Tugas dan Projek Kuliah\Data Tekanan Darah dan Berat Badan.csv'
df = pd.read_csv(path, sep=';')

# Visualisasi dataset
plt.scatter(df['TEKANAN DARAH'], df['BERAT BADAN'])
plt.title('Diagram Sebaran Data')
plt.xlabel('Tekanan Darah')
plt.ylabel('Berat Badan')
plt.show()

#3. Clustering dengan K-Means
km = KMeans(n_clusters=4)  # melakukan pengelompokan data menjadi 4 kelompok
y_predicted = km.fit_predict(df[['TEKANAN DARAH', 'BERAT BADAN']])

# penambahan kolom "Cluster" untuk menampilkan hasil klaster setiap data
df['cluster'] = y_predicted
df.head()

print(df)
# menampilkan nilai centroid
# print(km.cluster_centers_)

#4. Menampilkan histogram cluster
plt.hist(df['cluster'])
plt.title('Histogram Cluster')
plt.xlabel('Cluster')
plt.ylabel('Jumlah Data')
plt.show()

#5. visualisasi hasil clustering dengan scatter plot
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]
df4 = df[df.cluster == 3]

plt.title('Hasil Clustering')
plt.xlabel('TEKANAN DARAH')
plt.ylabel('BERAT BADAN')
plt.scatter(df1['TEKANAN DARAH'], df1['BERAT BADAN'], color='green')
plt.scatter(df2['TEKANAN DARAH'], df2['BERAT BADAN'], color='red')
plt.scatter(df3['TEKANAN DARAH'], df3['BERAT BADAN'], color='black')
plt.scatter(df4['TEKANAN DARAH'], df4['BERAT BADAN'], color='blue')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*')
plt.show()

# 2 Cluster
#1. import library
from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt

#2. membaca dataset
path = r'D:\Tugas dan Projek Kuliah\Data Tekanan Darah dan Berat Badan.csv'
df = pd.read_csv(path, sep=';')

# Visualisasi dataset
plt.scatter(df['TEKANAN DARAH'], df['BERAT BADAN'])
plt.title('Diagram Sebaran Data')
plt.xlabel('Tekanan Darah')
plt.ylabel('Berat Badan')
plt.show()

#3. Clustering dengan K-Means
km = KMeans(n_clusters=2)  # melakukan pengelompokan data menjadi 4 kelompok
y_predicted = km.fit_predict(df[['TEKANAN DARAH', 'BERAT BADAN']])

# penambahan kolom "Cluster" untuk menampilkan hasil klaster setiap data
df['cluster'] = y_predicted
df.head()

print(df)
# menampilkan nilai centroid
# print(km.cluster_centers_)

#4. Menampilkan histogram cluster
plt.hist(df['cluster'])
plt.title('Histogram Cluster')
plt.xlabel('Cluster')
plt.ylabel('Jumlah Data')
plt.show()

#5. visualisasi hasil clustering dengan scatter plot
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]

plt.title('Hasil Clustering')
plt.xlabel('TEKANAN DARAH')
plt.ylabel('BERAT BADAN')
plt.scatter(df1['TEKANAN DARAH'], df1['BERAT BADAN'], color='green')
plt.scatter(df2['TEKANAN DARAH'], df2['BERAT BADAN'], color='red')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*')
plt.show()

# 6 CLUSTER
#1. import library
from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt

#2. membaca dataset
path = r'D:\Tugas dan Projek Kuliah\Data Tekanan Darah dan Berat Badan.csv'
df = pd.read_csv(path, sep=';')

# Visualisasi dataset
plt.scatter(df['TEKANAN DARAH'], df['BERAT BADAN'])
plt.title('Diagram Sebaran Data')
plt.xlabel('Tekanan Darah')
plt.ylabel('Berat Badan')
plt.show()

#3. Clustering dengan K-Means
km = KMeans(n_clusters=6)  # melakukan pengelompokan data menjadi 4 kelompok
y_predicted = km.fit_predict(df[['TEKANAN DARAH', 'BERAT BADAN']])

# penambahan kolom "Cluster" untuk menampilkan hasil klaster setiap data
df['cluster'] = y_predicted
df.head()

print(df)
# menampilkan nilai centroid
# print(km.cluster_centers_)

#4. Menampilkan histogram cluster
plt.hist(df['cluster'])
plt.title('Histogram Cluster')
plt.xlabel('Cluster')
plt.ylabel('Jumlah Data')
plt.show()

#5. visualisasi hasil clustering dengan scatter plot
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]
df4 = df[df.cluster == 3]
df5 = df[df.cluster == 4]
df6 = df[df.cluster == 5]

plt.title('Hasil Clustering')
plt.xlabel('TEKANAN DARAH')
plt.ylabel('BERAT BADAN')
plt.scatter(df1['TEKANAN DARAH'], df1['BERAT BADAN'], color='green')
plt.scatter(df2['TEKANAN DARAH'], df2['BERAT BADAN'], color='red')
plt.scatter(df3['TEKANAN DARAH'], df3['BERAT BADAN'], color='black')
plt.scatter(df4['TEKANAN DARAH'], df4['BERAT BADAN'], color='yellow')
plt.scatter(df5['TEKANAN DARAH'], df5['BERAT BADAN'], color='purple')
plt.scatter(df6['TEKANAN DARAH'], df6['BERAT BADAN'], color='orange')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*')
plt.show()

# 8 CLUSTER
#1. import library
from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt

#2. membaca dataset
path = r'D:\Tugas dan Projek Kuliah\Data Tekanan Darah dan Berat Badan.csv'
df = pd.read_csv(path, sep=';')

# Visualisasi dataset
plt.scatter(df['TEKANAN DARAH'], df['BERAT BADAN'])
plt.title('Diagram Sebaran Data')
plt.xlabel('Tekanan Darah')
plt.ylabel('Berat Badan')
plt.show()

#3. Clustering dengan K-Means
km = KMeans(n_clusters=8)  # melakukan pengelompokan data menjadi 4 kelompok
y_predicted = km.fit_predict(df[['TEKANAN DARAH', 'BERAT BADAN']])

# penambahan kolom "Cluster" untuk menampilkan hasil klaster setiap data
df['cluster'] = y_predicted
df.head()

print(df)
# menampilkan nilai centroid
# print(km.cluster_centers_)

#4. Menampilkan histogram cluster
plt.hist(df['cluster'])
plt.title('Histogram Cluster')
plt.xlabel('Cluster')
plt.ylabel('Jumlah Data')
plt.show()

#5. visualisasi hasil clustering dengan scatter plot
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]
df4 = df[df.cluster == 3]
df5 = df[df.cluster == 4]
df6 = df[df.cluster == 5]
df7 = df[df.cluster == 6]
df8 = df[df.cluster == 7]

plt.title('Hasil Clustering')
plt.xlabel('TEKANAN DARAH')
plt.ylabel('BERAT BADAN')
plt.scatter(df1['TEKANAN DARAH'], df1['BERAT BADAN'], color='green')
plt.scatter(df2['TEKANAN DARAH'], df2['BERAT BADAN'], color='red')
plt.scatter(df3['TEKANAN DARAH'], df3['BERAT BADAN'], color='black')
plt.scatter(df4['TEKANAN DARAH'], df4['BERAT BADAN'], color='yellow')
plt.scatter(df5['TEKANAN DARAH'], df5['BERAT BADAN'], color='purple')
plt.scatter(df6['TEKANAN DARAH'], df6['BERAT BADAN'], color='orange')
plt.scatter(df7['TEKANAN DARAH'], df7['BERAT BADAN'], color='pink')
plt.scatter(df8['TEKANAN DARAH'], df8['BERAT BADAN'], color='brown')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*')
plt.show()