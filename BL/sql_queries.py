from DAL.sqlite_handler import SqliteConnection


class ParkingDecisionDb:
    def __init__(self):
        self.db_file = 'license_db'
        self.table_name = 'parking_decision_logs'
        self.create_license_plate_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name}(id integer PRIMARY KEY, 
                                                        plate_number text NOT NULL, 
                                                        decision integer, 
                                                        log_time timestamp)"""
        with SqliteConnection(db_file=self.db_file) as sqlite_connection:
            sqlite_connection.execute_query(query=self.create_license_plate_table_query)

    def insert_parking_decision(self, plate_number: str, decision: bool, log_time: float):
        with SqliteConnection(db_file=self.db_file) as sqlite_connection:
            sqlite_connection.execute_query(query=f"""INSERT INTO {self.table_name} (plate_number, decision, log_time)
                                            VALUES ('{plate_number}', {int(decision)}, {log_time})""")
