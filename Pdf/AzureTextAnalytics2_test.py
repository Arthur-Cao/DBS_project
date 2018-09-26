# -*- coding: utf-8 -*-
import AzureTextAnalytics as analysis

def test_basic():
    myList = ["Hello world. This is some input text that I love.","Bonjour tout le monde","La carretera estaba atascada. Había mucho tráfico el día de ayer."]
    result=analysis.azure_api(myList,'keyPhrases')

    print (result)

if __name__ ==  "__main__":
    test_basic()
