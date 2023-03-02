# Advertising_Sales_Prediction

## Problem Statements and Datasets

- Train and Build Machine Learning End to End a model which predicts sales based on the money spent on different platforms for marketing. and aslo devloped a web application for same

- Use the advertising dataset given in ISLR and analyse the relationship between 'TV advertising', 'Radio advertising', 'newspaper advertising'  and 'sales' using a Multiple linear regression model.

## Steps

### 1. import Libraries 

- import pandas as pd 
- import numpy as np
- from sklearn.linear_model 
- import matplotlib.pyplot as plt
- import seaborn as sns

### 2. Load Dataset 

### 3. Data Pre-Processing 
- describe the data
- drop unwanted columns
- check & handle outliers
   - it is clear that TV, Radio and target variable sales does not have outlier 
   - newspaper has the 2 outliers
   - so we will treat the outliers of newspapers
   - **Note:**it is upto us how we treat the outlier we may delet it, we may ignore it, or it we may pull it down, but while using linear regression it is nesessary to pull it down or delet it becouse one oulier also badly affect on our linear regression model 

### 4. Split the data
- Independent Variables 'TV', 'radio' and 'newspaper' saved in variable X
- Target Variable 'TV', 'radio' and 'newspaper' saved in variable y
- split the dataset into 80-20 using train_test_split

### 5. Train The Linear Regression Model
- Coefficients of the model  => array([ 0.04629801,  0.18880122, -0.00100282])
    * first coef for first column (TV)
    * second coef for second column (radio)
    * third coef for third column (newspaper)
- intercept_ of the model => 2.848412548439974
    * this is the y intercept in the linear Reggression 

- Therefor the equation become
    * **sales= 2.84 + 0.04\*TV + 0.19\*radio + 0.001\*newspaper**

    **note:**
    * even if spend 0 on advertisement on TV, Radio, newspaper 
    * then also we get the sales of 2.84 which is y intercept

### 6. Evaluate the Performance
- train dataset => rmse=1.6957711089912768 r2=0.8929135972742749
- test dataset => rmse=1.558510777921377 r2=0.9095593368967716

   * we are getting 90% r2_score in both train and test data 
   * which means that model is able to explain the 90% of variation in target variable of train and test data

### 7. Pickling of Model



# Linear Regression Using Statsmodels Library
- stats model gives some detailed analaysis so we are doing Linear Regression Using Statsmodels Library
- model.summary()
- OLS Regression Results
    - Dep. Variable:	sales	R-squared:	0.893
    - Model:	OLS	Adj. R-squared:	0.891
    - Method:	Least Squares	F-statistic:	433.6
    - Date:	Sat, 01 Oct 2022	Prob (F-statistic):	1.98e-75
    - Time:	02:28:39	Log-Likelihood:	-311.53
    - No. Observations:	160	AIC:	631.1
    - Df Residuals:	156	BIC:	643.4
    - Df Model:	3		
    - Covariance Type:	nonrobust		

            -           coef	std_err	  t	    P>|t| 	[0.025	0.975]
            - Intercept	2.8484	0.369	7.720	0.000	2.120	3.577
            - TV	        0.0463	0.002	28.692	0.000	0.043	0.049
            - radio	    0.1888	0.010	19.798	0.000	0.170	0.208
            - newspaper	-0.0010	0.007	-0.144	0.885	-0.015	0.013

    - Omnibus:	51.032	Durbin-Watson:	1.993
    - Prob(Omnibus):	0.000	Jarque-Bera (JB):	131.406
    - Skew:	-1.318	Prob(JB):	2.92e-29
    - Kurtosis:	6.572	Cond. No.	477.


### interpretation of output
* in first table the p value **(Prob (F-statistic)=1.98e-75)**
* the meaning of this is
                         
          *  P < 0.05 then it is statistically Valid LR model
          *  P > 0.05 then it is statistically not Valid LR model
   
 * R^2=0.893 and adj.R^2=0.891 are two important performance metrices
 * they define the independent variables(TV + radio + newspaper) ability to explain the  89% variation in dependent variable (Sales) 
   
  
 * second table gives the coefficient value
 * there also a p value column where same above concept is applied
 * therefor coefficient of intercept, TV and radio are statistically significant
 * where as newspaper 0.885 > 0.05 is statistically not significant this
 * we can say that sales value is not impacted by newspaper 
 * we can delet the newspaper feature 
 
 
 **Hypothesis testing**
 * Null Hypothesis (H0)= The relationship is not significant
 * Alternate Hypothesis (H1)= The relationship is Significant
 
 * P value < Threshold(0.05) then we reject the null hypothesis and accept the Alternate Hypothesis
 
 * in this model p value < 0.05 therefor model is Significant  

 
