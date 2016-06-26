#include <QtQml>
#include <QObject>
#include <QQmlApplicationEngine>

#include <clocale>

#include "platform.h"
#include "application.h"
#include "config.h"
#include "input.h"
#include "player.h"
#include "recent.h"
#include "remote.h"
#include "tray.h"
#include "update.h"
#include "window.h"

int main(int argc, char *argv[]) {
  // Consistency for high resolution displays
  QApp::setAttribute(Qt::AA_EnableHighDpiScaling);

  QApp app(argc, argv);
  app.setObjectName("qt");

  // Qt sets the locale in the QGuiApplication constructor, but libmpv
  // requires the LC_NUMERIC category to be set to "C", so change it back.
  std::setlocale(LC_NUMERIC, "C");

  // Register QML Types, exposing to QML Engine
  qmlRegisterType<Application>("Mochi", 1, 0, "Application");
  qmlRegisterType<Config>("Mochi", 1, 0, "Config");
  qmlRegisterType<Input>("Mochi", 1, 0, "Input");
  qmlRegisterType<Player>("Mochi", 1, 0, "Player");
  qmlRegisterType<Recent>("Mochi", 1, 0, "Recent");
  qmlRegisterType<Remote>("Mochi", 1, 0, "Remote");
  qmlRegisterType<Tray>("Mochi", 1, 0, "Tray");
  qmlRegisterType<Update>("Mochi", 1, 0, "Update");
  qmlRegisterType<Window>("Mochi", 1, 0, "Window");

  // Create and load qml engine
  QQmlApplicationEngine engine;
  engine.load(QUrl(QLatin1String("qrc:/MochiApplication.qml")));

  return app.exec();
}
