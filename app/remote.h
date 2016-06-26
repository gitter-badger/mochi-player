#ifndef REMOTE_H
#define REMOTE_H

#include <QObject>

class Remote : public QObject {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(bool listen MEMBER listen USER true)
  Q_PROPERTY(int port MEMBER port USER true)

public:
  explicit Remote(QObject *parent = 0);

public slots:
signals:
private:
  bool listen;
  int port;
};

#endif // REMOTE_H
