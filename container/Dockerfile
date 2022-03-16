# Version: 0.0.1
FROM archlinux
RUN chmod -R 755 /etc 
RUN pacman -Syu --noconfirm
RUN pacman -S binutils make gcc pkg-config fakeroot git sudo --noconfirm
# 将创建一个non-root用户
ENV NEWUSER soeo
COPY setup.sh /${NEWUSER}/
COPY worker.sh /${NEWUSER}/
RUN /bin/bash /${NEWUSER}/setup.sh 