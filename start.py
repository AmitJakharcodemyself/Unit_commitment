unitsNum = units[:,0].shape[0] # no of units
print(unitsNum)

#calculating different Combination if Units 
UCM = unitCombination(unitsNum, units)


startCombination = 12 # L=12
numOfTimes = 8

#sorting Units by Full-Load Avg cost [Priority ordering]
print(units)
sortedUnits = check

#final result matrix

result = np.zeros((UCM.shape[0], 8))
resultCombination = np.zeros((UCM.shape[0], 8))
print(result)

IHR = units[:, 4] # Incremental Heat Rate
NLC = units[:, 5] # No-Load Cost
FC = fuel_cost    #Fuel Cost
SUC = unit_status[:, 4] # Start-Up Cost : Cold

#calculating Fcost for time 0 to 1
load = load_pattern[0,1]  # Power that load need it in first hour
for i in range(UCM.shape[1]-1 ,-1,-1):
  if UCM[i][1]<load:
    break

  # total cost for stage 1
  result[i][0]=calculateFcost(UCM,1,0,UCM[i][0],12,sortedUnits,load,IHR,FC,NLC,SUC)

  #minimum combination of Fcost for stage 1

  resultCombination[i][0]=startCombination

for t in range(1,numOfTimes):
  load=load_pattern[t][1] # Power that load need it

  for i in range(UCM.shape[1],-1,-1):
    if UCM[i][1]<load:
      break

    minFcost=0
    minFcostCombination=0

    for j in range(0,UCM.shape[1]):

      if result[j][t-1]==0:
        continue

      Fcost=calculateFcost(UCM,t,t-1,UCM[i][0],UCM[j][0],sortedUnits,load,IHR,FC,NLC,SUC) + result[j][t-1]

      if minFcost==0:
        minFcost=Fcost
        minFcostCombination=j-1
      elif minFcost>Fcost:
        minFcost=Fcost
        minFcostCombination=j-1


    #save total cost
    result[i][t]=minFcost

    #save minimum combination for cost
    resultCombination[i][t]=minFcostCombination

#printing result
print('############## Minimum Total Cost of every Stage #############')

print(result)
print(resultCombination)

for i in range(0,result[1,:].shape[0]):
  print(i,end=' ')

print(end='\n')

for i in range(0,result.shape[0]):
  print(UCM[i][0],end=' ')
  for k in range(2,UCM[0,:].shape[0]):
    print(UCM[i][k])

  print(end=' ')

  for j in range(0,result[0,:].shape[0]):
    print(result[i][j],end=' ')

  print(end='\n')

print('##### Minimum Combination to every Stage ####')

for i in range(0, result[1,:].shape[0]):
  print(i,end=' ')

print(end='\n')

for i in range(0,result.shape[0]):
  print(UCM[i][0],end=' ')

  for k in range(2,UCM[1,:].shape[0]):
    print(UCM[i][k])

  print(end=' ')

  for j in range(0, result[0,:].shape[0]):
    print(resultCombination[i][j],end=' ')

  print(end='\n')

bestCombination=np.zeros((numOfTimes,1))
for i in range(0,numOfTimes):

  minOfFcost=0
  minCombination=0
  for j in range(result.shape[0]-1,-1,-1):
    Fcost=result[j][i]
    if Fcost>0:
      if minOfFcost==0:
        minFcost=Fcost
        minCombination=resultCombination[j][i]
      elif minOfFcost>Fcost:
        minOfFcost=Fcost
        minCombination=resultCombination[j][i]

  bestCombination[i]=minCombination

print('#### Best Combination of every stage ####')
for i in range(0,result[1,:].shape[0]):
  print(str(i-1)+'->'+str(),end=' ')

print(end='\n')

for i in range(0,result[1,:].shape[0]):
  if (i==(result[1,:].shape[0]-1)):
    print(str(bestCombination)+'->'+str(startCombination),end=' ')
  else:
    print(str(bestCombination)+'->'+str(bestCombination[i+1]),end=' ')

print(end='\n')
