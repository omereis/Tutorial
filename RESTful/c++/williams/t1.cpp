#include <thread>
#include <iostream>

using namespace std;

class background_task
{
public:
	void operator()() const
	{
		cout << "Class operator() method" << endl;
		//do_something();
		//do_something_else();
	}
};

int main (int argc, char *argv[])
{
	background_task f;
	std::thread my_thread(f);
	f.join();
	return (0);
}

