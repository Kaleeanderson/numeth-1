import numpy as np
import matplotlib.pyplot as plt

forplottime = np.zeros((10000))
energy=np.zeros((10000))
forplotenergy = np.zeros((10000))

g = -6.674e-8

#filenames = ['mercpos.txt','venuspos.txt','earthpos.txt','marspos.txt','juppos.txt']

#x,y,z,vx,vy,vz,time,mass
mx,my,mz,mvx,mvy,mvz,mt,mmass = np.loadtxt('data_1.txt',skiprows=1,unpack=True)
ex,ey,ez,evx,evy,evz,et,emass = np.loadtxt('data_3.txt',skiprows=1,unpack=True)    
vx,vy,vz,vvx,vvy,vvz,vt,vmass = np.loadtxt('data_2.txt',skiprows=1,unpack=True)
wx,wy,wz,wvx,wvy,wvz,wt,wmass = np.loadtxt('data_4.txt',skiprows=1,unpack=True)
jx,jy,jz,jvx,jvy,jvz,jt,jmass = np.loadtxt('data_5.txt',skiprows=1,unpack=True)
sx,sy,sz,svx,svy,svz,st,smass = np.loadtxt('data_6.txt',skiprows=1,unpack=True)

#note mars is now w
for i in range(len(mt)):
	#kinetic
	mk = mmass[i]*(mx[i]**2 + my[i]**2 + mz[i]**2)/2
	vk = vmass[i]*(vx[i]**2 + vy[i]**2 + vz[i]**2)/2
	ek = emass[i]*(ex[i]**2 + ey[i]**2 + ez[i]**2)/2
	wk = wmass[i]*(wx[i]**2 + wy[i]**2 + wz[i]**2)/2
	jk = jmass[i]*(jx[i]**2 + jy[i]**2 + jz[i]**2)/2
	sk = smass[i]*(sx[i]**2 + sy[i]**2 + sz[i]**2)/2
	#potental
	mv = g*mmass[i]*vmass[i]/(np.sqrt((mx[i]-vx[i])**2 + (my[i]-vy[i])**2 + (mz[i]-vz[i])**2))
	me = g*mmass[i]*emass[i]/(np.sqrt((mx[i]-ex[i])**2 + (my[i]-ey[i])**2 + (mz[i]-ez[i])**2))
	mw = g*mmass[i]*wmass[i]/(np.sqrt((mx[i]-wx[i])**2 + (my[i]-wy[i])**2 + (mz[i]-wz[i])**2))
	mj = g*mmass[i]*jmass[i]/(np.sqrt((mx[i]-jx[i])**2 + (my[i]-jy[i])**2 + (mz[i]-jz[i])**2))
	ms = g*mmass[i]*smass[i]/(np.sqrt((mx[i]-sx[i])**2 + (my[i]-sy[i])**2 + (mz[i]-sz[i])**2))
	ve = g*emass[i]*vmass[i]/(np.sqrt((ex[i]-vx[i])**2 + (ey[i]-vy[i])**2 + (ez[i]-vz[i])**2))
	vw = g*wmass[i]*vmass[i]/(np.sqrt((wx[i]-vx[i])**2 + (wy[i]-vy[i])**2 + (wz[i]-vz[i])**2))
	vj = g*jmass[i]*vmass[i]/(np.sqrt((jx[i]-vx[i])**2 + (jy[i]-vy[i])**2 + (jz[i]-vz[i])**2))
	vs = g*smass[i]*vmass[i]/(np.sqrt((sx[i]-vx[i])**2 + (sy[i]-vy[i])**2 + (sz[i]-vz[i])**2))
	ew = g*emass[i]*wmass[i]/(np.sqrt((ex[i]-wx[i])**2 + (ey[i]-wy[i])**2 + (ez[i]-wz[i])**2))
	ej = g*emass[i]*jmass[i]/(np.sqrt((ex[i]-jx[i])**2 + (ey[i]-jy[i])**2 + (ez[i]-jz[i])**2))
	es = g*emass[i]*smass[i]/(np.sqrt((ex[i]-sx[i])**2 + (ey[i]-sy[i])**2 + (ez[i]-sz[i])**2))
	wj = g*wmass[i]*jmass[i]/(np.sqrt((wx[i]-jx[i])**2 + (wy[i]-jy[i])**2 + (wz[i]-jz[i])**2))
	ws = g*wmass[i]*smass[i]/(np.sqrt((wx[i]-sx[i])**2 + (wy[i]-sy[i])**2 + (wz[i]-sz[i])**2))
	js = g*jmass[i]*smass[i]/(np.sqrt((jx[i]-sx[i])**2 + (jy[i]-sy[i])**2 + (jz[i]-sz[i])**2))
	
	forplottime[i]=mt[i]
	energy[i]=mk+vk+ek+wk+jk+sk+mv+me+mw+mj+ms+ve+vw+vj+vs+ew+ej+es+wj+ws+js

#abs value of fractional change in total energy
for j in range(len(mt)):
	forplotenergy[j] = abs((energy[j]-energy[0])/energy[0])
	
fig=plt.figure()
plt.scatter(forplottime[:],forplotenergy[:],color='cornflowerblue');
#plt.plot(forplottime[:],forplotenergy[:],color='magenta');
plt.title(' Leapfrog energy')
fig.savefig('leapfrogenergy.png')
# numeth
# numeth
