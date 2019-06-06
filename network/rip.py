# rip协议实现
# 语言环境 python3

import copy
from time import ctime

# 按照bellman-ford算法更新当前路由表
def bellman_ford(rip1, rip2, index_a, index_b):

    r1 = copy.deepcopy(rip1)
    r2 = copy.deepcopy(rip2)
    r3 = []
    next_des = 'r{}'.format(index_b)
    print (' 在{} 之前 r{}更新'.format(ctime(), index_a))
    print ('-' * 20)
    print (r1)
    print ('-' * 20)
    print ('r{} 接受 r{} 的路由表'.format(index_a, index_b))
    for m, x in enumerate(r2):
        flag = 0
        for n, y in enumerate(r1):
            if x['des'] == y['des']:
                flag = 1
                if x['next'] == next_des:
                    x['len'] += 1
                    r1[n] = x
                    break
                else:
                    flag = 1
                    if x['len'] + 1 < y['len'] + x['len']:
                        x['len'] += 1
                        x['next'] = next_des
                        r1[n] = x
                        break
                    else:
                        break
        if flag == 0:
            x['len'] += 1
            x['next'] = next_des
            r1.append(x)
    print ('在 {}之后 r{} 更新'.format(ctime(), index_a))
    print ('-' * 20)
    print (r1)
    print ('-' * 20)

# 初始化每一个router上的router表
def init_table(r_list):
    rip_table = []
    for i in xrange(len(r_list)):
        print ("输入 {} 号路由表长度".format(i))
        print ("-"*20)
        l = input('>')
        temp_table = []
        for n in xrange(int(l)):
            print ("-" * 20)
            temp_table.append(input('>'))
        rip_table.append(convert_rip(temp_table))
    return rip_table


# 路由转化为字典
def convert_rip(table):
    rip_table = []
    for i in table:
        args_list = i.split(' ')
        rip_path = {'des': args_list[0], 'len': int(args_list[1]), 'next': args_list[2]}
        rip_table.append(rip_path)
    return rip_table

#邻接矩阵
def get_network():
    print ('-'*20)
    print ('输入路由器数量')
    r_num = input('>')
    r_list = []
    print ('-' * 20)
    print ('输入路由矩阵')
    for i in xrange(int(r_num)):
        r_list.append(input('>'))
    return r_list

#路由矩阵判断连接关系
def up_tables():
    r_list = get_network()
    table = init_table(r_list)
    for n, x in enumerate(r_list):
        for m, y in enumerate(x.split(' ')):
            if y == '1':
                bellman_ford(table[n], table[m], n+1, m+1)

if __name__ == '__main__':
    up_tables()