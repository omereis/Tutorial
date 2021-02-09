#include <iostream>
#include <thread>
#include <string>
#include <mutex>

#include <unistd.h>

using namespace std;
static const int g_nNumThreads = 10;
std::mutex mtx;

void thread_function(int n)
{
	mtx.lock();
    std::cout << std::endl << "thread function i#" << n << endl;
	mtx.unlock();
    //s = "Joe Shmow";
}

int main(int argc, char *argv[])
{
	int n;
	thread aThreads[g_nNumThreads];
	std::mutex m;

	for (n=0 ; n < g_nNumThreads ; n++)
		aThreads[n] = std::thread(thread_function, n+1);
	cout << "Main thread, thread ID: " << std::this_thread::get_id() << endl;
	for (n=0 ; n < g_nNumThreads ; n++)
		aThreads[n].join();
    return 0;
}

