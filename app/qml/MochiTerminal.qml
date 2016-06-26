import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

Rectangle {
    property var evaluate

    ColumnLayout {
        anchors.fill: parent

        TextArea {
            id: output

            Layout.fillWidth: true
            Layout.fillHeight: true

            font.family: 'monospace'
            readOnly: true
        }

        TextInput {
            id: input

            Layout.fillWidth: true

            font.family: 'monospace'

            Keys.onPressed: function(event) {
                if(event.key != Qt.Key_Return) {
                    if(completionsView.visible) {
                        if(event.key == Qt.Key_Up) {
                            // TODO: select next completion
                        }
                        else if(event.key == Qt.Key_Down) {
                            // TODO: select next completion
                        }
                        else if(event.key == Qt.Key_Tab) {
                            // TODO: expand completion
                        }
                        else {
                            // TODO: update completions
                        }

                        event.accepted = true;
                    }
                    else {
                        if(event.key == Qt.Key_Up) {
                            // TODO: initiate history completion
                            console.log('history')
                            event.accepted = true;
                        }
                        else if(event.key == Qt.Key_Tab ||
                                event.key == Qt.Key_Down) {
                            // TODO: initiate locals completion
                            console.log('completion')
                            event.accepted = true;
                        }
                    }
                }
                else {
                    output.append("In:  "+input.text);
                    output.append("Out: "+evaluate(input.text));
                    input.text = "";

                    event.accepted = true;
                }
            }

            ListView {
                id: completionsView

                visible: false

                Keys.forwardTo: input
                anchors.top: input
                anchors.left: input
                anchors.right: input

                model: ListModel {
                    id: completions
                }

                delegate: Text {
                    text: text
                }

            }
        }
    }
}
