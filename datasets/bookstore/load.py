from typedb.driver import TypeDB, DriverOptions
from typedb.api.connection.transaction import TransactionType
from typedb.api.connection.credentials import Credentials

ADDRESS = "127.0.0.1:1729"
USERNAME = "admin"
PASSWORD = "password"

DATABASE = "bookstore"
SCHEMA_PATH = "schema.tql"
DATA_PATH = "data.tql"

credential = Credentials(USERNAME, PASSWORD)
driver = TypeDB.driver(ADDRESS, credential, DriverOptions())

if driver.databases.contains(DATABASE):
    driver.databases.get(DATABASE).delete()
driver.databases.create(DATABASE)
print("Recreated database")

define = open(SCHEMA_PATH).read()
with driver.transaction(DATABASE, TransactionType.SCHEMA) as tx:
    tx.query(define).resolve()
    tx.commit()
print("Schema committed")


data = open(DATA_PATH)
lines_without_not = 0
lines_with_not = set()
total_inserted_rows = 0

with driver.transaction(DATABASE, TransactionType.WRITE) as tx:
    for line in data:
        line = line.strip()
        if line and not line.startswith("#"):
            inserted_rows = len([row for row in tx.query(line).resolve()])
            total_inserted_rows += inserted_rows
            if "not {" in line:
                lines_with_not.add(line)
            else:
                lines_without_not += 1
                assert inserted_rows == 1, "Inserted rows={} (expected 1) for query (without not) {}".format(inserted_rows, line)
    tx.commit()

print("lines without not:", lines_without_not)
print("unique lines with not:", len(lines_with_not))
print("lines without not + unique lines with not:", lines_without_not + len(lines_with_not))
print("Data committed: {} rows returned".format(total_inserted_rows))
