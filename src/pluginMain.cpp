#include <maya/MFnPlugin.h>

#include "splitShapeNode.h"

MStatus initializePlugin(MObject obj)
{
    MStatus status;
    MFnPlugin fnPlugin(obj, "xiyuhao", "1.0");
    status = fnPlugin.registerNode("splitShapeNode",
        SplitShapeNode::id,
        SplitShapeNode::creator,
        SplitShapeNode::initialize,
        MPxNode::kDeformerNode);
    CHECK_MSTATUS_AND_RETURN_IT(status);

    return MS::kSuccess;
};

MStatus uninitializePlugin(MObject obj)
{
    MStatus status;
    MFnPlugin fnPlugin(obj);
    status = fnPlugin.deregisterNode(SplitShapeNode::id);
    CHECK_MSTATUS_AND_RETURN_IT(status);

    return MS::kSuccess;
};