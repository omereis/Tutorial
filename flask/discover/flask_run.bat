docker container rm -f flask_dev
docker build --rm -t flask_dev -f Dockerfile_flask.oe .
# docker run -d -it -p 5000:5000 -h flask_dev --name flask_dev --env BROKER_SERVER=rabbit-server --env BACKEND_SERVER=redis-server flask_dev
docker run -d -it -p 5000:5000 -h flask_dev --name flask_dev flask_dev
docker exec -it flask_dev bash