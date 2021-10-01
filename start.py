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
  # IHR=IHR/1000
  mul=0
  num_units=unitP[:,0].shape[0]
  # print(num_units)
  for i in range(0,num_units):
  #  print(IHR[i])
  #  print(P[i,1])
    mul=mul+ P[i,1]*(IHR[i])
 # print('mul',mul)
  Pcost=mul
  print(P)
  return Pcost


# a=np.array([1,2,3])
# print(a.shape[0])
# combinaton=np.array([1,0,0,1])
IHR=np.array([20.88,18.0,17.46,23.8])

Pcost =calculatePcost(np.array([1,1,1,1]),check,450,IHR,2)
print('Pcost')
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
  # print('CC',end=' ')
  # print(K)
  K=int(K)
  L=int(L)
  CC=UCM[K,2:lc]
  PC=UCM[L,2:lc]
  print(CC)
  print(PC)
  
  Pcost = calculatePcost(CC, unitP, totallP, IHR, fuelCost);
  nld=0
  for i in range(0,len(CC)):
    if CC[i]==1:
      Pcost+=noLoadCost[i]
      nld+=noLoadCost[i]
 # Pcost = Pcost + CC * noLoadCost;
  # print('nld',nld )
  #calculate Scost
  Scost=0
  
  if K!=L:
    Scost=calculateScost(CC,PC,startFromCold)
  
  Fcost=Pcost+Scost


  return Fcost

NLC = units[:, 4]
SUC = unit_status[:, 3]
Fcost=calculateFcost(UCM,1,0,15,12,check,450,IHR,2,NLC,SUC)
print('Fcost')
print(Fcost)
print(type(Fcost))




























# unitsNum = units[:,0].shape[0] # no of units
# print(unitsNum)

# #calculating different Combination if Units 
# UCM = unitCombination(unitsNum, units)


# startCombination = 12 # L=12
# numOfTimes = 8

# #sorting Units by Full-Load Avg cost [Priority ordering]
# print(units)
# sortedUnits = check

# #final result matrix

# result = np.zeros((UCM.shape[0], 8))
# resultCombination = np.zeros((UCM.shape[0], 8))
# print(result)

# IHR = units[:, 4] # Incremental Heat Rate
# NLC = units[:, 5] # No-Load Cost
# FC = fuel_cost    #Fuel Cost
# SUC = unit_status[:, 4] # Start-Up Cost : Cold

# #calculating Fcost for time 0 to 1
# load = load_pattern[0,1]  # Power that load need it in first hour
# for i in range(UCM.shape[1]-1 ,-1,-1):
#   if UCM[i][1]<load:
#     break

#   # total cost for stage 1
#   result[i][0]=calculateFcost(UCM,1,0,UCM[i][0],12,sortedUnits,load,IHR,FC,NLC,SUC)

#   #minimum combination of Fcost for stage 1

#   resultCombination[i][0]=startCombination

# for t in range(1,numOfTimes):
#   load=load_pattern[t][1] # Power that load need it

#   for i in range(UCM.shape[1],-1,-1):
#     if UCM[i][1]<load:
#       break

#     minFcost=0
#     minFcostCombination=0

#     for j in range(0,UCM.shape[1]):

#       if result[j][t-1]==0:
#         continue

#       Fcost=calculateFcost(UCM,t,t-1,UCM[i][0],UCM[j][0],sortedUnits,load,IHR,FC,NLC,SUC) + result[j][t-1]

#       if minFcost==0:
#         minFcost=Fcost
#         minFcostCombination=j-1
#       elif minFcost>Fcost:
#         minFcost=Fcost
#         minFcostCombination=j-1


#     #save total cost
#     result[i][t]=minFcost

#     #save minimum combination for cost
#     resultCombination[i][t]=minFcostCombination

# #printing result
# print('############## Minimum Total Cost of every Stage #############')

# print(result)
# print(resultCombination)

# for i in range(0,result[1,:].shape[0]):
#   print(i,end=' ')

# print(end='\n')

# for i in range(0,result.shape[0]):
#   print(UCM[i][0],end=' ')
#   for k in range(2,UCM[0,:].shape[0]):
#     print(UCM[i][k])

#   print(end=' ')

#   for j in range(0,result[0,:].shape[0]):
#     print(result[i][j],end=' ')

#   print(end='\n')

# print('##### Minimum Combination to every Stage ####')

# for i in range(0, result[1,:].shape[0]):
#   print(i,end=' ')

# print(end='\n')

# for i in range(0,result.shape[0]):
#   print(UCM[i][0],end=' ')

#   for k in range(2,UCM[1,:].shape[0]):
#     print(UCM[i][k])

