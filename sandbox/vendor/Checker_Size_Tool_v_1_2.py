#  1. First select any faces or any object and click the Get checker size button. The checker size is now stored.
#  2. If you want to set the checker size of the whole object click the 'Set Checker size of object(s)' button. 
#  3. Otherwise if you want to set the checker size of shells, click the 'Set Checker size of shells' button

#  If 'Face shells' option is selected it will scale the UVs of a shell of faces as a whole, for all the shells
#  If 'UV Shells' option selected it will scale the UVs of a UV shell as a whole, for all the UV shells

#  varun.bondwal@yahoo.com, varun.bondwal@gmail.com. Please report any bugs or suggestions.
#  v1.2 . Modified script to work in Maya 2012, 2013


import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import string
import math

def chk_str_in_str_array(S1,S2):
    flag=0
    for i in range(0,len(S2)):
        if S1==S2[i]:
            flag=1
    return flag

def get_sel_faces_UV_ratio(set_active):
    global active_ratio
    totalUVArea = 0
    totalFaceArea =0
    orig_sele=cmds.ls(sl=True, fl=True)
    if len(orig_sele)==0:
        om.MGlobal.displayError("Select at least one object")
        return       
    areaParam = om.MScriptUtil()
    areaParam.createFromDouble(0.0)
    areaPtr = areaParam.asDoublePtr() 

    mel.eval("PolySelectConvert 1")      
    sele=om.MSelectionList()
    om.MGlobal.getActiveSelectionList(sele)
    it=om.MItSelectionList(sele)
    while not it.isDone():
        dagPath=om.MDagPath()
        component=om.MObject()
        it.getDagPath(dagPath,component)
        fn=om.MFnDependencyNode(dagPath.node())
        if not component.isNull():
            if component.apiType()==om.MFn.kMeshPolygonComponent:
                itPoly=om.MItMeshPolygon(dagPath,component)
                while not itPoly.isDone():

                    itPoly.getUVArea(areaPtr)
                    area = om.MScriptUtil.getDouble(areaPtr)
                    totalUVArea += area

                    itPoly.getArea(areaPtr,om.MSpace.kWorld)
                    area = om.MScriptUtil.getDouble(areaPtr)
                    totalFaceArea += area

                    itPoly.next()
        it.next()
    UV_ratio=totalUVArea/totalFaceArea
    if set_active==1:
        active_ratio=UV_ratio
        if (len(orig_sele)>3):
            cmds.text(current_obj, edit=True , l = 'Objects : ' + 'Multiple objects')
        elif (len(orig_sele)==1):
            cmds.text(current_obj, edit=True , l = 'Object : ' + orig_sele[0])
        elif (len(orig_sele)==2):
            cmds.text(current_obj, edit=True , l = 'Objects : ' + orig_sele[0] + ', ' + orig_sele[1])
        elif (len(orig_sele)==3):
            cmds.text(current_obj, edit=True , l = 'Objects : ' + orig_sele[0] + ', ' + orig_sele[1] + ', ' + orig_sele[2])
        mel.eval("select -cl")
        for i in range(0,len(orig_sele)):
            mel.eval("select -add " + orig_sele[i])
    return UV_ratio
   

def collect_shells():     # returns a list containing one UV from all UV shells of the selected object
    mel.eval("ConvertSelectionToUVs")
    main_list=cmds.ls(sl=True,fl=True)
    UV=cmds.ls(sl=True, fl=True)
    new_list=[" "]
    while (len(main_list)>0):
        #cmds.select(cl=True)
        new_list.append(main_list[0])
        mel.eval("select "+ main_list[0])
        mel.eval("SelectUVShell")
        temp_shell=cmds.ls(sl=True,fl=True)
        for j in range(0,len(temp_shell)):
            main_list.remove(temp_shell[j])
        
    new_list.remove(" ")
    return new_list


def get_UV_ratio(set_active):                        #returns uv ratio of selected object
    global active_ratio
    sList = om.MSelectionList()
    dagp = om.MDagPath()
    mobj = om.MObject()			

    sele=cmds.ls(sl=True, fl=True)

    sList.add(sele[0])	
    sIter = om.MItSelectionList(sList)
    sIter.getDagPath(dagp, mobj)
    pIter = om.MItMeshPolygon(dagp)    

    areaParam = om.MScriptUtil()
    areaParam.createFromDouble(0.0)
    areaPtr = areaParam.asDoublePtr() 
    totalUVArea = 0
    totalFaceArea =0
    while not pIter.isDone():
            pIter.getUVArea(areaPtr)
            area = om.MScriptUtil(areaPtr).asDouble()
            totalUVArea += area

            pIter.getArea(areaPtr,om.MSpace.kWorld)
            area = om.MScriptUtil(areaPtr).asDouble()
            totalFaceArea += area

            pIter.next()
    UV_ratio=totalUVArea/totalFaceArea
    print "UV area"
    print totalUVArea
    print "total face area"
    print totalFaceArea
    if set_active==1:
        active_ratio=UV_ratio
    return UV_ratio
 
