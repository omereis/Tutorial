rem Source: https://hub.docker.com/r/agaveapi/slurm/
echo Source: https://hub.docker.com/r/agaveapi/slurm/

docker run -h docker.example.com -p 10022:22 --rm -d --name slurm agaveapi/slurm

docker exec -i -t slurm "bash"

