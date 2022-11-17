import datetime

from googlesearch import search as gsearch
import newspaper
from pprint import pprint
import re
from feedsearch import search
import feedparser
from summarizer import get_summary
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
    glinks = gsearch(query)
    print('links')
    for link in glinks:
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


def fetch_article(query):
    links = get_links(query, 10)
    news = ""
    image = None
    for link in links[:10]:
        try:
            current_text = fetch_news(link)
            if image is None and current_text["top_image"] != "":
                image = current_text["top_image"]
            news += ". " + current_text["text"]
            if len(news) >= int(2e3):
                break
        except Exception as e:
            pass

    ### find summary of news here
    news = get_summary(news)
    print("got summary")
    ###

    if image is None:
        image = ""

    news = create_search_news(image, news)
    print(news)
    print("mast")
    return news


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
        # carousel.append(create_search_news(post["imgsrc"], post["date"], post["title"], post["text"], post["topic"]))

    return carousel
    # return


def create_search_news(imgsrc, text):
    news = f"""
        <div class="row">
          <div style="float:left; width:30%;">
            <img class="img-fluid w-100" src={imgsrc} style="object-fit: cover;">
          </div>
          <div style="float:left; width:60%; text-align:center; display: flex; justify-content: center; align-items: center;">
            {text}
            </div>
        </div>
    """
    return news


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



