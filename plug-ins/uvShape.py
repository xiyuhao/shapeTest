#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :uvShape.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.OpenMayaMPx as 



import maya.cmds as cmds
import maya.OpenMaya as om

cmds.polySphere(r= 1.0, ch=True)

sel = om.MSelectionList()
om.MGlobal.getActiveSelectionList(sel)
myMeshDagPath = om.MDagPath()
sel.getDagPath(0, myMeshDagPath)

myMeshFn = om.MFnMesh(myMeshDagPath)

myMeshVtxIt = om.MItMeshVertex(myMeshDagPath)
while not myMeshVtxIt.isDone():
    uCoords = om.MFloatArray()
    vCoords = om.MFloatArray()
    faceIDs = om.MIntArray()
    myMeshVtxIt.getUVs(uCoords, vCoords, faceIDs)
    newVertexPosition = om.MPoint(uCoords[0], 0.0, vCoords[0])
    myMeshVtxIt.setPosition(newVertexPosition, om.MSpace.kObject)
    myMeshVtxIt.next()


import maya.cmds as cmds
import maya.OpenMaya as om

cmds.polySphere(r= 1.0, ch=True)
cmds.polyPlane(w=1.0, sw=10, sh=10, ch=True)
cmds.select("pSphere1", "pPlane1")

sel = om.MSelectionList()
om.MGlobal.getActiveSelectionList(sel)
myOriginalDagPath = om.MDagPath()
myTargetDagPath = om.MDagPath()
sel.getDagPath(0, myOriginalDagPath)
sel.getDagPath(1, myTargetDagPath)

originalMeshFn = om.MFnMesh(myOriginalDagPath)

targetMeshVtxIt = om.MItMeshVertex(myTargetDagPath)
while not targetMeshVtxIt.isDone():
    uCoords = om.MFloatArray()
    vCoords = om.MFloatArray()
    faceIDs = om.MIntArray()
    targetMeshVtxIt.getUVs(uCoords, vCoords, faceIDs)
    newVertexPosition = om.MPoint(0.0, 0.0, 0.0)

    util = om.MScriptUtil()
    util.createFromDouble(uCoords[0], vCoords[0])
    uvCoord = util.asFloat2Ptr()

    for faceIdx in range(originalMeshFn.numPolygons()):
        try:    
            originalMeshFn.getPointAtUV(faceIdx, newVertexPosition, uvCoord, om.MSpace.kObject)
            break
        except:
            continue
    targetMeshVtxIt.setPosition(newVertexPosition, om.MSpace.kObject)
    targetMeshVtxIt.next()