(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["main","manage"],{"03af":function(t,e,a){"use strict";var i=a("d575"),n=a.n(i);n.a},"0597":function(t,e,a){t.exports=a.p+"img/jumbo 2.5d0fcb35.jpg"},"06aa":function(t,e,a){},1681:function(t,e,a){},2240:function(t,e,a){"use strict";var i=a("db85"),n=a.n(i);n.a},"4aa8":function(t,e,a){"use strict";var i=a("ed5e"),n=a.n(i);n.a},"770d":function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("Jumbotron",{directives:[{name:"intersect",rawName:"v-intersect",value:{handler:t.onIntersect,options:{threshold:[0,1]}},expression:"{\n      handler: onIntersect,\n      options: {\n        threshold: [0.0, 1.0]\n      }\n    }"}],attrs:{index:"0"}}),a("About",{directives:[{name:"intersect",rawName:"v-intersect",value:{handler:t.onIntersect,options:{threshold:[0,1]}},expression:"{\n      handler: onIntersect,\n      options: {\n        threshold: [0.0, 1.0]\n      }\n    }"}],attrs:{index:"1"}}),a("Features"),a("Banner",{attrs:{height:"300"}})],1)},n=[],s=(a("a9e3"),a("5530")),r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-parallax",{staticClass:"pb-5",attrs:{dark:"",src:t.imgPath,height:t.imgHeight}},[a("v-container",{staticClass:"pb-0",staticStyle:{"max-width":"800px"}},[a("v-row",{style:{height:1*t.imgHeight/3+"px"},attrs:{align:"center",justify:"center"}},[a("v-btn-toggle",{key:t.forceUpdate,attrs:{rounded:"",borderless:"",dense:"",color:"primary"},model:{value:t.btnToggle,callback:function(e){t.btnToggle=e},expression:"btnToggle"}},[a("v-tooltip",{attrs:{value:"Shorten"===t.btnToggle,bottom:""},scopedSlots:t._u([{key:"activator",fn:function(e){var i=e.attrs;return[a("v-btn",t._b({attrs:{value:"Shorten",width:"100"}},"v-btn",i,!1),[t._v(" Shorten ")])]}}])},[a("span",[t._v("Create a short link")])]),a("v-tooltip",{attrs:{value:"Check"===t.btnToggle,bottom:""},scopedSlots:t._u([{key:"activator",fn:function(e){var i=e.attrs;return[a("v-btn",t._b({attrs:{value:"Check",width:"100"}},"v-btn",i,!1),[t._v(" Check ")])]}}])},[a("span",[t._v("Check the original link")])])],1)],1),a("v-row",{style:{height:1*t.imgHeight/3+"px"},attrs:{align:"center"}},[a("ShortenLink",{key:t.btnToggle,attrs:{alert:"",behavior:t.btnToggle}})],1),a("v-row",{style:{height:1*t.imgHeight/3+"px"},attrs:{align:"center"}})],1)],1)},o=[],l=a("0a70"),c={name:"Jumbotron",data:function(){return{imgPath:a("0597"),imgHeight:700,tabItems:[{tab:"Create",component:"ShortenLink"},{tab:"Check",component:"CheckLink"}],btnToggle:null,forceUpdate:1,resizeTimeOut:null}},methods:{tooltipUpdate:function(){this.resizeTimeOut&&clearTimeout(this.resizeTimeOut),this.resizeTimeOut=setTimeout(function(){var t=this,e=String(this.btnToggle);this.btnToggle="",this.$nextTick((function(){t.btnToggle=e})),this.forceUpdate=-1*this.forceUpdate}.bind(this),200)}},mounted:function(){var t=this;this.$nextTick((function(){t.btnToggle="Shorten"}))},created:function(){window.addEventListener("resize",this.tooltipUpdate)},destroyed:function(){window.removeEventListener("resize",this.tooltipUpdate)},components:{ShortenLink:l["a"]}},u=c,d=(a("2240"),a("2877")),h=a("6544"),m=a.n(h),f=a("8336"),p=(a("7e58"),a("604c")),v=p["a"].extend({name:"button-group",provide:function(){return{btnToggle:this}},computed:{classes:function(){return p["a"].options.computed.classes.call(this)}},methods:{genData:p["a"].options.methods.genData}}),g=a("a9ad"),b=a("58df"),y=Object(b["a"])(v,g["a"]).extend({name:"v-btn-toggle",props:{backgroundColor:String,borderless:Boolean,dense:Boolean,group:Boolean,rounded:Boolean,shaped:Boolean,tile:Boolean},computed:{classes:function(){return Object(s["a"])(Object(s["a"])({},v.options.computed.classes.call(this)),{},{"v-btn-toggle":!0,"v-btn-toggle--borderless":this.borderless,"v-btn-toggle--dense":this.dense,"v-btn-toggle--group":this.group,"v-btn-toggle--rounded":this.rounded,"v-btn-toggle--shaped":this.shaped,"v-btn-toggle--tile":this.tile},this.themeClasses)}},methods:{genData:function(){var t=this.setTextColor(this.color,Object(s["a"])({},v.options.methods.genData.call(this)));return this.group?t:this.setBackgroundColor(this.backgroundColor,t)}}}),x=a("a523"),w=(a("94aa"),a("2b0e")),C=w["a"].extend({name:"translatable",props:{height:Number},data:function(){return{elOffsetTop:0,parallax:0,parallaxDist:0,percentScrolled:0,scrollTop:0,windowHeight:0,windowBottom:0}},computed:{imgHeight:function(){return this.objHeight()}},beforeDestroy:function(){window.removeEventListener("scroll",this.translate,!1),window.removeEventListener("resize",this.translate,!1)},methods:{calcDimensions:function(){var t=this.$el.getBoundingClientRect();this.scrollTop=window.pageYOffset,this.parallaxDist=this.imgHeight-this.height,this.elOffsetTop=t.top+this.scrollTop,this.windowHeight=window.innerHeight,this.windowBottom=this.scrollTop+this.windowHeight},listeners:function(){window.addEventListener("scroll",this.translate,!1),window.addEventListener("resize",this.translate,!1)},objHeight:function(){throw new Error("Not implemented !")},translate:function(){this.calcDimensions(),this.percentScrolled=(this.windowBottom-this.elOffsetTop)/(parseInt(this.height)+this.windowHeight),this.parallax=Math.round(this.parallaxDist*this.percentScrolled)}}}),_=Object(b["a"])(C),S=_.extend().extend({name:"v-parallax",props:{alt:{type:String,default:""},height:{type:[String,Number],default:500},src:String,srcset:String},data:function(){return{isBooted:!1}},computed:{styles:function(){return{display:"block",opacity:this.isBooted?1:0,transform:"translate(-50%, ".concat(this.parallax,"px)")}}},mounted:function(){this.init()},methods:{init:function(){var t=this,e=this.$refs.img;e&&(e.complete?(this.translate(),this.listeners()):e.addEventListener("load",(function(){t.translate(),t.listeners()}),!1),this.isBooted=!0)},objHeight:function(){return this.$refs.img.naturalHeight}},render:function(t){var e={staticClass:"v-parallax__image",style:this.styles,attrs:{src:this.src,srcset:this.srcset,alt:this.alt},ref:"img"},a=t("div",{staticClass:"v-parallax__image-container"},[t("img",e)]),i=t("div",{staticClass:"v-parallax__content"},this.$slots.default);return t("div",{staticClass:"v-parallax",style:{height:"".concat(this.height,"px")},on:this.$listeners},[a,i])}}),k=a("0fd9"),j=a("3a2f"),T=Object(d["a"])(u,r,o,!1,null,"c509c2e8",null),I=T.exports;m()(T,{VBtn:f["a"],VBtnToggle:y,VContainer:x["a"],VParallax:S,VRow:k["a"],VTooltip:j["a"]});var H=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"pb-3 pt-12",attrs:{id:"about"}},[a("SubHeader",{attrs:{title:"About"}},[t._v(" MiniPy provides simplified version of any links ready to share on SNSs, blogs, etc. "),a("br"),t._v(" Just with one click— shorten, share, manage altogether come in handy. "),a("br")]),a("v-container",{staticClass:"limit-width mt-5"},[a("v-row",{attrs:{justify:"center"}},[a("v-col",{staticClass:"d-flex justify-center",attrs:{cols:"12",sm:"9",md:"4"}},[a("AvatarCard",{attrs:{icon:"fa-link","icon-hoist":""},scopedSlots:t._u([{key:"title",fn:function(){return[t._v(" Shorten ")]},proxy:!0},{key:"content",fn:function(){return[t._v(" Lenghy URLs that take up almost 3 or 4 lines long are just eyesores to everyone. They look unnatural and simply ruin your message. Copy your messy link and hit the shorten button. We will deliver you a nice and clean link. ")]},proxy:!0}])})],1),a("v-col",{staticClass:"d-flex justify-center",attrs:{cols:"12",sm:"9",md:"4"}},[a("AvatarCard",{attrs:{icon:"share","icon-hoist":""},scopedSlots:t._u([{key:"title",fn:function(){return[t._v(" Share ")]},proxy:!0},{key:"content",fn:function(){return[t._v(" Many Social Networks have its limit on each post. Some messagings cost more if exceeded. A shortened link will not only solve these problems but enhance the readability of your message when shared. ")]},proxy:!0}])})],1),a("v-col",{staticClass:"d-flex justify-center",attrs:{cols:"12",sm:"9",md:"4"}},[a("AvatarCard",{attrs:{icon:"poll","icon-hoist":""},scopedSlots:t._u([{key:"title",fn:function(){return[t._v(" Manage ")]},proxy:!0},{key:"content",fn:function(){return[t._v(" MiniPy provides analytical data that allow for making smarter decisions on your projects. You will see how many clicks your link gained, what browsers people prefer, from where they clicked, click-through rates on a daily basis, and whatnots. ")]},proxy:!0},{key:"actions",fn:function(){return[a("GLoginBtn",{staticClass:"mb-3",attrs:{block:"",long:""}})]},proxy:!0}])})],1)],1)],1)],1)},O=[],B=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"text-center"},[a("h3",{staticClass:"display-2"},[t._v(t._s(t.title))]),a("div",{staticClass:"decor mx-auto my-5"},[a("v-divider",{staticClass:"decor primary"})],1),a("div",{staticClass:"mx-auto",staticStyle:{"max-width":"800px"}},[t._t("default")],2)])},V=[],N={name:"SubHeader",props:["title"]},$=N,E=(a("d859"),a("ce7e")),z=Object(d["a"])($,B,V,!1,null,"f0099594",null),A=z.exports;m()(z,{VDivider:E["a"]});var L=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-card",{staticClass:"mx-5 my-8",style:[t.cardStyle,t.mouseHover?t.hoverStyle:""],attrs:{"min-height":t.minHeight,"min-width":t.minWidth,"max-width":t.maxWidth},on:{mouseenter:function(e){t.mouseHover=!0},mouseleave:function(e){t.mouseHover=!1}}},[a("div",{staticClass:"text-center",style:{height:t.iconDivHeight+"px"}},[a("v-avatar",{staticClass:"mx-auto",style:t.iconStyle,attrs:{size:t.iconSize,color:"white",rounded:""}},[a("v-icon",{attrs:{size:.6*t.iconSize,color:"rgb(55,115,165)"}},[t._v(t._s(t.icon))])],1)],1),a("v-card-title",{staticClass:"justify-center title pt-1",style:t.titleStyle},[t._t("title")],2),a("v-card-text",{staticClass:"px-8",class:t.textContent},[t._t("content")],2),a("v-card-actions",{staticClass:"px-8"},[t._t("actions")],2)],1)},M=[],P=(a("99af"),{name:"AvatarCard",data:function(){return{mouseHover:!1}},props:{icon:String,iconSize:{type:Number,default:function(){return 100}},iconHoist:{type:Boolean,default:function(){return!1}},titleSize:{type:Number,default:function(){return 1.5}},borderWidth:{type:Number,default:function(){return 2}},borderColor:{type:String,default:function(){return"rgb(55,115,165)"}},hoverWidth:{type:Number,default:function(){return 3}},hoverColor:{type:String,default:function(){return"rgb(55,115,165)"}},minWidth:{type:String,default:function(){return"250px"}},minHeight:{type:String,default:function(){return"300px"}},maxWidth:{type:String,default:function(){return"360px"}},textContent:{type:String,default:function(){return"text-justify"}}},computed:{iconStyle:function(){return{position:"relative",top:"-".concat(this.iconHoist?this.iconSize/2:0,"px"),"border-radius":"50% !important"}},iconDivHeight:function(){return this.iconHoist?this.iconSize/2:this.iconSize},titleStyle:function(){return{fontSize:"".concat(this.titleSize,"em !important")}},cardStyle:function(){return{border:"".concat(this.borderWidth,"px solid ").concat(this.borderColor),transition:"transform .2s"}},hoverStyle:function(){return{border:"".concat(this.hoverWidth,"px solid ").concat(this.hoverColor),transform:"scale(1.1)"}}}}),R=P,D=a("8212"),G=a("b0af"),W=a("99d9"),q=a("132d"),U=Object(d["a"])(R,L,M,!1,null,"06357557",null),F=U.exports;m()(U,{VAvatar:D["a"],VCard:G["a"],VCardActions:W["a"],VCardText:W["c"],VCardTitle:W["d"],VIcon:q["a"]});var J=a("f7a0"),Y={name:"About",components:{SubHeader:A,AvatarCard:F,GLoginBtn:J["a"]}},K=Y,Q=a("62ad"),X=Object(d["a"])(K,H,O,!1,null,"7119ebb2",null),Z=X.exports;m()(X,{VCol:Q["a"],VContainer:x["a"],VRow:k["a"]});var tt=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"pb-9",attrs:{id:"features"}},[a("HSpacer",{staticClass:"mb-9"}),a("SubHeader",{attrs:{title:"Features"}},[t._v(" These features are combined to create one comprehensive platform, MiniPy. ")]),a("v-container",{staticClass:"limit-width px-6 mx-auto"},[a("v-sheet",{staticClass:"border-decor mt-12 mb-8",attrs:{elevation:"2"},on:{mouseenter:t.haltSlide,mouseleave:t.resumeSlide}},[a("v-slide-group",{staticClass:"pa-3",attrs:{"show-arrows":"always"},model:{value:t.slideModel,callback:function(e){t.slideModel=e},expression:"slideModel"}},t._l(t.slideItems,(function(e,i){return a("v-slide-item",{key:i,attrs:{"center-active":""}},[a("AvatarCard",{staticClass:"ma-8 mx-10 pt-5",attrs:{minHeight:"250px",minWidth:"250px",maxWidth:"250px",iconSize:"60",icon:e.icon,borderColor:"transparent",hoverWidth:"1",titleSize:"1.2",textContent:"text-center"},scopedSlots:t._u([{key:"title",fn:function(){return[t._v(" "+t._s(e.title)+" ")]},proxy:!0},{key:"content",fn:function(){return[t._v(" "+t._s(e.desc)+" ")]},proxy:!0}],null,!0)})],1)})),1)],1)],1)],1)},et=[],at=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("v-container",{staticClass:"h-spacer limit-width pa-0"})],1)},it=[],nt={},st=nt,rt=(a("03af"),Object(d["a"])(st,at,it,!1,null,"20e3706f",null)),ot=rt.exports;m()(rt,{VContainer:x["a"]});var lt={name:"Features",data:function(){return{slideModel:null,slideItems:[{icon:"fa-chart-bar",title:"Traffic Tracing",desc:"You can collect access and traffic information by looking at the simplified graph in your dashboard."},{icon:"fa-id-badge",title:"Personal Profile",desc:"Personal Profile is automatically created via Google Login. No additional personal data is required."},{icon:"fa-check-square",title:"Link Check",desc:"By attaching # after a link or by using the check tab above, suspicious links can be verified beforehand."}],pauseSlide:!1}},components:{SubHeader:A,AvatarCard:F,HSpacer:ot},methods:{activateCard:function(t){console.log("hi"),this.slideModel=t},consoleLog:function(){console.log("HI")}}},ct=lt,ut=(a("8ef2"),a("8dd9")),dt=a("7efd"),ht=a("ade3"),mt=a("4e82"),ft=a("d9bd"),pt=w["a"].extend({props:{activeClass:String,value:{required:!1}},data:function(){return{isActive:!1}},methods:{toggle:function(){this.isActive=!this.isActive}},render:function(){return this.$scopedSlots.default?(this.$scopedSlots.default&&(t=this.$scopedSlots.default({active:this.isActive,toggle:this.toggle})),Array.isArray(t)&&1===t.length&&(t=t[0]),t&&!Array.isArray(t)&&t.tag?(t.data=this._b(t.data||{},t.tag,{class:Object(ht["a"])({},this.activeClass,this.isActive)}),t):(Object(ft["c"])("v-item should only contain a single element",this),t)):(Object(ft["c"])("v-item is missing a default scopedSlot",this),null);var t}}),vt=(Object(b["a"])(pt,Object(mt["a"])("itemGroup","v-item","v-item-group")).extend({name:"v-item"}),Object(b["a"])(pt,Object(mt["a"])("slideGroup")).extend({name:"v-slide-item"})),gt=Object(d["a"])(ct,tt,et,!1,null,"6ac892ba",null),bt=gt.exports;m()(gt,{VContainer:x["a"],VSheet:ut["a"],VSlideGroup:dt["b"],VSlideItem:vt});var yt=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-img",{attrs:{src:t.imgPath,height:t.height,dark:""}},[a("v-row",{staticClass:"fill-height overlay",attrs:{align:"center"}},[a("v-col",[a("blockquote",[a("p",[a("span",{attrs:{"data-duration":"1.1","data-delay":".23"}},[t._v('"The ')]),a("span",{attrs:{"data-duration":"1.1","data-delay":".43"}},[t._v("Simpler ")]),a("span",{attrs:{"data-duration":"1.8","data-delay":".42"}},[t._v("It ")]),a("span",{attrs:{"data-duration":"1.2","data-delay":".25"}},[t._v("Is, ")]),a("span",{attrs:{"data-duration":"1.7","data-delay":".30"}},[t._v("The ")]),a("span",{attrs:{"data-duration":"1.2","data-delay":".29"}},[t._v("Better ")]),a("span",{attrs:{"data-duration":"1.4","data-delay":".26"}},[t._v("I ")]),a("span",{attrs:{"data-duration":"1.7","data-delay":".19"}},[t._v("Like ")]),a("span",{attrs:{"data-duration":"1.2","data-delay":".11"}},[t._v('It." ')])]),a("cite",[t._v("Peter Lynch")])])])],1)],1)},xt=[],wt=(a("4160"),a("159b"),{name:"Banner",data:function(){return{imgPath:a("e160")}},methods:{setTextAnimation:function(){for(var t=this,e=this.$el.getElementsByTagName("span"),a=this.$el.getElementsByTagName("cite")[0],i=0,n=0,s=0;s<e.length;s++){var r=e[s],o=r.dataset.duration,l=r.dataset.delay;r.dataset.blur;i=Math.max(l,i),n=Math.max(o,n),r.style.transition="all ".concat(o,"s ease-in ").concat(l,"s"),r.classList.add("animate")}a.style.transition="all ".concat(n,"s ease-in ").concat(i,"s"),a.classList.add("animate");var c=1e3*(n+i);setTimeout((function(){var i=5e3;setTimeout((function(){e.forEach((function(t){t.classList.remove("animate")})),a.classList.remove("animate")}),i),setTimeout((function(){t.setTextAnimation()}),i+2*c)}),c)}},mounted:function(){this.setTextAnimation()},props:{type:{type:String,default:"page"},height:{type:String,default:"200"}}}),Ct=wt,_t=(a("4aa8"),a("adda")),St=Object(d["a"])(Ct,yt,xt,!1,null,"251c77d9",null),kt=St.exports;m()(St,{VCol:Q["a"],VImg:_t["a"],VRow:k["a"]});var jt=a("2f62"),Tt="main",It={name:"MainPage",data:function(){return{intersectInfo:[{index:0,y:0},{index:1,y:0}]}},computed:Object(s["a"])({},Object(jt["e"])(Tt,["intersectEnabled","tabIndex","listIndex"])),methods:Object(s["a"])(Object(s["a"])({},Object(jt["d"])(Tt,["setTabIndex"])),{},{onIntersect:function(t,e){var a=t[0],i=Number(a.target.getAttribute("index")),n=this.intersectInfo[i].y,s=a.boundingClientRect.y;this.intersectEnabled&&(a.isIntersecting?1===a.intersectionRatio&&this.setTabIndex(i):i===this.tabIndex&&(n>s?this.setTabIndex(i+1):n<s&&this.setTabIndex(i-1)),this.intersectInfo[i].y=s)}}),components:{Jumbotron:I,About:Z,Features:bt,Banner:kt}},Ht=It,Ot=a("269a"),Bt=a.n(Ot),Vt=a("90a2"),Nt=Object(d["a"])(Ht,i,n,!1,null,null,null);e["default"]=Nt.exports;Bt()(Nt,{Intersect:Vt["a"]})},"7bd8":function(t,e,a){},"7e58":function(t,e,a){},"8ef2":function(t,e,a){"use strict";var i=a("7bd8"),n=a.n(i);n.a},"94aa":function(t,e,a){},ac3b:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[t._v(" Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur harum perferendis temporibus ipsam nisi omnis in, eligendi aspernatur quas, doloremque impedit beatae sapiente voluptatum animi rerum ratione magnam suscipit nam. ")])},n=[],s={name:"MainPageAPI"},r=s,o=a("2877"),l=Object(o["a"])(r,i,n,!1,null,null,null);e["default"]=l.exports},b8fa:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",{staticClass:"pt-0 px-0",class:{"limit-width":t.isMain}},[a("div",{staticClass:"polygon white--text text-center"},[a("div",{staticClass:"pt-5 mb-3 text-h5 font-weight-medium"},[t._v(" E-Mail Us ")]),a("div",{staticClass:"px-3 text-subtitle-1"},[t._v(" If you have questions or issues with using our service, use the form below. "),a("br"),t._v(" We would be happy to answer your questions and watch your problems solved! ")])]),a("v-form",{ref:"form",staticClass:"mx-auto px-5 mt-10 mb-5"},[a("v-row",{attrs:{justify:"center"}},[a("v-col",{staticClass:"pb-0",attrs:{cols:"12",sm:"5"}},[a("v-text-field",{attrs:{outlined:"",label:"First Name"},model:{value:t.firstName,callback:function(e){t.firstName=e},expression:"firstName"}})],1),a("v-col",{staticClass:"pb-0",attrs:{cols:"12",sm:"5"}},[a("v-text-field",{attrs:{outlined:"",label:"Last Name*",rules:t.nameRules},model:{value:t.lastName,callback:function(e){t.lastName=e},expression:"lastName"}})],1)],1),a("v-row",{attrs:{justify:"center"}},[a("v-col",{staticClass:"pb-0",attrs:{cols:"12",sm:"10"}},[a("v-text-field",{attrs:{outlined:"",label:"E-mail*",rules:t.emailRules,disabled:t.emailDisabled},model:{value:t.email,callback:function(e){t.email=e},expression:"email"}})],1)],1),a("v-row",{attrs:{justify:"center"}},[a("v-col",{staticClass:"pb-0",attrs:{cols:"12",sm:"10"}},[a("v-text-field",{attrs:{outlined:"",label:"Subject"},model:{value:t.subject,callback:function(e){t.subject=e},expression:"subject"}})],1)],1),a("v-row",{attrs:{justify:"center"}},[a("v-col",{staticClass:"pb-0",attrs:{cols:"12",sm:"10"}},[a("v-textarea",{attrs:{outlined:"",name:"message",label:"Your Message*",counter:"800",rules:t.messageRules},model:{value:t.message,callback:function(e){t.message=e},expression:"message"}})],1)],1),a("v-row",{attrs:{justify:"center"}},[a("v-btn",{staticClass:"mb-5 px-8",attrs:{outlined:"",color:"primary"},on:{click:t.sendMessage}},[t._v(" Send ")])],1)],1)],1)},n=[],s=a("5530"),r=a("2f62"),o=a("bc3a"),l=a.n(o),c={name:"Contact",data:function(){return{firstName:"",lastName:"",nameRules:[function(t){return!!t||"Name is required"}],email:"",emailDisabled:!1,emailRules:[function(t){return!!t||"E-mail is required"},function(t){return/.+@.+\..+/.test(t)||"E-mail must be valid"}],subject:"",message:"",messageRules:[function(t){return!!t||"Message is required"},function(t){return t.length<=800||"Message must be less than 800 characters"}],isMain:null}},computed:Object(s["a"])({},Object(r["e"])(["userInfo","serverURL"])),methods:{sendMessage:function(){var t=this.$refs.form.validate();if(t){var e=this.firstName?this.firstName+" "+this.lastName:this.lastName,a=this.email,i=this.subject,n=this.message,s={name:e,email:a,subject:i,message:n};l.a.post(this.serverURL["contact"],s).then((function(t){alert("Email successfully sent!")})).catch((function(t){alert("An error occurred during sending email.")}))}else alert("Please fill in the required forms.")}},created:function(){var t=/\/main.*/,e=this.$route.fullPath;t.test(e)&&(this.isMain=!0);var a=this.userInfo.loggedIn;a&&(this.email=this.userInfo.email,this.emailDisabled=!0)}},u=c,d=(a("c1e6"),a("2877")),h=a("6544"),m=a.n(h),f=a("8336"),p=a("62ad"),v=a("a523"),g=(a("4de4"),a("7db0"),a("4160"),a("caad"),a("07ac"),a("2532"),a("159b"),a("58df")),b=a("7e2b"),y=a("3206"),x=Object(g["a"])(b["a"],Object(y["b"])("form")).extend({name:"v-form",provide:function(){return{form:this}},inheritAttrs:!1,props:{disabled:Boolean,lazyValidation:Boolean,readonly:Boolean,value:Boolean},data:function(){return{inputs:[],watchers:[],errorBag:{}}},watch:{errorBag:{handler:function(t){var e=Object.values(t).includes(!0);this.$emit("input",!e)},deep:!0,immediate:!0}},methods:{watchInput:function(t){var e=this,a=function(t){return t.$watch("hasError",(function(a){e.$set(e.errorBag,t._uid,a)}),{immediate:!0})},i={_uid:t._uid,valid:function(){},shouldValidate:function(){}};return this.lazyValidation?i.shouldValidate=t.$watch("shouldValidate",(function(n){n&&(e.errorBag.hasOwnProperty(t._uid)||(i.valid=a(t)))})):i.valid=a(t),i},validate:function(){return 0===this.inputs.filter((function(t){return!t.validate(!0)})).length},reset:function(){this.inputs.forEach((function(t){return t.reset()})),this.resetErrorBag()},resetErrorBag:function(){var t=this;this.lazyValidation&&setTimeout((function(){t.errorBag={}}),0)},resetValidation:function(){this.inputs.forEach((function(t){return t.resetValidation()})),this.resetErrorBag()},register:function(t){this.inputs.push(t),this.watchers.push(this.watchInput(t))},unregister:function(t){var e=this.inputs.find((function(e){return e._uid===t._uid}));if(e){var a=this.watchers.find((function(t){return t._uid===e._uid}));a&&(a.valid(),a.shouldValidate()),this.watchers=this.watchers.filter((function(t){return t._uid!==e._uid})),this.inputs=this.inputs.filter((function(t){return t._uid!==e._uid})),this.$delete(this.errorBag,e._uid)}}},render:function(t){var e=this;return t("form",{staticClass:"v-form",attrs:Object(s["a"])({novalidate:!0},this.attrs$),on:{submit:function(t){return e.$emit("submit",t)}}},this.$slots.default)}}),w=a("0fd9"),C=a("8654"),_=(a("a9e3"),a("1681"),Object(g["a"])(C["a"])),S=_.extend({name:"v-textarea",props:{autoGrow:Boolean,noResize:Boolean,rowHeight:{type:[Number,String],default:24,validator:function(t){return!isNaN(parseFloat(t))}},rows:{type:[Number,String],default:5,validator:function(t){return!isNaN(parseInt(t,10))}}},computed:{classes:function(){return Object(s["a"])({"v-textarea":!0,"v-textarea--auto-grow":this.autoGrow,"v-textarea--no-resize":this.noResizeHandle},C["a"].options.computed.classes.call(this))},noResizeHandle:function(){return this.noResize||this.autoGrow}},watch:{lazyValue:function(){this.autoGrow&&this.$nextTick(this.calculateInputHeight)},rowHeight:function(){this.autoGrow&&this.$nextTick(this.calculateInputHeight)}},mounted:function(){var t=this;setTimeout((function(){t.autoGrow&&t.calculateInputHeight()}),0)},methods:{calculateInputHeight:function(){var t=this.$refs.input;if(t){t.style.height="0";var e=t.scrollHeight,a=parseInt(this.rows,10)*parseFloat(this.rowHeight);t.style.height=Math.max(a,e)+"px"}},genInput:function(){var t=C["a"].options.methods.genInput.call(this);return t.tag="textarea",delete t.data.attrs.type,t.data.attrs.rows=this.rows,t},onInput:function(t){C["a"].options.methods.onInput.call(this,t),this.autoGrow&&this.calculateInputHeight()},onKeyDown:function(t){this.isFocused&&13===t.keyCode&&t.stopPropagation(),this.$emit("keydown",t)}}}),k=Object(d["a"])(u,i,n,!1,null,"087e9d6c",null);e["default"]=k.exports;m()(k,{VBtn:f["a"],VCol:p["a"],VContainer:v["a"],VForm:x,VRow:w["a"],VTextField:C["a"],VTextarea:S})},c1e6:function(t,e,a){"use strict";var i=a("06aa"),n=a.n(i);n.a},d575:function(t,e,a){},d859:function(t,e,a){"use strict";var i=a("fcf8"),n=a.n(i);n.a},db85:function(t,e,a){},e160:function(t,e,a){t.exports=a.p+"img/Banner_005.4cc55980.jpg"},ed5e:function(t,e,a){},fcf8:function(t,e,a){}}]);
//# sourceMappingURL=main.2c0c1b12.js.map