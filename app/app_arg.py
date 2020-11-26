import argparse
from zeppos_logging.app_logger import AppLogger

class AppArg:
    def __init__(self, args):
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--servername')
        parser.add_argument('-d', '--database')
        parser.add_argument('-m', '--schemaname')
        parser.add_argument('-t', '--tablename')
        parser.add_argument('-r', '--csvdirectory')
        argp = parser.parse_args(args)

        self.server_name = argp.servername
        self.database_name = argp.database
        self.schema_name = argp.schemaname
        self.table_name = argp.tablename
        self.csv_directory = argp.csvdirectory

        AppLogger.logger.debug(f"ARG: server_name: {self.server_name}")
        AppLogger.logger.debug(f"ARG: database_name: {self.database_name}")
        AppLogger.logger.debug(f"ARG: schema_name: {self.schema_name}")
        AppLogger.logger.debug(f"ARG: table_name: {self.table_name}")
        AppLogger.logger.debug(f"ARG: csv_directory: {self.csv_directory}")



