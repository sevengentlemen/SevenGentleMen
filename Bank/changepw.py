import time

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