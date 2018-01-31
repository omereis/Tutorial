docker stack deploy -c docker-compose.yml my_docker_stack
rem show container in a stack
docker service ps my_docker_stack_web
docker-machine create -d hyperv --hyperv-virtual-switch "docker_swarm_tutorial" myvm1

docker-machine.exe --native-ssh ssh myvm1 "docker swarm init --advertise-addr 129.6.1
22.63:2367"

docker-machine.exe ssh myvm2 "docker swarm join --token SWMTKN-1-SWMTKN-1-4o8klymriy1yz07k4vn0an1prpd8yw8zgvruiz2zd1io4crgoj-4hkib4333j57l9f6x1dziap0v 129.6.122.28:2377"

docker-machine create -d hyperv --hyperv-virtual-switch "DockerGS" myvm1
docker-machine create -d hyperv --hyperv-virtual-switch "DockerGSSwitch" myvm1
docker-machine create -d hyperv --hyperv-virtual-switch "DockerGSSwitch" myvm2

