aves(self):         #存款方法
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
