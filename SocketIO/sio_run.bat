docker container rm -f sio
docker build --rm -t sio5 -f sio5.dockerfile .
docker run -d -it --name sio5 -p 5000:5000 sio5
docker exec -i -t sio bash

