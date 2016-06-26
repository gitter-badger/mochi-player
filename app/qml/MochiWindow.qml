import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import Mochi 1.0 as Mochi

Mochi.Window {
    id: window

    property var app

    property alias input: input
    property alias player: player
    property alias recent: recent
    property alias playlist: playlist
    property alias terminal: terminal
    property alias panel: panel
    property alias menuBar: menuBar

    width: 640
    height: 480

    MochiMenu {
        id: menuBar
    }

    MochiInput {
       id: input

       anchors.fill: parent
    }

    ColumnLayout {
        anchors.fill: parent

        SplitView {
            orientation: Qt.Horizontal
            Layout.fillWidth: true
            Layout.fillHeight: true

            SplitView {
                orientation: Qt.Vertical
                Layout.fillWidth: true
                Layout.fillHeight: true

                MochiPlayer {
                    id: player

                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }

                MochiTerminal {
                    id: terminal

                    Layout.fillWidth: true
                    height: 100

                    evaluate: app.evaluate
                }
            }
            MochiPlaylist {
                id: playlist

                Layout.fillHeight: true
                width: 100
            }
        }
        MochiPanel {
            id: panel

            Layout.fillWidth: true
            height: 100
        }
    }

    MochiRecent {
        id: recent
    }
}
