#this module will visualize the data better

import numpy as np
import pandas as pd
import json
from IPython.display import display

"""  
This module contains functions to practice making API calls (GET and POST) and visualizing the responses using pandas DataFrames.
meaning of request get:
- GET: Retrieve data from a specified resource.
- POST: Submit data to be processed to a specified resource. in which the data will theoretically create a new resource, a part of the specified URL.
"""
def basic_get_request_practice(url:str):
    """
    This function makes a basic GET request to the provided URL and returns the response as a pandas DataFrame.
    """
    import requests

    #headers = {"accept": "application/json"}

    response = requests.get(url)
    
    status_code = response.status_code #200 means successful
    print(f"\n Status Code: {status_code}")
    
    if status_code == 200:
        print("API request successful.")
        headers = response.headers #dictionary format
        data = response.json() #dictionary format
        
        df_header = pd.DataFrame.from_dict(headers, orient='index')
        display(df_header)
        df_data = pd.DataFrame.from_dict(data, orient='index').T
        df_data = df_data["data"].apply(pd.Series).T  # Expand the 'data' column into separate columns
        display(df_data)
        print("\n\n")
    else:
        print(f"Error: Unable to fetch data from the API. Status code: {status_code}")
        
    #_________________________________________call API with parameters
    
    parameters = {"statusCode": 200, "limit": 2, "market": "US"} #example parameters, which will filter the API response
    respose_filtered = requests.get(url, params=parameters)
    
    status_code = respose_filtered.status_code
    if status_code == 200:
        print("API request with parameters successful.")
        headers = response.headers
        filtered_data = respose_filtered.json()
        df = pd.DataFrame.from_dict(filtered_data, orient='index').T
        df_header = pd.DataFrame.from_dict(headers, orient='index')
        display(df_header)
        df = df["data"].apply(pd.Series).T  # Expand the 'data' column into separate columns
        display(df)
    else:
        print(f"Error: Unable to fetch data from the API with parameters. Status code: {status_code}")
        
def POST_API_request_practice(url:str, payload:dict): #for post, status should be 201
    """
    this function makes a basic POST request to the provided URL with the given payload and returns the response as a pandas DataFrame.
    """
    import requests
    
    response_post = requests.post(url, json=payload)
    status_code = response_post.status_code
    print(f"\n Status Code: {status_code}")
    
    if status_code == 201:  #201 means resource created successfully
        print("POST API request successful.")
        headers = response_post.headers
        data_post = response_post.json()
        
        df_header = pd.DataFrame.from_dict(headers, orient='index')
        display(df_header)
        df_data = pd.DataFrame.from_dict(data_post, orient='index').T
        display(df_data)
        
        print("\n\n")
    else:
        print(f"Error: Unable to post data to the API. Status code: {status_code}")
    
def main():
    #first practice execution (GET request)
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    df = basic_get_request_practice(url)
    print(df)
    
    #second practice execution (POST request)
    url_post = "https://jsonplaceholder.typicode.com/posts" #example URL for testing POST requests
    data_json_post = {
        "name": "John Doe",
        "email": "johndoe@gmail.com",
        "age": 30,
        "city": "New York"
    }
    df_post = POST_API_request_practice(url_post, data_json_post)
    print(df_post)
    
if __name__ == "__main__":
    main()