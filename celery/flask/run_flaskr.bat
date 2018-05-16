docker container rm -f oe_flaskr
docker build --rm -t oe_flaskr -f Dockerfile_flaskr .
docker run --name oe_flaskr -dit -p 5000:5000 oe_flaskr
docker exec -it oe_flaskr bash
