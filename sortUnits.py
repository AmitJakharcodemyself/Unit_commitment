def sortedUnits(units):
  a=units.shape[0];
  sortedUnits_ar=np.zeros((a,4))
  sortedUnits_ar[:,0]=units[:,0]
  sortedUnits_ar[:,1]=units[:,1]
  sortedUnits_ar[:,2]=units[:,2]
  sortedUnits_ar[:,3]=units[:,5]
  sortedUnits_ar=sortedUnits_ar[sortedUnits_ar[:,3].argsort()]
  return sortedUnits_ar

check=sortedUnits(units)
print(check)
