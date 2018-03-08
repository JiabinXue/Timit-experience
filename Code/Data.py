import numpy as np
import random
class Data(object):
    def __init__(self,DataDir):
        self.dir = DataDir
        self.traindataSet = []
        self.traintargetSet = []
        self.testdataSet = []
        self.testtargetSet = []
        self.devdataSet = []
        self.devtargetSet = []
        self.index = []
        self.batchnum = 0
        pass
    def ReadData(self):
        train_data = self.dir + 'train/charactor.txt'
        with open(train_data) as file_read:
            while True:
                lines = file_read.readline()
                if not lines:
                    break
                if len(lines) < 5:
                    continue
                lines = lines.replace(']','')
                res = lines.split()
                self.traindataSet.append(res)
        self.traindataSet = np.array(self.traindataSet, dtype=np.float32)
        train_target = self.dir + 'train/target.txt'
        with open(train_target) as file_read:
            while True:
                lines = file_read.readline() + file_read.readline()
                if not lines:
                    break
                lines = lines.replace(']', '')
                lines = lines.replace('[', '')
                res = lines.split()
                self.traintargetSet.append(res)
        self.traintargetSet = np.array(self.traintargetSet, dtype=np.int)



        test_data = self.dir + 'test/charactor.txt'
        with open(test_data) as file_read:
            while True:
                lines = file_read.readline()
                if not lines:
                    break
                if len(lines) < 5:
                    continue
                lines = lines.replace(']', '')
                res = lines.split()
                self.testdataSet.append(res)
        self.testdataSet = np.array(self.testdataSet, dtype=np.float32)
        test_target = self.dir + 'test/target.txt'
        with open(test_target) as file_read:
            while True:
                lines = file_read.readline() + file_read.readline()
                if not lines:
                    break
                lines = lines.replace(']', '')
                lines = lines.replace('[', '')
                res = lines.split()
                self.testtargetSet.append(res)
        self.testtargetSet = np.array(self.testtargetSet, dtype=np.int)

        dev_data = self.dir + 'dev/charactor.txt'
        with open(dev_data) as file_read:
            while True:
                lines = file_read.readline()
                if not lines:
                    break
                if len(lines) < 5:
                    continue
                lines = lines.replace(']', '')
                res = lines.split()
                self.devdataSet.append(res)
        self.devdataSet = np.array(self.devdataSet, dtype=np.float32)
        dev_target = self.dir + 'dev/target.txt'
        with open(dev_target) as file_read:
            while True:
                lines = file_read.readline() + file_read.readline()
                if not lines:
                    break
                lines = lines.replace(']', '')
                lines = lines.replace('[', '')
                res = lines.split()
                self.devtargetSet.append(res)
        self.devtargetSet = np.array(self.devtargetSet, dtype=np.int)

    def GetTestSet(self):
        return self.testdataSet,self.testtargetSet
    def GetDevSet(self):
        return self.devdataSet,self.devtargetSet
    def SetBatchNum(self,num):
        self.batchnum = num
    def GetRandomIndex(self):
        self.index = random.sample(range(len(self.traintargetSet)),len(self.traintargetSet))
    def GetNextBatch(self):
        if len(self.index) < self.batchnum:
            self.GetRandomIndex()
        current = self.index[:self.batchnum]
        self.index = self.index[self.batchnum:]
        return np.array([self.traindataSet[i] for i in current]),np.array([self.traintargetSet[i] for i in current])
if __name__ == "__main__":
    d=Data("/home/xuejiabin/kaldi/egs/timit/s5/MY_program/data/")
    d.ReadData()
    d.SetBatchNum(100)
    res = d.GetNextBatch()