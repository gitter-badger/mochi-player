import QtQuick 2.6
import QtQuick.Controls 1.4

MenuBar {
    Menu {
        title: "File"
        MenuItem {
            text: "New"
        }
        MenuItem {
            text: "Open File"
        }
        MenuItem {
            text: "Exit"
            onTriggered: close()
        }
    }

    Menu {
        title: "Settings"
        MenuItem {
            text: "Preferences"
        }
    }

    Menu {
        title: "Help"
        MenuItem {
            text: "About"
        }
    }
}
