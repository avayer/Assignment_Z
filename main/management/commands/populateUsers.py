# main/management/commands/populateUsers.py

import datetime
import random


from django.core.management.base import BaseCommand

from main.models import User

class Command(BaseCommand):
    help = "Save randomly generated user record values."

    def add_arguments(self, parser):
    # Positional arguments
        parser.add_argument(
            'number_of_stock_records',
            type=int,
            help="Number of stock records to generate and save to database"
        )
    
    def get_start(self):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2014, 2017)
        return datetime.date(year, month, day)

    def handle(self, *args, **options):
        id = 0;
        records = []
        size = options["number_of_stock_records"]
        for i in range(size):
            kwargs = {
                'id' : id,
                'name' : "user" + str(i),
                'tz' : "place" + str(i)
                # 'activity_peroid' :{
                #     'start': datetime.datetime.now(),
                #     'end': datetime.datetime.now() + datetime.timedelta(hours = 2)
                # }
            }
            record = User(**kwargs)
            records.append(record)
            id = id + 1
        User.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('Users records saved successfully.'))