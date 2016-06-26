#ifndef TRAY_H
#define TRAY_H

#include <QObject>

class Tray : public QObject {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(bool visible MEMBER visible USER true)

public:
  explicit Tray(QObject *parent = 0);

public slots:

signals:

private:
  bool visible;
};

#endif // TRAY_H
