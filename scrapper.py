import newspaper
import os
from requests_html import HTMLSession


# session = HTMLSession()
# url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
# r = session.get(url)

# r.html.render(sleep=1, scrolldown=6)

# articles = r.html.find('article')
# newsLinks = []

# for i in articles:
#     try:
#         newsitem = i.find('a', first=True)
#         rawLink = newsitem.attrs['href']
#         fullLink = str("https://news.google.com" + rawLink[1:-1])
#         newsLinks.append(fullLink)
#     except:
#         pass

# print(len(newsLinks))
# print(newsLinks[5:10])

# # ---------------------------------------second part--------------------------------------------------------


# item = 1

# switch = 0

# os.chdir("articles/sports/training")
# for url in newsLinks:
#     if item <= 100 and switch == 0:
#         try:
#             file2write = open("TrSportsArticle" + str(item) + ".txt", 'w')
#             url_i = newspaper.Article(url=(url), language='en')
#             url_i.download()
#             url_i.parse()
#             text = url_i.text
#             if(len(text) > 0):
#                 file2write.write(text)
#                 print(url_i)
#                 item = item + 1
#                 file2write.close()
#             if(item == 101):
#                 os.chdir("../testing")
#                 switch = 1
#         except:
#             pass

#     elif item > 100 and switch == 1:
#         try:
#             file2write = open("TeSportsArticle" + str(item) + ".txt", 'w')
#             url_i = newspaper.Article(url=(url), language='en')
#             url_i.download()
#             url_i.parse()
#             text = url_i.text
#             if(len(text) > 0):
#                 file2write.write(text)
#                 print(url_i)
#                 item = item + 1
#                 file2write.close()
#         except:
#             pass
#     elif item >= 200:
#         break

# -------------------------------------------------technology---------------------------------------------------------------------------

session = HTMLSession()  # declare HTML session
url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'  # url of google news
r = session.get(url)  # open chromum and get the url

r.html.render(sleep=1, scrolldown=12)  # render the page with 12 scrolldowns

articles = r.html.find('article')  # find article element in page
newsLinks = []  # link for news

for i in articles:
    try:
        newsitem = i.find('a', first=True)  # find a in article
        rawLink = newsitem.attrs['href']  # get link within the <a> tag
        # append news google with the raw link
        fullLink = str("https://news.google.com" + rawLink[1:-1])
        newsLinks.append(fullLink)
    except:
        pass

print(len(newsLinks))
print(newsLinks[5:10])

item = 1

switch = 0

os.chdir("articles/technology/training")
for url in newsLinks:
    if item <= 100 and switch == 0:
        try:
            file2write = open("TrTechnologyArticle" + str(item) + ".txt", 'w')
            url_i = newspaper.Article(url=(url), language='en')
            url_i.download()
            url_i.parse()  # analyze the article
            text = url_i.text  # get text from the url whic is article
            if(len(text) > 0):  # if the text is not empty
                file2write.write(text)  # write the file
                item = item + 1
                file2write.close()  # close file
            if(item == 101):
                # continue writing in training directory if i
                os.chdir("../testing")
                switch = 1
        except:
            pass

    elif item > 100 and switch == 1:  # testing directory writing code
        try:
            file2write = open("TeTechnologyArticle" + str(item) + ".txt", 'w')
            url_i = newspaper.Article(url=(url), language='en')
            url_i.download()
            url_i.parse()
            text = url_i.text
            if(len(text) > 0):
                file2write.write(text)
                item = item + 1
                file2write.close()
        except:
            pass
    elif item >= 200:
        break
