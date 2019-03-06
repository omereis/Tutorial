docker rm -f mongo_docker
docker build --rm -f mongo.dockerfile -t mongo_docker .
docker run -it -d --name mongo_docker  mongo_docker
rem docker run -it -d --name docker_refsrv
docker exec -it mongo_docker bash