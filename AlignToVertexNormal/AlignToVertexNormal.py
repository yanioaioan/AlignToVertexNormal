'''create a sphere, place cubes on each of the sphere's vertex position, 
find average vertex normal of the sphere's vertex position (based on surrounding faces),
 transform normal from cartesian to spherical coordinates, rotate the placed cube according this
'''

import maya.cmds as cmds
cmds.select(all=True)
cmds.delete()


def getVtxPos( shapeNode ) :
 
	vtxWorldPosition = []    # will contain positions un space of all object vertex
 
	vtxIndexList = cmds.getAttr( shapeNode+".vrts", multiIndices=True )
 
	for i in vtxIndexList :
		curPointPosition = cmds.xform( str(shapeNode)+".pnts["+str(i)+"]", query=True, translation=True, worldSpace=True )    # [1.1269192869360154, 4.5408735275268555, 1.3387055339628269]
		vtxWorldPosition.append( curPointPosition )
 
	return vtxWorldPosition

s=cmds.polySphere()
vertexposlist=getVtxPos(s[0])

'''
for i in vertexposlist:
	cmds.polyCube()
	cmds.scale(0.1,0.1,0.1)
	cmds.move(i[0],i[1],i[2])
'''

for i in range(len(vertexposlist)):
	cmds.select(s[0]+'.vtx['+str(i)+']', r=True)
	surroundingfaceNormals=cmds.polyNormalPerVertex( query=True, xyz=True )
	print "surroundingfaceNormals length=%d"%(len(surroundingfaceNormals))
	
	
	cube=cmds.polyCube()
	cmds.scale(0.05,0.05,0.05)
	cmds.move(vertexposlist[i][0],vertexposlist[i][1],vertexposlist[i][2])
	cmds.refresh()
	
	sumx=0
	sumy=0
	sumz=0
	for component in range(0,len(surroundingfaceNormals),3):
		sumx += surroundingfaceNormals[component]
		sumy += surroundingfaceNormals[component+1]
		sumz += surroundingfaceNormals[component+2]
		
		print "component=%d"%(component)
		print "component+1=%d"%(component+1)
		print "component+2=%d"%(component+2)
	
	avX =sumx / len(surroundingfaceNormals)/3
	avY =sumy / len(surroundingfaceNormals)/3
	avZ =sumz / len(surroundingfaceNormals)/3
	
	vertexnormal=[avX,avY,avZ]
		
	print 'total average of x dimension=%f'%(vertexnormal[0])
	print 'total average of y dimension=%f'%(vertexnormal[1])
	print 'total average of z dimension=%f'%(vertexnormal[2])
	
	
	cmds.select(cube[0])
	'''
	r = math.sqrt(vertexnormal[0]*vertexnormal[0] + vertexnormal[1]*vertexnormal[1] + vertexnormal[2]*vertexnormal[2])
	fi = (math.acos(vertexnormal[1])/r) * (180.0/math.pi) # acos(y/r)
	theta = math.atan2(vertexnormal[0],vertexnormal[2]) * (180.0/math.pi) #atan2(x,z)) 
	'''
	theta = (math.acos(vertexnormal[1])/r) * (180.0/math.pi) # acos(y/r)
	fi = math.atan2(vertexnormal[0],vertexnormal[2]) * (180.0/math.pi) #atan2(x,z)) 
	
	cmds.rotate(theta, fi, 0)
	



'''
import maya.cmds as cmds 

s=cmds.polySphere()

import maya.cmds as cmds

s=cmds.polySphere()

# To set the xyz values of normals of selected vertices:
v=cmds.polyNormalPerVertex(  )
# To set just the "x" value of normal of selected vertices:
cmds.polyNormalPerVertex( x=.37 )
# To add to the current value of the "y" normal value of selected vertices:
cmds.polyNormalPerVertex( rel=True, y=.13 )
# To query the normal values on selected vertices - This returns all normals
# regardless of whether they are shared or not:
normals=cmds.polyNormalPerVertex( query=True, xyz=True )





# To query if the normals on the selected vertices are locked or not
cmds.polyNormalPerVertex( query=True, freezeNormal=True )
# To query if all the normals on the selected vertices are locked or not
cmds.polyNormalPerVertex( query=True, allLocked=True )
# More examples
cmds.file( f=True, new=True )
cmds.polyCube()
cmds.select( 'pCube1.vtxFace[2][1]', r=True )
cmds.polyNormalPerVertex( query=True, freezeNormal=True )
# Result: 0 #
# Now, lock the normal of a VertexFace on the cube
cmds.select('pCube1.vtxFace[2][1]', r=True )
cmds.polyNormalPerVertex( xyz=(0.7071, 0, 0.7071) )
# Query if the normal is locked for this vertexFace
cmds.polyNormalPerVertex( query=True, freezeNormal=True )
# Result: 1 #
# Query if the normal is locked for all the normals on this vertex
# Should return 0, because there are some other normals on
# this vertex that are not locked.
for i in 
cmds.select('pPlane1.vtx[i]', r=True)
cmds.polyNormalPerVertex( query=True, xyz=True )
# Result: 0 #
'''


	

'''
# To average normals when they are within 0.2 distance.
cmds.polyAverageNormal( distance=0.2 )
# To average normals when they are within 0.2 distance.
# Normalize the normals before computing the average.
cmds.polyAverageNormal( distance=0.2, prenormalize=True )
# To averge normals when they are within 0.2 distance. Do not
# normalize the normals before computing the average (so to get weighted
# average). But do normalize the resulting normal.
cmds.polyAverageNormal( distance=0.2, postnormalize=True )
# To average normals when they are within 0.2 distance. Do not
# allow zero normal and replace zero normal with (1 0 0).
cmds.polyAverageNormal( distance=0.2, allowZeroNormal=False, replaceNormalXYZ=(1,0,0) )

'''


























        