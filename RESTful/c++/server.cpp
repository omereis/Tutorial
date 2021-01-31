// Server side C/C++ program to demonstrate Socket programming 
#include <unistd.h> 
#include <stdio.h> 
#include <sys/socket.h> 
#include <stdlib.h> 
#include <netinet/in.h> 
#include <string.h> 

#include "comm.h"

int GetCliPort (int argc, char const *argv[])
{
	int nPort;
	
	if (argc > 1)
		nPort = atoi (argv[1]);
	else
		nPort = DEFAULT_PORT;
	return (nPort);
}

int OpenSocket (int nPort)
{
	struct sockaddr_in address; 
	int opt = 1; 
	int addrlen = sizeof(address); 
	int nServerFd;

	// Creating socket file descriptor 
	if ((nServerFd = socket(AF_INET, SOCK_STREAM, 0)) == 0) { 
		perror("socket failed"); 
		exit(EXIT_FAILURE); 
	} 

	// Forcefully attaching socket to the port
	if (setsockopt(nServerFd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt)))  { 
		perror("setsockopt"); 
		exit(EXIT_FAILURE); 
	} 
	address.sin_family = AF_INET; 
	address.sin_addr.s_addr = INADDR_ANY; 
	address.sin_port = htons(nPort); 

	// Forcefully attaching socket to the port
	if (bind(nServerFd, (struct sockaddr *)&address, sizeof(address)) < 0) { 
		perror("bind failed"); 
		exit(EXIT_FAILURE); 
	} 
	if (listen(nServerFd, 3) < 0)  { 
		perror("listen"); 
		exit(EXIT_FAILURE); 
	}
	return (nServerFd);
}

int main(int argc, char const *argv[]) 
{ 
	int server_fd, new_socket, valread;
	int nNewSocket, nServerFd;
	struct sockaddr_in address; 
	int opt = 1; 
	int addrlen = sizeof(address); 
	char buffer[1024] = {0}; 
	const char *hello = "Hello from server"; 
	
	int nPort = GetCliPort (argc, argv);

	nServerFd = OpenSocket (nPort);
	if ((nNewSocket = accept(nServerFd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
		perror("accept"); 
		exit(EXIT_FAILURE); 
	} 
	valread = read(new_socket , buffer, 1024); 
	printf("%s\n",buffer ); 
	send(new_socket , hello , strlen(hello) , 0 ); 
	printf("Hello message sent\n"); 
	return 0; 
} 
