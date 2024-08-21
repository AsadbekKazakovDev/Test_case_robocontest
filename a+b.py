import os 
import shutil
from random import randrange

path = 'tests'
try: 
    os.mkdir(path) 
except OSError as error: 
    pass

t=int(input('Testlar sonini kiriting: '))
for _ in range(1,t+1):
    a,b=randrange(1,10**3) * randrange(1,10**3),randrange(1,10**3) * randrange(1,10**3)
            
    file1=open(f"{path}/" + '0'*(3-len(str(_)))+str(_)+'.in','w')
    file1.write(f"{a} {b}")
    file1.close()
        
    file2=open(f"{path}/" + '0'*(3-len(str(_)))+str(_)+'.out','w')
    file2.write(str(int(a+b)))
    file2.close()
    
    print(_,'- Good')
shutil.make_archive(path, 'zip', path)