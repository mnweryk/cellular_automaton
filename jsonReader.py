import json

class JsonReader:


    def read_data(self):
        with open('data.json', 'r') as read_file:
            config = json.loads(read_file.read())
            self.columns = config['columns']
            self.rows = config['rows']
            self.rule = config['rule']

    def set_data(self, col, row, rule):
        with open('data.json', 'w') as outfile:
            data = {
                "columns": int(col),
                "rows": int(row),
                "rule": int(rule)
            }
            json.dump(data, outfile)
