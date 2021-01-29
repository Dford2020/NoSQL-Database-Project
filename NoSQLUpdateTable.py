#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pprint import pprint
import boto3


def put_songs(title, year, artist, genre, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Songs')
    response = table.put_item(
       Item={
            'year': year,
            'title': title,
            'info': {
                'artist': artist,
                'genre': genre
            }
        }
    )
    return response


if __name__ == '__main__':
    songs_resp = put_songs("The Big New Move", 2015,
                           "Python.", 'Jazz')
    print("Update succeeded:")
    pprint(songs_resp, sort_dicts=False)



# In[ ]:





# In[ ]:




