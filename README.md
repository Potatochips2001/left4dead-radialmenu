# left4dead-radialmenu
A script to make custom radial menus easier in l4d
# usage
After running the script, pick a name for a menu. <br/>
After that, pick a vocalize command and name them. Once done it will auto print out the text you need to copy to a file to finish the process. <br/>
Next, you have to go to your left 4 dead directory, for me it's `cd .steam/steam/steamapps/common/'left 4 dead'/left4dead/scripts` <br/>
Find a text file named radialmenu and add in the text that was printed out from the script before the last curly bracket '}'. <br/>
Last step, You need to assign a key for your menu, I used "c". Go to your left4dead location and go to the cfg folder, and add this line to your `autoexec.cfg` file: `bind "c" "+mouse_menu xyzmenu` You just replace "c" with whatever key you want and rename "xyzmenu" to whatever your menu name was. <br/>
If you don't have an autoexec.cfg file you can just create it,  autoexec.cfg is just console commands that get executed once the game launches.
