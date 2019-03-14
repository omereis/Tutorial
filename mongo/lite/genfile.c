#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <ctype.h>
#include "fm.h"
//-----------------------------------------------------------------------------
size_t get_file_size(struct FileMaker *pfm);
size_t size_from_mult (char cMult);
//-----------------------------------------------------------------------------
static const int s_nDataBufSize = 1024;
static const char *szNameBase = "tstfile";
//-----------------------------------------------------------------------------
bool generate_file (char szName[], struct FileMaker *pfm)
{
	size_t sizeFile;
	FILE *fOut;
	int n, i;
	char *pData;

	pData = (char*) malloc (s_nDataBufSize);
	sizeFile = get_file_size(pfm);
	fOut = fopen (pfm->szOutFile, "w+"); 
	for (n=0 ; n < pfm->count ; n++) {
		fOut = fopen (szName, "w+b");
		for (i=0 ; i < sizeFile ; i++)
			fwrite(pData, 1, s_nDataBufSize, fOut);
		fflush(fOut);
		fclose (fOut);
	}
	free (pData);
}

//-----------------------------------------------------------------------------
size_t get_file_size(struct FileMaker *pfm)
{
	size_t sMult = size_from_mult (pfm->mult);
	
	return (sMult * pfm->size);
} 
//-----------------------------------------------------------------------------
size_t size_from_mult (char cMult)
{
	size_t s = 1;
	char c;

	c = tolower(cMult);
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
