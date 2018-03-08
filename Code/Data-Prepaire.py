import numpy as np
class Data(object):
    def __init__(self):
        self.dic_target = {}
        self.dic_name = {}
        self.start = []
        self.end = []
        self.charactor = []
        self.time = 0
        self.cureent = 0
    def make_map(self):
        filename = '/home/xuejiabin/kaldi/egs/timit/s5/MY_program/target.map'
        with open(filename, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()
                if not lines:
                    break
                res = lines.split()
                target = np.zeros(shape=[61],dtype=int)
                target[int(res[0])] = 1
                self.dic_target[res[1]] = target
    def make_name_scp(self):
        filename = '/home/xuejiabin/kaldi/egs/timit/s5/MY_program/name.scp'
        with open(filename, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()
                if not lines:
                    break
                res = lines.split()
                self.dic_name[res[0]] = res[1]
    def Read_target(self,filename):
        self.start = []
        self.end = []
        self.charactor = []
        self.time = 0
        self.cureent = 0
        with open(filename, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()
                if not lines:
                    break
                res = lines.split()
                self.start.append(int(res[0]))
                self.end.append(int(res[1]) - 240)
                self.charactor.append(res[2])
        pass
    def CreateData(self):
        self.make_name_scp()
        self.make_map()
        name = ''
        f = open('charactor.txt','w')
        f1 = open('target.txt', 'w')
        for i in range(1, 10):
            filename = '/home/xuejiabin/kaldi/egs/timit/s5/mfcc.energy/raw_mfcc_dev.' + str(i) + '.txt'
            with open(filename, 'r') as file_to_read:
                while True:
                    lines = file_to_read.readline()
                    if not lines:
                        break
                    if lines.find('[') >= 0:
                        name = lines.strip('  [\n')
                        self.Read_target(self.dic_name[name])
                    else:
                        if lines.find(']') >= 0:
                            lines.strip(']\n')
                        if self.time > self.end[self.cureent]:
                            self.cureent += 1
                        if self.cureent >= len(self.end):
                            self.cureent -= 1
                        self.time += 160
                        f.write("%s\n" % (lines))
                        f1.write("%s\n" % (str(self.dic_target[self.charactor[self.cureent]])))
        f.close()
        f1.close()
if __name__ == "__main__":
    d = Data()
    d.CreateData()