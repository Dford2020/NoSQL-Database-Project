#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_songs(title, year, artist, genre, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Songs')


if __name__ == '__main__':
    print('Deleting...')
   


# In[8]:



from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_underrated_movie(title, year, artist, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Songs')

    try:
        response = table.delete_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "Delete Failed":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response


if __name__ == '__main__':
    print("Attempting to delete...")
    delete_response = delete_songs("The Big New Move", 2015, 'artist', 'genre')
    if delete_response:
        print("Delete songs successsfully:")
        pprint(delete_response, sort_dicts=False)


# In[ ]:




