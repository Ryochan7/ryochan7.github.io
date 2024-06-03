Title: Wagtail CMS Testing
Date: 2024-06-02T21:44:34+0000
Category: Tech
Tags: blog, cms, django, mezzanine, wagtail, webdev
Author: ryochan7
Keywords: blog, cms, disappointed, django, mezzanine, wagtail, webdev
Featured_image: images/disappointed.jpg
Featured_image_alt: Disappointed

### RIP Mezzanine CMS

Although I have played with Django since around version 0.96,
I have not published many public websites that used Django. I had
a small blog project that I made using Django with content
that I ported over from an old WordPress blog. That website was changed
to use [Mezzanine CMS](https://github.com/stephenmcd/mezzanine) with the
old posts converted.

Mezzanine was a pretty good CMS for the time. As the name implies,
Mezzanine provided some extra functionality to mainly extend upon
vanilla Django. Some nice features were the custom admin interface, well written
mixin classes, template overloading, ease of adding new Django apps to
an existing site, and probably others I cannot remember. Mezzanine was
the first Django CMS that I found that allowed me to easily extended an
installation and manage content easily. Merengue and Django CMS never
did what I wanted and those projects could not easily extend past a
brochure site; even using Drupal was easier.

When I thought about making a public website again, I looked into
the current state of Mezzanine. It looks like the community has dropped
the ball since Stephen McDonald left the project and Mezzanine has not been
updated in over two years. Since Mezzanine is pretty much a dead project,
I had to look into the current offerings for CMS projects made using Django.
There is not much out there. One of the most advertised alternatives
is the project [Wagtail](https://wagtail.org/).

### My Disappointment Is Immeasurable

![My Disappointment Is Immeasuable And My Day Is Ruined]({static}/images/reviewbrah_disappointment.png)

Looking into the Wagtail quick start project, there is close to nothing
available for making content by default. Wagtail is more of a framework
for writing a CMS rather than a dedicated CMS itself. Even with the more
complete [Wagtail CRX](https://docs.coderedcorp.com/wagtail-crx/) project,
making a simple blog is not really possible out of the box. Although there is
some documentation for Wagtail, it is not very detailed and I found cases
where the current documentation does not correspond with the current version of Wagtail (6.1).
I found myself having to look through the Wagtail source code to answer
some questions I had while trying to write custom models and block types.

![Wagtail Page Editor]({static}/images/wagtail-page-editor.png)

The included admin interface does look nice compared to the vanilla
Django admin; the vanilla Django admin interface is still available to use
with Wagtail. Navigating content seems like more of a chore than I
remember it being with Mezzanine; the expandable menu makes the task easier.
Searching and filtering content is done
differently with Wagtail and it seems to work well enough; the admin in
Mezzanine was fine even though it mostly used vanilla Django functionality.
Adding custom models (not Page based) is a bit of a chore in Wagtail
although it can be done with the snippet registration system.

Although Wagtail offers some model mixin classes, they do not seem self contained
and assume you will create a Page sub-class when you use them; I used
mixins bundled with Mezzanine for custom model types without a problem.
Template overloading can only be done per model type unless you write a custom
method to specify a template file for a single instance or based on
other parameters; Mezzanine offered more options for template overloading
by default and used a list of candidates rather than a single choice.
Despite Wagtail offering a page preview in the admin for the
page editor, I liked the inline field editor that Mezzanine offered more.

One positive content related feature in Wagtail is the StreamField field type.
[StreamField](https://docs.wagtail.org/en/stable/topics/streamfield.html)
is a flexible model field type that allows multiple blocks of content
to be defined and arranged for an instance. It is almost like how Django CMS
handles plugins in a page for adding many different pieces of content
in a page but with a more focused approach. Wagtail CRX offers many different
content and layout focused block types (StructBlock) to use in a model.
Creating custom block types with StructBlock and StreamBlock is fairly simple.
StreamField really is the killer feature of Wagtail.

On to a really bad point for Wagtail.
It really seems like many websites that are made with Wagtail run slowly.
Blog sites made with Wagtail that I have visited tend to be slow to
respond to requests. Even the official Wagtail project blog seems a
bit slow to me. Mezzanine was lean and pretty fast in my experience.

The biggest advertised directory of Wagtail created websites is
[Made with Wagtail](https://madewithwagtail.org/). There are some blogs
listed there along with many brochure websites.

### Unfortunately Drupal Wins

In the end, I was able to cobble together a working
prototype for a blog made with Wagtail. It took around two days
to learn Wagtail and find extra packages to add functionality
that I wanted; I could make a blog faster in vanilla Django
even back in 2011. Even if I had a proper place to host it, I do not
know if I would want to; using
[Wagtail Bakery](https://github.com/wagtail-nest/wagtail-bakery)
as an SSG was not an option due to some limitations even compared to
Pelican SSG.

It really seems like I would be better off choosing Drupal
if I need to use a CMS to manage a website. Despite the extreme
learning cliff when first learning Drupal, it is more flexible
and feature complete than Wagtail will likely ever be. I have made
three decent sized websites using Drupal 7 and 8 and those sites were
pretty responsive.
