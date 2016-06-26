#include "window.h"
#include "player.h"

#include <QRect>
#include <QQuickWindow>
#include <QApplication>
#include <QDesktopWidget>
#include <QStyle>

void Window::fit(int percent)
{
  QRect mG = player->window()->geometry(),                      // video geometry
      wfG = this->window()->frameGeometry(),                  // frame geometry of window (window geometry + window frame)
      wG = this->window()->geometry(),                        // window geometry
      aG = QApplication::desktop()->availableGeometry();  // available geometry of the screen we're in--(geometry not including the taskbar)

  double a = player->aspect(), // aspect ratio
      w, h; // dimensions of the video we want

  if(percent == 0) { // fit to window
      // set our current video element dimensions
      w = mG.width();
      h = mG.height();

      // epsilon comparison, we consider -eps < 0 < eps ==> 0
      double cmp = w/h - a,
          eps = 0.01;

      if(cmp > eps) // too wide
        w = h * a; // width based height
      else if(cmp < -eps) // too long
        h = w / a; // height based on width
    }
  else { // scale to desired dimensions
      double scale = percent / 100.0;

      //        w = scale * player->videoWidth();
      //        h = scale * player->videoHeight();
    }

  // display window dimensions (player display + every thing else)
  double dW = w + (wfG.width() - mG.width()),
      dH = h + (wfG.height() - mG.height());

  if(dW > aG.width()) { // width is greater, scale height
      dW = aG.width();
      w = dW - (wfG.width() - mG.width());
      h = w / a;
      dH = h + (wfG.height() - mG.height());
    }
  if(dH > aG.height()) { // if the height is bigger, scale width
      dH = aG.height();
      h = dH - (wfG.height() - mG.height());
      w = h * a;
      dW = w + (wfG.width() - mG.width());
    }

  // get the centered rectangle we want
  QRect rect = QStyle::alignedRect(Qt::LeftToRight,
                                   Qt::AlignCenter,
                                   QSize(dW, dH),
                                   percent == 0 ? wfG : aG);

  // adjust the rect to compensate for the frame
  // this is required because there is no setFrameGeometry function
  rect.setLeft(rect.left() + (wG.left() - wfG.left()));
  rect.setTop(rect.top() + (wG.top() - wfG.top()));
  rect.setRight(rect.right() - (wfG.right() - wG.right()));
  rect.setBottom(rect.bottom() - (wfG.bottom() - wG.bottom()));

  this->window()->setGeometry(rect);
}
