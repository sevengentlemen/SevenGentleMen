# 定义一个银行类
class Rank:
    def init(self, user, password, rank_number, money):
        pass

    # 存钱
    def exixtMoney(self):
        pass

    # 取钱
    def withMoney(self):
        pass

    # 修改密码
    def modifyPassword(self, password):
        pass

    def __str__(self):
        pass


# 1,登陆 2,注册 3,取钱 4,存钱 5,修改密码 6,退出
if __name__ == '__main__':
    while True:
        number = input('请选择1.登陆 2.注册 3.取钱 4.存钱 5 修改密码 6.退出')
        # 登陆模块 登陆时写一个旗
        if number == '1':
            pass
        # 注册模块
        if number == '2':
            pass

        # 取钱模块 判断是否登陆
        if number == '3':
            pass

        # 存钱模块 判断是否登陆
        if number == '4':
            pass

        # 修改密码
        if number == '5':
            pass

        if number == '6':
            pass
