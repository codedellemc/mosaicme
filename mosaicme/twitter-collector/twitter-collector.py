from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import logging
import logging.config
import dotenv
import os
import sys

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger('twitterCollector')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
dotenv.read_dotenv(os.path.join(BASE_DIR, '..', '.env'))

try:
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
except KeyError, e:
    logger.error('Could not obtain environment variable: %s', str(e))
    sys.exit(1)


class MosaicmeListener(StreamListener):
    """
    This listener handles tweets that contain the #EMCWORLD hashtag and
    gets the pictures
    """
    def on_data(self, str_data):
        # print(str_data)

        try:
            data = json.loads(str_data)
        except ValueError, e:
            logger.warning('Could not parse JSON data. %s', str(e))
            return True

        if 'extended_entities' not in data:
            logger.info('No extended entities found')
            return True
        if 'media' not in data['extended_entities']:
            logger.info('No media found')
        if not data['extended_entities']['media']:
            logger.info('No media found')
        for media in data['extended_entities']['media']:
            if media['type'] != 'photo':
                pass
            media_url = media['media_url']
            media_id = media['id_str']
            logger.info('Media found. ID: %s - URL: %s', media_id, media_url)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = MosaicmeListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#felizmiercoles'])