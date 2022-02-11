import json


class StudentEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
