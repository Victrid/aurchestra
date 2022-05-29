#!/bin/bash
# prepare the environment before chroot
# mkdir /run/shm
systemd-machine-id-setup
# extra-x86_64-build -c >/dev/null 2>&1
# echo "Preparing worker environment..."
# cd /sys/fs/cgroup/systemd/docker || exit
# tempFileDir=$(find ./ -name "payload" | head -n 1)
# parentFileDir=${tempFileDir%/*}
# mkdir -p "${parentFileDir}/docker/${parentFileDir##*/}/payload"
# cp -rf "${tempFileDir}" "${parentFileDir}/docker/${parentFileDir##*/}/payload" >/dev/null 2>&1   #字符串操作
# 是因为chroot时报错: Failed to chown() cgroup /sys/fs/cgroup/systemd/docker/417bd4c05a51fbc44d925315771896c86a3276fa9e26c32a3acf643db2ac2ef7/docker/417bd4c05a51fbc44d925315771896c86a3276fa9e26c32a3acf643db2ac2ef7/payload: No such file or directory

# Add nobody to sudo
echo "nobody ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

echo "Worker is ready now. "
python /container/script.py
