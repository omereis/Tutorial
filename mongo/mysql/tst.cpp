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
//#include <resultset.h>
#include <cppconn/resultset.h>
#include <metadata.h>
#include <resultset_metadata.h>
#include <exception.h>
#include <warning.h>

using namespace sql;
using namespace std;

void retrieve_data_and_print (ResultSet *rs, int type, int colidx, string colname);

#define NUMOFFSET 100

//-----------------------------------------------------------------------------
void print_error (sql::SQLException &e, const string &strFile, const string &strFunction, int nLine)
{
	cout << "# ERR: SQLException in " << strFile << endl;
	cout << "(" << strFile << ") on line " << std::to_string (nLine) << endl;
	cout << "# ERR: " << e.what();
	cout << " (MySQL error code: " << e.getErrorCode();
	cout << ", SQLState: " << e.getSQLState() << " )" << endl << endl;
}

//-----------------------------------------------------------------------------
int getMaxID (sql::Statement *stmt, const string &strTable, const string &strID)
{
	string strSql;
	sql::ResultSet *rs;
	int nMax;

	strSql = "select max(" + strID + ") from " + strTable + ";";
	//strSql = "select * from " + strTable + ";";
	try {
		cout << strSql << endl;
		rs = stmt->executeQuery (strSql);
		rs->first ();
		nMax = rs->getInt(1);
	}
	catch (sql::SQLException &e) {
        cout << "# ERR: SQLException in " << __FILE__;
        cout << "(" << __FUNCTION__ << ") on line " << __LINE__ << endl;
        cout << "# ERR: " << e.what();
        cout << " (MySQL error code: " << e.getErrorCode();
        cout << ", SQLState: " << e.getSQLState() << " )" << endl << endl;
		nMax = -1;
    }
	return (nMax);
}

static const string TableBlob ("T_BLOB");
//-----------------------------------------------------------------------------
int main(void)
{
	cout << endl;
	//cout << "Running 'SELECT 'Hello World!' AS _message'..." << endl;

	try {
		sql::Driver *driver;
		sql::Connection *con;
		sql::Statement *stmt;
		sql::ResultSet *res;
		string strSql;

#define NUMOFFSET 100

  /* Create a connection */
#define NUMOFFSET 100

		driver = get_driver_instance();
		con = driver->connect("tcp://ncnr-r9nano.campus.nist.gov", "myblob", "myblob");
  /* Connect to the MySQL test database */
		con->setSchema("lite");
		cout << "\nDatabase connection\'s autocommit mode = " << con -> getAutoCommit() << endl;
		stmt = con->createStatement();
		int id = getMaxID (stmt, "T_BLOB", "ID") + 1;
		cout << "Next max ID: " << id << endl;
		for (int n=0 ; n < 50 ; n++) {
			try {
				strSql = "insert into " + TableBlob + " (id) values (" + std::to_string (id++) + ");";
				stmt->executeQuery (strSql);
			}
			catch (sql::SQLException &e) {
				print_error (e, __FILE__, __FUNCTION__, __LINE__);
			}
		}

		res = stmt->executeQuery ("select * from T_BLOB;");

		retrieve_data_and_print (res, NUMOFFSET, 1,"");

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

#define	COLNAME	200
//-----------------------------------------------------------------------------
void retrieve_data_and_print (ResultSet *rs, int type, int colidx, string colname)
{
	ResultSetMetaData *pMeta;

	try {
		pMeta = rs->getMetaData();
		cout << "Number of columns : " << pMeta->getColumnCount() << endl;
		while (rs->next()) {
			cout << rs->getString(1) << endl;
		}
	}
	catch (sql::SQLException &e) {
		cout << "Error";
		cout << e.getErrorCode();
	}

} // retrieve_data_and_print()
