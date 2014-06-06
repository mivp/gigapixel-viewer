from webView import *
import subprocess
import sys

#Launch the local server...
#subprocess.call(['/home/okaluza/zoomserv_local.sh'])
#p = subprocess.Popen([sys.executable, './zoomserv_local.sh'], 
#                                    stdout=subprocess.PIPE, 
#                                    stderr=subprocess.STDOUT)

ww = None

ui = UiModule.createAndInitialize()
uiroot = ui.getUi()

browsers = {}

#Hard coded way to get tile details by node in CAVE2
width = 1366
height = 3072
htiles = 20
vtiles = 1
#getHostname returns an array of characters instead of string
node = ""
host = getHostname()
for h in range(0,len(host)):
    node += host[h]
print node
if node == "":
    node = "head1"

nodes = [{"node" : "head1", "tile" : "headTile"}, 
         {"node" : "n01",   "tile" : "t0x0"},
         {"node" : "n02",   "tile" : "t1x0"},
         {"node" : "n03",   "tile" : "t2x0"},
         {"node" : "n04",   "tile" : "t3x0"},
         {"node" : "n05",   "tile" : "t4x0"},
         {"node" : "n06",   "tile" : "t5x0"},
         {"node" : "n07",   "tile" : "t6x0"},
         {"node" : "n08",   "tile" : "t7x0"},
         {"node" : "n09",   "tile" : "t8x0"},
         {"node" : "n10",   "tile" : "t9x0"},
         {"node" : "n11",   "tile" : "t10x0"},
         {"node" : "n12",   "tile" : "t11x0"},
         {"node" : "n13",   "tile" : "t12x0"},
         {"node" : "n14",   "tile" : "t13x0"},
         {"node" : "n15",   "tile" : "t14x0"},
         {"node" : "n16",   "tile" : "t15x0"},
         {"node" : "n17",   "tile" : "t16x0"},
         {"node" : "n18",   "tile" : "t17x0"},
         {"node" : "n19",   "tile" : "t18x0"},
         {"node" : "n20",   "tile" : "t19x0"}]

for n in range(1,len(nodes)):
    #Setup a webView per node
    if nodes[n]["node"] == node:
        ww = WebView.create(width, height, False) #No WebGL
        frame = WebFrame.create(uiroot)

        offset = width * (n-1);

        turl ="http://%s:5000#w=%d&h=%d&y=%d&x=%d" % (node, htiles, vtiles, 0, n-1)
        #turl ="http://localhost:5000#h=%d&w=%d&y=%d&x=%d" % (node, htiles, vtiles, 0, n-1)
        print "Node: %s %s Offset: %d" % (node, turl, offset)
        ww.loadUrl(turl)

        #Set the position to match tile
        frame.setPosition(Vector2(offset, 0))
        frame.setView(ww)

        browsers[node] = ww
        print "Node %s Browser %s Offset %d" % (node, ww, offset)

def evaljs(js):
    #Broadcast command to nodes instead of each processing input individually
    #(Attempts to keep all in sync)
    broadcastCommand("if (ww): ww.evaljs('%s')" % js)

