docker rm -f oe_alchemy
docker build --rm -f sa.dockerfile -t oe_alchemy .
docker run -it -d --name oe_alchemy oe_alchemy
docker exec -it oe_alchemy bash