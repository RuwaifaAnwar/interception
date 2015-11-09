import gzip
import os
"""
445326500|198.11.141.0/24|FINISHED|1445299200|1445299200|1445326200|2|6453,2 31500,1
1445326500|198.11.141.0/24|NEW|1445326500|1445326500|1445326500|3|6453,1 4766,1 31500,1
1445326500|101.251.224.0/20|ONGOING
"""


num_of_files=0

#Path of logs
path=os.getcwd()+"/logs/"
files = os.listdir( path )

# This would print all the files and directories
for file in files:
    print path+file
    file=path+file
    os.stat(file)
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
    #print mtime
    




def find_latest():
    """
    Check if there is a new file. if new file endswith done, it returns the file added before that
    """
#    return path+"moas.1445326500.1200s-window.events.gz"
    return path+"test_file"
    global num_of_files
    while (True):
        files = os.listdir( path )
        if len(files)> num_of_files:
            num_of_files=len(files)
            #new file found
            newlist = sorted(files, key=lambda x: os.stat(path+x).st_mtime, reverse=False)
            if str(newlist[-1]).endswith("done"):
                return path+newlist[-2]
        



if __name__ == "__main__":
    import sys