#include "fm.h"
//-----------------------------------------------------------------------------
size_t get_file_size(struct FileMaker *pfm);
size_t size_from_mult (char cMult);
//-----------------------------------------------------------------------------
bool generate_file (char []szName, struct FileMaker *pfm)
{
	size_t sizeFile;

	sizeFile = get_file_size(pfm);
		fOut = fopen (pfm->szOutFile, "w+"); 
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
