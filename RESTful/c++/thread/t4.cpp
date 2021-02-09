#include <iostream>
#include <thread>
#include <string>

#include <unistd.h>

using namespace std;

void thread_function(std::string &s)
{
    std::cout << std::endl << "thread function ";
    std::cout << "message is = " << s << std::endl;
    s = "Joe Shmow";
}

int main()
{
	std::cout << "Number of threads = " <<  std::thread::hardware_concurrency() << std::endl;
    std::string s = "Joe Smow";
	std::thread t(&thread_function, std::ref(s));
	sleep(1);
    std::cout << "main thread message = " << s << std::endl;
    //t.detach();
	std::thread t2 = move(t);
	cout << "Main thread, thread ID: " << std::this_thread::get_id() << endl;
	cout << "2nd thread, thread ID: " << t2.get_id() << endl;
    t2.join();
    return 0;
}

