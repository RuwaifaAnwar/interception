#Module for AS rank

as_rank={}
#reads as rank file and stores relations in dict
with open("/home/rufy/Dropbox/research/sim2/siblings/consolidated.txt") as file:
    for line in file:
        str1=line.split('|')
        provider=int(str1[0])	
        customer=int(str1[1])	
        relation=int(str1[2])
        if customer > 600000 or provider > 600000:
            continue
        if provider not in as_rank:
            as_rank[provider]={}
            as_rank[provider][customer]=relation
        else:
            as_rank[provider][customer]=relation


def find_relation(as1,as2):
    """ 
    Given two ASNs returns relation according to ASrank
    """
    global as_rank 
    if as1 in as_rank and as2 in as_rank[as1]:
        if as_rank[as1][as2]==-1:
            return "p-c"
        else:
            return "p-p"
    if as2 in as_rank and as1 in as_rank[as2]:
        if as_rank[as2][as1]==-1:
            return "c-p"
        else:
            return "p-p"
    return "Missing"      


if __name__ == "__main__":
    import sys