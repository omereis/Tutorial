#include <stdio.h>
#include <sqlite3.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#include "db_tst.h"
#include "get_cli.h"
#include "fm.h"

//-----------------------------------------------------------------------------
void print_usage(char *szAppName);
//void print_params(struct FileMaker *pfm);

//-----------------------------------------------------------------------------
int get_cli_params(struct FileMaker *pfm,  int argc, char *argv[], char szAppName[])
{
	int n, ok, c;
	char str[1024], mult;
	char *szSize, *szCount, *szMultiplier, cMult, *szOut;
	szSize = szCount = szMultiplier = szOut = NULL;

	pfm->count = 10;
	pfm->size = 5;
	pfm->mult = 'M';
	strcpy (pfm->szOutFile, "usage.csv");

	//print_params(pfm);
	while ((c = getopt (argc, argv, "Hhs:c:m:o:")) != -1) {
		switch (c) {
			case 's':
			case 'S':
				szSize = optarg;
				break;
			case 'c':
			case 'C':
				szCount = optarg;
				break;
			case 'm':
				szMultiplier = optarg;
				break;
			case 'o':
				strcpy (pfm->szOutFile, optarg);
				break;
			case 'h':
			case 'H':
				print_usage(szAppName);
				exit(0);
			default:
				fprintf (stderr, "Unknown option `-%c'.\n", optopt);
				fprintf (stderr, "proceeding with defaults\n");
				break;
		}
	}
	if (szSize)
		pfm->size = atoi(szSize);
	if (szCount)
		pfm->count = atoi(szCount);
	if (szMultiplier) {
		if (strlen(szMultiplier) == 1) {
			if (tolower(szMultiplier[0]) == 'm')
				pfm->mult = 'M';
			else if (tolower(szMultiplier[0]) == 'g')
				pfm->mult = 'G';
			else
				pfm->mult = 'K';
		}
	}
/*
	print_params(pfm);
	printf("fm.count=%d\n", pfm->count);
	printf("fm.size=%d\n", pfm->size);
	printf("fm.mult=%c\n", pfm->mult);
	printf("Output file: '%s'\n", pfm->szOutFile);
*/
} 

//-----------------------------------------------------------------------------
void print_usage(char *szAppName)
{
	printf ("Usage:\%s [-s <size> -c <count> -m <K | M | G>]\n", szAppName);
}
//-----------------------------------------------------------------------------

void print_params(struct FileMaker *pfm)
{
	printf("fm.count=%d\n", pfm->count);
	printf("fm.size=%d\n", pfm->size);
	printf("fm.mult=%c\n", pfm->mult);
	printf("Output file: '%s'\n", pfm->szOutFile);
}
