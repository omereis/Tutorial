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
	sleep(1);
    std::cout << "main thread message = " << s << std::endl;
    //t.detach();
	std::thread t2 = move(t);
    t2.join();
    return 0;
}

