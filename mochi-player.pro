VERSION = 2.1.0

TARGET = mochi-player
TEMPLATE = app

linux:!android {
    CONFIG += platform_desktop platform_linux
}
macx {
    CONFIG += platform_desktop platform_mac
}
win32 {
    CONFIG += platform_desktop platform_win
}
android|ios {
    CONFIG += platform_mobile
    error("Maybe someday [https://github.com/mpv-android/mpv-android]")
}

include($$PWD/app/app.pro)
