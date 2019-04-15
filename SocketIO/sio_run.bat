docker container rm -f sio
docker build --rm -t sio -f sio.dockerfile .
docker run -d -it --name sio -p 4000:4000 sio
docker exec -i -t sio bash

rem docker run --link redis-server --link rabbit-server -e "BACKEND_SERVER=ncnr-r9nano" -e "BROKER_SERVER=ncnr-r9nano" -p 5000:5000 -h bumps_gui --name bumps_gui bumps_gui
