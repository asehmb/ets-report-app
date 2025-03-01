"""
Bus stop number:
location:
# of reports
"""
import sqlite3

class Databases:
    def __init__(self):
        self.__bus_database = "Bus_Stop_Database"
    
    def create_bus_stop_database(self):
        try:
            cursor, connection = self.open_database(self.__bus_database)
            cursor.execute("""
                Create Bus Stop Database(
                bus_stop_number text,
                location text,
                num_of_reports text        
                )

            """)
        
        except:
            print("Bus Stop database has already been created")
        
    def open_database(self, database):
        """
        """
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        return cursor, connection
    
    def close_database(self, connection):
        """
        purpose: closes the database
        """
        connection.commit()
        connection.close()

    def push_to_bus_database(self, bus_stop_num, location, num_of_reports):
        """
        purpose: pushes to the bus database
        param bus_stop_num: string
        param location: string
        param num_of_reports: string
        return: None
        """
        cursor, connection = self.open_database(self.__bus_database)
        cursor.execute("""
            INSERT INTO Bus Stop Database
            VALUES (?, ?, ?)
            
        """, [bus_stop_num, location, num_of_reports])
        self.close_database(connection)
        print(f"Bus Stop Number {bus_stop_num} has saved to databases")
    
    def update_to_bus_database(self, bus_stop_num, num_of_reports):
        """
        purpose: updates the number of reports
        param bus_stop_num: string
        param num_of_reports: string
        return: None
        """
        bus_stop_info = self.get_a_bus_stop(bus_stop_num)
        cursor, connection = self.open_database()
    
    def get_a_bus_stop(self, bus_stop_num):
        """
        purpose: fetches a bus stop information from the database
        parameter bus_stop_num: string
        return: tuple (3)
        """
        cursor, connection = self.open_database(self.__bus_database)
        bus_stop_info = cursor.execute("""
            SELECT * FROM Bus Stop Database
            WHERE bus_stop_num = ?
        """, [bus_stop_num]).fetchone()
        self.close_database(connection)
        return bus_stop_info
