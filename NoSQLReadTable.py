#!/usr/bin/env python
# coding: utf-8

# In[8]:


from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_songs(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Songs')

    try:
        response = table.get_item(Key={'year': year, 'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    songs = get_songs("The Big New Move", 2015,)
    if songs:
        print("Retreived songs successfully:")
        pprint(songs, sort_dicts=False)


# In[ ]:




