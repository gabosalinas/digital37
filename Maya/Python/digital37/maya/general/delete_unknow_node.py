import maya.cmds as cmds
import traceback

def main(log=None):
    if not log:
        import logging
        log = logging.getLogger()
    # use ' ' as a fill char and center aligned
    log.debug('{0:-<40}'.format('delete_unknow_node'))
    
    allUnknow = cmds.ls(dep=True)
    if allUnknow:
        for n in allUnknow:
            try:
                node_type = cmds.nodeType(n)
            # TODO: No object matches name: rmanFinalGlobals
            #       so use try and except to catch this
            except:
                pass
            else:
                if( node_type == 'unknown' ):
                    try:
                        cmds.lockNode(n, l=False)
                        cmds.delete(n)
                    except:
                        log.error('can not delete%s' % n)
                        log.error(traceback.format_exc())
                    else:
                        log.warning('delete %s success' % n)

