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
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
row_dict = {"accumulated_blocks":879692}
route = '/rest/v1/test3'
# 将字典转换为 JSON 字符串
row_json = json.dumps(row_dict)
#row_json = json.loads(row_dict)

print('row_json: ', row_json)
supabase_user_email = os.environ.get('supabase_user_email')
supabase_user_password = os.environ.get('supabase_user_password')

response4 = supabase.auth.sign_in_with_password(
    {"email": supabase_user_email, "password": supabase_user_password}
)
response4_json = json.loads(response4.model_dump_json())
if response4_json['user']['aud'] == 'authenticated':
    #print('Authenticated user:', response4_json['user'])  # Debugging line added               
    # Post data by supabase
    response3 = (
        supabase.table("test3")#bitcoin_trade_signal
        .insert(row_json)
        .execute()
    )
    '''
    # Post data by requests 
    post_url = url + route
    headers ={
            "apikey": key,
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json"
        }
    response3 = requests.post(post_url, headers=headers, data=row_json)
    '''
    response3_json = json.loads(response3.model_dump_json())
    print('response3_json:', response3_json)
    if len(response3_json['data']) > 0:
        print('post data success.')
    else:
        raise Exception(f"Failed to post data: {response3_json}")
    
