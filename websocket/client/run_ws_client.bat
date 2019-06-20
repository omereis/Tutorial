docker rm -f wsock_client
docker build --rm -f wsock_client.dockerfile -t wsock_client .
docker run -it -d --name wsock_client -p 5555:5555 wsock_client
rem docker run -it -d --name docker_refsrv
docker exec -it wsock_client bash