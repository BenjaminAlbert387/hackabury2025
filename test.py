import json, requests

def uRLScan(uRL:str):
    headers = {'API-Key':'019711e1-3c21-754c-9f46-28d37ef18f80','Content-Type':'application/json'}
    data = {"url": uRL, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    response = response.json()
    
    return response

print("Hello, Hacakabury!")

print(uRLScan("Hi"))
print(uRLScan("https://google.com"))
print(uRLScan("https://www.google.com"))
print(uRLScan("www.google.com"))
print(uRLScan("www.goodfewqfwef23f3erfgle.com"))

url = "https://google.com"
print(f"Submission successful - <a href='{url}'>Click me for a report</a>")