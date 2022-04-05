# 这是一个临时的Readme文件   
主要对node.js实现的服务器开发过程进行临时性记录和说明  
**更详细和具体的文档请见wiki界面**(待整理)

### 主要命令
- 初始化npm包至本地
    ```
    npm install
    ```
- 运行服务器
    ```
    npm start
    ```
- 运行用户访问监听
    ```
    npm run build-dev
    ```
## Package state 约定
- 0: 等待审核
- 1: 等待编译
- 2: 编译中 (不允许删除)
- 3: 编译完成

- 6: 编译错误
- 7: 等待删除

## 守护模块 HTTP 约定
POST(ip:port,data)  
> ip: 为服务器的地址  
> port: 为服务器的端口号  
> data: 为字典格式  
> 对于前端：  
> data = {'name': 'SoftwareName', 'address': 'some address', 'state': 'somestate'}   
> 其中name为软件名，address 为git地址，当是要下载时，state='wait'，当是要删除时，state = 'delete'

## TO DO List  

- [ ] Package Page 
    - [x] 获得数据库信息并展示
    - [x] 实现用户申请
    - [ ] 展示内容处理
    - [ ] 申请已有包的处理
    - [ ] CSS优化
- [ ] Admin Page
    - [ ] Login Page
        - [x] 基本页面框架
        - [x] 实现管理员登录
    - [ ] Package Management
        - [x] 基本页面框架
        - [x] 从数据库获得列表
        - [x] 审核申请
            - [x] 通过:更改状态
            - [x] 通过:通知后端
            - [x] 不通过:删除条目
        - [ ] 管理已有包
            - [x] 删除已有条目:更改状态=>通知后端
            - [ ] 更新已有条目:更新已有条目=>更新状态
    - [ ] CSS优化
- [ ] 实现本地部署
- [ ] 非核心内容补充
    - [ ] Home Page 
    - [ ] About Page
    - [ ] Help Page
- [ ] Package page搜索功能
- [ ] 保持admin登录状态
- [ ] 审核结果发送邮件


