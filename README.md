gigapixel-viewer
================

Omegalib based viewer for gigapixel images on tiled displays

**gigaview.py**

Omegalib script to run image viewer
- loads webView components on each tile
- passes tile information on url (config currently hard-coded for CAVE2, need to fix this)
- calls pan and zoom functions on wand controller button presses
- Analog stick (or d-pad): pans
- Trigger buttons: zoom in/out
- Can also use WASD keys to pan, ZX to zoom for testing

**webView.cpp** 
Slightly modified version of the webView module
https://github.com/omega-hub/webView

- Don't flag events processed so they can still be acted on in the python script
- WebGL/hardware acceleration optional (extra parameter when creating view): this is because the libawesomium/chromium browser would go glitchy and spit out GLES errors after a while, disabling GPU use in the browser seems to fix the problem.

**server.sh**

Launch the deepzoom viewer server for the image tiles, set to accept connections from all IP ranges
- Pass image resource as first command line arg

Uses openslide + slightly hacked demo from openslide-python

http://openslide.org/
https://github.com/openslide/openslide-python

Key modifications:

examples/deepzoom/templates/slide_tiled.html
- Modified copy of slide_fullpage.html to hide most UI components
- Receives tiled display parameters from url x,y,w,h
- Sets initial pan based on tile info
- zoomBy/zoomTo/panBy/panTo functions to simplify calling API from Omegalib
examples/deepzoom/deepzoom_tiled.py
- Modified deepzoom_server.py to use slide_tiled.html

**Testing**
Currently 
test/cave2-emu.cfg

**TODO**
- Start and stop the server from the gigaview.py script
- Add a menu to the script with different example images, when selected stop the server and start with a new image resource
- Add an Omegalib module to allow retrieval of the tile information instead of hard coding it in gigaview.py

