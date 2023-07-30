title: confkingdom -- readme.md
date: 2023-07-21


== Welcome ==
date: 2023-07-21

  Project Title: Lion's Conf Kingdom
  Project Summary: a Python-based (but multi-language compatible) configuration system for One Computer


== Quick Introduction ==

    "Look, Simba, Everything the light touches, is our kingdom..."

  I've got ADHD and I wrote programs like that: Lots of little itty
  bitty programs, working together, and I need to be able to configure
  them.

  Maybe more relevant: I want to share my programs with my friends
  on the Internet.  But how does the installation work out?  "Well,
  pip."  No, specifically: How does the system configuration work out?
  The configuration files?

  Now we've hit a nerve.  You "pip install" something -- but there's
  no real concept of, "Oh, and it'll also install configuration
  files."  When you use pip install, it installs the package, but --
  there's nothing for configuration files.

  I looked around to see how Python programs that are packaged with
  pip are supposed to be configured, and all I see is people
  scratching their heads about that.

  (examples of said head scratching follow:)
  * https://stackoverflow.com/questions/7567642/where-to-put-a-configuration-file-in-python
  * https://stackoverflow.com/questions/56551337/python-package-storing-configuration-settings
  * https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

  This system of configuring ("Lion's Conf Kingdom") is meant to
  provide an answer.  And it should work for all kinds of programs,
  not just Python packages.



  I don't like the things people are suggesting:
  
  * "Just use a dot-file in the home directory."
  
     -- No, because what about when two different programmers choose
        the same name for a dot file?

     -- No, because I want to configure globally, not just for my user
        account.

  * "Environment variables for everything!"

     UGH!!
     
     -- You can't write to them. [1]
     
     -- The interface for interacting with environment variables is
        horrible.  I really, really, really do not like the
        Windows [2] little interface window for editing environments. [3]

     -- It's all tied up with the process hierarchy, and we shouldn't
        be messing with that, when we're trying to configure the
        entirety of the system for the entire computer. [4] Your
        particular parentage is not global state.

     Incredulity:
     Can you imagine if everything in Apache had to be configured
     through environment variables?

  * "Keep it in the Python repository."
     -- No.  People shouldn't have to program Python, and nothing in a
        configuration system should be reliant on Python.
        I'm configuring a SYSTEM, not Python.


  So, what I think, is that there should just be a folder, configured
  with an environment variable, and then each module or program keeps
  its information in a subfolder of that folder.
  

                              ______/ folder \   .-- project specific folder A
                             |               |  /    -------------------------
  ENVIRONMENT_VARIABLE ====> |               |
    ("CONFKINGDOM")          |               |  ---- project specific folder B
                             |_______________|       -------------------------
                                                \
                                                 `-- project specific folder C
                                                     -------------------------
                                                                    /|\
                                                                     |
                               python -m <packagename> confinstall --'


  When you install a Python package, you'll need to run it in a
  special way, to tell it: "Hey, now install your config files into
  that folder."  And I don't think that pip can do that automatically.
  So -- there has to be a "python -m <packagename> confinstall" step,
  or something like that.  But if everything does that, then it should
  be good.


    UPDATE 2023-07-30:
  .--------------------------------------------------------------------.
  | I think I'm going to add in a feature, where a Python package can, |
  | on import, register itself with the confkingdom package, and then  |
  | the confkingdom package will, on initialization, automatically     |
  | create the directory and default files for that package.           |
  |                                                                    |
  | It's not there yet, though.                                        |
  `--------------------------------------------------------------------'
      -- (see note "2023-07-30: Auto-Defaulting Configuration" in the
          notes/devlog.txt for more on this)


  The aims of my system are:

  1. Conflict-Free.

     Programs written by different people should place nice with one
     another.

    -- the way we're going to get this, is through modified TAG URIs [5];
       -- Tag URIs look like so:
            "tag:taoriver.net,2023-07-21:lions-conf-kingdom-example-taguri"
       -- But, Windows doesn't allow that to be a filename, so it will instead be:
            "taoriver_net_2023-07-21_lions-conf-kingdom-example-taguri"


  2. Human Readable.

    The system will use human readable names.  No GUIDs.
    Again, tag URIs.


  3. Single-System Assumption.

    Generally, I'm assuming global configuration.
    It should assume global configuration.


  4. TOML or JSON.

    These are popular formats for storing config data.

    You can do your own things, of course -- the program gets control
    over an entire folder, after all.


  5. Programmatically easily readable.

    It should be easy for a program to get its configuration.

    It should be easy to write systems to get at configuration.


  6. One Environment Variable

    I tried to figure out how to do the whole thing without
    environment variables, and it just...  It doesn't work.

    If you define a specific file location to look at, there's always
    the likelihood that somebody can't write at that file location,
    for whatever reason, even with the Single-System assumption.

    I think the easiest thing to do is to just have one environment
    variable, and that's the environment variable that points to your
    configuration root.

    I'm fine with that.  I have made peace with it.  As long as it's
    not more than one, single, environment variable, set for all time.


  7. Written by Me, for me, and for my friends and for "my people."

    I'm not writing this for "the world."  If people find this useful,
    "yay."  But presently, this is so that I can share my work with my
    friends.


  So, this is kind of the manifesto for "what this is."


  For a more technical description, in the docs/ folder, there is
  overview.md, which details the system.


== Footnotes ==
date: 2023-07-21

None of these footnotes are really important.
But if you want to know what I was thinking at some point, here it is.


[1] I'm not saying program's can't write to their own process's
    variables.  Of course they can.  I'm saying that, without some
    kind of additional support, they can't write to their state in the
    future.  There's no standard defined way of doing that.

    Like, if you are in a shell, and you set FOO to BAR, and then you
    close the shell and reopen a new one, FOO won't be set to BAR any
    more.

[2] Yes, I use Windows.
    I love Linux/UNIX, but I also love Windows.

[3] re: the Windows Environment Variable Editing box.

    It's ugly, it's couched in with a bunch of other stuff, it's not
    programmatically accessible (that I know how to do), and it's just
    a really unpleasant experience over all.

    There's nothing on hand that tells you what the environment
    variables mean, it doesn't prompty you for what to fill out, and
    environment variables are just grouped arbitrarily.  It doesnt'
    help you do anything, except write to an environment variable.

    Contrast with, say, an Apache config file, with comments, and
    prompts, and all kinds of stuff to help you configure Apache.

[4] I think my point is illustrated with something like: If you're
    running Apache, I want to look at the Apache config file, and see
    how it's configured.  What I do NOT want to be doing, is examining
    the process parentage tree, to figure out who set what environment
    variable, and what effect it had on the execution.  I prefer to
    configure things through easily readable files that represent a
    single source of truth, rather than looking in multiple places
    that could mask and remask a definition for a key.

[5] Tag URIs are great because they are (A) guaranteed unique,
    if you follow the simple system, and (B) human readable.

    See for yourself:

    A v4 GUID:    4d164cfa-41d0-438b-a432-ff161fa26773

    A Tag URI:    tag:taoriver.net,2023-07-21:conf-kingdom

    Learn more about Tag URIs at:
    * https://en.wikipedia.org/wiki/Tag_URI_scheme
    * https://datatracker.ietf.org/doc/html/rfc4151
    * http://www.taguri.org/


