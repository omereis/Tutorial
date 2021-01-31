CPP = g++
CFLAGS = -g -c -ljsoncpp

SERVER = server
CLIENT = client

%.o : %.cpp
	$(CPP) -c $(CFLAGS) $< -o $@

SERVER: $(SERVER).o
	$(CPP) -$(CFLAGS) -c $(SERVER).cpp

CLIENT: $(CLIENT).o
	$(CPP) -$(CFLAGS) -c $(CLIENT).cpp

clean:
	rm *.o client server
