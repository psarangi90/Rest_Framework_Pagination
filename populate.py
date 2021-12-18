import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","CursorPaginationProject.settings")
import django
django.setup()
import faker
import random
import string
from CursorPaginationPApp.models import Employee
fake=faker.Faker("en_IN")
import time
def populate(n):
    for _ in range(n):
        feno=random.randint(111,999)
        fename=fake.name()
        fesal=random.uniform(11111.00, 99999.99)
        feaddr=fake.address()
        # fcreated=str(fake.datetime())
        # print(type(fcreated))
        Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
        time.sleep(2)

populate(10)