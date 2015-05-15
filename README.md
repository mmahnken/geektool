# Geektool Scripts  

## What is geektool?
Geektool is a desktop application that allows the output of any script (python, bash, etc.) to be displayed on your desktop screen. The output can be styled using Geektool as well. 

With the help of geektool my desktop looks like this:

![my desktop](desktop.png)

You can download geektool [here](http://projects.tynsoe.org/en/geektool/).

## These scripts

You can accomplish a lot on geektool using built-in Bash functions for date, time, CPU, etc. However, I wanted to display the trending Github repos each day, as well as the daily pizza ingredients at one of my favorite pizza spots. So, I used python and beautiful soup to scrape the relevant websites for that data.

## What about those arcs?

In order to programmatically create those big transparent arcs on my desktop, I used the ARCfont. The a in ARCfont will display as a 0% arc, the b as 2%, the c as 4%, and on up to capital A - Y to make 100%.

To download the ARCfont, visit [this page](
http://www.macosxtips.co.uk/geeklets/system/system-info-circular-graphics/).

In order to convert the numbers for disc space and CPU into letters, I used python. (See `user_cpu.py`, `sys_cpu.py`, and `disc_space.py`).

## Setup

1) Install the requirements with `pip install -r requirements.txt`. 

2) Launch geektool (see above to download).

3) From the Geektool window with the 3 icons (file, image, and shell), drag
   the shell icon onto your desktop.

4) In the properties pane (black window), find the section that says "command".
   Type the proper command for the script you'd like to display.

   For example, if you'd like to display the trending github repos, type the 
   following in then command input area.
   ```
   cd path/to/the/script && python top_repos.py
   ```

Troubleshooting:
 - if the output does not show up after following the above steps, you may need to be explicit about which Python to use when running the script. For me, sometimes I have to modify the command slightly to be 
```
cd path/to/the/script && */usr/bin/local/python* top_repos.py
```



Happy geeking.
