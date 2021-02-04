#include <iostream>
#include <thread>
#include <string>

#include <unistd.h>

void thread_function(std::string &s)
{
    std::cout << std::endl << "thread function ";
    std::cout << "message is = " << s << std::endl;
    s = "Joe Shmow";
}

int main()
{
    std::string s = "Joe Smow";
	std::thread t(&thread_function, std::ref(s));
	//std::thread t(&thread_function, std::move(s));
	usleep(1);
    std::cout << "main thread message = " << s << std::endl;
    //t.detach();
    t.join();
    return 0;
}

