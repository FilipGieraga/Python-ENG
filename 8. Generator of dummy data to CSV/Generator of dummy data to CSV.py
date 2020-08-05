import csv
import random
from faker import Faker

faker = Faker()


def generate_CSV(n):
    x = set(random.sample(range(10000, 100000), k=1000))
    with open("Fake data.csv", "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['id', 'full name', 'date of birth', 'address', 'job position', 'phone number', 'email'])
        for id in range(n):
            name = faker.name()
            address = faker.address()
            address = address.replace('\n', ' ')
            job = faker.job()
            phone = faker.phone_number()
            email = faker.email()
            date_of_birth = faker.date_of_birth()
            id = x.pop()
            csv_writer.writerow([id, name, date_of_birth, address, job, phone, email])


generate_CSV(50)
