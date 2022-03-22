docker rm -f open_cv
docker build --rm -f open_cv.dockerfile -t open_cv .

docker run -it -d -h open_cv --name open_cv -p 5005:5005 open_cv
rem docker run -it -d --name docker_refsrv
docker exec -it open_cv bash
