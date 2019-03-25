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
#include <fstream>      // std::filebuf
#include <streambuf>

#include "genfile.h"
#include "misc.h"
#include "get_cli.h"

/*
using namespace sql;
using namespace std;

static const string TableBlob ("T_BLOB");
static const string FieldID   ("ID");
static const string FieldFile  ("FILE_BLOB");
*/

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

enum	SqlCommand	{SQLExecute, SQLQuery};

using namespace sql;
using namespace std;

static const string TableBlob ("T_BLOB");
static const string FieldID   ("ID");
static const string FieldFile  ("FILE_BLOB");

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

void print_sql_error (sql::SQLException &e, const string &strFile, const string &strFunction, int nLine);
void print_error (exception &e, const string &strFile, const string &strFunction, int nLine);
void insert_file (sql::Connection *con, int idStart, const string &strFile, int nInsertCount = 1);
void insert_file (sql::Connection *con, int idStart, const std::string &strDataFileName, struct FileMaker *pfm);
long GetFileSize(std::string filename);
bool RunSql (sql::Connection *con, const std::string &strSql, const SqlCommand &cmd, sql::ResultSet *res=NULL);
//-----------------------------------------------------------------------------
void print_sql_error (sql::SQLException &e, const string &strFile, const string &strFunction, int nLine)
{
    print_error (e, strFile, strFunction, nLine);
    cout << " (MySQL error code: " << e.getErrorCode();
    cout << ", SQLState: " << e.getSQLState() << " )" << endl << endl;
}

//-----------------------------------------------------------------------------
void print_error (exception &e, const string &strFile, const string &strFunction, int nLine)
{
    cout << "# ERR: SQLException in " << strFile << endl;
    cout << "(" << strFile << ") on line " << std::to_string (nLine) << endl;
    cout << "# ERR: " << e.what();
}

void retrieve_data_and_print (ResultSet *rs, int type, int colidx, string colname);

#define NUMOFFSET 100

