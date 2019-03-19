/* Copyright 2008, 2010, Oracle and/or its affiliates. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 of the License.

There are special exceptions to the terms and conditions of the GPL
as it is applied to this software. View the full text of the
exception in file EXCEPTIONS-CONNECTOR-C++ in the directory of this
software distribution.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
*/

/* Standard C++ includes */
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

/*
  Include directly the different
  headers from cppconn/ and mysql_driver.h + mysql_util.h
  (and mysql_connection.h). This will reduce your build time!
*/
#include "mysql_connection.h"

#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>


/* MySQL Connector/C++ specific headers */
#include <driver.h>
#include <connection.h>
#include <statement.h>
#include <prepared_statement.h>
#include <cppconn/resultset.h>
#include <metadata.h>
#include <resultset_metadata.h>
#include <exception.h>
#include <warning.h>

using namespace std;
using namespace sql;

void retrieve_data_and_print (ResultSet *rs, int type, int colidx, string colname);

#define NUMOFFSET	100
#define	COLNAME		200

#include <fstream>
#include <sstream>

int main(void)
{
	cout << endl;
	cout << "Running 'SELECT 'Hello World!' AS _message'..." << endl;

	try {
		sql::Driver *driver;
		sql::Connection *con;
		sql::Statement *stmt;
		sql::ResultSet *res;

		std::streambuf *buf;// = std::streambuf();

  /* Create a connection */
		driver = get_driver_instance();
		//con = driver->connect("tcp://127.0.0.1:3306", "root", "root");
		con = driver->connect("tcp://ncnr-r9nano.campus.nist.gov", "myblob", "myblob");
  /* Connect to the MySQL test database */
		//con->setSchema("test");
		con->setSchema("lite");
		cout << "\nDatabase connection\'s autocommit mode = " << con -> getAutoCommit() << endl;
		stmt = con->createStatement();
		std::string strSql;
		std::istream *istrim;
		streambuf *sbuf;
		char *pData;

		ifstream is ((const char*) "jaja", std::ifstream::binary);
		istrim = new istream ("file", std::ifstream::binary);
		istream & istr = is;

		strSql = "update T_BLOB set FILE=? where ID=1';";
		sql::PreparedStatement *pstmt;
		pstmt = con->prepareStatement (strSql);

		pstmt->setBlob (1, istrim);
		pstmt->setBlob (1, &is);
		res = stmt->executeQuery ("select * from T_BLOB;");

		retrieve_data_and_print (res, NUMOFFSET, 1,"");
/*
		stmt = con->createStatement();
		res = stmt->executeQuery("SELECT 'Hello World!' AS _message");
		while (res->next()) {
			cout << "\t... MySQL replies: ";
    ** Access column data by alias or column name **
			cout << res->getString("_message") << endl;
			cout << "\t... MySQL says it again: ";
    ** Access column data by numeric offset, 1 is the first column **
			cout << res->getString(1) << endl;
		}
*/
		delete res;
		delete stmt;
		delete con;

	}
	catch (sql::SQLException &e) {
		cout << "# ERR: SQLException in " << __FILE__;
		cout << "(" << __FUNCTION__ << ") on line " << __LINE__ << endl;
		cout << "# ERR: " << e.what();
		cout << " (MySQL error code: " << e.getErrorCode();
		cout << ", SQLState: " << e.getSQLState() << " )" << endl;
	}
	cout << endl;

	return EXIT_SUCCESS;
}

//-----------------------------------------------------------------------------
void retrieve_data_and_print (ResultSet *rs, int type, int colidx, string colname) {

	/* retrieve the row count in the result set */
	cout << "\nRetrieved " << rs -> rowsCount() << " row(s)." << endl;

	cout << "\nCityName" << endl;
	cout << "--------" << endl;

	/* fetch the data : retrieve all the rows in the result set */
	while (rs->next()) {
		if (type == NUMOFFSET) {
                       cout << rs -> getString(colidx) << endl;
		} else if (type == COLNAME) {
                       cout << rs -> getString(colname) << endl;
		} // if-else
	} // while

	cout << endl;

} // retrieve_data_and_print()
