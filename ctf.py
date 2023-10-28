import requests

# Define the URL of the web application where the flag is located
flag_url = "http://challenge.ctf.games:30072/flag.txt"  # Replace XXXXX with the actual port

# Define the local file path to save the flag
local_flag_path = "flag.txt"

# Send an HTTP GET request to the flag URL
response = requests.get(flag_url)

if response.status_code == 200:
    flag_content = response.text
    print(f"Flag content: {flag_content}")

    # Save the flag content to a local file
    with open(local_flag_path, "w") as flag_file:
        flag_file.write(flag_content)
    print(f"Flag saved to {local_flag_path}")

else:
    print("Failed to fetch the flag.")
