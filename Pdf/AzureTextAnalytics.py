#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:04:54 2018

@author: Cris
"""

import requests
from pprint import pprint


def azure_api(list, s):
    # subscription_key = '93ea34d48fea4da5ac110ffac986511c'
    # subscription_key='dc0b1fdf3a8444d1a6ac88dec991f0dc'
    # subscription_key='ed995c619293478e940a381fa433c288'
    # subscription_key='30b407a2f6d04d75bb45b904e34d1665'
    # subscription_key='2fb39bbf894d442eb191b12ffdf81dcf'
    # subscription_key = '5f63ea25eda84c49989bc42b5b4f52eb'
    subscription_key = '7d762f59c9964fda93097b43b170ef9c'
    assert subscription_key

    text_analytics_base_url = "https://southeastasia.api.cognitive.microsoft.com/text/analytics/v2.0/"
    language_api_url = text_analytics_base_url + "languages"
    sentiment_api_url = text_analytics_base_url + "sentiment"
    key_phrase_api_url = text_analytics_base_url + "keyPhrases"
    entity_linking_api_url = text_analytics_base_url + "entities"

    # dynamic query for unpredictable documentation size
    temp_list = [{'id': 1, 'text': list[0]}]
    iter = 2
    while iter <= len(list):
        temp_dict = {'id': iter, 'text': list[iter - 1]}
        iter = iter + 1
        temp_list.append(temp_dict)
    documents = {'documents': temp_list}
    # documents = {'documents' : [
    #  {'id': '1', 'text': intersected_string[0]},
    #  {'id': '2', 'text': intersected_string[1]},
    #  {'id': '3', 'text': intersected_string[2]},]}

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response_language = requests.post(language_api_url, headers=headers, json=documents)
    response_sentiment = requests.post(sentiment_api_url, headers=headers, json=documents)
    response_key = requests.post(key_phrase_api_url, headers=headers, json=documents)
    response_entities = requests.post(entity_linking_api_url, headers=headers, json=documents)
    languages = response_language.json()
    key_phrases = response_key.json()
    sentiments = response_sentiment.json()
    entities = response_entities.json()

    if s == 'keyPhrases':
        return (key_phrases)
    elif s == 'sentiment':
        return (sentiments)
    elif s == 'entities':
        return (entities)
    else:
        return ('Wrong input')
