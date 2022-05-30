FROM archlinux:latest
WORKDIR /data
COPY ./daemon ./
COPY ./MQ ./MQ

RUN echo 'Server = https://mirror.sjtu.edu.cn/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist \
 && echo 'Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch' >> /etc/pacman.d/mirrorlist
RUN pacman -Syu base-devel python-pip python-psycopg2 git --noconfirm 
RUN pip install -r MQ/requirements.txt
RUN pip install -r requirements.txt


ENTRYPOINT python Schedule.py
