# Python_for_data_analysis : Seoul Bike demand Predictor

For this project, we studied and exploited data from a bike renting company based in Seoul. The dataset which was given to us to analyse gathered data regarding the date (and info on said date such as the season, wheter it is a holiday...),the meteorological conditions, as well as the number of bikes rented on said date. 

Here is the link to the dataset : https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand

We placed ourselves in the position of people from the bike renting company, wanting to understand the factors playing in the demand, to be able to anticipate it. Therefore our goal was to look at all the conditions reunited (all the predicators) and study their impact on the the number of rented bikes. 

## Importing and exploring our data

### Attribute Information

Date : year-month-day

Rented Bike count - Count of bikes rented at each hour

Hour - Hour of he day

Temperature-Temperature in Celsius

Humidity - %

Windspeed - m/s

Visibility - 10m

Dew point temperature - Celsius

Solar radiation - MJ/m2

Rainfall - mm

Snowfall - cm

Seasons - Winter, Spring, Summer, Autumn

Holiday - Holiday/No holiday

Functional Day - NoFunc(Non Functional Hours), Fun(Functional hours)


### What we noticed
Upon importing the data, we were able to notice important aspect of the dataset :
- No NAs we present, saving us some time in cleaning up the dataframe
- The columns were improperly names (spaces, accents...), so we had to rename them

We were able to look at the type and repartition of values for all columns:
- Most of our variables were numerical and continuous, including our target (number of bikes)
- We also had categorical values included in the temporal variables
- The date variable was the only variable of type datetime, which tends to be impractical for visualizing and modeling
- There were some discreptencies in the season labels, which we corrected using the dates given to us

## What we observed

