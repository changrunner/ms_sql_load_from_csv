# ms_sql_load_from_csv
load data from a CSV into Microsoft Sql Server


## requirements
- python version 3.8 (https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe)
- Microsoft BCP (https://go.microsoft.com/fwlink/?linkid=2142258)

## install
- upgrade pip
```
python -m pip install --upgrade pip
```
- install pipenv
```
pip install pipenv==2018.11.26
```
- install python project requirements
```
pipenv install
```

## usage

- from a windows command prompt or powershell run
```
pipenv run python load_csv.py -s localhost\sqlexpress -d master -m dbo -t test_table -f c:\temp\test.csv
```

- query.sql example for c:\temp\query.sql
```
select TABLE_SCHEMA, TABLE_NAME from information_schema.tables
```

- extract_csv.py arguments
```
-s or --servername: sql server name with instance
-d or --database: database name
-r or --rootdirectory: root directory where the csvfile will land.
-f or --csvfilename: suffix of the csv filename
-q or --queryfilename: full path to the file that contains the sql command
-o or --odbcversion: version of the odbc driver (default is 17)
```
