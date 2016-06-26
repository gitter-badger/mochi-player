#ifndef WINDOW_H
#define WINDOW_H

#include <QQuickItem>
#include <QObject>
#include <QString>

class Player;

class Window : public QQuickItem {
  Q_OBJECT
  Q_CLASSINFO("Version", "2.1.0")

  Q_PROPERTY(int autoFit MEMBER autoFit NOTIFY autoFitChanged USER true)
  Q_PROPERTY(QString onTop MEMBER onTop NOTIFY onTopChanged USER true)
  Q_PROPERTY(bool remaining MEMBER remaining NOTIFY remainingChanged USER true)
  Q_PROPERTY(QString lang MEMBER lang NOTIFY langChanged USER true)
  Q_PROPERTY(bool screenshotDialog MEMBER screenshotDialog NOTIFY screenshotDialogChanged USER true)
  Q_PROPERTY(bool showAll MEMBER showAll NOTIFY showAllChanged USER true)
  Q_PROPERTY(int splitter MEMBER splitter NOTIFY splitterChanged USER true)
  Q_PROPERTY(bool hidePopup MEMBER hidePopup NOTIFY hidePopupChanged USER true)
  Q_PROPERTY(bool hideAllControls MEMBER hideAllControls NOTIFY hideAllControlsChanged USER true)
  Q_PROPERTY(QString title MEMBER title NOTIFY titleChanged USER true)

  Q_PROPERTY(Player* player MEMBER player)
public:
  explicit Window(QQuickItem *parent = 0);

public slots:
  void fit(int percent);

signals:
  void autoFitChanged(int);
  void onTopChanged(QString);
  void remainingChanged(bool);
  void langChanged(QString);
  void screenshotDialogChanged(bool);
  void showAllChanged(bool);
  void splitterChanged(int);
  void hidePopupChanged(bool);
  void hideAllControlsChanged(bool);
  void titleChanged(QString);

private:
  Player *player;

  int autoFit;
  QString onTop;
  bool remaining;
  QString lang;
  bool screenshotDialog;
  bool showAll;
  int splitter;
  bool hidePopup;
  bool hideAllControls;
  QString title;
};

#endif // WINDOW_H
