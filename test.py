from database import Databases

bus_database = Databases()
bus_database.update_to_bus_database('2250', 1)
bus_database.print_bus_database()