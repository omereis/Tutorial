rem Source: https://hub.docker.com/r/agaveapi/slurm/
echo Source: https://hub.docker.com/r/agaveapi/slurm/

rem docker run -h docker.example.com -p 10022:22 --rm -d --name slurm agaveapi/slurm
docker run -h docker.example.com -p 10022:22 --rm -d --name slurm omereis/slurm:man_pages
docker run -h docker.example.com -p 10022:22 --rm -d --link bumps_gui_slurm  --name slurm omereis/slurm:man_pages
docker exec -i -t slurm "bash"



