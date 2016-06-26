import Mochi 1.0

Input {
    id: input

    gestures: true

    mouse: {
       "LeftVDrag": "function(p) { player.volume(p*100) }",
       "LeftHDrag": "function(p) { player.seek(p*player.length) }",
       "DoubleClick": "window.fullscreen = !window.fullscreen",
       "RightClick": "player.pause = !player.pause",
       "WheelDown": "player.volume -= 5",
       "WheelUp": "player.volume += 5"
    }

    key: {
       "Alt+1": "window.fit()",
       "Alt+2": "window.fit(50)",
       "Alt+3": "window.fit(75)",
       "Alt+4": "window.fit(100)",
       "Alt+5": "window.fit(150)",
       "Alt+6": "window.fit(200)",
       "Alt+Return": "window.fullscreen = not window.fullscreen",
       "Ctrl+-": "player.sub_scale -= 0.1",
       "Ctrl++": "player.sub_scale += 0.1",
       "Ctrl+D": "window.dim()",
       "Ctrl+Down": "player.volume -= 5",
       "Ctrl+E": "window.showInFolder()",
       "Ctrl+F": "playlist.show = !playlist.show",
       "Ctrl+G": "window.output = !window.output",
       "Ctrl+J": "window.jump()",
       "Ctrl+Left": "playlist.prev()",
       "Ctrl+M": "player.mute = !player.mute",
       "Ctrl+N": "engine.new()",
       "Ctrl+O": "window.open()",
       "Ctrl+Q": "qt.quit()",
       "Ctrl+R": "player.time_pos = 0",
       "Ctrl+Right": "playlist.next()",
       "Ctrl+S": "player.stop()",
       "Ctrl+Shift+Down": "player.speed -= 0.1",
       "Ctrl+Shift+R": "player.speed = 1",
       "Ctrl+Shift+T": "player.screenshot('window')",
       "Ctrl+Shift+Up": "player.speed += 0.1",
       "Ctrl+T": "player.screenshot('subtitles')",
       "Ctrl+U": "window.openUrl()",
       "Ctrl+Up": "player.volume += 5",
       "Ctrl+V": "player.play(qt.clipboard().text())",
       "Ctrl+W": "player.sub_visibility = not player.sub_visibility",
       "Del": "playlist.remove(playlist.selected)",
       "Down": "playlist.selection += 1",
       "Esc": "window.isFullScreen() ? window.fullscreen(False) : window.boss()",
       "F1": "window.onlineHelp()",
       "Left": "player.time_pos -= 5",
       "PgDown": "player.chapter += 1",
       "PgUp": "player.chapter -= 1",
       "Return": "player.play(playlist.selected)",
       "Right": "player.time_pos += 5",
       "Shift+Left": "player.frame_back_step()",
       "Shift+Right": "player.frame_step()",
       "Space": "player.pause = !player.pause",
       "Tab": "overlay.media_info = !overlay.media_info",
       "Up": "playlist.selection -= 1",
       "S": "player.speed = 2.0",
       "S*": "player.speed = 1.0"
    }
}
