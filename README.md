# ms_sql_load_from_csv
load data from a CSV into Microsoft Sql Server


## requirements
- python version 3.8 (https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe)
- Microsoft BCP (https://go.microsoft.com/fwlink/?linkid=2142258)
- Microsoft SQLCMD.exe (https://www.microsoft.com/en-us/download/details.aspx?id=53591)
- Microsoft ODBC driver version 17 (https://www.microsoft.com/en-us/download/details.aspx?id=56567)

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
pipenv run python load_csv.py -s localhost\sqlexpress -d master -m dbo -t test_table -r c:\temp\test
```

- query.sql example for c:\temp\query.sql
```
set nocount on  -- make sure the last statement is going to be the select statement
set transaction isolation leve read uncommitted -- Global with nolock

drop table if exists #tmp

select TABLE_SCHEMA, TABLE_NAME into #tmp from information_schema.tables
select TABLE_SCHEMA, TABLE_NAME from #tmp
```

This is a very simple example that uses a temp table as this is needed in more complex queries.
The "set nocount on" is a very important statement to ensure the python pandas framework can iterate through the records.

- extract_csv.py arguments
```
-s or --servername: sql server name with instance
-d or --database: database name
-m or --schemaname: schema name
-t or --tablename: table name
-r or --csvdirectory: directory to the csv location
```
## result
This application will load the data into a table as specified in the application arguments.
The columns will become the header name formated as follows:
- capitalized
- non-alphanumeric characters become '_'

Two extra column will be added:
- 'AUDIT_CREATE_UTC_DATETIME': This is one utc datetime per file.
- 'CSV_FILE_NAME': The name of the csv file that was load excluding the directory.