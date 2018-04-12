docker build -f Dockerfile.dd.base -t slurm_base .
docker pull datadrivenhpc/slurmctld
docker container rm -f slurm_ctld
docker run -d --name slurm_base -e "SLURM_CLUSTER_NAME=ddhpc" -e "SLURM_CONTROL_MACHINE=slurmctld" -e "SLURM_NODE_NAMES=slurmd_1" -h slurmctld slurm_base

 
