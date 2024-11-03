from serpapi import GoogleSearch
import json

params = {
  "engine": "google_scholar_author",
  "author_id": "o_1Q_G4AAAAJ",
  "api_key": "1da549f85beee3858b1deca637a98b2945f566ab1362a067d60edd930172ba39"
}

search = GoogleSearch(params)
results = search.get_dict()
articles = results["articles"]

with open("articles.json", "w") as f:
    f.write(json.dumps(articles, indent=4))