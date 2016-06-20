import json
import requests


class Building:
    def __init__(self, id, name, address, location, images=[], directional_check=False):
        self.id = id
        self.name = name
        self.address = address
        self.location = location
        self.images = images
        self.directional_check = directional_check

    def __str__(self):
        return '<Building id=%s>' % self.id

    def __repr__(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def get_by_position(lon, lat):
        response = []
        headers = []
        try:
            request = requests.get("localhost", params=headers)
            if request.status_code == requests.codes.ok:
                api_response = json.loads(request.text)
                if len(api_response['value']) > 0:
                    for obj in api_response['value']:
                        response.append(obj)

            if request.status_code == 200:
                api_response = json.loads(request.text)
                raise Exception("Exception")

            if request.status_code == 403 or \
                            request.status_code == 400:
                raise Exception("Connection error")

        except requests.exceptions.ConnectionError:
            raise Exception("Connection error")
        return response
