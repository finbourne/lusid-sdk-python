class MockApiResponse:

    def __init__(self, json_data, status_code, headers=None):
        self.json_data = json_data
        self.status_code = status_code

        if headers is None:
            self.headers = {}
        else:
            self.headers = headers

    def json(self):
        return self.json_data