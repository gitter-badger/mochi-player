CONFIG += link_pkgconfig
PKGCONFIG += mpv

SOURCES += $$PWD/mpv.cpp
HEADERS += \
  $$PWD/mpv.h
  $$PWD/lib_player.h

INCLUDEPATH += $$PWD
