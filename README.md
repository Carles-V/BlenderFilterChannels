# Blender addon to Filter channels in Graph Editor like Maya by Carles Vallbona

I couldn't find this functionality in Blender, so I made this addon for the Graph Editor to solve it. It filters X, Y, Z for both Translations and Euler Rotations.

Note that this doesn't work for Quaternion, and I didn't add scales as those are things that you usually don't need this type of behavior for. There's room to add them, and probably in a future version, I will make a button to search for attributes with the same name to cover those or other special attributes shared between different controls.

You can use hide and unhide hotkeys instead of buttons, made them for Maya users who are not familiar with hotkeys. You can use Shift key to make multiple selections.


# HOW TO INSTALL

-For Blender 4.1 or Lower

Edit/Preferences/Install 

Search for the "FilterChannels_Addon_v01.py" you downloaded, Install addon and then search it on the addons list to enable the tab on the graph editor.

-For Blender 4.2 or above

Use Extensions 

https://extensions.blender.org/

### v1.0.3 ###

Added Scale buttons
Added Ctrl+key to subtract selection

### v1.0 ###

Basic functionality to filter X, Y, Z channels for Translations and Euler Rotations on Graph Editor "N" tab.

Using Shift+Key you can make additive selection

Made and tested for Blender 4.1, I quick tested on 3.0 and 4.2 and it seems to work on those versions too