#   print(end=' ')

#   for j in range(0, result[0,:].shape[0]):
#     print(resultCombination[i][j],end=' ')

#   print(end='\n')

# bestCombination=np.zeros((numOfTimes,1))
# for i in range(0,numOfTimes):

#   minOfFcost=0
#   minCombination=0
#   for j in range(result.shape[0]-1,-1,-1):
#     Fcost=result[j][i]
#     if Fcost>0:
#       if minOfFcost==0:
#         minFcost=Fcost
#         minCombination=resultCombination[j][i]
#       elif minOfFcost>Fcost:
#         minOfFcost=Fcost
#         minCombination=resultCombination[j][i]

#   bestCombination[i]=minCombination

# print('#### Best Combination of every stage ####')
# for i in range(0,result[1,:].shape[0]):
#   print(str(i-1)+'->'+str(),end=' ')

# print(end='\n')

# for i in range(0,result[1,:].shape[0]):
#   if (i==(result[1,:].shape[0]-1)):
#     print(str(bestCombination)+'->'+str(startCombination),end=' ')
#   else:
#     print(str(bestCombination)+'->'+str(bestCombination[i+1]),end=' ')

# print(end='\n')



# ####UPDATED

# unitsNum = units[:,0].shape[0] # no of units
# print(unitsNum)

# #calculating different Combination if Units 
# UCM = unitCombination(unitsNum, units)


# startCombination = 12 # L=12
# numOfTimes = 8

# #sorting Units by Full-Load Avg cost [Priority ordering]
# print(units)
# sortedUnits = check

# #final result matrix

# print('tuple shape')
# print(UCM.shape)

# result = np.zeros((max(UCM.shape), 8))
# print('result shape')
# print(result.shape)
# resultCombination = np.zeros((max(UCM.shape), 8))
# print(result)

# IHR = units[:, 3] # Incremental Heat Rate
# NLC = units[:, 4] # No-Load Cost
# FC = fuel_cost    #Fuel Cost
# SUC = unit_status[:, 3] # Start-Up Cost : Cold

# #calculating Fcost for time 0 to 1
# load = load_pattern[0][1]  # Power that load need it in first hour
# for i in range(UCM.shape[1]-1 ,-1,-1):
#   if UCM[i][1]<load:
#     break

#   # total cost for stage 1
#   result[i][0]=calculateFcost(UCM,1,0,UCM[i][0],12,sortedUnits,load,IHR,FC,NLC,SUC)

#   #minimum combination of Fcost for stage 1

#   resultCombination[i][0]=startCombination

# for t in range(1,numOfTimes):
#   load=load_pattern[t][1] # Power that load need it

#   for i in range(max(UCM.shape)-1,-1,-1):
#     if UCM[i][1]<load:
#       break

#     minFcost=0
#     minFcostCombination=0

#     for j in range(0,max(UCM.shape)):

#       if result[j][t-1]==0:
#         continue

#       Fcost=calculateFcost(UCM,t,t-1,UCM[i][0],UCM[j][0],sortedUnits,load,IHR,FC,NLC,SUC) + result[j][t-1]

#       if minFcost==0:
#         minFcost=Fcost
#         minFcostCombination=j-1
#       elif minFcost>Fcost:
#         minFcost=Fcost
#         minFcostCombination=j-1


#     #save total cost
#     result[i][t]=minFcost

#     #save minimum combination for cost
#     resultCombination[i][t]=minFcostCombination

# #printing result
# print('############## Minimum Total Cost of every Stage #############')

# print(result)
# print(resultCombination)

# for i in range(0,max(result[1,:].shape)):
#   print(i,end=' ')

# print(end='\n')

# for i in range(0,max(result.shape)):
#   print(UCM[i][0],end=' ')
#   for k in range(2,max(UCM[0,:].shape)):
#     print(UCM[i][k])

#   print(end=' ')

#   for j in range(0,max(result[0,:].shape)):
#     print(result[i][j],end=' ')

#   print(end='\n')

# print('##### Minimum Combination to every Stage ####')

# for i in range(0, max(result[1,:].shape)):
#   print(i,end=' ')

# print(end='\n')

# for i in range(0,max(result.shape)):
#   print(UCM[i][0],end=' ')

#   for k in range(2,max(UCM[1,:].shape)):
#     print(UCM[i][k])

#   print(end=' ')

#   for j in range(0, max(result[0,:].shape)):
#     print(resultCombination[i][j],end=' ')

#   print(end='\n')

# bestCombination=np.zeros((numOfTimes,1))
# for i in range(0,numOfTimes):

