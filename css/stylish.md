% Styles for [Stylish](https://addons.mozilla.org/ru/firefox/addon/stylish)

# myshows
```css
@-moz-document domain("myshows.ru"){
*{font-family: caption !important}
div.inner {
 min-width: 0 !important;
 padding-left: 10px !important
}
@media only screen and (max-width: 768px) {
 .lside{ display:none;}
 .rside{ margin-left: 10px!important;}
 table.bserial_series td{ padding: 1px!important;}
}}
```

# youtube
```css
@-moz-document domain("youtube.com"){
body{font-family: caption !important; background: none !important;}
#masthead-positioner {
  position: relative !important;
}
#yt-masthead-container{
  background: none !important;
  border: 0 !important;
  padding:0 0 66px !important;}
.yt-card {
  box-shadow: none!important;}
#page.watch{padding:0px !important;}
#guide-container{
  left:0px !important;
  top: -60px !important;
  padding:0 !important;
}
#watch7-container, #watch7-content{
  padding-left:5px !important;
  margin: auto !important;
}
#watch7-content {
  max-width: 75% !important;
}
.comments-iframe-container iframe{
 width: 100% !important;
}
.site-left-aligned.guide-expanded #player,
.site-left-aligned.guide-expanded #watch7-main-container{
  padding-left: 190px !important;
}
.watch-sidebar{
  max-width:none !important;
  margin-top: -420px !important;
  top:30px!important;}
.watch-wide #watch7-sidebar, .watch-wide #watch7-preview {
  margin-top: -17px !important;}
.watch7-playlist-bar {
  position: absolute !important;
  top: -34px !important;
  max-width: 1060px;
}
.video-list .video-list-item .title {
  font-weight: normal !important;
}
#watch7-headline h1 .long-title {letter-spacing:0 !important;}
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
}
#watch7-ytcenter-buttons{
 position: relative;
 top: -40px;
 left: 200px;
 height:0;
}
.yt-card.yt-card-has-padding {padding: 0;
}
.yt-card {margin:0;
}
.yt-uix-clickcard-card{
 left: 730px !important;}
#player-api > div {
 z-index: 1;
 position: absolute;
}
#page.watch .content-alignment {
 min-width: auto;
}
.yt-base-gutter, .yt-unlimited #footer-container.yt-base-gutter {
 min-width: 0;
}
.related-list-item .related-item-action-menu {
 right: 10px;
}
  .watch-title-container{width: 100%}
}
```

# yadisk
```css
@-moz-document domain("yandex.ru"){
.b-case-aside_expanded{left: 0 !important;}
.b-case-aside_default-fixed{left: 246px !important;}
}
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

# t
```css
@namespace url(http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul);

.tabbrowser-tabs{
  margin: 0 -1px  
}
.tabbrowser-tabs *{
      background-image: none !important;
    -moz-border-image: none !important;
}
.tabbrowser-tab{
  -moz-appearance: none;
  margin: 0 1px ;
  padding:0;
  background: transparent;
/*   -moz-margin-start:50px; */
}
/* pinned tabs need position: fixed for separator when overflowing */
#tabbrowser-tabs[overflow] > .tabbrowser-tab[pinned] {
  position: fixed;
}
.tabbrowser-tab > .tab-stack > .tab-content:not([selected="true"]) {
  -moz-appearance: none;
  background: rgba(225,225,225,0.66);
}
.tabbrowser-tab:hover > .tab-stack > .tab-content:not([selected="true"]) {
  -moz-appearance: none;
  background: rgba(247,247,247,0.8);
}
.tabbrowser-tab > .tab-stack > .tab-content[selected="true"] {
  -moz-appearance: none;
  background: #F4F4F4;
}
.tabbrowser-tab:not([pinned]) > .tab-stack > .tab-content{
  border: 1px solid transparent;
/*   border: 1px solid #828282; */
}

.tab-background-start[selected=true]::after,
.tab-background-start[selected=true]::before,
.tab-background-start,
.tab-background-end,
.tab-background-end[selected=true]::after,
.tab-background-end[selected=true]::before {
  min-height: 30px;
  width: 0px;
/*     border-right: 1px solid #828282; */
/*     margin:0 14px; */
} 
/* .tab-background-middle{
  -moz-box-flex: 1;
  background-clip: padding-box;
  border: 1px solid #828282;
  margin: 0px 13px 4px 14px;
}
 */
