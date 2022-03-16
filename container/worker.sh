#!/bin/bash
# 创建一个input目录 用于接收消息队列的信息
mkdir input 
chmod 777 input
cd input || exit
# TODO receive()
# sudo git clone https://aur.archlinux.org/endlessh-git.git
sudo chmod -R 777 ./
packageName=$(ls)
cd "${packageName}" || exit
timeout 600 makepkg -s --noconfirm &> PKGlog.log
if [ $? -ne 0 ];
then NULL # sendback(makepkg error) TODO
fi 
for file in *.pkg.tar.zst;
do 
    uploadSuccess=0
    for try in $(seq 0 2); # 尝试上传3次
    do 
        # sudo curl --request POST --url http://hostIP/api/package --header 'content-type: multipart/form-data' --form uploadfile=@"${file}"
        if [ $? -eq 200 ]; # 200 成功; 400 失败
        then 
            uploadSuccess=1
            break
        fi 
    done 
    if [ ${uploadSuccess} -eq 1 ];
    then NULL #sendback(success)
    else NULL #sendback(uploadfail)
    fi 
done 
sudo rm -rf ./*
