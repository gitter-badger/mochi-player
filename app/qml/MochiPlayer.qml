import Mochi 1.0

Player {
    id: player

    volume: 100
    speed: 1

    config: {
        "af": "scaletempo",
        "hwdec": "auto",
        "msg-level": "status",
        "screenshot-directory": ".",
        "screenshot-format": "jpg",
        "screenshot-template": "screenshot%#04n",
        "vo": "vdpau,opengl-hq",
        "ytdl-format": "bestvideo+bestaudio",
        "volume": player.volume,
        "speed": player.speed
    }

    // onMpvEvent: window.updateProperty(player, prop)
}
