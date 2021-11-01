import numpy as np

def calculate(list):

  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")

  vector=np.array(list)
  matriz=vector.reshape(3,3)
  v1=matriz[0,:]
  v2=matriz[1,:]
  v3=matriz[2,:]

  h1=matriz[:,0]
  h2=matriz[:,1]
  h3=matriz[:,2]

  axis1_mean=([h1.mean(),h2.mean(),h3.mean()])
  axis2_mean=([v1.mean(),v2.mean(), v3.mean()])
  flattened_mean=matriz.mean()
  Mean=[axis1_mean, axis2_mean, flattened_mean]
  

  axis1_std=([h1.std(),h2.std(),h3.std()])
  axis2_std=([v1.std(),v2.std(),v3.std()])
  flattened_std=matriz.std()
  Desviation=[axis1_std, axis2_std, flattened_std]

  axis1_var=([h1.var(),h2.var(), h3.var()])
  axis2_var=([v1.var(),v2.var(), v3.var()])
  flattened_var=matriz.var()
  Variance=[axis1_var, axis2_var, flattened_var]

  Maximun=([[h1.max(),h2.max(), h3.max()],[v1.max(), v2.max(), v3.max()],matriz.max()])
  Minimun=([[h1.min(),h2.min(), h3.min()],[v1.min(), v2.min(), v3.min()],matriz.min()])
  Sum=([[h1.sum(),h2.sum(), h3.sum()],[v1.sum(), v2.sum(), v3.sum()],matriz.sum()])

  calculations= {'mean':Mean,'variance':Variance,'standard deviation':Desviation, 'max':Maximun, 'min':Minimun, 'sum':Sum}

  return calculations


  