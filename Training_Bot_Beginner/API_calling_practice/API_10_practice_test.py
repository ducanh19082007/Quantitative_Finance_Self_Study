import numpy as np
import pandas as pd
import json
from IPython.display import display

"""
## **Practice Test 1 — Easy**

Write Python code to send a GET request to:

```
https://pokeapi.co/api/v2/pokemon/pikachu
```

Print the Pokémon’s **name** and **base experience**.

---
    """
def practice_1():
    import requests
    
    print("practice 1")
    params = {"ability": "static", "limit": 10}
    requests = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu", params=params)
    status_code = requests.status_code
    
    if status_code == 200: 
        data = requests.json()
        df = pd.json_normalize(data)
        display(df.T)
        
        df_name = df["forms"].at[0][0]["name"]
        display("name: ", df_name)
        display("base_experience: ", df["base_experience"].at[0])
        print("\n\n")
        
        header_data = dict(requests.headers)
        df_header = pd.json_normalize(header_data).T
        display(df_header)
    else:
        print(f"Request failed with status code: {status_code}")
        
"""
## **Practice Test 2 — Easy**

Call an API with parameters:

```
https://api.agify.io/?name=michael
```

Print the JSON result.
    """
def practice_2():
    import requests
    
    print("practice 2")
    requests_ = requests.get("https://api.agify.io/?name=michael")
    
    status_code = requests_.status_code
    
    if status_code == 200:
        data = requests_.json()
        
        df_data = pd.json_normalize(data)
        display(df_data.T)
        
        header = dict(requests_.headers)
        df_header = pd.json_normalize(header).T
        display(df_header)
    else:
        print(f"Request failed with status code: {status_code}")

"""
## **Practice Test 3 — Medium**

Call this API with a parameter:

```
https://catfact.ninja/fact?max_length=60
```

Extract only the `"fact"` string.
    """
def practice_3():
    import requests
    
    print("practice 3")
    requests = requests.get("https://catfact.ninja/fact?max_length=60")
    
    status_code = requests.status_code
    
    if status_code == 200:
        print("API request successful.")
        
        data = requests.json()
        df_data = pd.json_normalize(data)["fact"][0]
        display("fact of the day?: ", df_data)
    else:
        print(f"Request failed with status code: {status_code}")
    
"""
## **Practice Test 4 — Medium**

Send a POST request to:

```
https://httpbin.org/post
```

Send JSON data:

```json
{"task": "api practice", "status": "start"}
```

Print the server's response.
"""
def practice_4():
    import requests
    
    print("practice 4")
    url = "https://httpbin.org/post"
    data_json_post = {
        "name": "John Doe",
        "email": "johndoe@gmail.com",
        "age": 30,
        "city": "New York"
    }
    response_post = requests.post(url, json=data_json_post)
    
    status_code = response_post.status_code
    
    if status_code == 200:
        print("POST API request successful.")
        
        data_post = response_post.json()
        df_data = pd.json_normalize(data_post)
        display(df_data.T)
        
        header_post = dict(response_post.headers)
        df_header = pd.json_normalize(header_post)
        display(df_header.T)
    else:
        print("failed API")

"""
## **Practice Test 5 — Medium**

Call an API that returns a list:

```
https://jsonplaceholder.typicode.com/posts
```

Print the **title** of the first 5 posts.
"""
def practice_5():
    import requests
    
    print("practice 5")
    requests_call = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = requests_call.status_code
    
    if status_code == 200:
        print("API called successfully")
        data = requests_call.json()
        header = dict(requests_call.headers)
        
        df_data = pd.json_normalize(data).iloc[0:5]["title"]
        df_header = pd.json_normalize(header)
        
        display(df_data)
        display(df_header)
        
        list_title = [title for title in df_data]
        print("title: ", list_title)

"""

## **Practice Test 8 — Hard**

Write a function `get_weather(city)` that calls:

```
https://wttr.in/<city>?format=j1
```

Return the **current temperature**.
 
"""
def practice_8():
    import requests
    
    print("practice 8")
    requests_call = requests.get("https://wttr.in/<city>?format=j1")

    
    status_code = requests_call.status_code
    print("status code is: ", status_code)
    
    if status_code == 200:
        header = dict(requests_call.headers)
        data = requests_call.json()
        
        df_header = pd.json_normalize(header).T 
        df_data = pd.json_normalize(data)["current_condition"][0] 
        
        print("data")
        print(df_data)
        print("header?")
        display(df_header.head())
    else:
        print("failed to get api")
    
"""
You are given an API that sometimes fails:

```
https://httpbin.org/status/500
```

Write Python code that:

* retries the request up to **3 times**
* waits **1 second** between tries
* prints “Failed after retries” if still 500
"""
def practice_10():
    import requests
    
    print("practice 10")
    status_code = None
    tries = 0
    
    try:
        while status_code != 200 and tries < 5:
            requests_call = requests.get("https://httpbin.org/status/500", timeout=2)
            
            status_code = requests_call.status_code
            
            print("status code: ", status_code)
            
            if status_code == 200:
                requests_header = dict(requests_call.headers)
                requests_data = requests_call.json()
                
                df_header = pd.json_normalize(requests_header)
                df_data = pd.json_normalize(requests_data).T
                
                display(df_data)
                display(df_header.head())
                
            tries += 1
            
        if status_code != 200:
            print(f"Failed after {tries} tries.")
            
    except requests.exceptions.RequestException as e:
        print(f"failed {e}")



def main():
    practice_1()
    practice_2()
    practice_3()
    practice_4()
    practice_5()
    practice_8()
    practice_10()
    
if __name__ == "__main__":
    main()