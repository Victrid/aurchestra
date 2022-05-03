#!/bin/bash
# prepare the environment before chroot
mkdir /run/shm
systemd-machine-id-setup
extra-x86_64-build -c
cd /sys/fs/cgroup/systemd/docker || echo  "1" >> $ERR_FILE
tempFileDir=$(find ./ -name "payload" | head -n 1)
parentFileDir=${tempFileDir%/*}
mkdir -p "${parentFileDir}/docker/${parentFileDir##*/}/payload"
cp -rf "${tempFileDir}" "${parentFileDir}/docker/${parentFileDir##*/}/payload"  #字符串操作
# 是因为chroot时报错: Failed to chown() cgroup /sys/fs/cgroup/systemd/docker/417bd4c05a51fbc44d925315771896c86a3276fa9e26c32a3acf643db2ac2ef7/docker/417bd4c05a51fbc44d925315771896c86a3276fa9e26c32a3acf643db2ac2ef7/payload: No such file or directory
pip install -r /soeo/pythonrequirements.txt
python /soeo/script.py