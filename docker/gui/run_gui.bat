docker rm -f rp_gui
docker build --rm -f rp_gui.dockerfile -t rp_gui .
docker run -it -d -h rp_gui --name rp_gui -p 5005:5005 rp_gui
docker exec -it rp_gui bash