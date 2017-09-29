#include <maya/MString.h>

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MFnMessageAttribute.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MFnSkinCluster.h>
#include <maya/MFnMesh.h>
#include <maya/MItGeometry.h>
#include <maya/MMatrix.h>
#include <maya/MPlugArray.h>
#include <maya/MDagPathArray.h>
#include <maya/MDagPath.h>
#include <maya/MGlobal.h>

#include "splitShapeNode.h"

MTypeId SplitShapeNode::id(0xabc004);

MObject SplitShapeNode::oInputs;
MObject SplitShapeNode::oOrgMesh;
MObject SplitShapeNode::oSculptMesh;
MObject SplitShapeNode::oSkinMessage;

SplitShapeNode::SplitShapeNode()
{

};

SplitShapeNode::~SplitShapeNode()
{

};

void *SplitShapeNode::creator()
{
    SplitShapeNode *SSNode = new SplitShapeNode();
    SSNode->isInit = true;
    SSNode->isInputDirty = false;
    SSNode->isSkinDirty = false;
    SSNode->isSculptDirty = false;
    SSNode->isOrgDirty = false;
    return new SplitShapeNode();
};


MStatus SplitShapeNode::initialize()
{
    MFnNumericAttribute nAttr;
    MFnTypedAttribute tAttr;
    MFnMessageAttribute msAttr;

    oInputs = nAttr.create("weightInputs", "weightInputs", MFnNumericData::kFloat, 0.0);
    nAttr.setArray(true);
    nAttr.setKeyable(true);
    nAttr.setStorable(true);
    nAttr.setMin(0.0);
    nAttr.setMax(1.0);
    nAttr.setUsesArrayDataBuilder(true);
    addAttribute(oInputs);

    oOrgMesh = tAttr.create("orgMesh", "orgMesh", MFnData::kMesh);
    addAttribute(oOrgMesh);

    oSculptMesh = tAttr.create("sculptMesh", "sculptMesh", MFnData::kMesh);
    addAttribute(oSculptMesh);

    oSkinMessage = msAttr.create("skinWeight", "skinWeight");
    addAttribute(oSkinMessage);

    attributeAffects(oInputs, outputGeom);
    attributeAffects(oOrgMesh, outputGeom);
    attributeAffects(oSculptMesh, outputGeom);
    attributeAffects(oSkinMessage, outputGeom);


    return MS::kSuccess;
};

MStatus SplitShapeNode::deform(MDataBlock &block,
    MItGeometry &iter,
    const MMatrix &mat,
    unsigned int multiIndex)
{
    if (isInit == true)
    {
        moveVects.clear();
        orgPoints.clear();
        sculptPoints.clear();
        skinWeights.clear();
        inputValues.clear();
        isInit = false;
    }
    if (!block.isClean(outputGeom))
    {
        if (!block.isClean(oInputs) 
            || isInputDirty 
            || inputValues.length() == 0)
        {
            inputValues.clear();
            inputValues = getInputWeights(block, oInputs);
            isInputDirty = false;
            block.setClean(oInputs);
        }
        if (!block.isClean(oSkinMessage) 
            || isSkinDirty 
            || skinWeights.empty())
        {
            skinWeights.clear();
            MFnDependencyNode mfnThisObj(thisMObject());
            MPlug skinMessagePlug = mfnThisObj.findPlug(oSkinMessage);
            MPlug skinNodePlug = getFirstConnectedPlug(skinMessagePlug);
            if (!skinNodePlug.isNull())
            {
                skinWeights = getSkinWeights(skinNodePlug);
            }
            block.setClean(oSkinMessage);
            isSkinDirty = false;
        }
        if (!block.isClean(oOrgMesh) 
            || isOrgDirty 
            || orgPoints.length() == 0)
        {
            orgPoints.clear();
            orgPoints = getMeshPoints(block, oOrgMesh);
            block.setClean(oOrgMesh);
            isOrgDirty = false;
        }
        if (!block.isClean(oSculptMesh) 
            || isSculptDirty 
            || sculptPoints.length() == 0)
        {
            sculptPoints.clear();
            sculptPoints = getMeshPoints(block, oSculptMesh);
            block.setClean(oSculptMesh);
            isSculptDirty = false;
        }
        if (orgPoints.length() > 0
            && sculptPoints.length() >0 
            && orgPoints.length() == sculptPoints.length())
        {
            moveVects = subTwoPointArray(sculptPoints, orgPoints);
        }
        if (moveVects.length() > 0
            || !skinWeights.empty()
            || inputValues.length() > 0)
        {
            if (skinWeights.size() != inputValues.length())
            {
                return MS::kSuccess;
            }
            float env = block.inputValue(envelope).asFloat();
            for (iter.reset(); !iter.isDone(); iter.next())
            {
                float w = weightValue(block, multiIndex, iter.index());
                float scale = w  * env;
                if (scale == 0.0f) continue;
                float wt = 0.0f;
                int idx = iter.index();
                for (unsigned int i = 0; i < inputValues.length(); i++)
                {
                    wt += inputValues[i] * skinWeights[i][idx];
                }
                if (wt == 0.0f) continue;
                wt *= scale;
                MPoint pt = orgPoints[idx] + moveVects[idx] * wt;
                iter.setPosition(pt);
            }
        }
    }
    return MS::kSuccess;
};

