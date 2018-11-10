# FSND - Logs Analysis

A project for the Udacity Full Stack Nanodegree program.

The logs analysis program is a reporting tool that connects to the FSND sample database using Python 3, runs a series of SQL queries, then prints the results to the screen in an easy to read format.

The report lists:

1. Top 3 most popular articles on the site
2. Most popular authors for the site
3. Days when more than 1% of requests to side lead to errors

A sample of the output produced can be found in the SampleReport.txt file.

## Created View
The reporting tool makes use of three saved views: one joins all three tables to allow tracking requests by article or author, the second creates a table showing how many requests resulted in errors each day, and the third shows both the number of errors per day and the total requests per day to allow calculating the percentage of errors per day.

The code for creating the view joining all tables is:

```
create view article_info as
    select articles.title, articles.author, authors.name, count(log.path) as views
        from articles, authors, log
        where articles.author = authors.id and log.path like concat('%', articles.slug)
        group by articles.title, articles.author, authors.name;
```

The code for creating the request error view is:

```
create view request_errors as
    select date_trunc('day', time) as date, count(*) as errors
        from log
        where status like '4%' or status like '5%'
        group by date
        order by date;
```

The code for creating the errors vs totals view:

```
create view daily_requests as
    select request_errors.date, request_errors.errors, count(log.status) as total
        from request_errors, log
        where request_errors.date = date_trunc('day', log.time)
        group by date, request_errors.errors
        order by date;
```

## Running the Logs Analysis tool
The Logs Analysis tool is run from the command line inside the Vagrant virtual machine hosting the database.

**Note:** The LogsAnalysis.py file will need to be in the Vagrant folder for the VM hosting the database in order to run it in the VM.

1. cd into the directory where your VM is, for example:
   `$ cd fullstack-nanodegree-vm/`
2. run the `$ vagrant up` command
3. run the `$ vagrant ssh` command
4. run the LogAnalysis file using `python LogsAnalysis.py`:

    `vagrant@vagrant-ubuntu-trusty32:/vagrant$ python LogsAnalysis.py`
