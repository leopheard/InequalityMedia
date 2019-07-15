# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/UCuDv5p8E-evaRSh542hDV5g
#------------------------------------------------------------
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.inequalitymedia'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID = "UCuDv5p8E-evaRSh542hDV5g"

# Entry point
def run():
    plugintools.log("inequalitymedia.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("inequalitymedia.main_list "+repr(params))
#note below - some YTs are /user/xxx and some /channel/xxx
    plugintools.add_item( 
        #action="", 
        title="Inequality Media",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail=icon,
        folder=True )

run()
