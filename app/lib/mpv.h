// https://github.com/mpv-player/mpv-examples/tree/master/libmpv/qt

#ifndef MPVRENDERER_H_
#define MPVRENDERER_H_

#include <QQuickItem>
#include <QQuickFramebufferObject>

#include <mpv/client.h>
#include <mpv/opengl_cb.h>
#include <mpv/qthelper.hpp>

class MpvRenderer;

class MpvObject : public QQuickFramebufferObject {
  Q_OBJECT

  friend class MpvRenderer;
public:
  MpvObject(QQuickItem * parent = 0);
  virtual ~MpvObject();
  virtual Renderer *createRenderer() const;

public slots:
  void command(const QVariant& params);
  void setProperty(const QString& name, const QVariant& value);

private slots:
  void doUpdate();

signals:
  void onUpdate();

private:
  static void on_update(void *ctx);

  mpv::qt::Handle mpv;
  mpv_opengl_cb_context *mpv_gl;
};

#endif