#   minOfFcost=0
#   minCombination=0
#   for j in range(max(result.shape)-1,-1,-1):
#     Fcost=result[j][i]
#     if Fcost>0:
#       if minOfFcost==0:
#         minFcost=Fcost
#         minCombination=resultCombination[j][i]
#       elif minOfFcost>Fcost:
#         minOfFcost=Fcost
#         minCombination=resultCombination[j][i]

#   bestCombination[i]=minCombination

# print('#### Best Combination of every stage ####')
# for i in range(0,max(result[1,:].shape)):
#   print(str(i-1)+'->'+str(),end=' ')

# print(end='\n')

# for i in range(0,max(result[1,:].shape)):
#   if (i==(result[1,:].shape[0]-1)):
#     print(str(bestCombination)+'->'+str(startCombination),end=' ')
#   else:
#     print(str(bestCombination)+'->'+str(bestCombination[i+1]),end=' ')

# print(end='\n')



# ###updated 2
# def calculatePcost(combination,unitP,totallP,IHR,fuelCost):
#   #here combination is 1-d Array/vector
#   #len_of_combination = len(combination ) or combination.shape[0]

#   P=np.zeros((unitP[:,0].shape[0],2))
#   P[:,0]=unitP[:,0]#all units in sorted order
#   # print(P)
#   # print(type(P[0,0]))
#   # print(int(P[0,0]))

#   #here P[n,1] represent sharing load for nth unit

#   for i in range(0,len(combination)):
#     # print(unitP[i,0])
#     # print(type(unitP[i,0]))
#     # print(int(unitP[i,0]))

#     #for 0-indexed
#     if combination[int(unitP[i,0])-1]==1:
#       P[i,1]=int(unitP[i,2])
#   print(P)

#   #first we'll run all units at minimum than one by one run at maximum 
# #starting from units (according to sorted)

#   smOfP=P.sum(axis=0)
#   print(smOfP)
#   if smOfP[1]!=totallP:
#     for n in range(0,len(combination)):
#       # print(len(combinaton))
#       sumP=smOfP[1]
#       if sumP==totallP:
#         break
#       elif combination[int(P[n,0])-1]==1:
#         P[n,1]=unitP[n,1]#unit[n,1]=max generation by unit n
#         print(P)
#         smOfP=P.sum(axis=0)
#         print(smOfP)
#         sumP=smOfP[1]
#         print(sumP)
#         if sumP>totallP:
#           P[n,1]=P[n,1]-(sumP-totallP)# sharing load for nth unit
      
#   P=P[P[:,0].argsort()]# again arranged in 0,1,3,...n units order
#   # IHR=IHR/1000
#   mul=0
#   num_units=unitP[:,0].shape[0]
#   # print(num_units)
#   for i in range(0,num_units):
#   #  print(IHR[i])
#   #  print(P[i,1])
#     mul=mul+ P[i,1]*(IHR[i])
#  # print('mul',mul)
#   Pcost=mul
#   print(P)
#   return Pcost


# # a=np.array([1,2,3])
# # print(a.shape[0])
# # combinaton=np.array([1,0,0,1])
# IHR=np.array([20.88,18.0,17.46,23.8])

# Pcost =calculatePcost(np.array([1,1,1,1]),check,450,IHR,2)
# print('Pcost')
# print(Pcost)



# def calculateScost(CC,PC,startFromCold):
#   Scost=0
#   for i in range(0,len(CC)):
#     if CC[i]!=PC[i]:
#       Scost=Scost+startFromCold[i]

#   return Scost


# # print(UCM[:,1:3])
# def calculateFcost(UCM,CJ,PJ,K,L,unitP,totallP,IHR,fuelCost,noLoadCost, startFromCold):
#   # calculate Pcost
#   lc=len(UCM[0,:])
#   print('CC',end=' ')
#   print(K)

#   CC=UCM[K,2:lc]
#   PC=UCM[L,2:lc]
#   print(CC)
#   print(PC)
  
#   Pcost = calculatePcost(CC, unitP, totallP, IHR, fuelCost);
#   nld=0
#   for i in range(0,len(CC)):
#     if CC[i]==1:
#       Pcost+=noLoadCost[i]
#       nld+=noLoadCost[i]
#  # Pcost = Pcost + CC * noLoadCost;
#   # print('nld',nld )
#   #calculate Scost
#   Scost=0
  
#   if K!=L:
#     Scost=calculateScost(CC,PC,startFromCold)
  
#   Fcost=Pcost+Scost


#   return Fcost

# NLC = units[:, 4]
# SUC = unit_status[:, 3]
# Fcost=calculateFcost(UCM,1,0,15,12,check,450,IHR,2,NLC,SUC)
# print('Fcost')
# print(Fcost)
# print(type(Fcost))

