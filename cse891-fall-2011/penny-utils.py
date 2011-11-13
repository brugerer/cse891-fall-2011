import csv, urllib

# makes dictionary from input url
def load_csv(url):
    d = {}
    fp = urllib.urlopen(url)
    for row in csv.DictReader(fp):
        key = row['date']
        value = row['fish']
        x = d.get(key,[])
        x.append(value)
        d[key] = x

    return d

# returns a dictionary that has fish as keys and corresponding dates as values
def make_dates_dict(fish_dict):
    dates_d = {}
    name_list = []
    for name in fish_dict:

        for x in fish_dict[name]:
            key = x
            name_list = dates_d.get(key,[])
            name_list.append(name)
            list_short = set(name_list)
            back_list = list(list_short)
            dates_d[key] = back_list

    return dates_d
    
# returns list of fishes consumed on a given date
def get_fishes_by_date(fish_dict,date):
    fishlist = []

    for name in fish_dict:
        if date == name:    
            fishlist.append(fish_dict[name])
        else:
            pass

    fishset = set(fishlist[0])
    fish_l = list(fishset)
    print "The types of fish eaten on", date, "were:", fish_l
    return fish_l
    

# returns list of dates on which a given fish was eaten by Penny    
def get_dates_by_fish(dates_d, fish):
    dateslist = []
    
    for name in dates_d:
        if fish == name:
            dateslist.append(dates_d[name])
        else:
            pass

    dateset = set(dateslist[0])
    date_list = list(dateset)            

    print "The dates that", fish, "was eaten on were:", date_list
    return date_list

def get_fishes_by_datelist(fish_d, datelist):
    #print 'get fishes by datelist'
    #mainlist = []
    
    for i in range(0,len(datelist)):
        fishsub = []
        #print i
        #print len(datelist)
        for name in fish_d:
            if name == datelist[i]:
                fishsub.append(fish_d[name])
            else:
                pass
        #mainlist.append(fishsub)
        #print len(mainlist)
    #print mainlist
    unnest_list = fishsub[0]
    print "get fishes by datelist:", unnest_list
    return unnest_list


def get_dates_by_fishlist(dates_d, fishlist):
    #print 'get dates by fishlist'

    #mainlist = []
    #print "input list",len(fishlist)
    for i in range(0,len(fishlist)):
        datesub = []
        #print i
        #print "sublist",len(datesub)
        for name in dates_d:
            if name == fishlist[i]:
                datesub.append(dates_d[name])
                #print "sublist", len(datesub)
            else:
                pass
        #mainlist.append(datesub)
        #print "endlist",len(mainlist)

    #print mainlist
    #print "sub", datesub
    retry = datesub[0]
    #print "re", retry
    print "get dates by list of fish:", retry
    return retry


fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')

dates_d = make_dates_dict(fish_d)

print get_fishes_by_datelist(fish_d, get_dates_by_fish(dates_d, 'plaice'))
print get_dates_by_fishlist(dates_d, get_fishes_by_date(fish_d, '11/30'))


# test 1
x = get_fishes_by_date(fish_d, '1/1')
assert 'salmon' in x

###

# test 2
x = get_dates_by_fish(dates_d, 'salmon')
assert '1/1' in x
assert '1/2' in x

###

# test 3
x = get_fishes_by_datelist(fish_d, ['1/1'])
assert 'salmon' in x, x

###

# test 4
x = get_dates_by_fishlist(dates_d, ['salmon'])
assert '6/29' in x, x