def set_UV_ratio(obj):
    try:
        print active_ratio
    except:
        om.MGlobal.displayError("Please pick a checker size first")
        return
    
    orig_sele=cmds.ls(sl=True, fl=True)
    if len(orig_sele)==0:
        om.MGlobal.displayError("Select at least one object")
        return
    prog=0.00
    cmds.progressBar(progressControl, edit=True, visible=True)
    cmds.progressBar(progressControl, edit=True, beginProgress=True)
    
    for i in range(0,len(orig_sele)):
        if (len(orig_sele)!=0):
            if (obj==1):
                prog+=(i*1.000/len(orig_sele)*1.000)*20
                cmds.progressBar(progressControl, edit=True, pr=prog)
            else:
                prog+=(i*1.000/len(orig_sele)*1.000)*15
                cmds.progressBar(progressControl, edit=True, pr=4+prog)
        cmds.select(cl=True)
        mel.eval("select " + orig_sele[i])
        current_ratio=get_sel_faces_UV_ratio(0)
        if current_ratio==0:
            current_ratio=1
        scale_factor=active_ratio/current_ratio
        scale_factor=math.sqrt(scale_factor)
        mel.eval("PolySelectConvert 4")     
        UV_bounds=cmds.polyEvaluate(bc2=True)
        u_pivot = (UV_bounds[0][0]+UV_bounds[0][1])/2
        v_pivot = (UV_bounds[1][0]+UV_bounds[1][1])/2

        cmds.polyEditUV(pu=u_pivot, pv=v_pivot, su=scale_factor, sv=scale_factor)
    
    cmds.select(cl=True)
    for i in range(0,len(orig_sele)):
        mel.eval("select -add " + orig_sele[i])

    cmds.progressBar( progressControl,edit=True, endProgress=True)
    cmds.progressBar(progressControl, edit=True, visible=False)
    om.MGlobal.displayInfo("Done")
        
    

def collect_shells_and_set_shells_UV_ratio():
    orig_sele=cmds.ls(sl=True, fl=True)

    mel.eval("ConvertSelectionToUVs")
    main_list=cmds.ls(sl=True,fl=True)
    UV=cmds.ls(sl=True, fl=True)
    new_list=[" "]
    
    orig_len=len(main_list)
    cmds.progressBar(progressControl, edit=True, beginProgress=True)
    cmds.progressBar(progressControl, edit=True, visible=True)
    while (len(main_list)>0):
        mel.eval("select "+ main_list[0])
        mel.eval("SelectUVShell")
        prog=((1.000*orig_len-1.000*len(main_list))/(1.000*orig_len))*20
        cmds.progressBar(progressControl, edit=True, pr=prog)

        
        current_ratio=get_sel_faces_UV_ratio(0)
        if current_ratio==0:
            current_ratio=1
        scale_factor=active_ratio/current_ratio
        scale_factor=math.sqrt(scale_factor)
        mel.eval("PolySelectConvert 4;")   #to UVs
        UV_bounds=cmds.polyEvaluate(bc2=True)
        u_pivot = (UV_bounds[0][0]+UV_bounds[0][1])/2
        v_pivot = (UV_bounds[1][0]+UV_bounds[1][1])/2

        cmds.polyEditUV(pu=u_pivot, pv=v_pivot, su=scale_factor, sv=scale_factor)

        temp_shell=cmds.ls(sl=True,fl=True)
        for j in range(0,len(temp_shell)):
            main_list.remove(temp_shell[j])
        
    new_list.remove(" ")
    cmds.select(cl=True)
    for i in range(0,len(orig_sele)):
        mel.eval("select -add " + orig_sele[i])
   
    cmds.progressBar( progressControl,edit=True, endProgress=True)
    cmds.progressBar(progressControl, edit=True, visible=False)
    om.MGlobal.displayInfo("Done")
    return new_list


def set_shells_UV_ratio():
    orig_sele=cmds.ls(sl=True, fl=True)

    sele=cmds.ls(sl=True, fl=True)
    if (len(sele)>1):
        om.MGlobal.displayError("Select only one object")
        return
    shells=collect_shells()
    for i in range(0, len(shells)):
        cmds.select(cl=True)
        mel.eval("select "+ shells[i])
        mel.eval("SelectUVShell")
        #mel.eval("PolySelectConvert 1")  # to faces
    
        current_ratio=get_sel_faces_UV_ratio(0)
        scale_factor=active_ratio/current_ratio
        scale_factor=math.sqrt(scale_factor)
        mel.eval("PolySelectConvert 4;")   #to UVs
        UV_bounds=cmds.polyEvaluate(bc2=True)
        u_pivot = (UV_bounds[0][0]+UV_bounds[0][1])/2
        v_pivot = (UV_bounds[1][0]+UV_bounds[1][1])/2

        cmds.polyEditUV(pu=u_pivot, pv=v_pivot, su=scale_factor, sv=scale_factor)

    cmds.select(cl=True)
    for i in range(0,len(orig_sele)):
        mel.eval("select -add " + orig_sele[i])


