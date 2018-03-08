def Deal(filename):
  num = 0
  start = []
  end = []
  charactor = []
  with open(filename, 'r') as file_to_read:
    while True:
      lines = file_to_read.readline()
      if not lines:
        break
      res = lines.split()
      start.append(int(res[0]))
      end.append(int(res[1])-240)
      charactor.append(res[2])
  length = 0
  for i in range(len(start)):
    while True:
      num += 1
      length += 160
      if length  >= end[i]:
        break
  print filename,num
if __name__ == "__main__":
  filename = '/home/xuejiabin/kaldi/egs/timit/s5/MY_program/train.scp'
  with open(filename, 'r') as file_to_read:
    while True:
      lines = file_to_read.readline()
      if not lines:
        break
      Deal(lines.strip('\n'))