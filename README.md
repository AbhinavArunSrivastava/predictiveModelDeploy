# predictiveModelDeploy

>URL: https://breast-cancer-predictivemodel.herokuapp.com/


**Introduction**
This project was a basic attempt to deploy my ML Web App using flask and heroku. This model is capable of predicting Breast Cancer. 

**Contents**

This repository contains 7 files:



1. *Procfile* - It is a Process file that is required for all Heroku applications 'data.csv' file.

2. *app.py*: This contains Flask APIs that receives details through API calls, computes the predicted 
                 value based on our model and returns it.

3. *data.csv*: This is the preprocessed dataset on which feature engineering and data cleaning has already been done. 
                            This is the dataset which is used in the deployment app file.
             
4. *flaskCancerProject.py*: This file gives an insight on the approch taken to deal with the different 
                                            features to make them more prominent in model establishment.
                                            
5. *model.pkl*: PKL file is pickled to save space when being stored or transferred over a network then is unpickled and loaded back into program memory during runtime.

6. *templates*: This file contains the HTML file.
