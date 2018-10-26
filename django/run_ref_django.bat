docker container rm -f django_ref_oe
docker build --rm -t django_ref_oe -f django_ref.docker .
docker run -d -it -p 8000:8000 -p 6379:6379 -h django_ref_oe --name django_ref_oe django_ref_oe
docker exec -i -t django_ref_oe bash
