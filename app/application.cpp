#include "application.h"

Application::Application(QQuickItem *parent)
  : QQuickItem(parent),
    engine(this) {
  setObjectName("app");
  addObject(qApp);
}

void Application::addObject(QObject *obj) {
  static QScriptValue global = engine.globalObject();
  global.setProperty(obj->objectName().toUtf8().constData(), engine.newQObject(obj));
  emit objectAdded(obj);
}

QString Application::evaluate(const QString &cmd) {
  return engine.evaluate(cmd).toString();
}

QStringList Application::arguments() {
  return qApp->arguments();
}

QString Application::help() {
  return "Objects:\n"
         "  app\n"
         "  window\n"
         "  player\n"
         "  input\n"
         "Functions:\n"
         "  help()\n";
}
