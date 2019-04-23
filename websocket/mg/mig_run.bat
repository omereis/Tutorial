docker container rm -f ws_mig
docker build --rm -t ws_mig -f ws_mig.dockerfile .
docker run -d -it --name ws_mig -p 5000:5000 -p 5678:5678 ws_mig
docker exec -i -t ws_mig bash

