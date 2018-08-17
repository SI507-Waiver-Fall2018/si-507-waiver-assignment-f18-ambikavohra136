# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

#function to connect to database
def createConnection(dbfile):
	try:
		conn = sqlite3.connect(dbfile)
		return conn
	except:
		print(e)

	return none


#function print all customers
def printCustomers(conn):
	c = conn.cursor()
	c.execute("SELECT ID, ContactName FROM Customer")
	rows = c.fetchall()
	#print all rows
	print("ID", "\t", "Customer Name")
	for row in rows:
		print(str(row[0]), "\t", str(row[1]))


#function to print all employees
def printEmployees(conn):
	c = conn.cursor()
	c.execute("SELECT ID, FirstName, LastName FROM Employee")
	rows = c.fetchall()

	print("ID", "\t", "Employee Name")
	for row in rows:
		print(str(row[0]) + "\t" + str(row[1]) + " " + str(row[2]))


#function to return order date associated with customer ID
def getOrderDatefromID(conn, cust_ID):
	c = conn.cursor()
	c.execute("SELECT OrderDate FROM \"Order\" WHERE CustomerId=?", (cust_ID,))
	rows = c.fetchall()

	print("Order Date associated with customer ID " +str(cust_ID))
	for row in rows:
		print(str(row[0]))

#function to return order date after last name is input
def getOrderDatefromLN(conn, emp_lname):
	c = conn.cursor()
	c.execute('''SELECT OrderDate FROM "Order", "Employee" WHERE "Order".EmployeeId="Employee".Id AND "Employee".LastName="''' + str(emp_lname) + "\"")
	rows = c.fetchall()

	print("Order Date associated with employee last name " +str(emp_lname))
	for row in rows:
		print(str(row[0]))

#establish database connection and take arguments from command line
def main():
	database = "./Northwind_small.sqlite"

	#Establishing a Database connection
	conn = createConnection(database)
	#check command line arguments
	if(len(sys.argv)>1):
		with conn:
			if sys.argv[1] == "customers":
				printCustomers(conn)
			elif (sys.argv[1] == "employees"):
				printEmployees(conn)
			elif (sys.argv[1] == "orders"):
				#case if parameter is customer ID
				if (sys.argv[2][:4]=="cust"):
					getOrderDatefromID(conn, sys.argv[2][5:])
				#case if parameter is employee last name
				elif (sys.argv[2][:3]=="emp"):
					getOrderDatefromLN(conn, sys.argv[2][4:])
			else:
				print("Enter a valid argument please!")
	else:
		print("Please try again. Valid arguments include 'customers', 'employees', 'orders=<customer_ID>', 'orders=<customer last name>'")

main()
