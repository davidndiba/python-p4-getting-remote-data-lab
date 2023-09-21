import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response = requests.get(self.url)
        return json.loads(response.text)

def test_get_response():
    '''get_response_body function returns response.'''
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(URL)
    response_body = requester.get_response_body()
    
   
    expected_response = '[{"name": "Daniel", "occupation": "LG Fridge Salesman"}, {"name": "Joe", "occupation": "WiFi Fixer"}, {"name": "Avi", "occupation": "DJ"}, {"name": "Howard", "occupation": "Mountain Legend"}]'
    
    assert response_body.strip() == expected_response.strip()

def test_load_json():
    '''load_json function returns response.'''
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(URL)
    json_data = requester.load_json()
    expected_data = [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'}, {'name': 'Joe', 'occupation': 'WiFi Fixer'}, {'name': 'Avi', 'occupation': 'DJ'}, {'name': 'Howard', 'occupation': 'Mountain Legend'}]
    assert json_data == expected_data
