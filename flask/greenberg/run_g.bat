docker rm -f docker_green
docker build --rm -f green.dockerfile -t docker_green .
docker run -it -d --name docker_green -p 5000:5000 docker_green
rem docker run -it -d --name docker_refsrv
docker exec -it docker_green bash