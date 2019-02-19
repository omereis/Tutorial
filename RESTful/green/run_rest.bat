docker rm -f green_rest
docker build --rm -f green_rest.dockerfile -t green_rest .
docker run -it -d --name green_rest -p 5000:5000 green_rest
rem docker run -it -d --name docker_refsrv
docker exec -it green_rest bash