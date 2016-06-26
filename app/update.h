#ifndef UPDATE_H
#define UPDATE_H

#include <QObject>
#include <QString>
#include <QDateTime>

class Update : public QObject {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(QDateTime lastCheck MEMBER lastCheck USER true)
  Q_PROPERTY(QString checkInterval MEMBER checkInterval USER true)

public:
  explicit Update(QObject *parent = 0);

public slots:

signals:

private:
  QDateTime lastCheck;
  QString checkInterval;
};

#endif // UPDATE_H
