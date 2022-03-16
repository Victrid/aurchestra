#!/bin/bash 
# Global variables: 
NEWUSER="soeo"
WORKDIR="/$NEWUSER"
# add a new non-root user, in order to run makepkg
useradd -m -p $(openssl passwd -1 $NEWUSER) $NEWUSER
echo "$NEWUSER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
cd $WORKDIR || exit
chmod -R 777 ./
su $NEWUSER<<'EOF'
set -e
/bin/bash "/${NEWUSER}/worker.sh"
exit
EOF