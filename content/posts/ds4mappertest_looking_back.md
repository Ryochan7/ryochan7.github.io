Title: DS4MapperTest - Looking Back
Date: 2024-08-05T06:23:24+0000
Category: Dev
Tags: ds4windows, gui, mapper, portfolio, programming
Author: ryochan7
Keywords: ds4windows, mapper, programming
Featured_image: images/mappertest_example.png
Featured_image_alt: DS4MapperTest

### What Was It?

DS4MapperTest was the last version of a test ground application for
developing mapper ideas that would hopefully replace DS4Windows.
Several input controllers were supported including DS4, DualSense,
Switch Pro, JoyCon, and even the Steam Controller. Action Set and
Action Layer support was available. Many output action types were
available and preliminary activator support was available. Virtual KB+M
event support (via FakerInput) and virtual Xbox 360 and DS4 output
support (via ViGEmBus) was possible.

### Back History

Testing with implementing a new controller mapper started because
the mapper used in DS4Windows is a bit limiting and I figured
it would be easier to write brand new mapper code and test some
ideas rather than try to shoehorn something in the DS4Windows code.
The experimental mapper went through a few different iterations
over the span of about two years. The first iteration was
started as a way to test connecting a Switch Pro controller to
a Windows PC. All actions were coded directly and only basic
direct mapping in backend code was possible. The handshake routine
was added into DS4Windows a bit later on IIRC.

Later on, various actions were added to the code and a
separate Steam Controller version of the mapper was made.
My work on sc-controller helped with getting initial Steam Controller
connections working outside of Steam; some of the work in the
mapper made it back into sc-controller. Having some form of
Action Set support is necessary to take full advantage of
what the Steam Controller can offer so more of an effort was started
to add functionality that Steam Input offers. Creating an Action
Set system was not out of the question as I had made a system before.
It took quite a bit of experimenting to make an Action Layer system
that was quick to switch layers and functioned properly; even the
Action Layer system in Steam Input can get stuck on the wrong layer
sometimes. Allowing property cascading was a really tough feature to
work out.

![Profile Editor]({static}/images/example_mapper_profile_overview_20220614.png)

Eventually, I wanted to use the newly created Action Layer system
with the DS4 controller. That led to writing another version of the
experimental mapper.

### Consolidation

Having to carry changes over between three different projects
was becoming a big time sink. It was time to start merging projects
together and ease my workload. Switch Pro
support was carried over first as that backend code was closer to
what was written for the DS4 version; JoyCon controller support
was added later. It was not until about the
end of the DS4MapperTest project that Steam Controller support
was added into the code as the Steam Controller mapper had some custom
quirks that were a bit hard to carry over.

### Current Status

I stopped pushing changes for DS4MapperTest around the end of
January 2024. I have made some small changes on my machine but not
anything too great. The biggest change was adding haptic feedback
for the Circular touchpad action; having haptic feedback when
mouse wheel clicks happen really makes that type of action easier
to control. One recent small change is that I realized that throttling
the poll rate double remainder makes a big difference for smoothing
out the mouse cursor without losing precision. If only I had
thought of that idea when I was still working on DS4Windows.
Stick mouse and Gyro mouse could have been improved even more.

Although the project was technically a failure, I still use it
occasionally so it was not a complete waste of time.
