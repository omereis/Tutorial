docker rm -f wsock
docker build --rm -f wsock.dockerfile -t wsock .
docker run -it -d --name wsock wsock
rem docker run -it -d --name docker_refsrv
docker exec -it wsock bash