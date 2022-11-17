import datetime

from googlesearch import search
import newspaper
from pprint import pprint
import re
from feedsearch import search
import feedparser
import time


def cleaned_text(text):
    cleaned = ""
    for line in text.split('\n'):
        if len(line.split()) <= 5:
            line = ""
        if line != "":
            cleaned += line + " "
    cleaned = re.sub(' +', ' ', cleaned)
    return cleaned


def get_links(query, total_links):
    links = list()
    for link in search(query, num_results=total_links):
        links.append(link)
    return links


def fetch_news(url):
    article = newspaper.Article(url=url, language='en')
    article.download()
    article.parse()

    article ={
        "title": str(article.title),
        "text": cleaned_text(str(article.text)),
        "authors": article.authors,
        "published_date": str(article.publish_date),
        "top_image": str(article.top_image),
        "videos": article.movies,
        "keywords": article.keywords,
        "summary": str(article.summary)
    }

    return article


def create_post(imgsrc, date, title, text, topic):
    post = f"""
         <div class="col-lg-12" style="border-radius: 10px;">
              <div class="position-relative mb-3" style="border-radius: 10px;">
                  <img class="img-fluid w-100" src={imgsrc} style="object-fit: cover;">
                  <div class="overlay position-relative bg-light">
                      <div class="mb-2" style="font-size: 14px;">
                          <a href="">{topic}</a>
                          <span class="px-1">/</span>
                          <span>{date}</span>
                      </div>
                      <a class="h4" href="">{title}</a>
                      <p class="m-0">{text}</p>
                  </div>
            </div>
        </div>
    """
    # post = f"""
    # <div class="col-lg-12" style="border-radius: 10px;">
    #     <div class="position-relative mb-3" style="border-radius: 10px;">
    #         <img class="img-fluid w-100" src={imgsrc} style="object-fit: cover;">
    #           <div class="overlay position-relative bg-light">
    #               <div class="mb-2" style="font-size: 14px;">
    #                   <a href="">{topic}</a>
    #                   <span class="px-1">/</span>
    #                   <span>{date}</span>
    #               </div>
    #               <a class="h4" href="">{title}</a>
    #               <p class="m-0">{text}</p>
    #           </div>
    #     </div>
    # </div>
    # """
    return post


def create_carousel(data):
    carousel = []
    for post in data:
        carousel.append(create_post(post["imgsrc"], post["date"], post["title"], post["text"], post["topic"]))
    for p in carousel:
        print(p)
    return carousel
    # return


def get_current_news():
    feeds = search('nytimes.com')
    urls = [f.url for f in feeds]

    data = []

    if len(urls) > 0:
        news_feed = feedparser.parse(urls[0])
        entries = news_feed["entries"]
        # print(entries[0].keys())
        # print(len(entries))
        count = 0

        for entry in entries:
            imgsrc = ""
            try:
                imgsrc = entry["media_content"][0]["url"]
            except Exception:
                continue

            topic = ""
            try:
                topic = entry["tags"][0]["term"]
            except Exception:
                continue

            post = {
                "imgsrc": imgsrc,
                "title": entry["title"],
                "text": entry["summary"],
                "date": datetime.datetime.now().strftime("%d %B, %Y"),
                "topic": topic
            }

            if post["title"] == "" or post["text"] == "":
                continue

            count += 1
            data.append(post)

            if count >= 10:
                break

        return create_carousel(data)


if __name__ == '__main__':
    get_current_news()

# links = get_links("indian sports news", 5)
# pprint(fetch_news(links[0]))



