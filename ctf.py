import requests

# Define the URL of the web application where the flag is located
flag_url = "http://challenge.ctf.games:30072/flag.txt"  # Replace XXXXX with the actual port

# Send an HTTP GET request to the flag URL
response = requests.get(flag_url)

if response.status_code == 200:
    flag_content = response.text
    print(f"Flag content: {flag_content}")
else:
    print("Failed to fetch the flag.")
