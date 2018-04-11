docker build -f Dockerfile.dd.base -t slurm_ctld .
docker pull datadrivenhpc/slurmctld
docker container rm -f ctld
docker run -d --name ctld -e "SLURM_CLUSTER_NAME=ddhpc" -e "SLURM_CONTROL_MACHINE=slurmctld" -e "SLURM_NODE_NAMES=slurmd_1" -h slurmctld datadrivenhpc/slurmctld

 