MStatus SplitShapeNode::setDependentsDirty(const MPlug &plug,
    MPlugArray &plugArray)
{
    if (plug == oInputs || plug.parent() == oInputs)
    {
        isInputDirty = true;
        return MS::kSuccess;
    }
    return MS::kSuccess;
};

MStatus SplitShapeNode::connectionMade(const MPlug &plug,
    const MPlug &otherPlug, bool asSrc)
{
    MString pName = MString(plug.partialName());
    MStringArray pNameArray;
    pName.split('.', pNameArray);
    MString name = pNameArray[pNameArray.length()-1];
    if (name == "orgMesh")
    {
        isOrgDirty = true;
    }
    else if (name == "sculptMesh")
    {
        isSculptDirty = true;
    }
    else if (name == "skinWeight")
    {
        isSkinDirty = true;
    }
    return MPxDeformerNode::connectionMade(plug, otherPlug, asSrc);
};

MStatus SplitShapeNode::connectionBroken(const MPlug &plug,
    const MPlug &otherPlug, bool asSrc)
{
    MString pName = MString(plug.partialName());
    MStringArray pNameArray;
    pName.split('.', pNameArray);
    MString name = pNameArray[pNameArray.length() - 1];

    if (name == "orgMesh")
    {
        isOrgDirty = true;
    }
    else if (name == "sculptMesh")
    {
        isSculptDirty = true;
    }
    else if (name == "skinWeight")
    {
        isSkinDirty = true;
    }
    return MPxDeformerNode::connectionBroken(plug, otherPlug, asSrc);
};

MStringArray SplitShapeNode::getSkinInfNames(MPlug &plug)
{
    MStringArray infNames;
    MObject nodeObj = plug.node();
    if (nodeObj.hasFn(MFn::kSkinClusterFilter))
    {
        MFnSkinCluster fnSkin(nodeObj);
        MDagPathArray infs;
        unsigned int num = fnSkin.influenceObjects(infs);
        for (unsigned int i = 0; i < num;i++)
        {
            MString name = infs[i].fullPathName();
            infNames.append(name);
        }
    }
    return infNames;
};

TWeight SplitShapeNode::getSkinWeights(MPlug &plug)
{
    TWeight weights;
    MObject nodeObj = plug.node();
    if (nodeObj.hasFn(MFn::kSkinClusterFilter))
    {
        MFnSkinCluster fnSkin(nodeObj);
        MDagPathArray infs;
        unsigned int num = fnSkin.influenceObjects(infs);
        MDagPath dgPath;
        fnSkin.getPathAtIndex(0, dgPath);
        MItGeometry itGeo(dgPath);
        for (unsigned int i = 0; i < num; i++)
        {
            MFloatArray wts;
            for (itGeo.reset(); !itGeo.isDone(); itGeo.next())
            {
                MObject compObj = itGeo.component();
                MFloatArray infWts;
                fnSkin.getWeights(dgPath,compObj,i, infWts);
                wts.append(infWts[0]);
            }
            weights[i] = wts;
        }
    }
    return weights;
}

MPointArray SplitShapeNode::getMeshPoints(MDataBlock &block, MObject &obj)
{
    MPointArray points;
    MObject oMesh = block.inputValue(obj).data();
    if (!oMesh.isNull() && oMesh.hasFn(MFn::kMesh))
    {
        MFnMesh fnMesh(oMesh);
        fnMesh.getPoints(points);
    }
    if (points.length() > 0)
    {
        MGlobal::displayInfo(MString("point1 is :") + points[0].x);
    }
    return points;
};

MFloatArray SplitShapeNode::getInputWeights(MDataBlock &block, MObject &obj)
{
    MFloatArray values;
    MArrayDataHandle hValues = block.inputArrayValue(obj);
    unsigned int nItem = hValues.elementCount();
    for (unsigned int i=0; i<nItem; i++)
    {
        MDataHandle hValue = hValues.inputValue();
        float value = hValue.asFloat();
        values.append(value);
        hValues.next();
    }
    return values;
};

MPlug SplitShapeNode::getFirstConnectedPlug(MPlug &plug)
{
    MPlug conPlug;
    MPlugArray conPlugs;
    plug.connectedTo(conPlugs, true, false);
    if (conPlugs.length() > 0)
    {
        conPlug = conPlugs[0];
    }
    return conPlug;
}

MVectorArray SplitShapeNode::subTwoPointArray(MPointArray &fPoints, MPointArray &sPoints)
{
    MVectorArray vects;
    for (unsigned i = 0; i < fPoints.length(); i++)
    {
        MVector vect = fPoints[i] - sPoints[i];
        vects.append(vect);
    }
    return vects;
}