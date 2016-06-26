#ifndef INPUT_H
#define INPUT_H

#include <QQuickItem>
#include <QVariantMap>

class Input : public QQuickItem {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(QVariantMap key MEMBER key USER true)
  Q_PROPERTY(QVariantMap mouse MEMBER mouse USER true)
  Q_PROPERTY(bool gestures MEMBER gestures USER true)

public:
  explicit Input(QQuickItem *parent = 0);

public slots:

signals:

private:
  QVariantMap key;
  QVariantMap mouse;
  bool gestures;
};

#endif // INPUT_H
