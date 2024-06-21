from bs4 import BeautifulSoup

soup = None

# Opening a HTML file on computer and parsing it
with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")


# Look at the data
# print(soup.prettify())


# Getting albums
# ===========================================

# Get all albums by getting unordered list
# ul_list = soup.find('ul')
# print(ul_list)

# # Get different attributes of elements
# print(ul_list['id'])

# Get all albums by getting all list elements
# list_albums = soup.find_all('li')
# print("list of albums:", list_albums)

# list_albums = [li.text for li in list_albums]
# print(list_albums)

# Children, Parents and Contents
# ===========================================
songs = soup.select_one(".top-songs")
print("songs:", songs)

# Getting children
children = songs.contents
print("children:", children)

# length = len(children)
# second_child = children[1]
# print("second child and length:", second_child, length)


# siblings = songs.next_siblings
# for sibling in siblings:
#     print("sibling:", sibling) #navegableString

# parent = songs.parent
# print("parent:", parent)




