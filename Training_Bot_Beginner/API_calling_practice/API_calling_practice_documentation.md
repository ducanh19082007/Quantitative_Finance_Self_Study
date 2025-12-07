Here’s a clean, practical guide on **how to call an API**, followed by **10 practice test questions** so you can master it.

---

# ✅ **How to Call an API (Beginner-Friendly Guide)**

Below is the simplest, most common way people call APIs using **Python + the `requests` library**.

---

## **1. Install `requests`**

```bash
pip install requests
```

---

## **2. Make a Simple GET Request**

```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)

print(response.status_code)   # 200 means OK
print(response.json())        # API response in JSON format
```

---

## **3. Call an API With Parameters**

```python
params = {"query": "bitcoin", "limit": 10}
response = requests.get("https://api.example.com/search", params=params)

print(response.json())
```

---

## **4. Call an API With Headers (For Auth)**

Many APIs require API keys passed via headers.

```python
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get("https://api.example.com/me", headers=headers)

print(response.json())
```

---

## **5. Make a POST Request**

Useful for sending data, logins, etc.

```python
data = {
    "username": "anh",
    "password": "1234"
}

response = requests.post("https://api.example.com/login", json=data)

print(response.json())
```

---

## **6. Handle Errors**

```python
if response.status_code != 200:
    print("Error:", response.status_code, response.text)
```

---

# 🎯 **10 Practice Test Questions (API Calling)**

## **Practice Test 1 — Easy**

Write Python code to send a GET request to:

```
https://pokeapi.co/api/v2/pokemon/pikachu
```

Print the Pokémon’s **name** and **base experience**.

---

## **Practice Test 2 — Easy**

Call an API with parameters:

```
https://api.agify.io/?name=michael
```

Print the JSON result.

---

## **Practice Test 3 — Medium**

Call this API with a parameter:

```
https://catfact.ninja/fact?max_length=60
```

Extract only the `"fact"` string.

---

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

---

## **Practice Test 5 — Medium**

Call an API that returns a list:

```
https://jsonplaceholder.typicode.com/posts
```

Print the **title** of the first 5 posts.

---

## **Practice Test 6 — Medium**

Call:

```
https://api.coindesk.com/v1/bpi/currentprice.json
```

Print the **USD Bitcoin price**.

---

## **Practice Test 7 — Hard**

Call an API with headers:

URL:

```
https://httpbin.org/headers
```

Headers:

```
{"X-Test": "hello123"}
```

Print the value of `"X-Test"` returned in the response.

---

## **Practice Test 8 — Hard**

Write a function `get_weather(city)` that calls:

```
https://wttr.in/<city>?format=j1
```

Return the **current temperature**.

---

## **Practice Test 9 — Hard**

Call:

```
https://api.publicapis.org/entries
```

Count how many APIs have:

```
HTTPS = true
```

Print the count.

---

## **Practice Test 10 — Hard**

You are given an API that sometimes fails:

```
https://httpbin.org/status/500
```

Write Python code that:

* retries the request up to **3 times**
* waits **1 second** between tries
* prints “Failed after retries” if still 500

---

If you want, I can also:
✔ generate model solutions for all 10
✔ turn these into an assignment PDF
✔ create harder tests (OAuth, rate limits, async APIs)

Would you like the solutions?
