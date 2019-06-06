# 简单模拟 CIDR的IP分组转发算法
# 语言环境 python3
# 作者 软件164韦雪生 3160704402

class Route_Table(object):
    def __init__(self):
        self.direct = [{"interface":"0","net":"122.122.0.0","mask":"255.255.0.0"},{"interface":"1","net":"122.123.0.0","mask":"255.255.0.0"}]
        self.special=[{"net":"122.124.0.0","mask":"255.255.0.0","next":"122.125.0.0"}]
        self.default="122.122.0.0"
        print("简单模拟CIDR的IP分组转发:\n----------初始化示例路由表完成----------\n")

    def check(self,table,ip,type="direct"):
        for x in table:
            net=x["net"].split(".")
            res=self.check_mask(ip,x["mask"].split("."))
            if res==net:
                if type=="direct":
                    return x["net"]
                elif type=="special":
                    return x["next"]
        return False

    def check_mask(self,ip,mask):
        res=[]
        for x,data in enumerate(mask):
            data=int(data)
            res.append(str(ip[x]&data))
        return res

    def output(self):
        print("  当前路由表为:\n-----目的地址所在网络-------下一跳------")
        for i in self.direct:
            print("     %s    直接交付,接口%s" % (i["net"], i["interface"]))
        for i in self.special:
            print("     %s      %s" % (i["net"], i["next"]))
        print("     默认路由:     "+self.default+"\n-------------------------------\n")

    def run(self):
        self.output()
        while True:
            ip_split= list(map(int,input("请输入一个IP地址: ").split(".")))
            x=self.check(self.direct,ip_split)
            if x:
                print("-->直接转发到地址:"+x)
            else:
                y=self.check(self.special,ip_split,"special")

                if y:
                    print("--->未直接找到路由\n找到下一跳交付-->"+y)
                elif self.default:
                    print("--->未找到直接，特定路由-->\n")
                    print("--->找到默认路由转发到:"+self.default)
                else:
                    print("--->未找到默认路由\n-->转发出错\n")    


if __name__ == "__main__":
    my_table =Route_Table()
    my_table.run()
