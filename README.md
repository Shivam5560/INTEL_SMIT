# INTEL_SMIT

# Problem Statement : Predict the quality of freshwater

Link for the web App for Prediction : 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shivam5560-intel-smit-app-eleyjg.streamlit.app)

Steps to be followed :
1. Download the dataset from the above link(Unzip it) : https://s3-ap-southeast-1.amazonaws.com/he-public-data/datasetab75fb3.zip 
2. Clone the repository: Execute the following code 

```
git clone https://github.com/Shivam5560/INTEL_SMIT.git
```

3. Go to the repository folder 

```
cd INTEL_SMIT
```

4. Install the needed libraries by executing below comands
```
pip install warnings numpy seaborn matplotlib scikit-learn scikit-learn-intelex xgboost pickle
```

```
pip install -r requirements.txt
```

5. Open the ipynb file 'Code_FreshwaterPrediction.ipynb' and change the path in the ipynb file from circled part to the path of file in your system.
![WhatsApp Image 2023-03-19 at 11 31 48 PM](https://user-images.githubusercontent.com/59795223/226197342-9cff07b5-734c-498e-b7b9-ac9c84a0cf1f.jpeg)


6. Execute the python code and copy the model pickle file with the name 'intel_smit.pkl' in the project directory 

<img width="1312" alt="Screenshot 2023-03-19 at 11 42 32 PM" src="https://user-images.githubusercontent.com/59795223/226198185-fb91ecdd-749f-4e99-ac04-dbabb5f61b35.png">

7. Run the following command  for locally running of the web app fro predicting the target variable's output.
```
streamlit run app.py
```
8. Without cloning it you can predict dircetly through :[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shivam5560-intel-smit-app-eleyjg.streamlit.app)

 



# Web Page for Prediction using Streamlit after clicking with the given link  
<img width="1340" alt="Screenshot 2023-03-19 at 11 06 48 PM" src="https://user-images.githubusercontent.com/59795223/226195790-3c766ae6-c742-4715-bfe3-92a0f26ac02d.png">

# Result after having entered some input
<img width="1680" alt="Screenshot 2023-03-19 at 11 05 21 PM" src="https://user-images.githubusercontent.com/59795223/226195863-c602adf4-f4a6-43b3-86d7-e961e771c057.png">
