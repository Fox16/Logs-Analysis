#!/usr/bin/env python

import sys

import psycopg2

DBNAME = "news"

articles_query = """select title,views_count from articles_view
join log_view on CONCAT('/article/',
articles_view.slug) = log_view.path
 order by views_count
 desc limit 3; """

authors_query = """select name,sum(log_view.views_count) as total from authors
join articles_view on authors.id = articles_view.author
join log_view on CONCAT('/article/',
articles_view.slug) = log_view.path
group by authors.id,articles_view.author
order by total desc
limit 4"""

errors_query = """DROP TABLE IF EXISTS  TotalLogs;
DROP TABLE IF EXISTS  TotalFails;

Create Temporary Table TotalLogs as
select date(time) as DATE,count(*) LogsCount
from log
group by DATE(time);

Create Temporary Table TotalFails as
select date(time) as DATE,count(*) FailsCount
from log
where status ='404 NOT FOUND'
group by DATE(time);

select TotalFails.Date,
CONCAT(ROUND((TotalFails.FailsCount::decimal/TotalLogs.LogsCount)*100,2),' %')
as Percentage
from TotalLogs,TotalFails
where TotalFails.DATE = TotalLogs.DATE and
ROUND((TotalFails.FailsCount::decimal/TotalLogs.LogsCount)*100,2) >1;"""


def database_connect(query):
    # Connect to database
    try:
        database = psycopg2.connect(database=DBNAME)
    except psycopg2.OperationalError as e:
        print 'Unable to connect!\n{0}'.format(e)
        sys.exit(1)
    c = database.cursor()
    c.execute(query)
    result = c.fetchall()
    database.close()
    return result


def top_three_articles(query):
    articles = database_connect(query)
    for article in articles:
        print '"{}" - {} views \n'.format(article[0], article[1])


def top_authors(query):
    authors = database_connect(query)
    for author in authors:
        print('{} - {} views \n'.format(author[0], author[1]))


def error_percentage(query):
    errors = database_connect(query)
    for error in errors:
        print('{} - {} errors \n'.format(error[0], error[1]))


if __name__ == '__main__':
    top_three_articles(articles_query)
    top_authors(authors_query)
    error_percentage(errors_query)
