docker container rm -f django_oe
docker build --rm -t django_oe -f django.docker .
docker run -d -it -p 5000:5000 -h django_oe --name django_oe django_oe
docker exec -i -t django_oe bash