def onEvent():
    if not isMaster():
        return

    e = getEvent()

    #Initial movement factor for panning
    #(adjusted by zoom for sensible pan increment)
    factor = 0.02

    type = e.getServiceType()

    #print(getEvent().getPosition())
    #print(getEvent().getSourceId())
    #print(e.getPosition())
    #print(e.getFlags())

    if e.isButtonDown(EventFlags.ButtonLeft): 
        print("Left button pressed")
    if e.isButtonDown(EventFlags.ButtonUp): 
        print("Up button pressed")

    if type == ServiceType.Keyboard:
        # DO NOT pass the character directly to isKeyDown, use ord().
        # The reason is that the isKeyDown function needs the key scan code,
        # not the character (since keys like Shift, Alt, etc do not have an 
        # ASCII character). ord() does the conversion for you.
        if(e.isKeyDown(ord('w'))):
          evaljs("panBy(0, -0.1);")
        elif(e.isKeyDown(ord('a'))):
          evaljs("panBy(-0.1, 0);")
        elif(e.isKeyDown(ord('s'))):
          evaljs("panBy(0, 0.1);")
        elif(e.isKeyDown(ord('d'))):
          evaljs("panBy(0.1, 0);")
        elif(e.isKeyDown(ord('z'))):
          #evaljs("viewer.zoomBy(1.1);")
          evaljs("zoomBy(1.1);")
        elif(e.isKeyDown(ord('x'))):
          evaljs("zoomBy(0.9);")
        elif(e.isKeyDown(261)):
          print "Left"
        elif(e.isKeyDown(262)):
          print "Up"
        elif(e.isKeyDown(263)):
          print "Right"
        elif(e.isKeyDown(264)):
          print "Down"
          #browser.setZoom(1)

    # If we want to check multiple controllers or other tracked objects,
    # we could also check the sourceID of the event
    sourceID = e.getSourceId()

    # Check to make sure the event we're checking is a Wand event
    if type == ServiceType.Wand:

        # If a button is pressed down do something
        if(e.isButtonDown( EventFlags.Button3 )): # Cross
            print("Wand ", sourceID, "Left button pressed")
        if(e.isButtonDown( EventFlags.Button2 )): # Circle
            print("Wand ", sourceID, "Right button pressed")
        ##NOTE: D-pad buttons or analog stick can be switched between
        ##      using controller but can't be mapped to separate functions
        if(e.isButtonDown( EventFlags.ButtonUp )): # D-Pad up
            print("Wand ", sourceID, "D-Pad up pressed")
            evaljs("panBy(0, %d);" % (-factor))
        if(e.isButtonDown( EventFlags.ButtonDown )): # D-Pad down
            print("Wand ", sourceID, "D-Pad down pressed")
            evaljs("panBy(0, %d);" % (factor))
        if(e.isButtonDown( EventFlags.ButtonLeft )): # D-Pad left
            print("Wand ", sourceID, "D-Pad left pressed")
            evaljs("panBy(%d, 0);" % (factor))
        if(e.isButtonDown( EventFlags.ButtonRight )): # D-Pad right
            print("Wand ", sourceID, "D-Pad right pressed")
            evaljs("panBy(%d, 0);" % (factor))
        if(e.isButtonDown( EventFlags.Button6 )): # Analog stick button (L3)
            print("Wand ", sourceID, "L3 button pressed")

        # Check if some buttons are also released
        if(e.isButtonUp( EventFlags.Button3 )): # Cross
            print("Wand ", sourceID, "Left button released")
        if(e.isButtonUp( EventFlags.Button2 )): # Circle
            print("Wand ", sourceID, "Right button released")

        # If L1 is pressed print mocap data
        if(e.isButtonDown( EventFlags.Button5 )): # L1 button
            #print("Wand ", sourceID, " position: ", e.getPosition() )
            #print("Wand ", sourceID, " orientation: ", e.getOrientation() )
            print("Wand ", sourceID, "L1 button pressed")
            evaljs("zoomBy(0.9);")
            factor /= 0.9

        # Button7 is a special case, L2 is an analog trigger whose values
        # are accessed below.
        # As a shortcut Button7 will be triggered if L2 has a value greater than 0.5
        if(e.isButtonDown( EventFlags.Button7 )): # Analog Trigger (L2)
            print("Wand ", sourceID, "L2 button pressed")
            evaljs("zoomBy(1.1);")
            factor /= 1.1

        # Grab the analog stick horizontal axis
        analogLR = e.getAxis(0)

        # Grab the analog stick vertical axis
        analogUD = e.getAxis(1)

        if( (analogUD + analogLR) > 0.001 or  (analogUD + analogLR) < -0.001 ):
            #print("Wand ", sourceID, "Analog stick: ", analogUD, " ", analogLR)
            #z = 1.0 + 0.01 * analogUD
            #zoom *= z
            #browser.evaljs("zoomBy(%f);" % z)
            x = analogLR * factor
            y = analogUD * factor
            evaljs("panBy(%f, %f);" % (x, y))

        ## Grab the analog trgger
        analogL2 = e.getAxis(4)

        if( analogL2 > 0.001 ):
            print("Wand ", sourceID, "Analog trigger L2: ", analogL2 )

        ## Grab the analog trgger
        analogL1 = e.getAxis(4)

        if( analogL2 > 0.001 ):
            print("Wand ", sourceID, "Analog trigger L2: ", analogL2 )

        #Wand Motion Tracker...
        #elif(e.getServiceType() == ServiceType.Mocap):
        #    print("Trackable ", sourceID, " position: ", e.getPosition() )
        #    print("Trackable ", sourceID, " orientation: ", e.getOrientation() )


setEventFunction(onEvent)
