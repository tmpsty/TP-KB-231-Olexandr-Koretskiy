import requests

rates = {item["cc"]: item["rate"] for item in requests.get(
    "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
).json() if item["cc"] in ["USD", "EUR", "PLN"]}

while True:
    currency = input("Введіть валюту (EUR, USD, PLN) або 'exit': ").upper()
    if currency == "EXIT":
        break
    if currency not in rates:
        print("Невірний код валюти.")
        continue
    try:
        amount = float(input("Введіть суму: "))
        print(f"{amount} {currency} = {amount * rates[currency]:.2f} UAH")
    except ValueError:
        print("Некоректна сума.")