import pdb

from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# article_text = soup.select_one(".titleline a").text
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.find('a').get("href"))

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name='span', class_='score')]



most_upvotes = max(article_upvotes)
most_upvotes_index = article_upvotes.index(most_upvotes)
print()
print(f"{article_texts[most_upvotes_index]}")
print(f"{article_links[most_upvotes_index]}")
print(f"{most_upvotes} up Votes")
# pdb.set_trace()
# print(response.text)


# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
#
#
# # print(soup.title())
# # print(soup.title)
# # print(soup.title.string)
# #
# # print(soup)
# # print(soup.prettify())
#
# # print(soup.p)
#
#
# # h = soup.find_all(name="a")
# # print(h)
# #
# # for tag in h:
# #     print(tag.get("href"))
# # #     print(tag.getText())
#
# heading = soup.find(name="h1", id="name")
#
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one("name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)
