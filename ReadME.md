# Logs Analysis Project - Udacity  Full Stack ND

#### DESCRIPTION
This reporting tool is a Python program with PostgreSQL database to print out reports based on the data given from news database.
#### The reports answers the following three questions given below:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
#### RUNNING THE PROGRAM
To get started, I recommend you to download Vagrant, VirtualBox and VM configuration from links given below, 
* Download [Vagrant](https://www.vagrantup.com/) 
* Download [VirtualBox](https://virtualbox.org/wiki/Downloads)
* Download VM configuration [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)

**TO INSTALL AND MANAGE THE PROGRAM USING VIRTUAL MACHINE**
* Go to VM configuration folder
* Change to this directory in your terminal with `cd`
* Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login.

* Download the database provided by Udacity from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
* Unzip the file in inside the vagrant folder.
* Change to vagrant directory in your terminal with `cd /vagrant/`
* Load the database using `psql -d news -f newsdata.sql`.
* Connect to the database using `psql -d news`.
* Create the Views given below. `Then exit psql`.
* Now execute the Python file - `python logs_analysis.py`

Otherwise download [python 2.7](https://www.python.org/downloads/) and [PostgreSQL](https://www.postgresql.org/download/) to run this program.


#### Project Views 
```sql
CREATE VIEW articles_view AS select id,title,slug,author from articles;
```
```sql
CREATE VIEW log_view as select path,count('*') as views_count from log group by path
``` 
