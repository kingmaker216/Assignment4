
try:
    filename ='samplefile.txt'
    file1 = open(filename, 'r+')
    read_in = file1.read()
    print(read_in)
    file1.close()


except FileNotFoundError:
    print(filename,'file not exists')

finally:
    print('File operation attempt finished.')