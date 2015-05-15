def scanner(name,function):
    file=open(name,'r')
    while True:
        line=file.readline()
        if not line:break
        function(line)
    file.close()

def display(line):
    print(line)

if __name__=='__main__':
    scanner('scanfile.py',display)