#include <stdio.h>
#include <sqlite3.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include "db_tst.h"

//-----------------------------------------------------------------------------
//using namespace std;
//-----------------------------------------------------------------------------
/*
// prototypes
bool open_database (char *szDB, sqlite3 **db, int argc, char *argv[]);
void create_blobs_table(sqlite3* db);
string get_blobs_table_create_sql ();
bool blob_table_exists(sqlite3 *db);
*/

//-----------------------------------------------------------------------------
int main(int argc, char* argv[])
{
    sqlite3 *db;
    char *zErrMsg = 0;
    char szDB[] = "db_blobs.sqlite";
    int rc;

    if (open_database (szDB, &db, argc, argv)) {
        printf ("Database opened\n");
        create_blobs_table(db);
        sqlite3_close(db);
        printf ("Database Closed\n");
    }
}

//-----------------------------------------------------------------------------
bool open_database (char *szDB, sqlite3 **db, int argc, char *argv[])
{
    int rc = sqlite3_open(szDB, db);
    if (rc) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(*db));
        return(0);
    }
    else {
        printf ("Database opened\n");
    }
    return (rc == 0);
}

static bool s_fBlobTableExists = false;
static const string strBlobTable = "t_blob";

//static const string strSqlCreateTable =
static const char szSqlCreateTable[] =
	"CREATE TABLE `%s` ("
	//"CREATE TABLE `t_blob` ("
		"`id`	INTEGER NOT NULL,"
		"`file_name`	TEXT,"
		"`file`	BLOB,"
		"PRIMARY KEY(`id`)"
	");"
	;

//-----------------------------------------------------------------------------
static int callback(void *data, int argc, char **argv, char **azColName){
   int i;
   fprintf(stderr, "%s: ", (const char*)data);
   
   for(i = 0; i<argc; i++){
      printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
   }
   
   printf("\n");
   return 0;
}

/*
//-----------------------------------------------------------------------------
static int callback(void *NotUsed, int argc, char **argv, char **azColName)
{
	int i;

	for(i = 0; i<argc; i++)
		printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
	printf("\n");
	return 0;
}
*/

//-----------------------------------------------------------------------------
void create_blobs_table (sqlite3 *db)
{
	char *zErrMsg = 0;

	if (!blob_table_exists(db)) {
		string strSqlCreateTable = get_blobs_table_create_sql ();
		int rc = sqlite3_exec(db, strSqlCreateTable.c_str(), callback, 0, &zErrMsg);
		if (rc != SQLITE_OK ){
			fprintf(stderr, "SQL error: %s\n", zErrMsg);
			sqlite3_free(zErrMsg);
		}
		else
			printf("BLOB Table Created\n");
   }
}

//-----------------------------------------------------------------------------
static int cbCreate(void *NotUsed, int argc, char **argv, char **azColName) {
	int i;
	for(i = 0; i<argc; i++) {
		printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
	}
	printf("\n");
	return 0;
}

//-----------------------------------------------------------------------------
bool blob_table_exists(sqlite3 *db)
{
	char *zErrMsg = 0;

    string strSql = "SELECT name FROM sqlite_master WHERE type='table' AND name='" + strBlobTable + "';";
    int rc = sqlite3_exec(db, strSql.c_str(), cbCreate, 0, &zErrMsg);
	if (rc != SQLITE_OK) {
		fprintf(stderr, "SQL error: %s\n", zErrMsg);
		sqlite3_free(db);
	} else {
		fprintf(stdout, "Table created successfully\n");
	}
	exit(0);
	return (false);
}

//-----------------------------------------------------------------------------
string get_blobs_table_create_sql ()
{
	char *szBuf;
	string str;

	szBuf = new char [strlen(szSqlCreateTable) + strBlobTable.length()];
	sprintf (szBuf, szSqlCreateTable, strBlobTable.c_str());
	str = string(szBuf);
	delete[] szBuf;
	//printf ("SQL statement:\n%s\n", str.c_str());
	return (str);
	//exit(0);
}

