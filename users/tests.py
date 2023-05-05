from faker import Faker
import requests
fake = Faker()

url = "http://127.0.0.1:8000/api/auth/custom_user/"

i = 0
while i < 100:
    name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    password = email.split('@')[0]
    print(password)
    data = {
        'username': name.replace(' ', '_').lower(),
        'phone_number': phone_number,
        'password': password
    }
    r = requests.post(url, data)
    if r.status_code == 201:
        i += 1
        print(r.json())
        print(f"Create user:\n Name: {name}\nPhone Number: {phone_number}\n")

