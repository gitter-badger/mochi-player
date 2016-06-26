# mochi-player

The tasty mpv based media player

## Compiling

```
mkdir build
cd build
qmake-qt5 ..
make -j $(grep -c '^processor' /proc/cpuinfo)
```
