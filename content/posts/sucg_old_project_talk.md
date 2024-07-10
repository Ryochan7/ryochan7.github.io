Title: Stepmania Unlock Code Generator - Looking Back
Date: 2024-07-10T21:08:34+0000
Category: Dev
Tags: gui, portfolio, programming, stepmania
Author: ryochan7
Keywords: programming, stepmania
Featured_image: images/StepMania.webp
Featured_image_alt: Stepmania

Every once in a while, I look back at some of my older projects.
It is a good thing to see how I handled problems in the past and also
reflect on how I think I have improved over the years.
I should have kept better records of my old applications so
I could have a more fleshed out portfolio. For this blog,
I feel like talking a little about an old Stepmania related project
that I wrote called Stepmania Unlock Code Generator.

### DDR Craze and Leading To A Use Case

I used to be a big fan of the video game Dance Dance Revolution.
My local arcade has a DDR machine and it was one of the biggest
attractions at that arcade. The machine usually had a line of
people waiting to play it. Despite there being console ports of DDR,
playing the game on the official arcade cabinet was the best way to
play it. Despite that, I wanted to have a similar experience at home.
Beside the console ports of DDR, I also played around with the apps
Dance With Intensity and Stepmania. Stepmania was my preferred
DDR clone.

Stepmania 3.9 had an unlock system to try to make a more arcade experience
for people who hosted dedicated Stepmania systems. Songs in a collection
would unlock after certain criteria (such as high score) were met.
Although, there was no system in place within the application to
set the unlock criteria. That task needed to be done manually in
a specific Unlocks.dat text file. I got interested in using the unlock
system a little bit but I did not want to have to edit the file by hand
with every change. That gave me a valid use case for trying to
implement an application to handle the task.

### Making Of The Application

Up until that point (February 2007), pretty much any small program I had
made was a command line application. Also, pretty much any personal
project that I coded was a clone of an existing application
so those projects served no purpose outside of my studies.
I tried to learn GTK in the past and basic event driven programming
but it did not work out then; I still have the GTK book I bought to
learn from. I was really hooked into Python then so I wanted to
code an application in Python. PyGTK and Glade were used to construct
the GUI for the first version. The application was very simple with only
two list views and a few text box controls. Stepmania Unlock Code
Generator allowed reading an Unlocks.dat file, setting supported unlock
criteria for a song, and writing the updated criteria back to the
Unlocks.dat file.

Stepmania Unlock Code Generator was in sporadic development from
February 2007 until April 2008. Three major builds were made as I
improved the application and experimented with other software stacks.
There was a GTK version, a Qt version was later made, and an experimental
Java version was created. The initial GTK version was
very crude with a good amount of spaghetti code. The model
classes were very basic as well. Later on, I did try to separate the
backend business logic from the GUI code somewhat. I tried to
utilize the Use Case Controller pattern that was taught at one of my
classes in University. Eventually, I lost interest in Stepmania and
other problems became more important.

### Ending Words

SUCG was likely the first application that I wrote that had some form of
identity and purpose. It was nice to be able to actually scratch my own
itch rather than mimic something that already existed. Back when I
started learning programming, I did not have many ideas about what I
would want to implement as I was more concerned with learning
programming concepts. Nowaways, I have many ideas but very little
time to invest in any of them.

I plan on making some posts about other old projects I have
developed. It is too bad I do not have any old screenshots
and I have no way to use the application anymore without a
Stepmania setup and song collection.

[Main SUCG Repository](https://github.com/Ryochan7/StepMania-Unlock-Code-Generator)  
[Test Java SUCG Repository](https://github.com/Ryochan7/SUCG-Java)
