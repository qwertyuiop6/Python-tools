
class Forward_Table(object):
    def __init__(self):
        self.max = 50
        self.write = 0
        self.data = []
        self.index = 0

        # for i in range(0,self.max):
        # self.data[i]={}
        # self.data[i]["addr"]='0'
        # self.data[i]["port"]=0
        self.data = [{"addr": "0", "port": 0} for i in range(0, self.max)]

    def find_addr(self, data) -> bool:
        for i, v in enumerate(self.data):
            if v["addr"] == data["addr"]:
                self.index = i
                return True
        return False

    def add_data(self, data):

        self.data[self.write]["addr"] = data["addr"]
        self.data[self.write]["port"] = data["port"]
        self.write = (self.write + 1) % self.max

    def output(self):
        print("当前转发表为:\n-------转发表-------\n----地址----端口----")
        for i in range(0, self.write):
            print("     %s     %s" % (self.data[i]["addr"], self.data[i]["port"]))
        print("--------------------\n")

    def run(self):
        while True:
            addr, port = map(str, input("输入源地址和端口号 以空格隔开: ").split(" "))
            port = int(port)
            source_data = {"addr": addr, "port": port}
            send_addr = input("输入发送地址: ")
            send_data = {}
            send_data["addr"] = send_addr
            send_data["port"] = 0
            if not self.find_addr(source_data):
                self.add_data(source_data)
            if not self.find_addr(send_data):
                print("\n转发表未找到目标地址，将从其他端口将此帧转发给别的网桥")
            else:
                if self.data[self.index]["port"] == source_data["port"]:
                    print("目的地址和源址在同一接口，本帧丢弃")
                else:
                    print("将此帧从查找到的目标端口发出: %s" % self.data[index]["port"])
            self.output()


if __name__ == "__main__":
    my_table = Forward_Table()
    my_table.run()

