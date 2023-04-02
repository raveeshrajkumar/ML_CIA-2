#!/usr/bin/env python
# coding: utf-8

# In[63]:


import numpy as np
import pandas as pd


# In[64]:


df= pd.read_csv(r'D:\ml cia 2\car_price.csv')


# In[65]:


df


# In[66]:


df.info()


# In[67]:


df.isna().sum()


# In[68]:


data= df.copy()


# In[69]:


data.drop(columns = ["CarName","aspiration","enginelocation"], inplace = True)
data.columns


# In[70]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['carbody'] = le.fit_transform(data['carbody'])
data['doornumber'] = le.fit_transform(data['doornumber'])
data['fueltype'] = le.fit_transform(data['fueltype'])
data['enginetype'] = le.fit_transform(data['enginetype'])
data['cylindernumber'] = le.fit_transform(data['cylindernumber'])
data['fuelsystem'] = le.fit_transform(data['fuelsystem'])
data['drivewheel'] = le.fit_transform(data['drivewheel'])
data['symboling'] = le.fit_transform(data['symboling'])


# In[71]:


data.corr()


# In[72]:


data


# In[73]:


data.to_csv("newdata.csv")


# In[74]:


data.info()


# In[75]:


x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values


# In[76]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,
                                                test_size=0.3, random_state=21)


# In[77]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


# In[78]:


from sklearn.linear_model import LinearRegression 
reg = LinearRegression()  
reg.fit(x_train,y_train)


# In[79]:


y_pred= reg.predict(x_test)  


# In[80]:


y_pred


# In[81]:


print('Train Score: ', reg.score(x_train, y_train))  
print('Test Score: ', reg.score(x_test, y_test))  


# In[56]:


##### print("Enter Car Details to Predict Price")
def predictor:
    a = int(input("Car Body: 0- Convertible,1- Hardtop, 2-Hatchback , 3- Sedan, 4- Wagon:"))
    b = int(input("DriveWheel: 0- 4WD, 1- FWD, 2- RWD:"))
    c = int(input("Fuel Type: 1-Gas,0- Diesel:"))
    d = int(input("Number of doors: 1- Twodoor, 0- Fourdoor:"))
    e = int(input("Number of cylinders: 0- Eight, 1-five, 2-Four, 3- six, 4-three, 5- twelve, 6-two: "))
    f = int(input("Engine Type: 0- DOHC, 1-DOHCV, 2- I, 3- OHC, 4-OHCF, 5- OHCV, 6-ROTOR: "))
    g = int(input("Fuel System: 0- 1BBL, 1-2BBL, 2- 4BBL, 3- IDI, 4-MFI, 5- MPFI, 6-SPDI, 7-SPFI: "))
    h = int(input("Symboling: 0- Negative Two, 1- Negative One, 2- Zero, 3- One, 4-Two, 5- Three: "))
    i = float(input("WheelBase(cm): "))
    j = float(input("CarLength(cm): "))
    k = float(input("CarWidth(cm): "))
    l = float(input("CarHeight(cm): "))
    m = float(input("CurbWeight(kg): "))
    n = float(input("EngineSize(cm^3): "))
    o = float(input("BoreRatio: "))
    p = float(input("Stroke: "))
    q = float(input("CompressionRatio: "))
    r = float(input("HorsePower(hp): "))
    s = float(input("PeakRPM: "))
    t = float(input("CityMPG: "))
    u = float(input("HighwayMPG: "))
    features = np.array([[a, b, c, d, e, f, g, h,i,j,k,l,m,n,o,p,q,r,s,t,u]])
    return("Predicted Car Price = ", reg.predict(features))

