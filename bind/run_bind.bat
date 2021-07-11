docker rm -f p_bind
docker build --rm -f p_bind.dockerfile -t p_bind .
docker run -it -d -h p_bind --name p_bind p_bind
rem docker run -it -d --name docker_refsrv
docker exec -it p_bind bash
