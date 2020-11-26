import sys
from zeppos_logging.app_logger import AppLogger
from app.app_arg import AppArg
from zeppos_csv.csv_file import CsvFile
from zeppos_csv.csv_files import CsvFiles

from zeppos_bcpy.sql_configuration import SqlConfiguration
def main(args):
    AppLogger.logger.debug("Extracting sql to csv")
    app_arg = AppArg(args)

    csv_files = CsvFiles(base_dir=app_arg.csv_directory)
    csv_files.to_sql_server_with_chunking(
        sql_configuration=SqlConfiguration(
                    server_type='microsoft',
                    server_name=app_arg.server_name,
                    database_name=app_arg.database_name,
                    schema_name=app_arg.table_schema,
                    table_name=app_arg.table_name
                ),
        use_existing=True,
        mark_as_processed=True
    )


if __name__ == '__main__':
    AppLogger.configure_and_get_logger()
    AppLogger.set_debug_level()

    main(sys.argv[1:])


