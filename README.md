Git-Releaseit
==========

`git-releaseis` adds a git command which will smartly auto-increment git release tags.  It currently only supports tags following the `major.minor` convension.

Getting Started
===============

You can get started with `git-releaseit` by using PIP:

```
pip install git-releaseit
```

This can be done in a virtual environment or at the system level.  

From then on, you can tag your new releases with something like:
```
git release major
```
or
```
git release minor
```
where `major` indicates a major release and will increment the major version number and reset the minor, and `minor` indicates a minor release and will increment the minor version number and leave the major version number alone.

The command also supports the `-s` option, which will attempt to sign the tag.

The tags are annotated by default, so a `-a` option is not needed.
