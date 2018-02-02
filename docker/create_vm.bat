
docker-machine rm -f $(docker-machine ls -q)

docker-machine create -d hyperv --hyperv-virtual-switch "DockerVirtualSwitch" myvm1
docker-machine create -d hyperv --hyperv-virtual-switch "DockerVirtualSwitch" myvm2


docker-machine ls
