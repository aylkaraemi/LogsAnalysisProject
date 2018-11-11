#!/usr/bin/env python3

import psycopg2

db_name = "news"


def ask_queries():
    try:
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
                    select name, sum(views) as total_views
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
    except psycopg2.OperationalError:
        print("There was an issue connecting to the database")


def generate_report():
    articles, authors, request_errors = ask_queries()

    report = 'The top three articles of all time are:\n\n'
    i = 1
    for row in articles:
        report = report + "{}. {} with {} views\n".format(i, row[0], row[1])
        i += 1
    report = report + "\n\nThe most popular authors of all time are:\n\n"
    i = 1
    for row in authors:
        report = report + "{}. {} with {} views\n".format(i, row[0], row[1])
        i += 1
    report = report + "\n\nMore than 1% of requests returned errors on:\n\n"
    for row in request_errors:
        date = row[0].date()
        errors = round(row[1], 1)
        report = report + "{} with {} % errors\n".format(date, errors)

    print(report)
    return report


if __name__ == '__main__':
    report = generate_report()
