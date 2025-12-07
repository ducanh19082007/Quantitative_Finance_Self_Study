"""
This is an documentation string for the API_calling_practice module.
where i will practice making API calls using Python.

1. basic GET request
2. handling JSON responses
3. error handling for API requests
4. using query parameters in API calls
5. API authentication methods
6. combining multiple API calls
7. rate limiting and retries
8. parsing complex JSON data
9. working with RESTful APIs
10. using third-party libraries for API calls like binance-python
11. API calling interative with Broker
12. API calling interactive with User 
"""

1. #basic GET request
import numpy as np
import pandas as pd
import json
import tabulate as tb
#pip install requests #alrdy installed in the setup file

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
        
        print(f"\n Response Headers: {headers}")
        print(f"\n JSON format Response: {data}")
    else:
        print(f"Error: Unable to fetch data from the API. Status code: {status_code}")
        
    #_________________________________________call API with parameters
    
    parameters = {"statusCode": 200}
    respose_filtered = requests.get(url, params=parameters)
    
    status_code = respose_filtered.status_code
    if status_code == 200:
        print("API request with parameters successful.")
        headers = response.headers
        filtered_data = respose_filtered.json()
        df = pd.DataFrame.from_dict(filtered_data, orient='index').T
        print(f"\n Filtered Response Headers: {headers}")
        print(f"\n Filtered JSON format Response: {df}")
    else:
        print(f"Error: Unable to fetch data from the API with parameters. Status code: {status_code}")

    
    
    
def main():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    df = basic_get_request_practice(url)
    
if __name__ == "__main__":
    main()