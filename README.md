# INTEL ONE API HACKATHON SMIT
Link for the web App for Prediction : 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shivam5560-intel-smit-app-eleyjg.streamlit.app)

# Problem Statement : Predict the quality of freshwater

### Expected Solution:
In this track of the hackathon, we apply Machine learning concepts and leverage oneAPI capabilities to help global water security and environmental sustainability efforts by predicting whether freshwater is safe to drink and use for the ecosystems that rely on it. 

# Objective 

The objective of this project are :
a. Create a prediction model which can determine whether the target source is a freshwater or not(i.e Either Safe or Unsafe).
b. Make the model accessable to end users, and aid them solve real world problem 

# Steps to be followed :
1. Download the dataset from the above link(Unzip it) : https://s3-ap-southeast-1.amazonaws.com/he-public-data/datasetab75fb3.zip 
2. Go to the project directory in your local system. Activate the python version 3.9 environment
3. Download the repository (.zip file) 
4. Extract the zip file.
5. Copy the path of extracted folder.
6. Go to the repository folder
```
cd INTEL_SMIT-main
```

7. Install the needed libraries by executing below comands
```
pip install warnings numpy seaborn matplotlib scikit-learn scikit-learn-intelex xgboost pickle streamlit
```

```
pip install -r requirements.txt
```

8. Open the ipynb file 'intel_smit.ipynb' and change the path in the ipynb file from circled part to the path of file in your system.
![WhatsApp Image 2023-03-19 at 11 31 48 PM](https://user-images.githubusercontent.com/59795223/226197342-9cff07b5-734c-498e-b7b9-ac9c84a0cf1f.jpeg)

9. Run the following command  for locally running of the web app for predicting the target variable's output.
```
streamlit run app.py
```
10. Without cloning it you can predict dircetly through :[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shivam5560-intel-smit-app-eleyjg.streamlit.app)

# XGBOOST IS USED AS A ML MODEL , RANDOM FOREST CLASSIFIER PICKLE SIZE IS HUGE(AROUND 8GB OF SPACE REQUIRED) AND BOTH HAVE NEARLY NO DIFFERENCE SO WE USE XGBOOST CLASSIFIER

## Data Analysis
Mapping of Color Attribute :  {'Colorless': 0, 'Faint Yellow': 1, 'Light Yellow': 2, 'Near Colorless': 3, 'Yellow': 4, 'Other': 5}
Mapping of Source Attribute :  {'Aquifer': 0, 'Ground': 1, 'Lake': 2, 'Reservoir': 3, 'River': 4, 'Spring': 5, 'Stream': 6, 'Well': 7, 'Other': 8}

## Feature Enginerring
Index,day,month attributes are removed as it does not correlate with the target data values.
<img width="1296" alt="Screenshot 2023-03-19 at 11 50 04 PM" src="https://user-images.githubusercontent.com/59795223/226198894-b5505292-3b9b-47b8-81fc-35865950e117.png">
We have removed Water Temperature,Air Temperature,Conductivity as it does not correlate with the target value.



## Feature Importances after fitting values in XGBoost Classifier
We can see Manganese,Turbidity,pH values are of high importances for correct prediction of the target value.
<img width="1134" alt="Screenshot 2023-03-19 at 11 49 35 PM" src="https://user-images.githubusercontent.com/59795223/226198875-e6445033-6e36-44d4-b1e1-1bb066855a20.png">

## ROC Curve comparison B/w Logistic Regression and XGBoost Classifier
That's why XGBoost Classifier is Used for ML MODELLING.
<img width="1134" alt="Screenshot 2023-03-19 at 11 49 44 PM" src="https://user-images.githubusercontent.com/59795223/226199076-21bf1d32-7338-4fa1-8b85-9eec706dbfeb.png">



# Web Page for Prediction using Streamlit after clicking with the given link  
<img width="1340" alt="Screenshot 2023-03-19 at 11 06 48 PM" src="https://user-images.githubusercontent.com/59795223/226195790-3c766ae6-c742-4715-bfe3-92a0f26ac02d.png">

# Result after having entered some input
<img width="1680" alt="Screenshot 2023-03-19 at 11 05 21 PM" src="https://user-images.githubusercontent.com/59795223/226195863-c602adf4-f4a6-43b3-86d7-e961e771c057.png">
