# 定义一个银行类
class Bank:
    def init(self, username, password, rank_number, money):
        pass

    # 存钱
    def exixtMoney(self):
        pass

    # 取钱
    def withMoney(self):
        pass

    pass

    # 修改密码
    def modifyPassword(self, password):
        pass

    def login(self, username, password):
        x = 2
        while x:
            username = input('请输入您的用户名：')
            password = input('请输入您的密码：')
            pin = input('请确认您的密码；')
            with open(r'路径', mode='r') as rstream:     #文件存储的路径。
                users = list(rstream.readable())
                for i in users:
                    if i[0] == username and i[1][:-1] == password and password == pin:
                        print('---------登陆成功！----------')
                        pass  # 登录成功 返回其他界面。跳出。
                else:
                    print('-----用户名或者密码错误！-----   剩余次数：', x)
                    x -= 1
                    if x == 0:
                        print('用户名或者密码错误超过3次，银行卡被冻结。')
                        pass  # 登录失败银行卡被冻结。跳出。

    def __str__(self):
        pass


# 1,登陆 2,注册 3,取钱 4,存钱 5,修改密码 6,退出
if __name__ == '__main__':
    pass