tick_count=int(input())
count_of_pass-int(input())
trainlist=['MUM-GOA','DEL-MUM','LKO-KOL','MUM-DEL','GOA-MUM','KOL-LKO']
trainIdlist=[1221,2331,7654,5690,5463,9854]
trainpricegen=[100,200,300,400,500,600]
trainpricetat=[700,800,900,1000,1100,1200]
if t_type=='general':
    traintuple=((trainlist[0],trainIdlist[0],trainpricegen[0]),(trainlist[1],trainIdlist[1],trainpricegen[1]),(trainlist[2],trainIdlist[2],
                trainpricegen[2]),(trainlist[3],trainIdlist[3],trainpricegen[3]),
                (trainlist[4],trainIdlist[4],trainpricegen[4]),(trainlist[5],trainIdlist[5],trainpricegen[5]))
else:
    traintuple=((trainlist[0],trainIdlist[0],trainpricetat[0]),(trainlist[1],trainIdlist[1],trainpricetat[1]),(trainlist[2],trainIdlist[2],
                trainpricetat[2]),(trainlist[3],trainIdlist[3],trainpricetat[3]),
                (trainlist[4],trainIdlist[4],trainpricetat[4]),(trainlist[5],trainIdlist[5],trainpricetat[5]))
for i in range(tick_count):
    t_type = input()
    tr_typr = input()
    travel_dest = input()
    for j in range(count_of_pass):
        pass_id=int(input())
        name=input()
        age=int(input())
        print("Ticket fare is",)
