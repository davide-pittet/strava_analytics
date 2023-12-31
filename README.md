# Analysis of running performance with Python

## Introduction
This project aims to analyze my running performance, comparing the 2022 and the 2023 seasons. All of my runs are recorded and publicly available on Strava, a popular fitness social network to share sporting activities. First, we retrieve the necessary data through the Strava APIs using Python's requests package in the strava_api.py script. 
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

The last one is just a package needed to suppress a harmless warning that comes up when we make API requests.

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
In the first part of this script we define a series of convenient functions that could be helpful in the future.

### authorization_refresh
Following what we mentioned earlier, we define a function that gets the refresh token obtained through the manual procedure saved in a json file and returns the updated access token to make all type of requests with a 'read_all' permission. 

### all_activities
This function takes in the access token and multiple optional parameters:

* before (default: empty string): get all activities before a given date 'dd/mm/yyyy'
* after (default: empty string): get all activities after a given date 'dd/mm/yyyy'
* page (default: 1): number of pages requested
* per_page (default: 30): number of activities per page requested (MAX 200)

It returns a json object with all activities that satisfy the requirements specified.

### activity_by_id
This function returns a json object with more specific details about a particular activity. It takes in the access token and the activity id, which we can find in the dictionary corresponding to that activity in the json object obtained with the previous function.

### route_by_id 
This function returns a json object with information about a particular route saved in Strava. It takes in the access token and the route id, which we can find within the URL of the activity on Strava.

## activities_analysis
After acquiring data from two different seasons, in this script, we clean the datasets and compare the performance of flat runs. Flat runs can be roughly divided into 5 zones depending on the average heart rate. As most of my runs occurred in zones 2 and 3, we consider those subsets. First, we plot zone 2 and zone 3 runs versus the average speed; then, we plot the number of runs in each zone for both seasons.