Below are the plots we were able to trace and what we could gather from them.
### Global view of the data
![image](https://user-images.githubusercontent.com/116392151/205530591-8917ba99-9040-4ca9-ba73-9a0b0c8009bf.png)

### Rented bikes over time
![image](https://user-images.githubusercontent.com/116392151/205530755-4d8c4256-9c9c-4f17-bcfe-74fe7331881a.png)

### Rented depending on the year and month
![image](https://user-images.githubusercontent.com/116392151/205530814-004fd83d-36e2-4f5f-a375-a7c68c55fdb7.png)

### Rented bikes depending on the month and day
![image](https://user-images.githubusercontent.com/116392151/205530925-26a49495-95be-4f11-ab27-9a6d969ea7c3.png)

### Rented bikes depending on the 
![image](https://user-images.githubusercontent.com/116392151/205531121-e54d168e-f59a-4207-8d7a-fd1f8b80c51c.png)

### Rented bikes depending on the year, month and season
![image](https://user-images.githubusercontent.com/116392151/205531163-953e758e-45b8-4305-8db4-45609e1b5202.png)
![image](https://user-images.githubusercontent.com/116392151/205531182-15271ba5-da7f-478b-950a-f5d607d8da07.png)

### Rented bikes depending on the season
![image](https://user-images.githubusercontent.com/116392151/205531240-8c50bec6-df21-4b4a-9009-5c358ea73f65.png)

### Rented bikes depending on the season, rainfall and snowfall
![image](https://user-images.githubusercontent.com/116392151/205531320-e6bcead1-1a8f-4c65-9ab1-5bca7fae16f4.png)

### Rented bikes depending on the hour, rainfall and snowfall
![image](https://user-images.githubusercontent.com/116392151/205531351-4d9434a7-c161-4281-a526-e397477eef55.png)

### Rented bikes depending on the holidays, functioning days and hour
![image](https://user-images.githubusercontent.com/116392151/205531465-c50bace5-1d5d-4307-aaa3-813ed10d609e.png)

### Rented bikes depending on the moment of the day and the season
![image](https://user-images.githubusercontent.com/116392151/205531628-daae5fca-f973-4bc8-9676-305fe1947675.png)

### Rented bikes depending on meteorological conditions
#### Temperature and seasons
![image](https://user-images.githubusercontent.com/116392151/205531835-04579b1b-c939-4678-8f67-dc1abec2f2e6.png)

#### Humidity and temperature
![image](https://user-images.githubusercontent.com/116392151/205531890-9f34f8af-2153-4bf9-b8b7-38fe6df8f9b1.png)

#### Wind Speed
![image](https://user-images.githubusercontent.com/116392151/205531949-d1bc9ea9-710d-4e5a-9d5f-9fc45c818d3e.png)

#### Visibility
![image](https://user-images.githubusercontent.com/116392151/205531999-5e98bbeb-a09c-49cf-9603-18f5ca8f145b.png)

#### Dew point temperature
![image](https://user-images.githubusercontent.com/116392151/205532045-72bcb4ca-f0df-47db-a0f3-c2a9f6c0eae0.png)

#### Solar radiation
![image](https://user-images.githubusercontent.com/116392151/205532110-8b8ca241-b1f6-4d97-984b-46133761e644.png)

#### Temperature, humidity and wind speed
![image](https://user-images.githubusercontent.com/116392151/205532144-5564cafc-74a2-445b-b346-0302aae5fc3c.png)


## What we changed
Upon exploring and visualizing our data, we made some choices in order to facilitate our work.

### What we added

We ended up adding the following columns :
- day, integer from 1 to 31
- month, integer from 1 to 12
- year, integer between 2017 and 2018
- bike_affluence, categorical varaible among ("very few","few", "some", "many") (to allow us to use classification models to predict the demand, instead of just regression models)

### What we removed
Upon manipulating our data, we discovered that :
- the functioning_day variables, which was not originally explained in the description of the dataset, was actually telling us on which days the company did not rent bikes (days when no bikes were ever rented). Since we were focusing on causes for the demand of bikes that were external to the company, whe dropped the column to focus on the other predicators.

- the date column would be difficult to manipulate, and we already had created new time variables (see added variables above), so we dropped it as well

- almost no data was recorded in the year 2017, and the great majority of our rows were from 2018. This does not mean that no bikes were rented then. By the looks of it, we most likely had little to no data recorded before november of 2017. Furthermore we only had two years to use. We figured that the year variable would disrupt, rather than help, our study and models, and since most of the data was from 2018, the loss of information would be minimal. We therefore dropped the year column as well.

## Preprocessing the data

In preprocessing, we focused on two main tasks :
- to une label encoder and label binarizer to change our categorical predicators into numerical values
- to normalize (minmaxscaler) our numerical values to help improve the accuracy of classification models

## Models

### Regression Models

We started by splitting our data into a training and testing set, with the continuous variable number of rented bikes as target. The training set was composed of 90% of the dataset, and the testing set of 10%.

In order to define which regression models to use for out data, we used the lazypredict package on our training set to give us a first evaluation of all models available (using only the default parameters).
Although we were unable to fully run the selection, we were left with the results for 31 out of 42 of the models evaluated. We chose the ones which had the lowest RMSE, as they would be the most accurate.
This left us with the following models :
- Gradient Boosting Regressor
- Hist Gradient Boosting Regressor
- Bagging Regressor
- Random Forest Regressor
- Extra Trees Regressor

We then used GridSearchCV to find the best hyperparameters, which gave us :
- Gradient Boosting Regressor {'learning_rate': 0.3, 'loss': 'huber', 'n_estimators': 108}
- Hist Gradient Boosting Regressor {'learning_rate': 0.2, 'loss': 'poisson', 'max_iter': 109}
- Bagging Regressor {'max_samples': 1.0, 'n_estimators': 17}
- Random Forest Regressor
- Extra Trees Regressor

We then evaluated the score of each optimized model (comparing predicted values to observed values), and came to the conclusion that the models were, from best to worst :
- Hist Gradient Boosting Regressor (~0.89)
- Extra Trees Regressor (~0.88)
- Random Forest Regressor (~0.87)
- Bagging Regressor (~0.86)
- Gradient Boosting Regressor (~0.85)

### Classification Models

We started by splitting our data into a training and testing set, with the categorical variable bike affluence as target. The training set was composed of 90% of the dataset, and the testing set of 10%.

We again used the lazypredict package on our training set to give us a first evaluation of all models available .
We were this time able to fully run the selection, and we were left with the following models, which had the best evaluated accuracy.
From most to least accurate :
- LGBM Classifier
- Random Forest Classifier
- Extra Trees Classifier

We then used GridSearchCV to find the best hyperparameters, which gave us :
- LGBM Classifier {boosting_type='gbdt', max_depth= -1, num_leaves= 37}
- Random Forest Classifier {criterion='gini', n_estimators=106}
- Extra Trees Classifier {criterion='entropy', n_estimators= 130}

We then evaluated the accuracy of each optimized model :
- LGBM Classifier (~0.80)
- Random Forest Classifier (~0.80)
- Extra Trees Classifier (~0.78)

## API

We then created an API with Flask, allowing a user to find out how many bikes would be rented in a day based on:
- the hour 	
- the temperature 	
- the humidity 	
- the wind speed 	
- the visibility 	
- the dew point temperature 	
- the solar radiation 	
- the rainfall 	
- the snowfall 	
- the seasons 	
- the holiday 	
- the day 	
- the month

The API uses our most accurate model, which is the Hist Gradient Boosting Regressor.
It presents as follows :
![image](https://user-images.githubusercontent.com/116392151/205535689-d62ed582-cdc5-4a9d-836c-aeca7d52e627.png)

The aim is to allow professionnals to anticipate the demand for bikes based on time and on the predicted meteorological conditions.
