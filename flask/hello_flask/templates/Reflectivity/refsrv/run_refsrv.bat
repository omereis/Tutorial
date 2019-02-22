docker rm -f docker_refsrv
docker build --rm -f refsrv.dockerfile -t docker_refsrv .
docker run -it -d --name docker_refsrv -p 5000:5000 docker_refsrv
rem docker run -it -d --name docker_refsrv
docker exec -it docker_refsrv bash