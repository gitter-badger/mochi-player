QT += qml quick script
CONFIG += window c++11

SOURCES += \
    $$PWD/main.cpp \
    $$PWD/config.cpp \
    $$PWD/application.cpp \
    $$PWD/player.cpp \
    $$PWD/input.cpp \
    $$PWD/recent.cpp \
    $$PWD/tray.cpp \
    $$PWD/remote.cpp \
    $$PWD/update.cpp \
    $$PWD/window.cpp

HEADERS += \
    $$PWD/config.h \
    $$PWD/application.h \
    $$PWD/player.h \
    $$PWD/input.h \
    $$PWD/recent.h \
    $$PWD/tray.h \
    $$PWD/remote.h \
    $$PWD/update.h \
    $$PWD/window.h

INCLUDEPATH += $$PWD

include($$PWD/lib/lib.pro)
include($$PWD/qml/qml.pro)

CONFIG(platform_desktop) {
    include($$PWD/desktop/desktop.pro)
}

CONFIG(platform_mobile) {
    include($$PWD/mobile/mobile.pro)
}
