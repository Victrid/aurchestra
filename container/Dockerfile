FROM archlinux
RUN echo 'Server = https://mirror.sjtu.edu.cn/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist
RUN pacman -Syu --noconfirm
RUN pacman -S binutils make gcc pkg-config fakeroot git sudo devtools --noconfirm
RUN pacman -S python python-pip --noconfirm
COPY ./container/ /soeo
COPY ./MQ/ /soeo/MQ/
CMD /bin/bash /soeo/setup.sh