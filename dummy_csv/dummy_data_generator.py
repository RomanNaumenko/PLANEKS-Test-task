from __future__ import absolute_import, unicode_literals
import random

import csv
from faker import Faker
from dummy_csv.models import Scheme
import datetime


def csv_data_generator(records, columns, names, filename, scheme_id, req):
    scheme = Scheme.objects.get(id=scheme_id)
    scheme.upload = 'Progressing...'
    scheme.save()

    fake = Faker('uk_UA')  # adding nightingale locale

    with open(filename, 'w', encoding='UTF-8', ) as csvFile:  # rows writing process
        writer = csv.writer(csvFile)
        if names:
            writer.writerow(names)

        writer = csv.DictWriter(csvFile, fieldnames=columns)
        writer.writeheader()

        for i in range(records):

            email = fake.ascii_company_email()
            domain_name = email.split("@")
            domain_name = domain_name[1]
            gen_dict = {

                'Full name': fake.name(),
                'Job': fake.job(),
                'Email': email,
                'Domain Name': domain_name,
                'Phone': fake.phone_number(),
                'Company name': fake.company(),
                'Text': fake.text(),
                'Integer': random.randrange(0, 100),
                'Address': fake.address(),
                'Date': fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),

            }

            filtered_dict = {}
            for (k, v) in gen_dict.items():
                if k in columns:
                    filtered_dict[k] = v

            writer.writerow(filtered_dict)

        scheme.upload = filename
        scheme.save()

    return filename + ' have been generated!'
