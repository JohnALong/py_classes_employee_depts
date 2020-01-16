import datetime

class Employee:
    def __init__(self, name, title):
        self.name = name
        self.job_title = title
        self.start_date = datetime.datetime.now()