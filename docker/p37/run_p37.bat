docker rm -f p37
docker build --rm -f p37.dockerfile -t p37 .
docker run -it -d --name p37 p37
docker exec -it p37 bash