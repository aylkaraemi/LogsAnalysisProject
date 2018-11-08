# FSND - Logs Analysis

Project for the Udacity Full Stack Nanodegree program.

The logs analysis program is a reporting tool that connects to the FSND sample database using Python 3, runs a series of SQL queries, then prints the results to the screen in an easy to read format.

The report lists:

1. Top 3 most popular articles on the site
2. Most popular authors for the site
3. Days when more than 1% of requests to side lead to errors

A sample of the output produced can be found in the SampleReport.txt file.

## Created View
The reporting tool makes use of a saved view that joins all three tables of the sample news database.

The code for creating this view is:

```
placeholder for view code
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
