import json

class JsonReader:

    def __init__(self):
        with open('data.json', 'r') as read_file:
            config = json.loads(read_file.read())
            self.columns = config['columns']
            self.rows = config['rows']
            self.rule = config['rule']
