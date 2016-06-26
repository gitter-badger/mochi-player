#ifndef PLAYER_H
#define PLAYER_H

#include <QObject>
#include <QString>
#include <QVariantMap>

#include "lib_player.h"

class Player : public PlayerEngine {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(QString file MEMBER file)
  Q_PROPERTY(int volume MEMBER volume NOTIFY volumeChanged USER true)
  Q_PROPERTY(float speed MEMBER speed NOTIFY speedChanged USER true)
  Q_PROPERTY(QVariantMap config MEMBER config USER true)

public:
  explicit Player(QQuickItem * parent = 0);

public slots:
  void load(const QStringList &args);
  double aspect();

protected slots:
  void setConfig(const QVariantMap &config);

signals:
  void volumeChanged(int);
  void speedChanged(float);

private:
  QString file;
  int volume;
  float speed;
  QVariantMap config;
};

#endif // PLAYER_H
