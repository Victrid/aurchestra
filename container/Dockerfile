FROM archlinux
RUN echo 'Server = https://mirror.sjtu.edu.cn/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist
RUN pacman -Syu --noconfirm
RUN pacman -S binutils make gcc pkg-config fakeroot git sudo devtools --noconfirm
# 将创建一个non-root用户
ENV NEWUSER soeo
COPY setup.sh /${NEWUSER}/
COPY worker.sh /${NEWUSER}/
# COPY receive_source_file /usr/bin/
CMD /bin/bash /${NEWUSER}/setup.sh 