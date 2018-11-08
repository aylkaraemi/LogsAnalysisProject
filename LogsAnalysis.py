#! python3

import psycopg2

db_name = "news"


def top_articles():
    # retuns a list of the top 3 most popular articles rated by # of views
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()
    c.execute("query")
    articles = c.fetchall()
    db.close()
    return articles

def top_authors():
    # returns a sorted list of the authors based on article views
    pass

def request_errors():
    # returns a list of the days on which more than 1% of HTTP requests resulted
        # in errors
    pass

if __name__ == '__main__':
    pass