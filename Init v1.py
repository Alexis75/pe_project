# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import emploi_store
import requests

#EMPLOI_STORE_CLIENT_ID = 
#EMPLOI_STORE_CLIENT_SECRET = 

#r = requests.get("http://linuxfr.org/")
#print(r.text)


r = requests.post()

url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token"
data = '''{
  "query": {
    "bool": {
      "must": [
        {
          "text": {
            "record.document": "SOME_JOURNAL"
          }
        },
        {
          "text": {
            "record.articleTitle": "farmers"
          }
        }
      ],
      "must_not": [],
      "should": []
    }
  },
  "from": 0,
  "size": 50,
  "sort": [],
  "facets": {}
}'''

response = requests.post(url, data=data)

POST /connexion/oauth2/access_token?realm=%2Fpartenaire
Content-Type: application/x-www-form-urlencoded

