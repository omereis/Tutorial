#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include <ctype.h>
#include <dir.h>
#include <dirent.h>
#include <io.h>
#include <fcntl.h>
#include <sys/stat.h>

//-----------------------------------------------------------------------------
int get_cli_size(struct FileMaker *pfm,  int argc, char *argv[]);
void create_files (struct FileMaker *pfm);
void remove_old ();
//-----------------------------------------------------------------------------
struct FileMaker {
	int count;
	int size;
	char mult;
};
//-----------------------------------------------------------------------------
int main (int argc, char *argv[])
{
	struct FileMaker fm;
	int nSize;
	printf ("Creating file with givn size\n");
	nSize = get_cli_size(&fm, argc, argv);
	create_files (&fm);
	printf ("Hit key to continue\n");
	getch ();
	exit(0);
}
//-----------------------------------------------------------------------------
int get_cli_size(struct FileMaker *pfm,  int argc, char *argv[])
{
	int n, ok;
	char str[1024], mult;
#ifdef   _DEBUG
	printf("Debug mode\n");
	pfm->count = 10;
	pfm->size = 5;
	pfm->mult = 'M';
#else
	if (argc > 1) {
		pfm->count = atoi (argv[1]);
	}
	if (argc > 2) {
		pfm->size = atoi (argv[2]);
	}
	ok = 0;
	if (argc >= 3) {
		if (strlen(argv[3]) == 1) {
			mult = tolower(argv[3][0]);
			if ((mult == 'k') || (mult == 'm') || (mult == 'g')) {
				ok = 1;
			}
		}
//		pfm->size = atoi (argv[2]);
	}
	if (ok)
		pfm->mult = mult;
	else
		pfm->mult = 'm';
	if (pfm->count == 0)
		pfm->count = 1;
	if (pfm->size == 0)
		pfm->size = 1;
#endif
/*
*/
	printf("fm.count=%d\n", pfm->count);
	printf("fm.size=%d\n", pfm->size);
	printf("fm.mult=%c\n", pfm->mult);
}
//-----------------------------------------------------------------------------
static const char *szNameBase = "tstfile";
//-----------------------------------------------------------------------------
void remove_old ()
{
	struct ffblk ffblk;
	char szName[1024];
	int done, n=0, rm, ch;

	sprintf (szName, "%s*.*", szNameBase);
	done = findfirst (szName, &ffblk, FA_HIDDEN | FA_SYSTEM);
	while (done == 0) {
		n++;
		ch = chmod (ffblk.ff_name, _S_IREAD | _S_IWRITE);
		if (ch < 0) {
			sprintf (szName, "Error: %d\n", errno);
		}
		rm = remove (ffblk.ff_name);
		if (rm < 0) {
			sprintf (szName, "Error: %d\n", errno);
		}
		done = findnext (&ffblk);
	}
	printf ("deleted %d old files\n", n);
//	getch ();
}
//-----------------------------------------------------------------------------
void create_files (struct FileMaker *pfm)
{
	FILE* file;
	char str[1024], szNameFmt[1000];
	char *ptr =  malloc (1024);
	int n, fd, i;
	size_t sFile;

	for (n=0 ; n < 1024 ; n++)
		ptr[n] = n + 1;
	remove_old ();
	sprintf (szNameFmt, "%s%%0%dd.dat", szNameBase, pfm->count);

	for (n=0 ; n < pfm->count ; n++) {
		sprintf (str, szNameFmt, n);
		file = fopen (str, "w+b");
		//fwrite(ptr, 1, 1024, file);
		for (i=0 ; i < 1024; i++) {
			fwrite(ptr, 1, 1024, file);
		}
//		fwrite(ptr, 1, 1024, file);
		fflush(file);
		fclose (file);
/*
		fd = open (str, O_CREAT| O_TRUNC | O_BINARY);
		if (fd) {
			write (fd, str, 1024);//sizeof(str));
		}
		close(fd);
*/
	}
    free(ptr);
	printf ("created %d new files\n", n);
}
//-----------------------------------------------------------------------------
int match(const char *pattern, const char *candidate, int p, int c) {
	if (pattern[p] == '\0') {
		return candidate[c] == '\0';
	}
	else if (pattern[p] == '*') {
		for (; candidate[c] != '\0'; c++) {
			if (match(pattern, candidate, p+1, c))
				return 1;
		}
		return match(pattern, candidate, p+1, c);
	}
	else if (pattern[p] != '?' && pattern[p] != candidate[c]) {
		return 0;
	}
	else {
		return match(pattern, candidate, p+1, c+1);
	}
}
//-----------------------------------------------------------------------------

