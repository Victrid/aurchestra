FROM archlinux:latest
RUN echo 'Server = https://mirror.sjtu.edu.cn/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist \
 && echo 'Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch' >> /etc/pacman.d/mirrorlist
RUN pacman -Syu binutils make gcc pkg-config fakeroot git sudo devtools python python-pip --noconfirm
COPY ./container/ /container
COPY ./MQ/ /container/MQ/
RUN pip install -r /container/MQ/requirements.txt
CMD /bin/bash /container/setup.sh
