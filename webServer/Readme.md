# 这是一个临时的Readme文件   
主要对node.js实现的服务器开发过程进行临时性记录和说明  
**更详细和具体的文档请见wiki界面**(待整理)

- 运行服务器[port: `8080`]
    ```shell
    npm start
    ```

    运行服务器前需要保证调试用sqlite正常
    ```shell
    npm run initDB
    ```
- 访问示例  
    可以通过浏览器访问相应的API接口进行查看server提供的数据库服务  
    http://localhost:8080/api/package/  
    http://localhost:8080/api/admin/ 

    访问两个地址，可以看到预设的信息正常显示，(对应`getall`)


(在开发阶段，暂时只允许localhost进行访问)