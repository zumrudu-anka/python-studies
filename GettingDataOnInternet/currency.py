import requests

url="https://data.fixer.io/api/latest"

first=input("\nFirst Currency: ")
second=input("\nSecond Currency: ")
amount = float(input("\nAmount: "))

response = requests.get(url + first)

print(response)

json_data = response.json()

print(float(json_data["rates"][second])*amount)