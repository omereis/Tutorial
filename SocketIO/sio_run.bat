docker container rm -f sio
docker build --rm -t sio -f sio.dockerfile .
docker run -d -it --name sio -p 4000:4000 -p 8765:8765 sio
docker exec -i -t sio bash

