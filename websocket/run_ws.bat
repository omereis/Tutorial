docker rm -f wsock_server
docker build --rm -f wsock.dockerfile -t wsock_server .
docker run -it -d --name wsock_server -p 5678:5678 -p 5000:5000 wsock_server
rem docker run -it -d --name docker_refsrv
docker exec -it wsock_server bash