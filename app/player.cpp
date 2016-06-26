#include "player.h"

Player::Player(QQuickItem *parent) : MpvObject(parent) {
  setObjectName("player");
}

void Player::load(const QStringList &args) {
  if(args.length() == 1) {
    // TODO: if directory, expand
    command(QStringList({"loadfile",args[0]}));
  }
  else if(args.length() > 1) {
    command(QStringList({"loadlist"})+args);
  }
}

double Player::aspect()
{
  int width = property("width").toInt(),
      height = property("height").toInt(),
      dwidth = property("dwidth").toInt(),
      dheight = property("dheight").toInt();

  if(width == 0 || height == 0) // no video = no aspect
    return 0;
  if(dwidth == 0 || dheight == 0) // no display = video aspect
    return double(width)/height;
  else // else, display aspect
    return double(dwidth)/dheight;
}

void Player::setConfig(const QVariantMap &config)
{
  for(QVariantMap::const_iterator conf = config.begin(); conf != config.end(); conf++)
    setProperty(conf.key(), conf.value());
}
