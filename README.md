# Analysis of running performance with Python

## Introduction
This project aims to analyze my running performance, comparing the 2022 and the 2023 season. All of my runs are recorded and publicly available on Strava, a popular fitness social network to share sporting activities. First, we retrieve the necessary data through the Strava APIs using Python's requests package in the strava_api.py script. 
Then, we clean and analyze our data with the help of different Python packages such as Pandas and Seaborn in the activities_analysis.py script.

## Technologies
Here, we report a list of all Python packages that we used in this project:
* requests
* json
* datetime
* pandas
* seaborn
* matplotlib.pyploy
* urllib3

## Strava APIs
We retrieve our dataset from Strava using their free APIs. If you want to access your Strava data through APIs, there is a one-time manual procedure to do before diving into the code. 

### Manual procedure
The manual procedure is described in detail at   

https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86  

in the first three sections. However, I have modified a bit the last step to ensure that the access to the activities is automatic. To summarize briefly, you first have to register an app on the Strava website: this will give you access to information such as your client id, client secret and access token. Note, however, that the access token that you get in this
way will only give you 'read' permissions, but to get what we want we need an access token for 'read_all' types of content and that is why we need to do this manual procedure. Substitute your client id into the following link  

https://www.strava.com/oauth/authorize?client_id=your_client_id&redirect_uri=http://localhost&response_type=code&scope=activity:read_all  

and authorize. After that, you will get an error message from your browser. However, we just need a code that will be displayed in the URL of this error page, which will look like  

http://localhost/?state=&code=somecode&scope=read,activity:read_all  

Now, we have to use this code to make a request to the APIs that will give us a json file that contains, among other things, an access token and a refresh token. The point is that the access token, which is the code that will allow us to retrieve all activities,
is temporary, but we will use the refresh token to get a new access token every time the old one expires.

## strava_api

Description in progress
