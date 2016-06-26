#ifndef CONFIG_H
#define CONFIG_H

#include <QObject>
#include <QFileSystemWatcher>
#include <QString>
#include <QVariantMap>

class Config : public QFileSystemWatcher {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(QObject *app MEMBER app)
  Q_PROPERTY(QString file MEMBER file WRITE setFile)

public:
  explicit Config(QObject *parent = 0);

public slots:
  bool load();
  bool save();

private slots:
  void setFile(const QString &file);

  QVariantMap getProperties(QObject *obj);
  void setProperties(QObject *obj, const QVariantMap &data);

signals:
  void loaded();
  void saved();

private:
  QObject *app;
  QString file;
};

#endif // CONFIG_H
