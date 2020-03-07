import numpy,matplotlib
from matplotlib import pyplot as plt

def render(x,cmap='seismic'):
    plt.figure(figsize=(15,1)); plt.axis('off')
        
    if x.ndim==4:
        plt.imshow(x.transpose(2,0,3,1).reshape([32,15*32,3])*0.5+0.5)

    if x.ndim==3:
        m = numpy.abs(x).max()
        plt.imshow(x.transpose(1,0,2).reshape([32,15*32]),cmap=cmap,vmin=-m,vmax=m)
    
    plt.show()

