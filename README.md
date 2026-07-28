# Blender addon to Filter channels in Graph Editor like Maya by Carles Vallbona

I couldn't find this functionality in Blender, so I made this addon for the Graph Editor to solve it. It filters X, Y, Z for both Translations and Euler Rotations.

Note that this doesn't work for Quaternion rotations.

You can use hide and unhide hotkeys instead of buttons, made them for users who are not familiar with hotkeys. You can use Shift key to make multiple selections and Ctrl to subtract multiple selections.


# HOW TO INSTALL

-For Blender 4.1 or Lower

Edit/Preferences/Install 

Search for the "FilterChannels_Addon_v01.py" you downloaded, Install addon and then search it on the addons list to enable the tab on the graph editor.

-For Blender 4.2 or above

Use Extensions 

[https://extensions.blender.org/](https://extensions.blender.org/add-ons/cv-filter-channels/)

### v1.0.9 ###
Added Compact Mode with colors as suggested by jametc.
Enable it through: Edit → Preferences → Add-ons → Filter Channels
Fixed and improved minor internal code.

### v1.0.8 ###
Fixed some errors when Reset and Unselect channels were called but there was no channel

### v1.0.7 ###
Added support for new action slots (blender +4.4)

### v1.0.6 ###
-Added support for Blender 4.4 -Fixed invoke error

### v1.0.5 ###
Added quaternion rotations options through addon preferences (Edit/Preferences/Add-ons/Filter Channels).

### v1.0.4 ###
Fixes bad naming and website

-Previous release

Added Scale buttons

Added Ctrl+key to subtract selection

### v1.0.3 ###

Added Scale buttons

Added Ctrl+key to subtract selection

### v1.0 ###

Basic functionality to filter X, Y, Z channels for Translations and Euler Rotations on Graph Editor "N" tab.

Using Shift+Key you can make additive selection

Made and tested for Blender 4.1, I quick tested on 3.0 and 4.2 and it seems to work on those versions too
