import requests

response = requests.get('https://api.github.com/users/vicziani')
user = response.json()
print(user["public_repos"])
