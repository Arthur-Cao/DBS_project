#import json
from string_handle import *


def test_basic():
  filename = 'case2.pdf'

  print(generate_keyword(filename))
  
  print(generate_sentiment(filename))

  print(generate_entity(filename))

if __name__ ==  "__main__":
    test_basic()
