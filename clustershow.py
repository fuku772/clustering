#!/usr/bin/env python3
import sys,re,argparse
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d

def clusterplot(clusterdf,title='cluster'):
	noods=list()
	alist=[]
	for index,i in clusterdf.iterrows():
		if index==0:
			continue
		#front_indexの行列
		front_idx=i.loc['front_index']
		#front_index,x,y,zの行列
		a=clusterdf.loc[front_idx].loc['x':'z']
		#num,x,y,zの行列
		b=i.loc['x':'z']
		alist.append([front_idx])
		noods.append(([a.x,b.x],[a.y,b.y],[a.z,b.z]))

	#print(alist)
	#print(clusterdf)

	fig = plt.figure(figsize = (12, 12))
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(clusterdf.x,clusterdf.y,clusterdf.z)
	ax.set_xlim(-5,5)
	ax.set_ylim(-5,5)
	ax.set_zlim(-5,5)
	for index,i in clusterdf.iterrows():
		text=i.atom+'_'+str(i.isite)
		ax.text(i.x,i.y,i.z,text)
	for nood in noods:
		line = art3d.Line3D(*nood)
		ax.add_line(line)
	fig.suptitle(title)
	plt.show()
	plt.close()
	


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('csvn')
	parser.add_argument('-e','--explanation', default=False)
	args = parser.parse_args()

	if args.explanation:
		print('''-csvn : /cluster_0_0.csv''')
		sys.exit()
	df=pd.read_csv(args.csvn,index_col=0)
	showname=re.split('/',args.csvn)[-1].replace('.csv','')
	clusterplot(df,title=showname)

if __name__ == '__main__':
	main()
