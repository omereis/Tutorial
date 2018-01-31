docker swarm init
docker run -p 80:80 omereis/docker_start:step_02
docker stack deploy -c docker-compose.yml getstartedlab
docker swarm leave --force

curl --raw -L -X DELETE  --user omereis:1q2w3e4r  -H "Accept: application/json"  -H "Content-Type: application/json" --post301 https://hub.docker.com/r/omereis/docker_start/