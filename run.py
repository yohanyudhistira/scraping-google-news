from pygooglenews import GoogleNews

gn = GoogleNews(country='US')


def get_titles(search):
    stories = []
    search = gn.search(search)
    news_item = search['entries']
    for item in news_item:
        story = {
            'item': item.title,
            'link': item.link
        }
        stories.append(story)
    return stories


print(get_titles('anime'))
