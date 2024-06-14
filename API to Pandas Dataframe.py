#!/usr/bin/env python
# coding: utf-8

# # API to Pandas Dataframe
# ###  NASA public APIs portal.

# we are going to practice consuming public APIs through the NASA public APIs portal.
# 
# Portal description : The objective of this portal is to make NASA data, including imagery, eminently accessible to application developers and data professionals. Before starting to use its APIs endpoints, it's mandatory that you generate your API KEY and store it somewhere for later use. The API key acts as the user identifier when requesting the API. To get your KEY, fill in the provided form with your personal information, and then we shall receive an email containing your personal API KEY.
# 
# ➡️ NASA API PORTAL

# #### Follow These Steps
# Go to the NASA API portal and generate your API KEY
# 
# Import the requests package and store your API KEY in variable
# 
# Go back to portal website and click on 'browse APIs'
# 
# Click on the first dropdown menu, named 'APOD' and read its documentation
# Follow the provided documentation to ask the API endpoint for the astronomy picture of the day.
# 
# Get then display the image on your notebook.
# 
# Go through the list of the provided API endpoints once again and select 'Astronomy Picture of the Day' option. Store the results in a pandas dataframe
# 
# Do the necessary data pre-processing tasks on the previous result in order to get a clean dataframe with the following columns :
# 
# Asteroid ID
# 
# Asteroid name
# 
# The Minimal estimated diameter in Kilometre
# 
# Absolute_magnitude
# 
# Relative_velocity(km/s)
# 
# Try to export the new dataframe into a CSV file and share it with your colleagues

# In[100]:


import pandas as pd 
import requests
import json
from IPython.display import Image


# In[101]:


# API key
api_key='FQ7RiAdslFxqcwmnY0axL608hYCUzZTOpoA6jDcg'
api_url = 'https://api.nasa.gov/planetary/apod'
date='2024-06-13'

params={
    'date':date,
    'hd' :'True',
    'api_key':api_key
}
response = requests.get(api_url,params=params)
json_data=json.loads(response.text)
# Extract the image URL from the response
image_url = json_data['hdurl']

# Display the image
Image(url=image_url)


# In[102]:


api_url='https://api.nasa.gov/neo/rest/v1/feed'

params={
    'start_date':date,
    'end_date' :date,
    'api_key':api_key
}


# In[103]:


# Load 
response = requests.get(api_url, params=params)
data= response.json()
data=list(data['near_earth_objects'].values())
data= sum(data, [])


# In[104]:


asteroid_ids = []
asteroid_names = []
diameters = []
absolute_magnitudes = []
relative_velocities = []

for item in data:
   asteroid_ids.append(item['id'])
   asteroid_names.append(item['name'])
   diameters.append(item['estimated_diameter']['kilometers']['estimated_diameter_min'])
   absolute_magnitudes.append(item['absolute_magnitude_h'])
   relative_velocities.append(item['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])


# In[105]:


asteroid_df = pd.DataFrame({
        'asteroid_id': asteroid_ids,
        'asteroid_name': asteroid_names,
        'minimal_Kilometre': diameters,
        'absolute_magnitude': absolute_magnitudes,
        'relative_velocity_km/s': relative_velocities
    })
asteroid_df

