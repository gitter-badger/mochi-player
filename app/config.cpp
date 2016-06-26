#include "config.h"

#include <QFile>
#include <QJsonDocument>
#include <QMetaProperty>

Config::Config(QObject *parent):
  QFileSystemWatcher(parent) {
  setObjectName("config");
  connect(this, SIGNAL(fileChanged(QString)),
          this, SLOT(load()));
}

bool Config::load() {
  // Load configuration file as QJson

  if(!app)
    return false;

  QFile f(file);
  if(f.open(QFile::ReadOnly | QIODevice::Text)) {
    setProperties(app, QJsonDocument::fromJson(f.readAll()).toVariant().toMap());
    f.close();
  }
  else
    return false;

  emit loaded();
  return true;
}

bool Config::save() {
  // Save configuration file to QJson (temporarily stop watching file to prevent reload)

  if(!app)
    return false;

  removePath(file);

  QFile f(file);
  if(f.open(QFile::WriteOnly | QFile::Truncate | QIODevice::Text)) {
    f.write(QJsonDocument::fromVariant(getProperties(app)).toJson());
    f.close();
  }
  else
    return false;

  addPath(file);
  emit saved();
  return true;
}

void Config::setFile(const QString &file) {
  // Set/change the configuration file

  if(this->file != QString())
    removePath(this->file);
  addPath(this->file = file);
}

QVariantMap Config::getProperties(QObject *obj) {
  // Recurse through obj's properties and child QObjects' building a QVariantMap

  QVariantMap data;
  const QMetaObject *mobj = obj->metaObject();
  for(int i = mobj->propertyCount()-1; i >= 0; --i) {
    QMetaProperty mprop = mobj->property(i);
    const char *name = mprop.name();
    if(mprop.isUser())
      data[name] = obj->property(name);
  }
  for(auto &child : obj->children()) {
    if(child->objectName() != QString())
      data[child->objectName()] = getProperties(child);
  }
  return data;
}

void Config::setProperties(QObject *obj, const QVariantMap &data) {
  // Recurse through obj's properties and child QObjects setting properties

  for(QVariantMap::const_iterator d = data.begin(); d != data.end(); d++) {
    if(d.value().canConvert<QVariantMap>()) {
      QObject *child = obj->findChild<QObject*>(d.key());
      if(child) {
        setProperties(child, d.value().toMap());
        continue;
      }
    }
    obj->setProperty(d.key().toUtf8(), d.value());
  }
}
