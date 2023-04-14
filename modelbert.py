import requests 
import json

API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
headers = {"Authorization": "Bearer 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"}

def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        response_str = response.text
        response_list = json.loads(response_str)
        organizations = [entity['word'] for entity in response_list if entity['entity_group'] == 'ORG']
        print(organizations)

	


input = " Brokerages neutral on Tech M, negative on Infy, but investors cheer Mohit Joshi’s move"

output = query({
	"inputs": input
})