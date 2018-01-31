
docker-machine rm -f $(docker-machine ls -q)

docker-machine create -d hyperv --hyperv-virtual-switch "DockerGSSwitch" myvm1
docker-machine create -d hyperv --hyperv-virtual-switch "DockerGSSwitch" myvm2

