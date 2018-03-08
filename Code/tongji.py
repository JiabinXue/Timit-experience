if __name__ == "__main__":
  num = 0
  name = ''
  for i in range(1,10):
    filename = '/home/xuejiabin/kaldi/egs/timit/s5/mfcc.energy/raw_mfcc_train.' + str(i) + '.txt'
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
            if lines.find('[') >= 0:
                print name,num
                name = lines.strip('  [\n')
                num = 0
            else:
                num +=1