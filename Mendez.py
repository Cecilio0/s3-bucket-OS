import json
import requests
import boto3
from datetime import datetime

s3 = boto3.client('s3', 
                  aws_access_key_id='',
                  aws_secret_access_key='')

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

bucket_name = "pablo-mesa-hernandez-santamaria-saldarriaga-gonzalez-y-daniel"

headers = {
	"accept": "application/json",
	"X-RapidAPI-Key": "3386e39aefmsha4ff8984bd8b65fp15a33fjsn66f3adf6742b",
	"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}

for i in range(5):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_name = "chuck"+str(i)
        json_obj = json.dumps(response.json())
        now = datetime.now()
        folder_name = now.strftime('%Y-%m-%d')
        
        s3.put_object(Bucket=bucket_name, Key=f"{folder_name}/{file_name}.txt", Body=json_obj)
        

