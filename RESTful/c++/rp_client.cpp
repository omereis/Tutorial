// Client side C/C++ program to demonstrate Socket programming 
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include <netdb.h>

#include <string>
#include "comm.h"

using namespace std;

//-----------------------------------------------------------------------------
std::string FindHostIPByName (const std::string &strHostName)
{
	hostent* hostname = gethostbyname(strHostName.c_str());
	std::string strAddress;

	if(hostname)
		strAddress = std::string(inet_ntoa(**(in_addr**)hostname->h_addr_list));
	return (strAddress);
}
//-----------------------------------------------------------------------------
int SafeReadCliPort (const char *szPort)
{
	int nPort;

	try {
		nPort = atoi(szPort);
	}
	catch (const std::exception &e){
		nPort = DEFAULT_PORT;
	}
	return (nPort);
}
//-----------------------------------------------------------------------------
bool GetCliAddressPort (int argc, char const *argv[], int &nPort, string &strAddress, string &strErr)
{
	bool f;
		
	try {
		nPort = DEFAULT_PORT;
		strAddress = DEFAULT_ADDRESS;
		if (argc > 1)
			nPort = SafeReadCliPort (argv[1]);
		if (argc > 2)
			strAddress = FindHostIPByName (argv[2]);
			//strAddress = argv[2];
		f = true;
	}
	catch (exception &e){
		nPort = DEFAULT_PORT;
		strAddress = DEFAULT_ADDRESS;
		strErr = e.what();
		f = false;
	}
	return (f);
}
//-----------------------------------------------------------------------------
int main(int argc, char const *argv[])
{
	int sock = 0, valread;
	struct sockaddr_in serv_addr;
	const char *hello = "Hello from client";
	char buffer[1024] = {0};
	int nPort;
	string strAddress, strErr;

	if (GetCliAddressPort (argc, argv, nPort, strAddress, strErr)) {
		printf ("Conecting to server %s:%d\n", strAddress.c_str(), nPort);
		if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
			printf("\n Socket creation error \n");
			return -1;
		}
		serv_addr.sin_family = AF_INET;
		serv_addr.sin_port = htons(nPort);
	// Convert IPv4 and IPv6 addresses from text to binary form 
		if(inet_pton(AF_INET, strAddress.c_str(), &serv_addr.sin_addr) <=0 ) {
		//if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <=0 ) {
			printf("\nInvalid address/ Address not supported \n");
			return -1;
		}
		if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) { 
			printf("\nConnection Failed \n");
			return -1;
		}
		send(sock , hello , strlen(hello) , 0 );
		printf("Hello message sent\n");
		valread = read( sock , buffer, 1024);
		printf("%s\n",buffer );
	}
	return 0;
} 
