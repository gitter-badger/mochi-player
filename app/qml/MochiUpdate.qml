import Mochi 1.0

Update {
    id: update

    lastCheck: new Date()
    checkInterval: "startup" // never, startup, [interval in days]

    // onUpdated: window.notifyUpdated
}
