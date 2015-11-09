import csv
import reader
import gzip
import asrank asar
import db_store as db

#1445321100
#dict storing MOASes
moas_dict={}

class Moas_pref:
    """
    For a prefix,stores ASN and time in which they were first seen and ended
    """
    def __init__(self, ASN, time,status,primary):
        self.asn=ASN
        self.stime=time #start time
        self.etime=None #end time
        self.status=status  #ongoing or dead
        self.is_primary=primary #first seen?
        
def print_diag(prefix):
    global moas_dict
    for i in moas_dict[prefix]:
        print "***ASN: ",i.asn," stime: ",i.stime," etime: ",i.etime," status: ",i.status
        
def check_most_visibile(asns):
    """
    Given a moas event, returns the ASN with most visibility
    Sample imput 9930,2 65535,1
    """
    
    toks=asns.split()
    max_vis=0;
    max_asn=-99
    for i in toks:
        vis=i.split(',')[-1]
        if vis > max_vis:
            max_vis=vis
            max_asn=i.split(',')[0]
    return max_asn
    
def get_moas_change(current,prev):
    """
    Check what asns were changed for an ongoing MOAS"
    
    """
    asns_current=[i.split(',')[0] for i in current.split()]
    asns_prev=[i.split(',')[0] for i in prev.split()]
    removed=[]
    new=[]

    #ASNS added
    for i in asns_current:
        if i not in asns_prev:
            new.append(i)

    #ASNS removed
    for i in asns_prev:
        if i not in asns_current:
            removed.append(i)
            
    return removed,new




#Reading file from reader
file=reader.find_latest()
#f=gzip.open(file)
f=open(file)
lines=f.readlines()
#print lines

##
prev_line=""
for line in lines:
    new_moas=0
    if "NEW" in line and "FINISHED"  in prev_line:
        toks=line.split("|")
        toks_prev=prev_line.split("|")
        if toks[1]==toks_prev[1]: #same prefix in both lines?
            print prev_line
            print line
            removed,new=get_moas_change(toks[-1],toks_prev[-1])
            print_diag(toks[1])
            try:
                for i in removed:
                    for asn_info in moas_dict[toks[1]]:
                        if asn_info.asn==i:
                            asn_info.etime=toks[0]
                            asn_info.status=0
                            print "changed for",i
                for i in new:
                    moas_dict[toks[1]].append(Moas_pref(i,time,1,0))
                    print "changed do"
                    #print moas_dict[toks[1]]
                    print_diag(toks[1])
                        
            except:
                print "caught"  
                                  
                    
            #break
        else:
            new_moas=1

    if ("NEW" in line and "FINISHED" not in prev_line) or (new_moas==1): # what if finish is of diff prefix
        toks=line.split("|")
        prefix=toks[1]
        time=toks[0]
        """ New MOAS found """
        primary_asn=check_most_visibile(toks[-1])
        moas_dict[prefix]=[]
        moas_dict[prefix].append(Moas_pref(primary_asn,time,1,1))

 
    prev_line=line
    
    
    