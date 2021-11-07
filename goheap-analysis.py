import re
# pip3 install matplotlib
# pip3 install numpy

filename = "20211115_1132.txt"


Alloc = re.compile(r"^# Alloc = (\d+)")
TotalAlloc = re.compile(r"^# TotalAlloc = (\d+)")
Sys = re.compile(r"^# Sys = (\d+)")
Lookups = re.compile(r"^# Lookups = (\d+)")
Mallocs = re.compile(r"^# Mallocs = (\d+)")
Frees = re.compile(r"^# Frees = (\d+)")
HeapAlloc = re.compile(r"^# HeapAlloc = (\d+)")
HeapSys = re.compile(r"^# HeapSys = (\d+)")
HeapIdle = re.compile(r"^# HeapIdle = (\d+)")
HeapInuse = re.compile(r"^# HeapInuse = (\d+)")
HeapReleased = re.compile(r"^# HeapReleased = (\d+)")
HeapObjects = re.compile(r"^# HeapObjects = (\d+)")
Stack = re.compile(r"^# Stack = (\d+) / (\d+)")
MSpan = re.compile(r"^# MSpan = (\d+) / (\d+)")
MCache = re.compile(r"^# MCache = (\d+) / (\d+)")
BuckHashSys = re.compile(r"^# BuckHashSys = (\d+)")
GCSys = re.compile(r"^# GCSys = (\d+)")
OtherSys = re.compile(r"^# OtherSys = (\d+)")


def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value,s)
    return '%sB' % n
class GOMem():
    def __init__(self):
        self.Alloc = 0
        self.TotalAlloc = 0
        self.Sys = 0
        self.Lookups = 0
        self.Mallocs = 0
        self.Frees = 0
        self.HeapAlloc = 0
        self.HeapSys = 0
        self.HeapIdle = 0
        self.HeapInuse = 0
        self.HeapReleased = 0
        self.HeapObjects = 0
        self.StackInuse = 0
        self.StackSys = 0
        self.MSpanInuse = 0
        self.MSpanSys = 0
        self.MCacheInuse = 0
        self.MCacheSys = 0
        self.BuckHashSys = 0
        self.GCSys = 0
        self.OtherSys = 0

        with open(filename, "r") as fd:
            for l in fd.readlines():
                result = Alloc.findall(l)
                if len(result) != 0:
                    
                    self.Alloc = int(result[0])
                result = TotalAlloc.findall(l)
                if len(result) != 0:
                    
                    self.TotalAlloc = int(result[0])
                result = Lookups.findall(l)
                if len(result) != 0:
                    
                    self.Lookups = int(result[0])
                result = Mallocs.findall(l)
                if len(result) != 0:
                    
                    self.Mallocs = int(result[0])
                result = Frees.findall(l)
                if len(result) != 0:
                    
                    self.Frees = int(result[0])
                result = HeapAlloc.findall(l)
                if len(result) != 0:
                    
                    self.HeapAlloc = int(result[0])
                result = HeapSys.findall(l)
                if len(result) != 0:
                    
                    self.HeapSys = int(result[0])
                result = HeapIdle.findall(l)
                if len(result) != 0:
                    
                    self.HeapIdle = int(result[0])
                result = HeapInuse.findall(l)
                if len(result) != 0:
                    
                    self.HeapInuse = int(result[0])
                result = HeapReleased.findall(l)
                if len(result) != 0:
                    
                    self.HeapReleased = int(result[0])
                result = HeapObjects.findall(l)
                if len(result) != 0:
                    
                    self.HeapObjects = int(result[0])
                result = Stack.findall(l)
                if len(result) != 0:
                    
                    self.StackInuse = int(result[0][0])
                    self.StackSys = int(result[0][1])
                result = MSpan.findall(l)
                if len(result) != 0:
                    
                    self.MSpanInuse = int(result[0][0])
                    self.MSpanSys = int(result[0][1])
                result = MCache.findall(l)
                if len(result) != 0:
                    
                    self.MCacheInuse = int(result[0][0])
                    self.MCacheSys = int(result[0][1])
                result = BuckHashSys.findall(l)
                if len(result) != 0:
                    
                    self.BuckHashSys = int(result[0])
                result = GCSys.findall(l)
                if len(result) != 0:
                    
                    self.GCSys = int(result[0])
                result = OtherSys.findall(l)
                if len(result) != 0:
                    
                    self.OtherSys = int(result[0])

    def analysis(self):
        print("概要信息")
        print("------------------")
        print("堆空间: {}".format(bytes2human(self.Alloc)))
        print("累计分配堆空间: {}".format(bytes2human(self.TotalAlloc)))
        print("从系统分配的虚存: {}".format(bytes2human(self.Sys)))
        print("堆累计分配obj个数: {}".format(bytes2human(self.Mallocs)))
        print("堆累计归还obj个数: {}".format(bytes2human(self.Frees)))
        print("存活obj个数: {}".format(bytes2human(self.Mallocs-self.Frees)))
        print("")
        print("")
        print("堆信息")
        print("------------------")
        print("堆span空间中被obj用的空间: {}".format(bytes2human(self.HeapAlloc)))
        print("堆span累计空间: {}".format(bytes2human(self.HeapSys)))
        print("堆空闲span空间: {}".format(bytes2human(self.HeapIdle)))
        print("堆span的全部空间: {}".format(bytes2human(self.HeapInuse)))
        print("堆span中obj碎片空间: {}".format(bytes2human(self.HeapInuse - self.HeapAlloc)))
        print("从堆span归还给OS空间: {}".format(bytes2human(self.HeapReleased)))
        print("当前内存中obj个数: {}".format(bytes2human(self.HeapObjects)))
        print("")
        print("")
        print("栈信息")
        print("------------------")
        print("栈spans中使用全部内存块: {}".format(bytes2human(self.StackInuse)))
        print("栈从OS中获取的内存块: {}".format(bytes2human(self.StackSys)))
        print("")
        print("")
        print("非堆栈内存")
        print("------------------")
        print("mspan使用内存: {}".format(bytes2human(self.MSpanInuse)))
        print("mspan从OS中获取的内存块: {}".format(bytes2human(self.MSpanSys)))
        print("mcache使用内存: {}".format(bytes2human(self.MCacheInuse)))
        print("mcache从OS中获取的内存块: {}".format(bytes2human(self.MCacheSys)))
        print("分析hash桶表大小: {}".format(bytes2human(self.BuckHashSys)))
        print("gc元数据: {}".format(bytes2human(self.GCSys)))
        print("杂项: {}".format(bytes2human(self.OtherSys)))
if __name__ == "__main__":
    g = GOMem()
    g.analysis()