def show_window():
    global progressControl
    global current_obj
    global radio_col
    UV_window = cmds.window( title="Maya Checker Size Tool", iconName='Short Name', rtf = 1, s=1, widthHeight=(300, 100), mxb = 0 )
 
    if cmds.window(UV_window, ex = True ):
        cmds.deleteUI( UV_window,window=True)
    UV_window = cmds.window( title="Maya Checker Size Tool", iconName='Short Name', rtf = 1, s=1, widthHeight=(300, 100), mxb = 0 )
    cmds.columnLayout( adjustableColumn=True )
    cmds.frameLayout(label ="Get Size", w = 30 , h = 80 , mh = 5, mw = 5, bs = "etchedOut" )
    cmds.columnLayout( adjustableColumn=True )
    UV_get_but = cmds.button( label='Pick Checker Size',en=True, annotation='Store the checker size', command = 'get_sel_faces_UV_ratio(1)' )
    current_obj= cmds.text(w = 175 , l = '' , al =  'center')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.frameLayout(label ="Set Size",  w = 30 , h = 110 , mh = 5, mw = 5, bs = "etchedOut" )
    cmds.columnLayout( adjustableColumn=True )
    UV_set_but = cmds.button( label='Set Checker Size of object(s)',en=True,annotation='Change checker size of one or more meshes', command='set_UV_ratio(1)')
    UV_shell_but = cmds.button( label='Set Checker Size of shells (Single object)', en = True,annotation='Change checker size of object with several shells', command='set_shell_button()')
    cmds.rowLayout( numberOfColumns=2, columnWidth2=(100, 100))
    radio_col=cmds.radioCollection()
    cmds.radioButton('radio_Face', label = 'Face shells',  al =  'left')
    cmds.radioButton('radio_UV', label = 'UV shells',al =  'left')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.columnLayout( adjustableColumn=True )
    progressControl = cmds.progressBar(maxValue=20, width=300)
    cmds.progressBar(progressControl, edit=True, visible=False)
    cmds.text(w = 175 , l = 'varunbondwal@yahoo.com  ' , al =  'right')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.showWindow( UV_window ) 	

def set_shell_button():
    tmp_sele=cmds.ls(sl=True, fl=True)
    
    try:
        print active_ratio
    except:
        om.MGlobal.displayError("Please pick a checker size first")
        return
        
    if(len(tmp_sele)==1):
        mel.eval("constructionHistory -toggle false")
        mel.eval("autoUpdateAttrEd")
        mel.eval("updateConstructionHistory")
        selected_button = cmds.radioCollection(radio_col,query=1,sl=1)
        if (selected_button=="radio_UV"):
            collect_shells_and_set_shells_UV_ratio()
        else:
            shell_UV_scaler()
        mel.eval("constructionHistory -toggle false")
        mel.eval("autoUpdateAttrEd")
        mel.eval("updateConstructionHistory")
    else:
        om.MGlobal.displayError("Select only one object")


def shell_UV_scaler():
    global sele
    sele=cmds.ls(sl=True, fl=True)
    if len(sele)>1:
        om.MGlobal.displayError("Select only one object")
        return 
    mel.eval("select " + sele[0])
    old_mesh_dupe=cmds.duplicate()
    cmds.progressBar( progressControl,edit=True, beginProgress=True)
    cmds.progressBar(progressControl, edit=True, visible=True)
    try:
        separated = cmds.polySeparate(ch=True)
        cmds.progressBar(progressControl, edit=True, pr=5)
        set_UV_ratio(0);
        combined_mesh=cmds.polyUnite(ch=True) 
        mel.eval("polyTransfer -uv 1 -ch off -ao \"" + combined_mesh[0] +  "\" \"" + sele[0] +  "\"");
        cmds.delete(combined_mesh[0])
        mel.eval("select "+ sele[0])
        cmds.progressBar(progressControl, edit=True, pr=0)
    except:
        cmds.delete(old_mesh_dupe)
        mel.eval("select " + sele[0])
        om.MGlobal.displayError("The object has only one face shell")
    cmds.progressBar(progressControl, edit=True, endProgress=True)
    cmds.progressBar(progressControl, edit=True, visible=False)
    om.MGlobal.displayInfo("Done")
        

show_window()



