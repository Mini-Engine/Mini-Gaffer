

import Gaffer
import GafferUI
import os

def __miniCurvesRigidBind() :

	return Gaffer.Reference( "MiniCurvesRigidBind" )

def __miniCurvesRigidBindPostCreator( node, menu ) :

	node.load(
		os.path.expandvars( "${HOME}/dev/mini/Mini-Gaffer/nodes/MiniCurvesRigidBind.grf" )
	)

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
	path = "/Mini/MiniCurvesRigidBind",
	nodeCreator = __miniCurvesRigidBind,
	postCreator = __miniCurvesRigidBindPostCreator,
	searchText = "MiniCurvesRigidBind"
)