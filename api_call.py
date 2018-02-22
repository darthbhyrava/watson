import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, SentimentOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='fe7e83ab-fe27-432a-816e-428e79c992db',
  password='kaTY4H6r3HbY',
  version='2017-02-27')

response = natural_language_understanding.analyze(text='@divyaspandana Getting Freebies is in their blood.. congis telling Gareeb Atavo since 6 decade.. and still saying.. did everyone become rich? No right', features=Features(sentiment=SentimentOptions(document=True))

print response