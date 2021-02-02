#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <string>

#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <unistd.h>

#include <string>
#include <iostream>
#include <thread>
#include <mutex>


#include <netdb.h>
#include <stdio.h>

//using namespace std::chrono_literals;
//using namespace std::literals::chrono_literals;
std::string g_strAddress;

int f()
{
    //std::this_thread::sleep_for(10s); //change value here to less than 1 second to see Success
    std::this_thread::sleep_for(std::chrono::milliseconds(10)); //change value here to less than 1 second to see Success
    return 1;
}

std::string FindIP (const std::string &strHostName)
{
	std::string strIp;

	hostent* hostname = gethostbyname(strHostName.c_str());
	if (hostname != 0)
		g_strAddress = std::string(inet_ntoa(**(in_addr**)hostname->h_addr_list));
	strIp = g_strAddress;
	return (strIp);
}

int f_wrapper(const std::string &strHostName)
{
    std::mutex m;
    std::condition_variable cv;
    int retValue;

    std::thread t([&cv, &retValue, &strHostName]() 
    {
		std::string str;
		g_strAddress = "";
		fprintf (stderr, "started thread\n");
		str = FindIP (strHostName);
		//f();
		fprintf (stderr, "IP for host '%s' is '%s'\n", strHostName.c_str(), str.c_str());
        retValue = f();
        cv.notify_one();
		fprintf (stderr, "thread ended\n");
    });

    t.detach();

    {
        std::unique_lock<std::mutex> l(m);
        if(cv.wait_for(l, std::chrono::seconds(3)) == std::cv_status::timeout) {
            throw std::runtime_error("Timeout");
			fprintf (stderr, "Timeout\n");
		}
    }

    return retValue;    
}

int main(int argc, char *argv[])
{
    bool timedout = false;
	std::string strHostName;
	
	if (argc > 1)
		strHostName = std::string (argv[1]);
	else
		strHostName = std::string("www.nist.gov");
    try {
        f_wrapper(strHostName);
    }
    catch(std::runtime_error& e) {
        std::cout << e.what() << std::endl;
        timedout = true;
    }

    if(!timedout)
        std::cout << "Success" << std::endl;

    return 0;
}
