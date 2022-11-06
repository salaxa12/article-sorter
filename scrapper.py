import newspaper

item = 1

# Define list of urls
list_of_urls = ['https://www.geeksforgeeks.org/how-to-get-the-magnitude-of-a-vector-in-numpy/',
                'https://www.geeksforgeeks.org/3d-wireframe-plotting-in-python-using-matplotlib/',
                'https://www.geeksforgeeks.org/difference-between-small-data-and-big-data/']
for url in list_of_urls:
    print(url)
    file2write = open("Article" + str(item) + ".txt", 'w')
    url_i = newspaper.Article(url=(url), language='en')
    url_i.download()
    url_i.parse()
    text = url_i.text
    file2write.write(text)
    print(url_i)
    item = item + 1
file2write.close()

# for item in  [ "one", "two", "three" ]:
#     f = open (item + " hello_world.txt", "w")
#     f.write("This is my first line of code")
#     f.write("\nThis is my second line of code with " + item  + " the first item in my list")
#     f.write ("\nAnd this is my last line of code")
#     f.close()
