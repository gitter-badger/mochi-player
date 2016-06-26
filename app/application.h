#ifndef APPLICATION_H
#define APPLICATION_H

#include <QQuickItem>
#include <QObject>
#include <QScriptEngine>
#include <QString>

class Application : public QQuickItem {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(QString version MEMBER version USER true)
  Q_PROPERTY(bool debug MEMBER debug USER true)
  Q_PROPERTY(QStringList audioFiletypes MEMBER audioFiletypes NOTIFY audioFiletypesChanged)
  Q_PROPERTY(QStringList videoFiletypes MEMBER videoFiletypes NOTIFY videoFiletypesChanged)
  Q_PROPERTY(QStringList mediaFiletypes MEMBER mediaFiletypes NOTIFY mediaFiletypesChanged)
  Q_PROPERTY(QStringList subtitleFileypes MEMBER subtitleFileypes NOTIFY subtitleFiletypesChanged)
public:
  explicit Application(QQuickItem *parent = 0);

public slots:
  void addObject(QObject*);
  QStringList arguments();
  QString evaluate(const QString &cmd);
  QString help();

signals:
  void objectAdded(QObject*);
  void audioFiletypesChanged();
  void videoFiletypesChanged();
  void mediaFiletypesChanged();
  void subtitleFiletypesChanged();

private:
  QScriptEngine engine;

  QString version;
  bool debug;

  QStringList audioFiletypes;
  QStringList videoFiletypes;
  QStringList mediaFiletypes;
  QStringList subtitleFileypes;
};

#endif // APPLICATION_H
