import QtQuick 2.6
import QtQuick.Controls 1.4
import Mochi 1.0 as Mochi

Mochi.Application {
    id: app

    version: "2.1.0"
    debug: true

    audioFiletypes: [
      '*.mp3', '*.ogg', '*.wav', '*.wma', '*.m4a', '*.aac',
      '*.ac3', '*.ape', '*.flac', '*.ra', '*.mka']
    videoFiletypes: [
      '*.avi', '*.divx', '*.mpg', '*.mpeg', '*.m1v', '*.m2v',
      '*.mpv', '*.dv', '*.3gp', '*.mov', '*.mp4', '*.m4v',
      '*.mqv', '*.dat', '*.vcd', '*.ogm', '*.ogv', '*.asf',
      '*.wmv', '*.vob', '*.mkv', '*.ram', '*.flv', '*.rm',
      '*.ts', '*.rmvb', '*.dvr-ms', '*.m2t', '*.m2ts',
      '*.rec', '*.f4v', '*.hdmov', '*.webm', '*.vp8', '*.letv',
      '*.hlv']
    mediaFiletypes: audioFiletypes + videoFiletypes
    subtitleFileypes: [
      '*.sub', '*.srt', '*.ass', '*.ssa']

    property alias player: window.player
    property alias input: window.input
    property alias recent: window.recent

    ApplicationWindow {
        title: window.title
        width: window.width
        height: window.height
        visible: true
        menuBar: window.menuBar

        MochiWindow {
            id: window
            app: app
        }
    }

    MochiTray {
        id: tray
    }

    MochiRemote {
        id: remote
    }

    MochiUpdate {
        id: update
    }

    MochiConfig {
        id: config
        app: app
    }

    Component.onCompleted: function() {
        // Expose objects to Application's QtScript Engine
        [window, player, input, recent,
         tray, remote, update, config].map(function(obj) {
            app.addObject(obj);
        });

        // Load in user configuration
        config.load();

        // Load file/playlist from command line
        var args = app.arguments().slice(1);
        // TODO: parse command line arguments
        player.load(args);
    }
}
