import json, requests

def uRLScan(uRL:str):
    prefix = "Submission failed - "
    headers = {'API-Key':'019711e1-3c21-754c-9f46-28d37ef18f80','Content-Type':'application/json'}
    data = {"url": uRL, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    response = response.json()
    
    print(response)
    if response.get('message') == 'Submission successful': 
        status = response['result']
        return (f"Submission successful - <a href='{status}'>Click me for a report</a>")
    if response.get('message') == 'Scan prevented ...': return str(prefix+response["errors"][0]["detail"])
    if response.get('message') == 'DNS Error - Could not resolve domain': return str(prefix+response['detail'])
    return str(response.get('message'))

