# FSND - Logs Analysis

A project for the Udacity Full Stack Nanodegree program.

The logs analysis program is a reporting tool that connects to the FSND sample database using Python 3, runs a series of SQL queries, then prints the results to the screen in an easy to read format.

The report lists:

1. Top 3 most popular articles on the site
2. Most popular authors for the site
3. Days when more than 1% of requests to side lead to errors

A sample of the output produced can be found in the SampleReport.txt file.

## Dependencies
This tool requires python (2 or 3), VirtualBox, Vagrant, a Unix-style terminal and the news database. Instructions for downloading and installing each of these are below.

### Python
To download python click [here](https://www.python.org/downloads/) and select the version to install. This tool works on both python 2 and 3 so the most recent version is fine to use.

_Note_: The site should detect the OS, but if not there are links to the installers for each OS directly below the button for the latest version.

Once the installer is downloaded, run it and follow the instructions to install.

### Unix shell
For Mac or Linux systems the built-in terminal program can be used.

For Windows you will need to download a program, such as Git Bash, if you do not already have one. You can download Git Bash [here](https://git-scm.com/downloads) and find information on how to use it [here](https://git-scm.com/doc).

### VirtualBox & Vagrant
VirtualBox and Vagrant work together to run the virtual machine this tool runs in. VirtualBox runs the VM and Vagrant is how the VM is accessed and used.

VirtualBox can be downloaded [here](https://www.virtualbox.org/wiki/Downloads). There are links for each OS in the section "VirtualBox 5.2.22 platform packages". Once the installer is downloaded, run it and follow the instructions.

_Note_: some users have difficulty using newer versions of VirtualBox with Vagrant, so you may need to use an older version of VirtualBox instead which can be downloaded [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).

Vagrant can be downloaded [here](https://www.vagrantup.com/downloads.html). Select the correct version for your OS and download and run the installer.

_Note_: if you are using Git Bash make sure to run it as an administrator or you may have issues getting vagrant to function

Documentation for Vagrant can be found [here](https://www.vagrantup.com/docs/index.html) to assist in troubleshooting any issues.

### VM Configuration
To make sure you have the correct configuration of your VM you can either download the zipfile [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) or fork and clone [this](https://github.com/udacity/fullstack-nanodegree-vm) repository on GitHub.
Either link will give you a new directory containing the necessary VM files.

To start the VM:
1. change to the new directory using `cd`
2. inside is another directory called vagrant, change to that with `cd vagrant/`
3. enter the command `vagrant up` to prompt Vagrant to download the linux operating system and install it
4. once completed enter the command `vagrant ssh` to log in to the VM.
   - **note**: for some versions of Windows you may need to use `winpty vagrant ssh` instead
5. when you are ready to exit your vm type `exit` in the shell prompt to log out

If you wish to log in again you can just cd back to the vagrant directory and type `vagrant ssh` as long as you have not rebooted your computer. If you reboot your computer, you will need to use `vagrant up` again to initialize the vm, then `vagrant ssh` to log in.

### Setting up the News Database
In order to use the reporting tool you will need to download and set up the news database it functions with.

First, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to get a zip file containing the file `newsdata.sql` which you will use to set up the database.

Next you will need to load the data to set up the news database in your VM:
1. move the `newsdata.sql` file into the vagrant directory
2. log into your vm using the instructions above
3. within vagrant cd into the vagrant directory: `cd /vagrant`
4. run the command `psql -d news -f newsdata.sql`

If there are any errors from the `psql -d news -f newsdata.sql`, and you already had an older version of the VM configuration previously installed you may need to download the VM configuration into a new directory by following the instructions above.

Once you have the database set up you will need to run the code below to create three new saved views that the reporting tool relies on.

**Note** Troubleshooting tips and VM configuration instructions sourced from Udacity "Installing the Virtual Machine" lesson within the Intro to Relational Databases course.

### Created Views
The reporting tool makes use of three saved views: one joins all three tables to allow tracking requests by article or author, the second creates a table showing how many requests resulted in errors each day, and the third shows both the number of errors per day and the total requests per day to allow calculating the percentage of errors per day.

To create this views in your copy of the database:
1. log into the vm using the instructions above
2. connect to the database using the command `psql -d news`
3. run each of the create view commands in the code blocks below one at a time
4. when complete, you can exit psql with the command `\quit`

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
**Note:** Make sure all the set up above has been completed before you try and run the Logs Analysis tool.

The Logs Analysis tool is run from the command line inside the Vagrant virtual machine hosting the database.

**Note:** The LogsAnalysis.py file will need to be in the Vagrant folder for the VM hosting the database in order to run it in the VM.

1. place LogsAnalysis.py in the vagrant directory
2. log into the vm using the instructions above
3. `cd` into the vagrant folder: `cd /vagrant`
3. run the LogAnalysis file using the command `python LogsAnalysis.py`:

    `vagrant@vagrant:/vagrant$ python LogsAnalysis.py`

After a few seconds it will print the results of the SQL queries to the screen.