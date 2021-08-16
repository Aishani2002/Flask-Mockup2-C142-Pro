import csv

with open ("articles.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]
    headers = data[0]

with open ("final.csv", "a+", encoding='utf-8') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)

with open ("article_links.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_article_links = data[1:]

for article_item in allArticles:
    posterFound = any(article_item[8] in article_link_items for article_link_items in all_article_links)
    if (posterFound):
        for article_link_item in all_article_links:
            if(article_item[8] == article_link_item[0]):
                article_item.append(article_link_item[1])
                if(len(article_item) == 28):
                    with open("final.csv", "a+", encoding='utf-8') as f:
                        csvWriter = csv.writer(f)
                        csvWriter.writerows(article_item)