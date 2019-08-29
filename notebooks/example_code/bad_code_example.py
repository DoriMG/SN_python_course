from sklearn.decomposition import NMF

import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from scipy import *

folder = "C:\\Users\\Dori\\Dropbox (Brain Energy Lab)\\Everything\\dori\\data\\BehaviourOnWheel\\Sawk\\20190404"
#folder = "C:\\Users\\Dori\\Dropbox (Brain Energy Lab)\\Everything\\dori\\data\\BehaviourOnWheel\\Sawk\\20190304"
#folder = "C:\\Users\\Dori\\Documents\\OIST\\20190218_09_38_05_R1spont\\cellsort\\"
#traces = scipy.io.loadmat(os.path.join(folder,'suite2p\\spikes.mat'))['traces']
traces = scipy.io.loadmat(os.path.join(folder,'suite2p\\traces.mat'))['traces']
#traces = traces-traces.min(axis=1,keepdims=True)
X = traces
X[X<0] = 0
traces.shape


Locomotion = scipy.io.loadmat([folder,'\\', 'locomotion.mat']))['loco']
vel = np.diff(Locomotion, axis=0)
vel = np.insert(vel, 0, 0)
vel[vel<-0.2/7.51] = 0
vel[vel>0.5/7.51] = 0


model = NMF(n_components=3, init='random', random_state=0)
W = model.fit_transform(X)
H = model.components_

plt.figure()
plt.plot(H[0,:].T,)#color=colors[i] )
plt.xlabel('Frames')
plt.ylabel('Component 1 weight')

plt.figure()
plt.plot(H[1,:].T,)#color=colors[i] )
plt.xlabel('Frames')
plt.ylabel('Component 1 weight')

plt.figure()
plt.plot(H[2,:].T,)#color=colors[i] )
plt.xlabel('Frames')
plt.ylabel('Component 1 weight')

for h in H:
    






