#include <stdio.h>
#include <netdb.h>

#include <string>
#include <iostream>
#include <arpa/inet.h>

using namespace std;


std::string HostToIp(const std::string& host)
{
	hostent* hostname = gethostbyname(host.c_str());
	if(hostname)
		return (std::string(inet_ntoa(**(in_addr**)hostname->h_addr_list)));
    return "";
}

int main (int argc, char *argv[])
{
	string str;
	bool f;
	struct hostent *h;

	printf ("Testing 'gethostbyname'\n");
	do {
		printf ("Please enter host name...");
		getline (cin, str);
		f = (str.size() > 0);
		if (f) {
			cout << "Required host: '" << str << "'\n";
			h = gethostbyname (str.c_str());
			cout << "HostToIP result:\n'" << HostToIp (str) << "'\n";
			f = true; // provide breakpoint
		}
	} while (f);
	cout << "Bye\n";
}

