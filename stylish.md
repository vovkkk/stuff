% Styles for [Stylish](https://addons.mozilla.org/ru/firefox/addon/stylish)

- myshows
```css
@-moz-document domain("myshows.ru"){
*{font-family: caption !important}
div.inner{
  min-width: 0 !important;
  padding-left: 10px !important
}}
```
- yadisk
```css
@-moz-document domain("yandex.ru"){
.b-case-aside_expanded{left: 0 !important;}
.b-case-aside_default-fixed{left: 246px !important;}
}
```
- youtube
```css
@-moz-document domain("youtube.com"){
body{font-family: caption !important;}
#yt-masthead-container{
  background: none !important;
  border: none !important;
  padding:0 0 116px !important;}
#page.watch{padding:0px !important;}
#guide-container{
  left:0px !important;
  top: -60px !important;
  padding:0 !important;
}
#player, #watch7-main-container{
  padding-left:0 !important;
  max-width: 1060px;
  margin: auto !important;
}
.site-left-aligned.guide-expanded #player,
.site-left-aligned.guide-expanded #watch7-main-container{
  padding-left: 190px !important;
}
.watch-sidebar{max-width:none !important;}
.watch7-playlist-bar{
  position: absolute !important;
  top: -34px;
  max-width: 1060px;
}
.video-list .video-list-item .title{
  font-weight: normal !important;
}
#watch7-headline h1 .long-title{letter-spacing:0 !important;}
.watch-content, .spf-nolink, .clearfix, .action-panel-content,
.yt-uix-button-panel, .scrolldetect{
  padding: 0 !important;
  border: 0 !important;
}
.playlist-pager, .playlist-video-item{
  border: 0 !important;
  padding: 4px 0 !important;
  color: black !important;
  background: white !important;
}
.playlist-pager, .playlist-video-item,
.playlist-video-item .video-details, .video-details{
  line-height: 1 !important;
  height: auto !important
}
.branded-page-v2-primary-col, #masthead-expanded-container{
  border: 0 !important;
}
#masthead-expanded{position:relative;top:-116px;}
#masthead-expanded-container{
  margin: 0px auto -10px !important;
  background: none !important;
  box-shadow: none !important;
}}
```
- width
```css
@namespace url(http://www.w3.org/1999/xhtml);
body, div, p, em, li, ol, ul, table, article{
width:100%!important;
}
```