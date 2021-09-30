def calculatePcost(combination,unitP,totallP,IHR,fuelCost):
  #here combination is 1-d Array/vector
  #len_of_combination = len(combination ) or combination.shape[0]

  P=np.zeros((unitP[:,0].shape[0],2))
  P[:,0]=unitP[:,0]#all units in sorted order
  # print(P)
  # print(type(P[0,0]))
  # print(int(P[0,0]))

  #here P[n,1] represent sharing load for nth unit

  for i in range(0,len(combination)):
    # print(unitP[i,0])
    # print(type(unitP[i,0]))
    # print(int(unitP[i,0]))

    #for 0-indexed
    if combination[int(unitP[i,0])-1]==1:
      P[i,1]=int(unitP[i,2])
  print(P)

  #first we'll run all units at minimum than one by one run at maximum 
#starting from units (according to sorted)

  smOfP=P.sum(axis=0)
  print(smOfP)
  if smOfP[1]!=totallP:
    for n in range(0,len(combination)):
      # print(len(combinaton))
      sumP=smOfP[1]
      if sumP==totallP:
        break
      elif combination[int(P[n,0])-1]==1:
        P[n,1]=unitP[n,1]#unit[n,1]=max generation by unit n
        print(P)
        smOfP=P.sum(axis=0)
        print(smOfP)
        sumP=smOfP[1]
        print(sumP)
        if sumP>totallP:
          P[n,1]=P[n,1]-(sumP-totallP)# sharing load for nth unit
      
  P=P[P[:,0].argsort()]# again arranged in 0,1,3,...n units order
  IHR=IHR/1000
  mul=0
  num_units=unitP[:,0].shape[0]
  # print(num_units)
  for i in range(0,num_units):
    print(IHR[i])
    print(P[i,1])
    mul=mul+ P[i,1]*(IHR[i])
  print('mul',mul)
  Pcost=mul
  print(P)
  return Pcost


# a=np.array([1,2,3])
# print(a.shape[0])
# combinaton=np.array([1,0,0,1])
IHR=np.array([20.88,18.0,17.46,23.8])

Pcost =calculatePcost(np.array([1,1,1,1]),check,450,IHR,2)
print(Pcost)



def calculateScost(CC,PC,startFromCold):
  Scost=0
  for i in range(0,len(CC)):
    if CC[i]!=PC[i]:
      Scost=Scost+startFromCold[i]

  return Scost


# print(UCM[:,1:3])
def calculateFcost(UCM,CJ,PJ,K,L,unitP,totallP,IHR,fuelCost,noLoadCost, startFromCold):
  # calculate Pcost
  lc=len(UCM[0,:])
  CC=UCM[K,2:lc]
  PC=UCM[L,2:lc]
  Pcost = calculatePcost(CC, unitP, totallP, IHR, fuelCost);
  Pcost = Pcost + CC * noLoadCost;

  #calculate Scost
  Scost=0
  
  if K!=L:
    Scost=calculateScost(CC,PC,startFromCold)
  
  Fcost=Pcost+Scost


  return Fcost
  
