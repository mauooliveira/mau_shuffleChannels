#--------------------------------------------------
# shuffleShortcuts.py
# version: 0.0.1
# last updated: 16.01.22 (DD.MM.YY)
#--------------------------------------------------

import nuke
import nukescripts

def createCustomShuffle(in_channel, out_channel, set_channel, rColor, gColor, bColor):

	#create Shuffle and assign a varible
	myshuffle = nuke.createNode('Shuffle')

	#change input and output channels
	myshuffle['in'].setValue(in_channel)
	myshuffle['out'].setValue(out_channel)

	#shuffle rgba channels
	myshuffle['red'].setValue(set_channel)
	myshuffle['green'].setValue(set_channel)
	myshuffle['blue'].setValue(set_channel)
	myshuffle['alpha'].setValue(set_channel)

	#assing tile color
	myshuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (rColor*255,gColor*255,bColor*255,1),16))

	#assing a label
	myshuffle['label'].setValue('[value red] > [value out]')


def shuffleRGBchannels():

	#selected node
	sel = nuke.selectedNode()
	selx = sel['xpos'].value()
	sely = sel['ypos'].value()

	#dot node
	dot = nuke.createNode('Dot')
	dot_xPos = dot['xpos'].value()
	dot_yPos = dot['ypos'].value()

	#create red, green and blue shuffles
	createCustomShuffle("rgba", "rgba", "red", 1, 0.25, 0.15)
	rshuffle = nuke.selectedNode()
	createCustomShuffle("rgba", "rgba", "green", 0.55, 1, 0.5)
	gshuffle = nuke.selectedNode()
	createCustomShuffle("rgba", "rgba", "blue", 0.2, 0.5, 1)
	bshuffle = nuke.selectedNode()

	rshuffle.setInput(0,dot)
	rshuffle['xpos'].setValue(selx-100)
	rshuffle['ypos'].setValue(sely+100)

	gshuffle.setInput(0,dot)
	gshuffle['xpos'].setValue(selx)
	gshuffle['ypos'].setValue(sely+100)

	bshuffle.setInput(0,dot)
	bshuffle['xpos'].setValue(selx+100)
	bshuffle['ypos'].setValue(sely+100)



#add items do Channel menu 
nuke.menu('Nodes').addCommand('Channel/Shuffle (red to all)','mau_shuffleShortcuts.createCustomShuffle("rgba","rgba","red",1,0.25,0.15)','ctrl+shift+r',shortcutContext=2)
nuke.menu('Nodes').addCommand('Channel/Shuffle (green to all)','mau_shuffleShortcuts.createCustomShuffle("rgba","rgba","green",0.55,1,0.5)','ctrl+shift+g',shortcutContext=2)
nuke.menu('Nodes').addCommand('Channel/Shuffle (blue to all)','mau_shuffleShortcuts.createCustomShuffle("rgba","rgba","blue",0.2,0.5,1)','ctrl+shift+b',shortcutContext=2)
nuke.menu('Nodes').addCommand('Channel/Shuffle (white to all)','mau_shuffleShortcuts.createCustomShuffle("rgba","rgba","white",0.8,0.8,0.8)','ctrl+shift+w',shortcutContext=2)
nuke.menu('Nodes').addCommand('Channel/Shuffle (black to all)','mau_shuffleShortcuts.createCustomShuffle("rgba","rgba","black",0.2,0.2,0.2)','ctrl+shift+k',shortcutContext=2)

nuke.menu('Nodes').addCommand('Channel/Shuffle (Split RGB)','mau_shuffleShortcuts.shuffleRGBchannels()','ctrl+shift+d',shortcutContext=2)


