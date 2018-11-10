#! python3

import psycopg2

db_name = "news"


def ask_queries():
    # retuns a list of the top 3 most popular articles rated by # of views
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()
    c.execute("""
                select title, views
                    from article_info
                    order by views desc
                    limit 3
                """)
    articles = c.fetchall()
    c.execute("""
                select sum(views) as total_views, name
                    from article_info
                    group by name
                    order by total_views desc
                """)
    authors = c.fetchall()
    c.execute("""
                select date, (errors * 100.0 / total) as percent
                    from daily_requests
                    where (errors * 100.0 / total) > 1.0;
                """)
    request_errors = c.fetchall()
    db.close()
    return articles, authors, request_errors

def generate_report():
    articles, authors, request_errors = ask_queries()
    report = ''
    print(articles + "\n" + authors + "\n" + request_errors)



if __name__ == '__main__':
    pass