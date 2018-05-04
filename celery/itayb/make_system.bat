docker build -t rabbit-mgmt -f Dockerfile.rabbit .
docker build -t redis-server -f Dockerfile.redis .

docker run -it -d -p 6379:6379 --name redis-server redis-server

docker run -it -d rabbit-mgmt -p 15672:15672 -p 5672:5672 --name rabbit-mgmt rabbit-mgmt