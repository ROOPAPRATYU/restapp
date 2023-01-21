try:
            ind=datelist.index(date1)
            dateval=datelist[ind]
            print(dateval)
                    
        except:
            dateval=0
            print(dateval)
                
        try:
            tnum=int(tnum)
            print('num is',tnum)
            xx=tlist.index(tnum)
            print('num',xx)
            tabval1=tlist[xx]
            print(tabval1)
                    
        except:
            tabval1=0
            print(tabval1)
            
        try:
            hotelname=str(hotelname)
            indexh=hotellist.index(hotelname)
            hotelval=hotellist[indexh]
            print(hotelval)
                    
        except:
            hotelval=serch
