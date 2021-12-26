# fw_rules.py
import pythoncom
import win32com
from win32com.client import Dispatch,gencache
class rule:
    items = {}
    # 中英文转换
    items_name = {
        "Action":'操作',
        "ApplicationName":'程序',
        "Description":'描述',
        "Direction":'进站/出站',
        "EdgeTraversal":'边缘穿越',
        "EdgeTraversalOptions":'边缘穿越选项',
        "Enabled":'已启用',
        "Grouping":'组',
        "IcmpTypesAndCodes":'ICMP设置',
        "InterfaceTypes":'接口类型',
        "Interfaces":'接口',
        "LocalAddresses":'本地地址',
        "LocalAppPackageId":'应用程序包',
        "LocalPorts":'本地端口',
        "LocalUserAuthorizedList":'授权的本地计算机',
        "LocalUserOwner":'本地用户所有者',
        "Name":'名称',
        "Profiles":'配置文件',
        "Protocol":'协议',
        "RemoteAddresses":'远程地址',
        "RemoteMachineAuthorizedList":'授权的远程计算机',
        "RemotePorts":'远程端口',
        "RemoteUserAuthorizedList":'授权的远程用户',
        "SecureFlags":'安全',
        "serviceName":'服务名'}
    items_shell = {
        "Action": 'action',
        "ApplicationName": 'program',
        "Description": 'description',
        "Direction": 'dir',
        "EdgeTraversal": 'edge',
        "EdgeTraversalOptions": '边缘穿越选项',
        "Enabled": 'enable',
        "Grouping": '组',
        "IcmpTypesAndCodes": 'ICMP设置',
        "InterfaceTypes": 'interfacetype',
        "Interfaces": '接口',
        "LocalAddresses": 'localip',
        "LocalAppPackageId": '应用程序包',
        "LocalPorts": 'localport',
        "LocalUserAuthorizedList": '授权的本地计算机',
        "LocalUserOwner": '本地用户所有者',
        "Name": 'name',
        "Profiles": 'profile',
        "Protocol": 'protocol',
        "RemoteAddresses": 'remoteip',
        "RemoteMachineAuthorizedList": 'rmtcomputergrp',
        "RemotePorts": 'remoteport',
        "RemoteUserAuthorizedList": 'rmtusrgrp',
        "SecureFlags": 'security',
        "serviceName": 'service'
    }
    def __init__(self,index):
        self.index = index
        for i in self.items_name.keys():
            self.items[i] = ''

    def init_by_app(self, app_in):
        for key in self.items_name.keys():
            self.items[key] = " " + str(eval("app_in."+key))
            print(self.items[key] )

    def init_by_dict(self,dirc_con):
        flag = False
        for item_key in self.items_name.keys():
            if self.items_name[item_key] in dirc_con.keys():
                flag = True
                self.items[item_key] = dirc_con[self.items_name[item_key]]

        if not flag:
            for key in dirc_con.keys():
                self.items[key] = dirc_con[key]

    def create_rule(self):
        app = Dispatch('HNetCfg.FwRule')
        res = []
        # 注意赋值顺序
        app.Action = int(self.items["Action"])
        app.Description = self.items["Description"]
        app.Direction = int(self.items["Direction"])
        app.EdgeTraversal = self.items["EdgeTraversal"]
        app.EdgeTraversalOptions = self.items["EdgeTraversalOptions"]
        app.Enabled = self.items["Enabled"]
        app.Grouping = self.items["Grouping"]
        ## app.IcmpTypesAndCodes = self.items["IcmpTypesAndCodes"]
        app.InterfaceTypes = self.items["InterfaceTypes"]
        ## app.Interfaces = self.items["Interfaces"]
        app.LocalAddresses = self.items["LocalAddresses"]
        app.LocalAppPackageId = self.items["LocalAppPackageId"]
        ## app.LocalPorts = str(self.items["LocalPorts"]),
        ## app.LocalUserAuthorizedList = self.items["LocalUserAuthorizedList"]
        app.LocalUserOwner = self.items["LocalUserOwner"]
        app.Name = self.items["Name"]
        app.Profiles = self.items["Profiles"]
        app.Protocol = self.items["Protocol"]
        app.RemoteAddresses = self.items["RemoteAddresses"]
        ## app.RemoteMachineAuthorizedList = self.items["RemoteMachineAuthorizedList"]
        app.RemotePorts = self.items["RemotePorts"]
        app.LocalPorts = self.items['LocalPorts']
        ## app.RemoteUserAuthorizedList = ''
        app.SecureFlags = self.items["SecureFlags"]
        # app.serviceName = "null"
        # app.ApplicationName = "null"
        return app

    def __str__(self):
        result = "="*10 + '\n序号 : ' + str(self.index) + '\n'
        for key in self.items_name.keys():
            result += self.items_name[key] + " : " + str(self.items[key]) +"\n"
        return result

def add_rule(dict_value):
    fw = gencache.EnsureDispatch('HNetCfg.FwPolicy2', 0)
    apps = fw.Rules
    print(apps.Count)
    # app = win32com.client.Dispatch('HNetCfg.FwRule3')
    rule_obj = rule(-1)
    rule_obj.init_by_dict(dict_value)
    app = rule_obj.create_rule()
    apps.Add(app)

def del_rule(dict_value):

    fw = gencache.EnsureDispatch('HNetCfg.FwPolicy2', 0)
    apps = fw.Rules
    print("before :", apps.Count)
    rule_obj = rule(-1)
    rule_obj.init_by_dict(dict_value)
    for app in apps:
        print(rule_obj.items['Name'] , str(app.Name))
        print(rule_obj.items['LocalPorts'] , str(app.LocalPorts))
        print(rule_obj.items['RemoteAddresses'] , str(app.RemoteAddresses))
        if rule_obj.items['Name'] == str(app.Name) and rule_obj.items['LocalPorts'] == str(app.LocalPorts) and rule_obj.items['RemoteAddresses'] == str(app.RemoteAddresses):
            # 只能根据Name删除,大概是个傻子哟
            apps.Remove(str(app.Name))
            # break
    print("after :", apps.Count)

if __name__ == '__main__':
    my_dict = {
    '序号' : '2',
    '操作' : '1', # 0 阻止，1通过
    '程序' : '',
    '描述' : '为serverlicense做认证',
    '进站/出站' : '1',
    '边缘穿越' : 'False',
    '边缘穿越选项' : '0',
    '已启用' : 'True',
    '组' : '',
    'ICMP设置' : '',
    '接口类型' : 'All',
    '接口' : 'None',
    '本地地址' : '*',
    '应用程序包' : '',
    '本地端口' : '9876',
    '授权的本地计算机' : '',
    '本地用户所有者' : '',
    '名称' : 'test_cmd',
    '配置文件' : '1',# 1为域，2为专用，3为公用
    '协议' : '6',
    '远程地址' : '114.115.250.41/255.255.255.255,114.115.250.43/255.255.255.255',
    '授权的远程计算机' : '',
    '远程端口' : '*',
    '授权的远程用户' : '',
    '安全' : '0',
    '服务名' : ''
    }
    add_rule(my_dict)
    # del_rule(my_dict)
