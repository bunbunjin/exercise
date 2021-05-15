class QuerParams:
    def __init__(self, params):
        self.params = params

    def __len__(self):
        return len(self.params)

    def __bool__(self):
        return bool(self.params)


query = QuerParams({})
a = bool(query)
query = QuerParams({'key': 'value'})
b = bool(query)
print(a, b)
