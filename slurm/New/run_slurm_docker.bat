docker build -t slurm_docker .
rem docker run -d --name slurm_mngr --link bumps_gui_slurm slurm_docker
docker run -d --name slurm_mngr slurm_docker:1
docker exec -i -t slurm_mngr "bash"

rem Source: https://hub.docker.com/r/agaveapi/slurm/
echo Source: https://hub.docker.com/r/agaveapi/slurm/

rem docker run -h docker.example.com -p 10022:22 --rm -d --name slurm agaveapi/slurm
rem docker run -h docker.example.com -p 10022:22 --rm -d --name slurm omereis/slurm:man_pages
rem docker run -h docker.example.com -p 10022:22 --rm -d --link bumps_gui_slurm  --name slurm omereis/slurm:man_pages
docker run -t -d   --name slurm_mngr -h s_manager slurm_docker
docker exec -i -t slurm_mngr "bash"




docker run -t -d  --name slurm_mngr --hostname slurm_mngr slurm_docker
docker exec -i -t slurm_mngr "bash"
docker exec -i -t slurm bash