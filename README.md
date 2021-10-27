# CAR-INSURANCE-FRAUD-CLASSIFICATION

[![wakatime](https://wakatime.com/badge/user/8f2e3b3a-321e-4119-b4f0-3a33c3752953/project/a7854631-977a-444a-bd66-1bdf27ccf8f1.svg)](https://wakatime.com/badge/user/8f2e3b3a-321e-4119-b4f0-3a33c3752953/project/a7854631-977a-444a-bd66-1bdf27ccf8f1)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://insurance-fraud-detector-sundi.herokuapp.com/)&nbsp;
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)&nbsp;
<img src="https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg">&nbsp;
![GitHub repo size](https://img.shields.io/github/repo-size/Shashank-Sundi/INSURANCE-FRAUD-CLASSIFICATION)&nbsp;
![Lines of code](https://img.shields.io/tokei/lines/github/Shashank-Sundi/INSURANCE-FRAUD-CLASSIFICATION?style=flat)

Machine Learning Project to detect whether a Car Insurance Claim made by a Customer is Fraudulent or Not

<img src="static\images\michael-jin-zI_R7sUQVF0-unsplash.jpg" style="width: 1000px;
    height: 500px; object-fit: cover;
    object-position: 20% 60%;" alt="affair" />
<hr>

## Deployment

The model has been deployed using REST API using flask, on Heroku :  https://insurance-fraud-detector-sundi.herokuapp.com/


## Original Dataset and Python Notebook

Original Dataset :  https://www.kaggle.com/roshansharma/fraud-detection-in-insurance-claims/data

Python Notebook : https://shashank-sundi.github.io/INSURANCE-FRAUD-CLASSIFICATION/

Python Notebook : https://github.com/Shashank-Sundi/NOTEBOOKS/blob/main/INSURANCE-CLAIM-FRAUD.ipynb

<hr>

## Project Description

| PROBLEM | MODELS USED  |LIBRARIES USED   |IDE's USED|
| :-------- | :------- | :------------------------- | :-------|
| **Predicting if a car insurance claim is fraudulent or not**| `Logistic Regression,`  `KNN,` `Kmeans,` `SVC,` `Naive Bayes,` `Bagging-Dtree,` `Adaboost` `Random Forest,` `XGBoost` | `Sklearn ,` ` Seaborn ,` `Plotly,` `Joypy,` `Pandas ,` `Numpy ,` `Scipy ,` `Xgboost `|`PyCharm,` `VS Code,` `Jupyter Notebook`|

<hr>

## Project Execution

### (A) **Analysis in Jupyter Notebook**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Validated and rectified the data types of the features and analysed their statistical properties|
|2|Performed Random Sample Imputation for Categorical columns and KNN imputation for Numerical Columns
|3| Performed EDA on data - checked the distribution of data using NPP, KDE plots , visualized relation between the different features|
|4|Performed Mean , Target Guided Ordinal , One-hot and frequency encoding on the various categorical features, according to the type and information of features
|6|Visualized Outliers via BoxPlots and removed the possible Outliers
|7| Created new features from existing date columns
|8| Visualized the correlation matrix and removed highly correlated columns
|9| Performed Feature Selection using various methods like SFS , SBS ,RFE,CHI2 etc. and compared overall performance of the individual features
|10|Chose 20 features based on feature v/s performance graph from SFS
|11| Handled the Imbalance in the dataset by using SMOTE
|12|Clustered the dataset into 4 clusters , using Kmeans and the kmeans-elbow graph
|13| Metric used to evaluate models - Recall and Accuracy
|14| Trained and tested various models on the data clusters and for each cluster , chose the model which gave highest adj r2 score
|15|By analyzing the performance of the models , it was unsderstood that the Models generalized better after clustering , hence we chose different models for each cluster
|16|Performed Hyperparameter Tuning on all the four models
|17|Cluster 1 - Model : Random Forest :Recall-90.34% Accuracy-89.51%
|18|Cluster 2 - Model : KNN :Recall-100% Accuracy-100%
|19|Cluster 3 - Model : Adaboost :Recall-100% Accuracy-96.55%
|20|Cluster 4 - Model : Logistic Regression :Recall-100% Accuracy-87.5%
|21| Exported all required models via pickle


### (B) **Building the Application**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Built Log Writer Package , for writing the log messages in a centralised log file
|2| Built the Data Formatter Package, for aggregating the inputs from the html form ; converting the input to a dataframe
|3| Buil the Valaidator Package , to validate the data types of inputs , column names , length etc.
|4| Built the Preprocessing Package ,for imputation , encoding and other transformations
|5| Built Package for finding the cluster to which the input data belongs ; exporting the model trained for the corresponding cluster
|5| Built REST API using Flask framework ; created routes for home page and prediction , by calling all the required modules 
|6| Created the requirements.txt , Procfile , etc. and all other requirements to be satisfied for deployment.
|7| Built html pages for data input and results prediction
|8| Deployed the model on Heroku via Git Bash terminal

<hr>

## Screenshots

### **Enter the required inputs in home page and press predict button**

<img src="static\images\home fraud.PNG" alt="FIFA" />

### **The Prediction Page**

<img src="static\images\result fraud.PNG" alt="FIFA" />

<hr>
  
## Contact

<a href="https://www.linkedin.com/in/shashank-sundi-4b78561b1"> ![alt text](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>&emsp;
<a href="https://www.instagram.com/shashank_sundi13/">![alt text](https://img.shields.io/badge/Shashank_Sundi-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>&emsp;
<a href="mailto:sundi.sn@gmail.com">![alt text](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>

<hr>
