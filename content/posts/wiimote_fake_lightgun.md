Title: Wiimote Lightgun Experiments with Touchmote
Date: 2024-05-30T19:58:25+0000
Category: Tech
Tags: gaming, lightgun, wiimote
Author: ryochan7
Keywords: gaming, wiimote, lightgun, touchmote
Featured_image: images/1200px-Wii_Zapper.jpg
Featured_image_alt: Wiimote Zapper

### Prior Wiimote Experiments

People might know some of the controller experiments I have played
with over the past few years. One of the bigger oddities is my usage
of the Wiimote on PC.

I have played around with Motion Plus (Gyro)
support available in the Linux kernel through the use of
[MoltenGamepad](https://github.com/jgeumlek/MoltenGamepad) with
custom modifications. Playing some Linux games with Wiimote Motion Plus
was how I got interested in Gyro motion controls which carried over to
my development of DS4Windows. Although the Wiimote Gyro is okay, there
seems to be consistent gyro drift and I have even experienced it
while playing [Red Steel 2](https://en.wikipedia.org/wiki/Red_Steel_2)
on real Wii hardware.

Because of the problems I have experienced with Motion Plus,
I usually use the Wiimote with a sensor bar and IR controls. I have
played some FPS PC games with a Wiimote and it is doable. It is not my
favorite method for playing PC games meant to be played with
keyboard and mouse. On Windows, I use [Touchmote](https://touchmote.net/)
with custom modifications.

More recent discussions on
[https://github.com/simphax/Touchmote/issues/65](https://github.com/simphax/Touchmote/issues/65)
have revolved around using the Wiimote as a pseudo light gun for playing
old school light gun games on modern displays. People have experimented
with using the Wiimote as a fake light gun for years with varying
results; there are plenty of videos on YouTube of people attempting to
play the game Blue Estate with a Wiimote. Most of the demos seem to be
a bit laggy and not mapped accurately enough to play a game without a
visible cursor on screen. Seeing the attempts was enough to get me
interested so I bought a Wii Zapper shell at my local
[Mega Replay](https://www.discreplay.com/peoria)
to get started.

### Working Towards A Prototype

There are not many tools available for attempting to use the Wiimote
as a light gun. Probably the most complete one would be a Python
program written for the Raspberry Pi mention at
[https://www.instructables.com/Accurate-Wiimote-Light-Gun-on-Raspberry-PI/](https://www.instructables.com/Accurate-Wiimote-Light-Gun-on-Raspberry-PI/);
it is a good reference but not something usable for me. On Windows,
the most complete project for making a Wiimote light gun mapping is
[WiimoteGun](https://github.com/fabricecaruso/WiimoteGun). It did
not work for me at first without modifying the Wiimote init routine in the source
code. Even when I got it working, the calibration portion of the program
was a bit too sparse and there was a lot of jitter with the output
mouse cursor. Unfortunately, it was pretty much unusable no matter
what settings were used.

To get any further, I had to attempt to write something myself. My objective
was to modify Touchmote just enough to make
a fake light gun profile. The calibration method used was a slightly modified
version of the routine used in WiimoteGun. It mainly involves a two point
calibration system where a user has to aim at the center of the screen
followed by the top left corner of the screen. The X and Y coordinates of
both points from the IR camera are saved (as percentages) and are then used
to interpolate the current IR camera readings into an absolute mouse position on screen.

To assist with finding better calibration points, I wrote
a small WPF program that is available at
[https://github.com/Ryochan7/WiimoteTestCalibration](https://github.com/Ryochan7/WiimoteTestCalibration).
It isn't much but it is a lot better than just trying to attempt to find good
points manually.

![Wiimote Gun Calibration Tool](https://raw.githubusercontent.com/Ryochan7/WiimoteTestCalibration/master/gun_calibration_demo_20240424.png)

Some modifications were made to ease the process of changing the points as desired.
After the intial calibration is finished, the program will show a dot marking the
interpreted cursor position. The calibration points can be manually adjusted to
improve screen mapping. [ModernWPF](https://github.com/Kinnara/ModernWpf) was used
to add proper number boxes with ways to more easily modify the values.
The last update was saving the calibration points to a config file and
then loading those points upon the next program launch.

Custom Touchmote [code](https://github.com/Ryochan7/Touchmote/tree/ryochan7_lightgun)
handles mapping the calibration points from the settings
file into screen coordinates and outputting an absolute mouse cursor.
Two new output modes were added in the Touchmote mapper for outputting
to absolute mouse and a virtual Xbox 360 analog stick position for mock light gun
on-rail shooters like [Alien 3: The Gun](https://en.wikipedia.org/wiki/Alien_3:_The_Gun).
In order to minimize cursor jitter, the [1€ Filter](https://gery.casiez.net/1euro/)
was used to add some smoothing; Touchmote includes a slightly flawed
implementation of the 1€ Filter.

### On To Playing Games

It took a couple of days to get to a point where I felt that playing
games with a fake light gun setup was doable. I started by playing
my favorite light gun game [House of the Dead 2](https://en.wikipedia.org/wiki/The_House_of_the_Dead_2).
There is a PC port that works fairly well. There are some minor graphical issues
and there is no way to disable the cursor within the game. I think I still
prefer the Dreamcast version although I do not own a CRT TV to play it with.
Besides that, I played Virtua Cop and the original House of the Dead
on a Model 2 emulator. An extra calibration step has to be done within the emulator
for each arcade game. Those were two games I did not play back in my youth.
Performance was pretty good and those two games were pretty fun.
Accuracy was even good enough to play without a cursor.

<iframe width="560" height="315" src="https://www.youtube.com/embed/b3TlmmYPsho" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

During a Steam sale, I picked up Blue Estate and played it through. People
have raved about it but the first two levels are the only fun levels in the game.
I kind of regret buying it.

<iframe width="560" height="315" src="https://www.youtube.com/embed/mRlVyNJm5To" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The next endeavour was playing around with MAME to play some more arcade
games. I tested both MAME through the MAME UI and RetroArch. Both had
assorted issues getting games to recognize the mouse cursor although
RetroArch seemed to make the process easier for some games. Another inherent
problem is input latency within the emulator itself. Many settings had to be modified
within the RetroArch menu to reduce perceived input latency: Hard GPU Sync,
Polling Behavior, Automatic Frame Delay, Frame Delay, etc.

![MAME Latency Settings Image]({static}/images/mame_retroarch_latency_settings.png)

Played some Lethal Enforcers 2: Gun Fighters,
Police Trainer, T2: The Arcade Game, Alien 3: The Gun, Jurassic Park,
Duck Hunt.

This section is getting long. I will briefly metion
I also played around with Super Scope games for the Super Nintendo.
Yoshi's Safari and Battle Clash are pretty fun. Super Scope 6
is not as bad as some YouTube personalities make it out to be; the two modes
of Blastris are pretty pointless though.

### Final Words

After playing around with the Wii Zapper for a while, I wish it would
have had some bit of plastic on top to act as a gun sight. Trying
to aim down the top of the shell is not a good idea and reduces
accuracy. I had better results when I calibrated to either focus
through the DPad of the Wiimote or even looking into the Wiimote
extension port. Cannot do one eyed aiming that way obviously.

Overall, I would say the experiment was worth my time. I got to play
several light gun style games I did not get to play in my youth
and I got to experience some favorites again. Using a Wiimote
as a fake light gun won't be as accurate as something like
[Gun4IR](https://www.gun4ir.com/) but it seems to be good enough to
compete with other solutions like the Sinden or Retro Shooter.
