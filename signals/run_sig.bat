docker rm -f signals_test
docker build --rm -f signals.dockerfile -t signals_test .
docker run -it -d --name signals_test signals_test
rem docker run -it -d --name docker_refsrv
docker exec -it signals_test bash