from typedb.driver import TypeDB, DriverOptions
from typedb.api.connection.transaction import TransactionType
from typedb.api.connection.credentials import Credentials

ADDRESS = "127.0.0.1:1729"
USERNAME = "admin"
PASSWORD = "password"

DATABASE = "social-network"
SCHEMA_PATH = "schema.tql"
DATA_PATH = "data.tql"

credential = Credentials(USERNAME, PASSWORD)
driver = TypeDB.core_driver(ADDRESS, credential, DriverOptions())

if driver.databases.contains(DATABASE):
    driver.databases.get(DATABASE).delete()
driver.databases.create(DATABASE)
print("Recreated database")

define = open(SCHEMA_PATH).read()
with driver.transaction(DATABASE, TransactionType.SCHEMA) as tx:
    tx.query(define)
    tx.commit()
print("Schema committed")


data = open(DATA_PATH)
executed_lines = 0
insert_results = 0
with driver.transaction(DATABASE, TransactionType.WRITE) as tx:
    for line in data:
        line = line.strip()
        if line and not line.startswith("#"):
            insert_results += len([row for row in tx.query(line).resolve()])
            executed_lines += 1
    tx.commit()
print("Data committed: {} lines/ {} rows returned".format(executed_lines, insert_results))


