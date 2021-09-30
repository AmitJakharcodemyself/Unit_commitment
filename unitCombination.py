# unitCombination
import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

def createCombination(num):

  combination=int2base(num,2)
  if len(combination) ==1:
    combination='000'+combination
  elif len(combination)==2:
    combination='00'+combination
  elif len(combination)==3:
    combination='0'+combination
  return combination

def unitCombination(numOfUnit,unitsData):
  allPossibleCombination =pow(2,numOfUnit)
  UCM=np.zeros((allPossibleCombination,numOfUnit+2))
    #UCM->Capacity ordering of the Units
    
  for i in range(0,allPossibleCombination):
    combination=createCombination(i)
    sumOfPmax=0
    for n in range(0,numOfUnit):
      if combination[n]=='1':
        # 1 means nth unit is Commited and 0 means UnCommited
        UCM[i,n+2]=1
        sumOfPmax=sumOfPmax+unitsData[n,1]
    UCM[i,0]=i #no of state
    UCM[i,1]=sumOfPmax # Maximum Net capacity for Combination 
  UCM=UCM[UCM[:,1].argsort()]
  for i in range(0,allPossibleCombination):
    UCM[i,0]=i

  return UCM  
UCM=unitCombination(4,units)  
print(UCM)
