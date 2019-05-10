docker rm -f refl_oe
docker build --rm -f refl.dockerfile -t refl_oe .
docker run -it -d --name refl_oe refl_oe
docker exec -it refl_oe bash