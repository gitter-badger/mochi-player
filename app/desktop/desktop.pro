QT += widgets

HEADERS += $$PWD/platform.h
SOURCES += $$PWD/desktop_window.cpp
INCLUDEPATH += $$PWD

CONFIG(platform_linux) {
  include($$PWD/linux/linux.pro)
}

CONFIG(platform_win) {
  include($$PWD/linux/win.pro)
}

CONFIG(platform_mac) {
  include($$PWD/mac/mac.pro)
}
