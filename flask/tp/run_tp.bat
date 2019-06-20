docker rm -f tut_pt
docker build --rm -f tut_pt.dockerfile -t tut_pt .
docker run -it -d --name tut_pt -p 6000:6000 tut_pt
rem docker run -it -d --name docker_refsrv
docker exec -it tut_pt bash