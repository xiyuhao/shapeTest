#ifndef _splitShapeNode_H_
#define _splitShapeNode_H_

#include <unordered_map>

#include <maya/MPxDeformerNode.h>
#include <maya/MPoint.h>
#include <maya/MFloatArray.h>
#include <maya/MVector.h>
#include <maya/MVectorArray.h>
#include <maya/MStringArray.h>
#include <maya/MPointArray.h>
#include <maya/MArrayDataHandle.h>

using TWeight = std::unordered_map<int, MFloatArray>;


class SplitShapeNode : MPxDeformerNode
{

public:
    SplitShapeNode();
    virtual ~SplitShapeNode();
    static void *creator();
    static MStatus initialize();
    virtual MStatus deform(MDataBlock &block,
        MItGeometry &iter,
        const MMatrix &mat,
        unsigned int multiIndex);
    virtual MStatus setDependentsDirty(const MPlug &plug,
        MPlugArray &plugArray);
    virtual MStatus connectionMade(const MPlug &plug,
        const MPlug &otherPlug, bool asSrc);
    virtual MStatus connectionBroken(const MPlug &plug,
        const MPlug &otherPlug, bool asSrc);

    MStringArray getSkinInfNames(MPlug &plug);
    MPointArray getMeshPoints(MDataBlock &block, MObject &obj);
    MFloatArray getInputWeights(MDataBlock &block,MObject &obj);
    MPlug getFirstConnectedPlug(MPlug &plug);
    TWeight getSkinWeights(MPlug &plug);
    MVectorArray subTwoPointArray(MPointArray &fPoints, MPointArray &sPoints);


public:
    static MTypeId id;
    static MObject oInputs;
    static MObject oOrgMesh;
    static MObject oSculptMesh;
    static MObject oSkinMessage;

private:
    bool isInit;
    bool isInputDirty;
    bool isSkinDirty;
    bool isSculptDirty;
    bool isOrgDirty;

    MVectorArray moveVects;
    MPointArray orgPoints;
    MPointArray sculptPoints;
    TWeight skinWeights;
    MFloatArray inputValues;
};

#endif // !_splitShapeNode_H_