/* ===================================================================================== */



#TabsToolbar {
    background: transparent !important;
    margin-bottom: 0 !important;
}
#TabsToolbar .arrowscrollbox-scrollbox {
    padding: 0 !important;
}
#TabsToolbar .tabbrowser-tabs {
    min-height: 26px !important;
}

#TabsToolbar .tabbrowser-tab {
    -moz-border-top-colors: none !important;
    -moz-border-left-colors: none !important;
    -moz-border-right-colors: none !important;
    -moz-border-bottom-colors: none !important;
    border-style: solid !important;
    border-color: #828282 !important;
    border-width: 1px 1px 0 1px !important;
/*     text-shadow: 0 0 4px rgba(255,255,255,.75) !important; */
/*     background: rgba(255,255,255,.27) !important; */
/*     background-clip: padding-box !important; */
    transition: all .1s !important;
    margin-left: -2px!important;
}
#TabsToolbar .tabbrowser-tab[first-tab]{
        margin-left: 0px !important;
}
#TabsToolbar .tabs-newtab-button {
    -moz-border-top-colors: none !important;
    -moz-border-left-colors: none !important;
    -moz-border-right-colors: none !important;
    -moz-border-bottom-colors: none !important;
    border-style: solid !important;
    border-color: transparent !important;
    border-width: 1px 1px 0 1px !important;
/*     text-shadow: 0 0 4px rgba(255,255,255,.75) !important; */
    background: transparent !important;
    background-clip: padding-box !important;
    transition: all .1s !important;
    margin-left: 1px !important;
}



#TabsToolbar .tabbrowser-tab[first-tab][last-tab],
#TabsToolbar .tabbrowser-tab[last-visible-tab] {
    border-right-width: 1px !important;
}

#TabsToolbar .tabbrowser-tab[afterselected] {
   border-left-color: rgba(0,0,0,.25) !important;
}

#TabsToolbar .tabbrowser-tab[selected] {
    color: rgba(0,0,0,1) !important;
    background: #EAF2FA !important;
    background-clip: padding-box !important;
    border-color: rgba(0,0,0,.25) !important;
}

#TabsToolbar .tabs-newtab-button:hover,
#TabsToolbar .tabbrowser-tab:hover:not([selected]) {
    border-color: rgba(0,0,0,.2) !important;
    background-color: rgba(255,255,255,.55) !important;
}

#TabsToolbar .tab-background {
    margin: 0 !important;
    background: transparent !important;
}

#TabsToolbar .tab-background-start,
#TabsToolbar .tab-background-end {
    display: none !important;
}

#TabsToolbar .tab-background-middle {
    margin: -4px -2px !important;
    background: transparent !important;
}

#TabsToolbar .tabbrowser-tab:after,
#TabsToolbar .tabbrowser-tab:before {
    display: none !important;
}
```

# Firefox Metro for Australis
```css
@namespace url(http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul);
/**
 * @Author: Heartripper
 */
#titlebar-content{
/*    z-index: 1 */
}
#titlebar-min, #titlebar-max, #titlebar-close{
   padding: 1px 15px;
}
.titlebar-button > .toolbarbutton-icon {
  width: 10px;
  height: 10px;
}
#main-window[sizemode="normal"] #tab-view-deck{
   margin-top: -11px;
}
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
#new-userstyle, #install-from-url{ min-width:30px;}
richlistitem hbox, richlistitem label { min-width: 30px;}

#userstyle-sorting{min-width: 30px}

.offlineapp .listcell-label {min-width: 70px}
```

# blockyasearchcontext
```css
@namespace ya "http://bar.yandex.ru/firefox/";
menuitem[ya|linkAction='11'] {
    display: none !important;
}
menuitem[ya|linkAction='620'] {
    display: none !important;
}
```

# github
```css
@-moz-document domain("github.com"){
body{min-width: auto;}
}
```

# thecodinglove.com
```css
@-moz-document domain("thecodinglove.com"){
#main {max-width: 100% !important; width: 100%}
}
```

# habitica
```css
@namespace url(http://www.w3.org/1999/xhtml);

@-moz-document domain("habitica.com") {
  div.footer-row {overflow-y: hidden;}
}
```

# marxists.org
```css
@namespace url(http://www.w3.org/1999/xhtml);

@-moz-document domain("marxists.org") {
  font, p {font-family: sans-serif !important;}
}
```