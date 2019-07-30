import time
import random
class Preson(object):                     #人类
    def __init__(self):
        self.name = ''
        self.idNum = ''
        self.phoneNum = ''
        self.cardNum = ""
        self.cardPass_word = ''
        self.cardCode = 0
        self.money = 0
class Bank(object):                     #银行类
    dict1 = {}
    list1 = []
    def shuijikahao(self):   #生成六位随机卡号
        str = "1234567890"
        str1 = ""
        while True:
            for x in range(6):
                str1 += random.choice(str)
            if str1 not in Bank.list1:
                Bank.list1.append(str1)
                break
        return str1
    def open(self):        #开户方法
        per1 = Preson()
        per1.name = input("请输入姓名：")
        per1.idNum = input("请输入身份证号：")
        while True:
            per1.cardPass_word = input("请输入登录密码:")
            a = input("请确认登录密码：")
            if a == per1.cardPass_word:
                break
            else:
                print("两侧密码不一致，请重新输入")
        per1.phoneNum = input("请输入联系电话：")
        while True:
            per1.money = int(input("请输入预存款金额:"))
            if per1.money <= 0:
                print("预存款金额必须大于0")
            else:
                break
        c = Bank.shuijikahao(self)
        per1.cardNum = c
        Bank.dict1[c] = per1
        print("开户成功，您的卡号为%s,请牢记您的卡号"%per1.cardNum)
    def see(self):           #查询方法
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():       #判断是否存在卡号
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        if Bank.dict1[a].cardCode >= 3:      #判断错误次数是否已有三次
            print("已错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
            return -1
        else:
            while Bank.dict1[a].cardCode < 3:
                b = input("请输入密码")
                if b == Bank.dict1[a].cardPass_word:          #判断密码是否正确
                    Bank.dict1[a].cardCode = 0
                    print("密码正确，您当前余额为：",Bank.dict1[a].money)
                    print("返回上一级...........")
                    time.sleep(1)
                    return -1
                else:
                    print("密码错误，请重新输入")
                    Bank.dict1[a].cardCode += 1
            print("已输入错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
    def saves(self):         #存款方法
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        if Bank.dict1[a].cardCode >= 3:
            print("已错误3次，卡已被冻结，请解冻后再试......")
            print("返回上一级.......")
            time.sleep(1)
            return -1
        else:
            while Bank.dict1[a].cardCode < 3:
                b = input("请输入密码")
                if b == Bank.dict1[a].cardPass_word:
                    Bank.dict1[a].cardCode = 0
                    while True:                          #判断存款金额
                        c= int(input("密码正确，请输入您的存款金额："))
                        if c <= 0:
                            print("存款金额必须大于0")
                        else:
                            break
                    Bank.dict1[a].money += c
                    print("存款成功您当前余额为：", Bank.dict1[a].money)
                    print("正在返回上一级.....")
                    time.sleep(1)
                    return -1
                else:
                    print("密码错误，请重新输入")
                    Bank.dict1[a].cardCode += 1
            print("已输入错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级.......")
            time.sleep(1)
    def draw(self):
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        if Bank.dict1[a].cardCode >= 3:
            print("已错误3次，卡已被冻结，请解冻后再试......")
            print("返回上一级.......")
            time.sleep(1)
            return -1
        else:
            while Bank.dict1[a].cardCode < 3:
                b = input("请输入密码")
                if b == Bank.dict1[a].cardPass_word:
                    Bank.dict1[a].cardCode = 0
                    while True:
                        c = int(input("密码正确，请输入您的取款金额："))
                        if c >  Bank.dict1[a].money:
                            print("余额不足,请重新输入取款金额")
                        elif c <= 0:
                            print("取款金额必须大于0")
                        else:
                            break
                    Bank.dict1[a].money -= c
                    print("取款成功您当前余额为：", Bank.dict1[a].money)
                    print("正在返回上一级.....")
                    time.sleep(1)
                    return -1
                else:
                    print("密码错误，请重新输入")
                    Bank.dict1[a].cardCode += 1
            print("已输入错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级.......")
            time.sleep(1)
    def transfer(self):#转账
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        if Bank.dict1[a].cardCode >= 3:
            print("已错误3次，卡已被冻结，请解冻后再试......")
            print("返回上一级.......")
            time.sleep(1)
            return -1
        else:
            while Bank.dict1[a].cardCode < 3:
                b = input("请输入密码")
                if b == Bank.dict1[a].cardPass_word:
                    Bank.dict1[a].cardCode = 0
                    c = input("密码正确，请输入你想转账的卡号：")
                    if c not in Bank.dict1.keys():
                        print("卡号不存在,返回上一级")
                        time.sleep(1)
                        return -1
                    if Bank.dict1[c].cardCode >= 3:
                        print("您想转账的卡已被冻结，请解冻后再试......")
                        print("返回上一级.......")
                        time.sleep(1)
                        return -1
                    if a == c:
                        print("不能给自己的卡转账，返回上一级")
                        time.sleep(1)
                        return -1
                    else:
                        while True:
                            d = int(input("请输入您想转账的金额："))
                            if  d > Bank.dict1[a].money:
                                print("余额不足，请重新输入转账金额")
                            elif d <= 0:
                                print("转账金额必须大于0")
                            else:
                                break
                        Bank.dict1[a].money -= d
                        Bank.dict1[c].money += d
                        print("转账成功，您当前余额为：", Bank.dict1[a].money )
                    print("正在返回上一级.....")
                    time.sleep(1)
                    return -1
                else:
                    print("密码错误，请重新输入")
                    Bank.dict1[a].cardCode += 1
            print("已输入错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级.......")
            time.sleep(1)
    def close(self):
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        if Bank.dict1[a].cardCode >= 3:
            print("已错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
            return -1
        else:
            while Bank.dict1[a].cardCode < 3:
                b = input("请输入密码")
                if b == Bank.dict1[a].cardPass_word:
                    Bank.dict1[a].cardCode = 0
                    c = input("请输入您的姓名：")
                    d = input("请输入您的身份证号:")
                    e = input("请输入您开卡时预留手机号：")
                    if c != Bank.dict1[a].name or d != Bank.dict1[a].idNum or e != Bank.dict1[a].phoneNum:
                        print("信息验证错误，返回上一级")
                        return -1
                    print("信息验证成功")
                    if input("确定销户吗？YES.NO").lower() == 'YES'.lower():
                        del Bank.dict1[a]
                        print("销户成功......")
                    else:
                        print("没有销户......")
                    print("返回上一级...........")
                    time.sleep(1)
                    return -1
                else:
                    print("密码错误，请重新输入")
                    Bank.dict1[a].cardCode += 1
            print("已输入错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
    def re_make(self):
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        if Bank.dict1[a].cardCode >= 3:
            print("已错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
            return -1
        else:
            while Bank.dict1[a].cardCode < 3:
                b = input("请输入密码")
                if b == Bank.dict1[a].cardPass_word:
                    Bank.dict1[a].cardCode = 0
                    while Bank.dict1[a].cardCode < 3:
                        c = input("请输入您的姓名：")
                        d = input("请输入您的身份证号:")
                        e = input("请输入您开卡时预留手机号：")
                        if c == Bank.dict1[a].name and d == Bank.dict1[a].idNum and e == Bank.dict1[a].phoneNum:
                            f = Bank.shuijikahao(self)
                            print("补卡成功，请取走您的卡片,您当前卡号为：",f)
                            time.sleep(1)
                            Bank.dict1[f] = Bank.dict1[a]
                            del Bank.dict1[a]
                            return  -1
                        else:
                            print("验证失败，您的输入有错误.....")
                            Bank.dict1[a].cardCode += 1
                    print("返回上一级...........")
                    time.sleep(1)
                    return -1
                else:
                    print("密码错误，请重新输入")
                    Bank.dict1[a].cardCode += 1
            print("已输入错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
    def unfreeze(self):
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        else:
            b = 0
            while b < 3:
                c = input("请输入您的姓名：")
                d = input("请输入您的身份证号:")
                e = input("请输入您开卡时预留手机号：")
                if c == Bank.dict1[a].name and d == Bank.dict1[a].idNum and e == Bank.dict1[a].phoneNum:
                    print("解冻成功.......")
                    time.sleep(1)
                    Bank.dict1[a].cardCode  = 0
                    return -1
                else:
                    print("验证失败，您的输入有错误.....")
                    b += 1
            print("已输入错误3次，解冻失败，卡已注销")
            del Bank.dict1[a]
            print("返回上一级...........")
            time.sleep(1)
    def freeze(self):
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        if Bank.dict1[a].cardCode >= 3:
            print("已错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
            return -1
        else:
            while Bank.dict1[a].cardCode < 3:
                b = input("请输入密码")
                if b == Bank.dict1[a].cardPass_word:
                    Bank.dict1[a].cardCode = 3
                    print("冻结成功.......")
                    print("返回上一级...........")
                    time.sleep(1)
                    return -1
                else:
                    print("密码错误，请重新输入")
                    Bank.dict1[a].cardCode += 1
            print("已输入错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
    def changepw(self):
        a = input("请输入您的卡号")
        if a not in Bank.dict1.keys():
            print("卡号不存在,返回上一级")
            time.sleep(1)
            return -1
        if Bank.dict1[a].cardCode >= 3:
            print("已错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
            return -1
        else:
            while Bank.dict1[a].cardCode < 3:
                b = input("请输入密码")
                if b == Bank.dict1[a].cardPass_word:
                    c = input("请输入新的密码....")
                    while c != input("请确认您的新密码"):
                        c = input("请输入新的密码....")
                    Bank.dict1[a].cardPass_word = c
                    print("密码重置成功")
                    print("返回上一级...........")
                    time.sleep(1)
                    return -1
                else:
                    print("密码错误，请重新输入")
                    Bank.dict1[a].cardCode += 1
            print("已输入错误3次，卡已被冻结，请解冻后再试")
            print("返回上一级...........")
            time.sleep(1)
    def exit1(self):
        while 1:
            c = input("请输入管理员账号：")
            d = input("请输入管理员密码：")
            if c == "admin" and d == "123456":
                print("登录成功,正在退出系统.....")
                time.sleep(1)
                break
            else:
                print("账号或密码错误，请重新输入")
                time.sleep(1)
        exit()
    def admin_register(self):
        print("******************************************************************")
        print("*                                                                *")
        print("*                                                                *")
        print("*                            银行系统                             *")
        print("*                                                                *")
        print("*                                                                *")
        print("******************************************************************")
        while 1:
            a = input("请输入管理员账号：")
            b = input("请输入管理员密码：")
            if a == "admin" and b == "123456":
                print("登录成功,正在跳转......")
                time.sleep(1)
                break
            else:
                print("账号或密码错误，请重新输入")
                time.sleep(1)
        while 1:
            print("******************************************************************")
            print("*           1、开户                      2、查询                  *")
            print("*           3、存款                      4、取款                  *")
            print("*           5、转账                      6、销户                  *")
            print("*           7、补卡                      8、解冻                  *")
            print("*           9、冻结                      0、更改密码               *")
            print("*                        t、退出                                  *")
            print("******************************************************************")
            a = input("请输入操作：")
            if a == "1":
                self.open()
            elif a == "2":
                self.see()
            elif a == "3":
                self.saves()
            elif a == "4":
                self.draw()
            elif a == "5":
                self.transfer()
            elif a == "6":
                self.close()
            elif a == "7":
                self.re_make()
            elif a == "8":
                self.unfreeze()
            elif a == "9":
                self.freeze()
            elif a == "0":
                self.changepw()
            elif a == "t":
               self.exit1()
            else:
                print("输入错误，请重新输入......")
a = Bank()
a.admin_register()