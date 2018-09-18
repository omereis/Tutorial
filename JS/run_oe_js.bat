docker rm -f oe_js
docker build --rm -f js_dockerfile.txt -t oe_js .
docker run -it -d --name oe_js oe_js
docker exec -it oe_js bash
