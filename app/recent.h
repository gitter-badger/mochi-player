#ifndef RECENT_H
#define RECENT_H

#include <QObject>
#include <QVariantList>

class Recent : public QObject {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(int max MEMBER max USER true)
  Q_PROPERTY(QVariantList recent MEMBER recent USER true)
  Q_PROPERTY(bool resume MEMBER resume USER true)

public:
  explicit Recent(QObject *parent = 0);

public slots:

signals:

private:
  int max;
  QVariantList recent;
  bool resume;
};

#endif // RECENT_H
