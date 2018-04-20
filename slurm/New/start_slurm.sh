#!/bin/bash
echo "Starting munged..."
chown munge:munge /etc/munge/munge.key
service munge start
echo "Updating scontrol..."
IP=`ifconfig eth0 | awk '/inet addr/{print substr($2,6)}'`
/usr/bin/scontrol update nodename=$HOSTNAME nodeaddr=$IP nodehostname=$HOSTNAME
echo "Starting slurmd..."
exec /usr/sbin/slurmd -D
