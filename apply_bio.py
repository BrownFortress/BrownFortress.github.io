import json

articles = {}

with open("articles_new.json") as f:
    articles = json.loads(f.read())

articles = sorted(articles, key=lambda el: el['year'], reverse=True)

output = ""
for art in articles:
    title = art['title']
    authors =  "<i>" +art['authors'].replace("Gabriel Roccabruna", "<b>Gabriel Roccabruna</b>") + "</i>"
    publication = art["publication"]
    link = art['link']
    year = art['year']
    output += f'<div class="row"><div class="col-1 text-danger pt-1">{year}</div><div class="col-10 ml-auto mr-3"><h6><a href="{link}" target="_blank">{title}</a></h6><p class="subtitle">{authors}</p><P class="subtitle" style="font-size:12"> <i>{publication}</i></P><hr></div></div>'.format(year, link, title, authors, publication)
    # output += f'<h6 class="title text-danger"><a href="{link}" target="_blank">{title}</a></h6> <P>{authors}</P> <P class="subtitle" style="font-size:12"> <i>{publication}</i></P> <hr>'.format(link, title, authors, publication)
    
with open("pubs.html", "w") as f:
    f.write(output)

