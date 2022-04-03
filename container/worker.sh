#!/bin/bash
# 创建一个input目录 用于接收消息队列的信息
WORKDIR="$(pwd)"
TIMEOUT=600
ORIGINAL_IFS="${IFS}"
# receive()
# sudo receive_source_file
# sudo tar xf source.tar.gz 
# cd source
git clone "https://aur.archlinux.org/endlessh-git.git"
cd "endlessh-git" || exit


getPackageName="$(makepkg --packagelist)"
IFS=$'\n'
packageName=("$getPackageName")
IFS=$ORIGINAL_IFS
for i in $(seq 0 $((${#packageName[@]}-1)));
do
    packageName[i]=${packageName[i]##*/}
    echo "${packageName[i]}" >> packageName.log;
done 

sudo timeout $TIMEOUT extra-x86_64-build 2>CompileErr.log # use local source: extra-x86_64-build -- -- -se
returnCode=$?
if [ $returnCode -eq 124 ];
then TimeoutErr=-1;
else TimeoutErr=0;
fi
if [ $returnCode -ne 0 ];
then echo -1 > FinalErr.log # FinalErr.log 格式为1个数表示成功失败 然后是报错信息
    echo "Time out: ${TimeoutErr}" >> FinalErr.log
    cat CompileErr.log >> FinalErr.log
else echo 0 > FinalErr.log
    for file in *.pkg.tar.zst-namcap.log;
    do 
        echo "Warnings: " >> FinalErr.log
        cat "$file" >> FinalErr.log
    done 
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
    if [ ${uploadSuccess} -eq 0 ];
    then echo -1 > FinalErr.log
        echo "Upload failed" >> FinalErr.log
    fi 
    # sendback(FinalErr.log)
done 
sudo rm -rf ./*