'''
import requests

url = 'http://localhost:5000/predict_api'
input = {'experience':2, 'test_score':9, 'interview_score':6}
r = requests.post(url, json=input)
print(r.status_code)

print(r.json())

'''


