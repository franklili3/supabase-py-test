import os
import numpy as np
import math
import pandas as pd
import datetime, time
import requests
import logging
import json
import os
from supabase import create_client, Client
from postgrest import APIError
import uuid

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
row_dict = {"id": str(uuid.uuid4())}
route = '/rest/v1/test3'
# 将字典转换为 JSON 字符串
row_json = json.dumps(row_dict)
#row_json = json.loads(row_dict)

print('row_json: ', row_json)
'''
supabase_user_email = os.environ.get('supabase_user_email')
supabase_user_password = os.environ.get('supabase_user_password')

response4 = supabase.auth.sign_in_with_password(
    {"email": supabase_user_email, "password": supabase_user_password}
)
response4_json = json.loads(response4.model_dump_json())
if response4_json['user']['aud'] == 'authenticated':
    print('Authenticated user:', response4_json['user']['email'])  # Debugging line added               
'''
    
# Update data by supabase
def update_by_supabase(row_json):
    try:
        response3 = (
            supabase.table("test3")#bitcoin_trade_signal
            .update(row_json)
            .eq('accumulated_blocks', 879690)
            .execute()
        )
    except APIError as e:
        print(f"ERROR: {e}")
    response3_json = json.loads(response3.model_dump_json())
    print('response3_json:', response3_json)
    if len(response3_json['data']) > 0:
        print('update data success.')
    else:
        raise Exception(f"Failed to update data: {response3}")

    
# Post data by requests 
post_url = url + route
#access_token = response4_json['session']['access_token']
headers ={
        "apikey": key,
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json"
    }
def insert_by_requests(row_json):
    try:
        response3 = requests.post(post_url, headers=headers, data=row_json)
        if response3.status_code == 201:
            #logger.info('post data success.')
            print('post data success.')
        else:
            raise Exception(f"{response3.text}")
    except Exception as e:
        print(f"Failed to post data: {e}")

def update_by_requests(row_json):
    params =  {'accumulated_blocks': 'eq.879690' }
    print('params: ', params)

    try:
        response3 = requests.patch(post_url, data=row_json, params=params, headers=headers)
        if response3.status_code == 204:
            #logger.info('post data success.')
            print(f'post data success.{response3.text}')
        else:
            raise Exception(f"{response3.text}")
    except Exception as e:
        print(f"Failed to post data: {e}")
        raise                                
update_by_requests(row_json)
    
#update_by_supabase(row_json)
