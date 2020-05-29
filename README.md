# GravAssist
Repository for physics independent study project

this is the buildfile for Unix flavor, it is meant to run on Mac OSX, NOT Windows

add assets using the original assets folder
create the kernels folder in this directory, then add
  de438.bsp
  gm_de431.tpc
  naif0012.tls
  pck00010.tpc
  voyager_1.ST+1991_a54418u.merged.bsp
  voyager_2.ST+1992_m05208u.merged.bsp
directly inside

then run pyinstaller app.spec
output will be in dist

images should match the file paths in app.spec

inaccurately running pyinstaller (i.e. using 'pyinstaller app.py' instead of '*.spec') will reset app.spec
app.spec.backup is to avoid this.
