#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <dirent.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <stdbool.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/statvfs.h> 

//-----------------------------------------------------------------------------
struct FileMaker {
	int count;
	int size;
	char mult;
	char szOutFile[1024];
};
//-----------------------------------------------------------------------------
off_t get_free_space ();
void print_usage();
bool match(const char *pattern, const char *candidate, int p, int c);
int get_cli_params(struct FileMaker *pfm,  int argc, char *argv[]);
void create_files (struct FileMaker *pfm);
size_t get_size(struct FileMaker *pfm);
//-----------------------------------------------------------------------------
int main (int argc, char *argv[])
{
	struct FileMaker fm;
	int nSize;
	printf ("Creating file with givn size\n");
	nSize = get_cli_params(&fm, argc, argv);
	create_files (&fm);
	exit(0);
}
//-----------------------------------------------------------------------------
int get_cli_params(struct FileMaker *pfm,  int argc, char *argv[])
{
	int n, ok, c;
	char str[1024], mult;
	char *szSize, *szCount, *szMultiplier, cMult, *szOut;
	szSize = szCount = szMultiplier = szOut = NULL;

	pfm->count = 10;
	pfm->size = 5;
	pfm->mult = 'M';
	strcpy (pfm->szOutFile, "usage.csv");

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
				print_usage();
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
	printf("fm.count=%d\n", pfm->count);
	printf("fm.size=%d\n", pfm->size);
	printf("fm.mult=%c\n", pfm->mult);
	printf("Output file: '%s'\n", pfm->szOutFile);
}
//-----------------------------------------------------------------------------
void print_usage()
{
	printf ("Usage:\nmkfiles [-s <size> -c <count> -m <K | M | G>]\n");
}
//-----------------------------------------------------------------------------
static const char *szNameBase = "tstfile";
//-----------------------------------------------------------------------------
#include <dirent.h>
void remove_old ()
{
	DIR *dir;
	struct dirent *item;
	char szPattern[100];
	int n = 0;

	sprintf (szPattern, "%s*", szNameBase);
	dir = opendir (".");
	while ((item = readdir(dir)) != NULL) {
		if (match(szPattern, item->d_name, 0, 0)) {
			remove(item->d_name);
			n++;
			//printf ("  %s\n", item->d_name);
		}
	}
	closedir (dir);
	//printf ("removed %d files\n", n);
}
//-----------------------------------------------------------------------------
bool match(const char *pattern, const char *candidate, int p, int c) {
	if (pattern[p] == '\0') {
		return candidate[c] == '\0';
	}
	else if (pattern[p] == '*') {
		for (; candidate[c] != '\0'; c++) {
			if (match(pattern, candidate, p+1, c))
				return true;
		}
		return match(pattern, candidate, p+1, c);
	}
	else if (pattern[p] != '?' && pattern[p] != candidate[c]) {
		return false;
	}
	else {
		return match(pattern, candidate, p+1, c+1);
	}
}

//-----------------------------------------------------------------------------
void create_files (struct FileMaker *pfm)
{
	FILE *file, *fOut;
	char str[1024], szNameFmt[1000];
	char *ptr =  malloc (pfm->size * 1024);
	int iOuter, nInner, fd, i;
	size_t sizeFile, sTotalSize, stBefore, stAfter;
	struct stat st;

	sprintf (szNameFmt, "%s%%0%dd.dat", szNameBase, pfm->count);
	sizeFile = get_size(pfm);
	printf ("sizeFile = %ld\n", sizeFile);
	if (sizeFile > 0) {
		fOut = fopen (pfm->szOutFile, "w+");
		printf ("results file opened\n");
		fprintf (fOut, "Files,Before,Size,After\n");
		printf ("results file header printed\n");
		printf ("\ncont:%d\n\n", pfm->count);
/*
		for (iOuter=0 ; iOuter < pfm->count ; iOuter++) {
			printf ("ready to old removed\n");
		}
*/
		for (iOuter=0 ; iOuter < pfm->count ; iOuter++) {
			//printf ("ready to old removed\n");
			remove_old ();
			//printf ("old removed\n");
			stBefore = get_free_space();
			sTotalSize = 0;
			for (nInner=0 ; nInner < iOuter ; nInner++) {
				sprintf (str, szNameFmt, nInner);
				file = fopen (str, "w+b");
				for (i=0 ; i < sizeFile ; i++)
					fwrite(ptr, 1, 1024, file);
				fflush(file);
				fclose (file);
				stat (str, &st);
				sTotalSize += st.st_size;
			}
			stAfter = get_free_space();
			if ((iOuter % 5) == 0)
				printf ("Created %3d Files\n", iOuter);
			fprintf (fOut, "%d,%ld,%ld,%ld\n", nInner, stBefore, sTotalSize, stAfter);
		}
		fclose (fOut);
	}
    free(ptr);
	printf ("created %d new files\n", iOuter);
	remove_old ();
	printf ("Removed data files\n");
}
//-----------------------------------------------------------------------------
off_t get_free_space ()
{
	struct statvfs vfs;
	statvfs (".", &vfs); 
	return (vfs.f_bfree);
}
//-----------------------------------------------------------------------------
size_t SizeFromMult (char cMult)
{
	size_t s = 1;
	char (c) = tolower(cMult);
	
	if (c == 'k') // Kilo
		s = 1;
	else if (c == 'm') // Mega
		s = 1024;
	else if (c == 'g') // giga
		s = 1024 * 1024;
	else
		s = 0;
	return (s);
}
//-----------------------------------------------------------------------------
size_t get_size(struct FileMaker *pfm)
{
	size_t sMult = SizeFromMult (pfm->mult);
	
	return (sMult * pfm->size);
}
//-----------------------------------------------------------------------------