//-----------------------------------------------------------------------------
int getMaxID (sql::Statement *stmt, const string &strTable, const string &strID)
{
	string strSql;
	sql::ResultSet *rs;
	int nMax;

	strSql = "select max(" + strID + ") from " + strTable + ";";
	//strSql = "select * from " + strTable + ";";
	try {
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

//-----------------------------------------------------------------------------
int main(int argc, char *argv[])
{
	cout << endl;
	//cout << "Running 'SELECT 'Hello World!' AS _message'..." << endl;

	try {
		sql::Driver *driver;
		sql::Connection *con;
		sql::Statement *stmt;
		struct FileMaker fm;
		string strSql, strDataFileName;

		get_cli_params(&fm, argc, argv, (char*) "btst");
		print_params (&fm);
		cout << "Free space: " << get_free_space() / (1024 * 1024) << " M bytes"<< endl;
		strDataFileName = gen_one_file ("", &fm);
		//exit(0);
#define NUMOFFSET 100

  /* Create a connection */
#define NUMOFFSET 100

		driver = get_driver_instance();
		con = driver->connect("tcp://ncnr-r9nano.campus.nist.gov", "myblob", "myblob");
  /* Connect to the MySQL test database */
		con->setSchema("lite");
		//cout << "\nDatabase connection\'s autocommit mode = " << con -> getAutoCommit() << endl;
		stmt = con->createStatement();
		int id = getMaxID (stmt, "T_BLOB", "ID") + 1;
		cout << "Next max ID: " << id << endl;
		id = getMaxID (stmt, "T_BLOB", "ID") + 1;
		//insert_file (con, id, "/home/one4/Source/disk_space/mysql/bari.jpg", 5);
		insert_file (con, id, strDataFileName, &fm);

		//retrieve_data_and_print (res, NUMOFFSET, 1,"");

		//delete res;
		//delete stmt;
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

}

//-----------------------------------------------------------------------------
void insert_file (sql::Connection *con, int idStart, const string &strFile, int nInsertCount)
{
	string strSql, strBase;
	sql::PreparedStatement *pstmt;
	char *pData;
	ifstream *blobFile;
	int nLen;

	try {
		//cout << "about to read file " << strFile << endl;
		//cout << "File " << strFile << " read" << endl;
		strBase = "insert into " + TableBlob + "(" + FieldID + "," + FieldFile + ") values (?,?);";
		for (int n=0 ; n < nInsertCount ; n++) {
			blobFile = new ifstream (strFile, ios::binary | ios::in);
			nLen = blobFile->tellg();
			pData = new char[nLen];
			blobFile->read (pData, nLen);
			strSql = strBase;
			pstmt = con->prepareStatement (strSql);
			pstmt->setInt (1, idStart++);
			pstmt->setBlob (2, blobFile);
			pstmt->executeUpdate();
			delete pstmt;
			delete pData;
			delete blobFile;
		}
		cout << "File " << strFile << " inserted to database" << endl;
	}
	catch (exception &e) {
		print_error (e, __FILE__, __FUNCTION__, __LINE__);
	}
}

//-----------------------------------------------------------------------------
void insert_file (sql::Connection *con, int idStart, const std::string &strDataFileName, struct FileMaker *pfm)
{
	string strSql, strBase;
	sql::PreparedStatement *pstmt;
	char *pData;
	ifstream *blobFile;
	int n, nLen, nBefore, nAfter;
	long lSize;
	FILE *fResults;
	clock_t cStart;
	double dSeconds;
	//sql::Statement *stmt;
	sql::ResultSet *res=NULL;

	try {
		//cout << "about to read file " << strFile << endl;
		//cout << "File " << strFile << " read" << endl;
		fprintf (stderr, "Optimizing Table\n");
		if (RunSql (con, "optimize table " + TableBlob + ";", SQLQuery, res))
			fprintf (stderr, "Table Optimized\n");
		else
			return;
		strBase = "insert into " + TableBlob + "(" + FieldID + "," + FieldFile + ") values (?,?);";
		fResults = fopen (pfm->szOutFile, "a+");
		fprintf (fResults, "Number,Before,After,Inserted,Time\n");
		lSize = GetFileSize (strDataFileName);
		printf ("File %s size: %ld\n", strDataFileName.c_str(), lSize);
		
		for (n=0 ; n < pfm->count ; n++) {
			cStart = clock();
			nBefore = get_free_space();

			blobFile = new ifstream (strDataFileName, ios::binary | ios::in);
			nLen = blobFile->tellg();
			//fprintf (stderr, "File size: %d\n", nLen);
			
			pData = new char[nLen];
			blobFile->read (pData, nLen);
			strSql = strBase;
			pstmt = con->prepareStatement (strSql);
			pstmt->setInt (1, idStart++);
			pstmt->setBlob (2, blobFile);
			pstmt->executeUpdate();
			delete pstmt;
			delete pData;
			fprintf (stderr, "Inserted %d files\r", n+1);
			delete blobFile;

			nAfter = get_free_space();
			dSeconds = ((double) (clock() - cStart)) / ((double) CLOCKS_PER_SEC);
			fprintf (stderr, "%d,%d,%d,%ldi,%g\r", (n+1), nBefore,nAfter,((n+1) * lSize) / (1024 * 1024), dSeconds);
			fprintf (fResults, "%d,%d,%d,%ld,%g\n", (n+1), nBefore,nAfter,((n+1) * lSize) / (1024 * 1024), dSeconds);
		}
		fprintf (stderr, "\nDone inserting\n");
		for ( ; n >= 0 ; n--) {
			cStart = clock();
			nBefore = get_free_space();
			strSql = "delete from " + TableBlob + " where " + FieldID + "=" + std::to_string(n + 1) + ";";
			RunSql (con, strSql, SQLExecute);
			//stmt = con->createStatement();
			//stmt->executeUpdate(strSql);
			//delete stmt;
			nAfter = get_free_space();
			dSeconds = ((double) (clock() - cStart)) / ((double) CLOCKS_PER_SEC);
			fprintf (stderr, "%d,%d,%d,%ldi,%g\r", (n+1), nBefore,nAfter,((n+1) * lSize) / (1024 * 1024), dSeconds);
			fprintf (fResults, "%d,%d,%d,%ld,%g\n", (n+1), nBefore,nAfter,((n+1) * lSize) / (1024 * 1024), dSeconds);
			fprintf (stderr, "Deleted file #%d\r", n+1);
		}
		fclose (fResults);
	}
	catch (exception &e) {
	//catch (sql::SQLException &e) {
		//fprintf (stderr, "\nSQL Error:\n%s\n\n", strSql.c_str());
		//fprintf (stderr, "what: %s\n", e.what());
		//fprintf (stderr, "code: %d\n", e.getErrorCode());
		//fprintf (stderr, "state: %s\n", e.getSQLState().c_str());
		print_error (e, __FILE__, __FUNCTION__, __LINE__);
	}
}

//-----------------------------------------------------------------------------
bool RunSql (sql::Connection *con, const std::string &strSql, const SqlCommand &cmd, sql::ResultSet *res)
{
	sql::Statement *stmt;
	bool f;

//enum	SqlCommand	{SQLExecute, SQLQuery};
	try {
		stmt = con->createStatement();
		//fprintf (stderr, "Statement Created\n");
		if (cmd == SQLExecute)
			stmt->executeUpdate (strSql);
		else if (cmd == SQLQuery)
			res = stmt->executeQuery (strSql);
		//fprintf (stderr, "Statement executed\n\n");
		delete stmt;
		f = true;
	}
	catch (exception &e) {
		fprintf (stderr, "\nSQL Error:\n%s\n\n", strSql.c_str());
		print_error (e, __FILE__, __FUNCTION__, __LINE__);
		fprintf (stderr, "\n");
		f = false;
	}
	return (f);
}

//-----------------------------------------------------------------------------
long GetFileSize(std::string filename)
{
    struct stat stat_buf;
    int rc = stat(filename.c_str(), &stat_buf);
    return rc == 0 ? stat_buf.st_size : -1;
}

//-----------------------------------------------------------------------------
