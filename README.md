# chrome-driver-backdoor


This is one of my first projects. What the script does: it goes to a pastebin link that you'll provide and searches for text that you pasted on pastebin.com,
then it executes anything that you typed to the pastebin textbox. 
It's like a blind injection of commands that is very primitive, but hard to detect (at least I think).

# Tutorial on how to use / how it was meant to be used:

1. First go to the pastebin.com and create a new unlisted paste.
2. Type your command/payload into the textbox.
3. Edit the script, so that it has your paste link.
4. Make the script a windows executable. You can name it something like some popular tech brand name or something and add a realistic icon. (I personally use auto-py-to-exe script to do this as It's like the easiest way and you don't have to watch any tutorials to do it.)
5. Install the script preferably to the startup folder on a victim's machine, or run it.
6. If you created the paste with an accound, you can edit it. You can use tor and tempmail to mitigate your privacy concerns about creating an accound.

# Options

You can edit some things for example the random time that is being used to decide the interval of the script execution. (default=<0,10>)
The script is writen to be easy to understand. Feel free to commit.


# Only for testing/fun/experimental/harmless usage. Please do not commit any felonies
