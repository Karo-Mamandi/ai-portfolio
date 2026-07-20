# 🛍️ Mall Customer Segmentation

A Machine Learning project that applies **unsupervised learning** techniques to segment mall customers based on their purchasing behavior. The project compares multiple clustering algorithms and identifies meaningful customer groups that can help businesses improve marketing strategies and customer targeting.

---

## 📌 Project Overview

Customer segmentation is one of the most common applications of **Unsupervised Machine Learning**.

In this project, I analyzed the **Mall Customers** dataset and implemented multiple clustering algorithms to discover hidden customer groups based on demographic information and spending behavior.

The project compares the performance of:

- K-Means Clustering
- Hierarchical (Agglomerative) Clustering
- DBSCAN

The optimal number of clusters was determined using both the **Elbow Method** and **Silhouette Score**.

---

## 📂 Dataset

The dataset contains information about mall customers, including:

- Customer ID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1–100)

**Target:** None (Unsupervised Learning)

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy

---

# 📚 Libraries Used

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder

from sklearn.cluster import (
    KMeans,
    AgglomerativeClustering,
    DBSCAN
)

from sklearn.metrics import silhouette_score

from scipy.cluster.hierarchy import (
    dendrogram,
    linkage
)
```

---

# 🚀 Project Workflow

## Step 1 — Load the Data

- Import the dataset
- Inspect data types
- Check missing values
- View summary statistics

---

## Step 2 — Exploratory Data Analysis (EDA)

Performed exploratory analysis to better understand customer behavior.

Included:

- Distribution of Age
- Distribution of Annual Income
- Distribution of Spending Score
- Gender distribution
- Correlation analysis
- Scatter plots
- Pair plots

---

## Step 3 — Data Preprocessing

Preprocessing included:

### Label Encoding

Encoded the `Gender` column for future modeling.

### Feature Selection

Started with:

- Annual Income
- Spending Score

Then extended clustering using:

- Age

### Feature Scaling

Applied **StandardScaler** since clustering algorithms rely on distance calculations.

---

## Step 4 — Determine the Optimal Number of Clusters

Two evaluation techniques were used.

### Elbow Method

Measured Within-Cluster Sum of Squares (Inertia) for different values of K.

The "elbow" point indicates the optimal number of clusters.

### Silhouette Score

Evaluated cluster quality using the Silhouette Score.

Higher scores indicate better-separated and more cohesive clusters.

---

## Step 5 — K-Means Clustering

Built the final K-Means model using the optimal number of clusters.

Generated:

- Cluster labels
- Cluster centroids
- Customer segmentation visualization

---

## Step 6 — Hierarchical Clustering

Applied Agglomerative Clustering for comparison.

Generated a **Dendrogram** to visualize hierarchical relationships between customers and help validate the number of clusters.

---

## Step 7 — DBSCAN

Applied Density-Based Spatial Clustering (DBSCAN).

Advantages:

- No need to specify the number of clusters
- Detects arbitrary-shaped clusters
- Identifies noise and outliers
- Labels outliers as `-1`

Experimented with:

- `eps`
- `min_samples`

to obtain meaningful clusters.

---

## Step 8 — Cluster Visualization

Visualized customer segments using scatter plots.

Included:

- K-Means clusters
- Hierarchical clusters
- DBSCAN clusters
- Cluster centroids (K-Means)

---

## Step 9 — Cluster Interpretation

Calculated the average characteristics of each cluster.

Profiled customer groups based on:

- Average Age
- Average Annual Income
- Average Spending Score

Assigned business-friendly labels such as:

- High Income, High Spending
- High Income, Low Spending
- Low Income, High Spending
- Budget Customers
- Average Customers

---

# 📊 Algorithms Compared

| Algorithm | Description |
|-----------|-------------|
| K-Means | Partitions customers into K clusters by minimizing within-cluster variance |
| Agglomerative Clustering | Builds hierarchical clusters using bottom-up merging |
| DBSCAN | Density-based clustering capable of detecting outliers |

---

# 📈 Evaluation Methods

- Elbow Method
- Silhouette Score
- Dendrogram Analysis
- Cluster Visualization

---

# 💡 Business Value

Customer segmentation enables businesses to:

- Identify high-value customers
- Personalize marketing campaigns
- Improve customer retention
- Optimize promotional strategies
- Better understand purchasing behavior
- Increase marketing ROI

---

# 📷 Example Outputs

The project generates:

- Distribution plots
- Correlation heatmap
- Elbow curve
- Silhouette Score comparison
- Dendrogram
- K-Means cluster visualization
- Hierarchical clustering visualization
- DBSCAN clustering visualization
- Cluster profiling summary

---

# 📁 Project Structure

```
Mall-Customers-Segmentation/
│
├── data/
│   └── Mall_Customers.csv
│
├── Mall_Customers_Segmentation.ipynb
└── README.md
```

---

# 🎯 Key Learning Outcomes

Through this project, I gained hands-on experience with:

- Unsupervised Machine Learning
- Customer Segmentation
- Feature Selection
- Data Preprocessing
- Feature Scaling
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Cluster Evaluation
- Elbow Method
- Silhouette Analysis
- Dendrogram Interpretation
- Cluster Profiling
- Business Interpretation of Machine Learning Results
- Data Visualization

---

# 📌 Future Improvements

- Apply Gaussian Mixture Models (GMM)
- Perform PCA for dimensionality reduction
- Tune DBSCAN hyperparameters automatically
- Build an interactive Streamlit dashboard
- Evaluate additional clustering metrics
- Deploy the project as a web application

---

## 👤 Author

**Karo Mamandiazar**

AI Engineer | Machine Learning | Deep Learning

If you found this project useful, consider giving it a ⭐.
