docker container rm -f $(docker container ls -aq)
docker rmi -f $(docker images -q)
docker build -t docker_start .
docker tag docker_start omereis/docker_start:latest
docker push omereis/docker_start:latest