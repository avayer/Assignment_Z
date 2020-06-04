# main/management/commands/populateUsers.py

import datetime
import random

    
from django.core.management.base import BaseCommand

from django_populate import Faker

from main.models import User
from main.models import Activity_peroid

class Command(BaseCommand):
    help = "Save randomly generated user record values."

    # def add_arguments(self, parser):
    # # Positional arguments
    #     parser.add_argument(
    #         'number_of_user_records',
    #         type=int,
    #         help="Number of user records to generate and save to database"
    #     )


    # stdout.write(style.SUCCESS('Users records and activity Periods saved successfully.'))

    # def get_start(self):
    #     day = random.randint(1, 28)
    #     month = random.randint(1, 12)
    #     year = random.randint(2014, 2017)
    #     return datetime.date(year, month, day)

    def handle(self, *args, **options):
            
            populator = Faker.getPopulator()
            populator.addEntity(User,5)
            populator.addEntity(Activity_peroid,10)
            insertedPks = populator.execute()
            populator.execute()
            self.stdout.write(self.style.SUCCESS('Users records saved successfully.'))
    
    #     size = options["number_of_user_records"]
    #     UserRecord = []
    #     activityRecord = []
    #     for _ in range(size):
    #         kwargs = {
    #             'id' : id,
    #             'name' : "user" + str(i),
    #             'tz' : "place" + str(i),
    #             'activity_peroid' :{
    #                 'start': datetime.datetime.now(),
    #                 'end': datetime.datetime.now() + datetime.timedelta(hours = 2)
    #             }
    #         }
    #         record = User(**kwargs)
    #         records.append(record)
    #         id = id + 1
    #     User.objects.bulk_create(records)
