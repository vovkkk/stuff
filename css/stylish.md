% Styles for [Stylish](https://addons.mozilla.org/ru/firefox/addon/stylish)

# myshows
```css
@-moz-document domain("myshows.ru"){
*{font-family: caption !important}
div.inner {min-width: 0 !important;
           padding-left: 10px !important}
}
```

# yadisk
```css
@-moz-document domain("yandex.ru"){
.b-case-aside_expanded{left: 0 !important;}
.b-case-aside_default-fixed{left: 246px !important;}
}
```

# youtube
```css
@-moz-document domain("youtube.com"){
body{font-family: caption !important; background: none !important;}
#masthead-positioner{
  position: relative !important;
}
#yt-masthead-container{
  background: none !important;
  border: 0 !important;
  padding:0 0 66px !important;}
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
.watch-sidebar{
  max-width:none !important;
  margin-top: -420px !important;
  top:30px!important;}
.watch7-playlist-bar {
  position: absolute !important;
  top: -34px !important;
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

# width
```css
@namespace url(http://www.w3.org/1999/xhtml);
//body, div, p, em, li, ol, ul, table, article
img{
width:95%!important;
height: auto;
}
```

# Firefox Metro for Australis
```css
@namespace url(http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul);
/**
 * @Author: Heartripper
 * | Firefox      | Thunderbird   |
 * | ------------ | ------------- |
 * | #TabsToolbar | #tabs-toolbar |
 * | .tabbrowser  | .tabmail      |
 */
/*Tabs*/
#TabsToolbar {
 background: transparent !important;
 margin-bottom: 0 !important;
}
#TabsToolbar .arrowscrollbox-scrollbox {
 padding: 0  !important;
}
#TabsToolbar .tabbrowser-tabs{
 min-height: 26px !important;
}
#TabsToolbar .tabs-newtab-button,
#TabsToolbar .tabbrowser-tab{
 -moz-border-top-colors: none !important;
 -moz-border-left-colors: none !important;
 -moz-border-right-colors: none !important;
 border-style: solid !important;
 border-color: rgba(0,0,0,.2);
 border-width: 1px 0 0 1px !important;
 text-shadow: 0 0 4px rgba(255,255,255,.75) !important;
 padding: 4px 2px !important;
 background: rgba(255,255,255,.27);
 background-clip: padding-box !important;
 transition: all .1s;
}
#TabsToolbar .tabbrowser-tab[first-tab][last-tab],
#TabsToolbar .tabbrowser-tab[last-visible-tab]{
 border-right-width: 1px !important;
}
#TabsToolbar .tabbrowser-tab[afterselected]{
   border-left-color: rgba(0,0,0,.25) !important;
}
#TabsToolbar .tabbrowser-tab[selected]{
 background: #f8f8f8 !important;
 background-clip: padding-box !important;
 border-color: rgba(0,0,0,.25) !important;
 color: rgb(43,87,154) !important;
}
#TabsToolbar .tabs-newtab-button:hover,
#TabsToolbar .tabbrowser-tab:hover:not([selected]){
 background-color: rgba(255,255,255,.55) !important;
}
#TabsToolbar .tab-background{
 margin: 0 !important;
 background: transparent !important;
}
#TabsToolbar .tab-background-start,
#TabsToolbar .tab-background-end{
 display: none !important;
}
#TabsToolbar .tab-background-middle{
 margin: -4px -2px !important;
 background: transparent !important;
}
#TabsToolbar .tabbrowser-tab:after,
#TabsToolbar .tabbrowser-tab:before{
 display: none !important;
}
#TabsToolbar .tabs-newtab-button{
 border-width: 1px 1px 0 0 !important;
 margin: 0 !important;
 width: auto !important;
 padding: 0 5px !important;
}
.tabbrowser-tab[pending] {
 background-color:#ece9d8 !important;
}

/*Toolbar*/
#addon-bar,
#PersonalToolbar,
#nav-bar{
 background: #f8f8f8 !important;
 background-clip: padding-box !important;
 border-color: rgba(0,0,0,.25) !important;
 border-radius: 0 !important;
}
#nav-bar{
 padding-right: 3px;
}
#main-window #navigator-toolbox:after {
 border-radius: 0 !important;
 height: 1px !important;
 background: #cccccc !important;
}
#customizableui-special-separator2{
 display: none !important;
}
#nav-bar-customization-target{
 margin-right: 3px !important;
 padding-right: 3px !important;
}
```