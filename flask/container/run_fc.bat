docker container rm -f docker_flask
docker build --rm -f flask_container.dockerfile -t docker_flask .
docker run -it -d --name docker_flask -p 6000:6000 -p 4567:4567 docker_flask
docker exec -i -t docker_flask bash
rem docker exec -i -t bumps_redis "redis-cli"
