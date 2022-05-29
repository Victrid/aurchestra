<template lang='pug'>
.card.card--slide-up(align='center')
      div(class="card__container")
        div(class="card__image", style="\
          background-image: url('/images/arch.png');\
          background-size: 280px 280px;\
          background-position: center 10px;\
          \
        ")
      div(class="card__mobile-title")
        .content
          .tile
            div(class="tile__container")
              p(class="tile__title") Aurchestra
              p(class="tile__subtitle") Aurchestra is an automated package build orchestration system.
      div(class="card__body content")
        p
          | Designed to establish a distributed, reproducible, and easy-to-manage
          | software package build process.
.about-content
  h1.headline-4(style="color:white" align='center') About
  .desp(align='center')
      p Welcome to 
          span.sign Aurchestra
          span , an automated package build orchestration system.
      p.sub This is also a course project for EE458(
          span.crouseName Software Engineering
          span ) 2022 Spring, 
      p.sub instructed by Prof. 
          a.link(href="https://www.cs.sjtu.edu.cn/~jdyu/") Jiadi Yu
  br
  br
  br
  h2.headline-6(style="color:white" align="center") System Introduction
  //- 基本情况介绍
      //- 前端
      //- 守护模块
      //- 编译模块
      //- 存储库系统
  .intro(align='center')
    p In the daily process of installing packages in the Arch OS, 
        p unstable network connections and lengthy compilation always trouble people.
    br
    p To solve this problem, Aurchestra,
        p a distributed, reproducible, and manageable package building process, 
        p is proposed for building packages to help users quickly deploy individual source.
    br
    p Aurchestra is currently only focusing on the package compilation in Arch Linux, 
        p and we also look forward to expanding Aurchestra's applicable systems in the future.
    br
    p Currently, Aurchestra consists of four independent components:
        .compo.card
            .content.u-text-left
                p A web framework to control build entries and display system information.
                p A daemon process to check updates and scadule compilation.
                p A complier process based on Arch Linux build system.
                p An atomic, manageable package repository.
    p The above modules communicate through RESTful HTTP interfaces 
        p and are deployed using Kubernetes.
    p BTW, as a course project, there are objective limitations in terms of time and technical background, 
        p and any criticisms or suggestions are welcome.
  //- 组员介绍
  br
  br
  br
  h2.headline-6(style="color:white" align="center") Group Memebers

  .members(align='center')
      .card
          .content.u-text-center.pt-3
              figure.avatar(style="height: 5rem; width:5rem;")
                  img(v-bind:src='jiang_avatar_src')
              p#projectname.title.mt-2.mb-0 Weihao Jiang  
                  span.chineseName 蒋圩淏
              p.motto We conjure the spirits of <br>the computer with our spells.
              div(align='center' style="max-height:4rem;")
                  a.smoothScroll(v-bind:href='jiang_github' target="_blank" rel="noopener noreferrer" style="color:inherit;" )
                      svg.svg-inline--fa.fa-github.fa-w-16.fa-wrapper.small(aria-hidden="true", focusable="false", data-prefix="fab", data-icon="github", role="img", xmlns="http://www.w3.org/2000/svg", viewBox="0 0 496 512",style="height: 3rem; width:3rem;")
                          path(fill="currentColor", d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z")
      .card
          .content.u-text-center.pt-3
              figure.avatar(style="height: 5rem; width:5rem;")
                  img(v-bind:src='tang_avatar_src')
              p#projectname.title.mt-2.mb-0 Peng Tang  
                  span.chineseName 唐鹏
              p.motto I will greet this day<br> with love in my heart.
              div(align='center' style="max-height:4rem;")
                  a.smoothScroll(v-bind:href='tang_github' target="_blank" rel="noopener noreferrer" style="color:inherit;" )
                      svg.svg-inline--fa.fa-github.fa-w-16.fa-wrapper.small(aria-hidden="true", focusable="false", data-prefix="fab", data-icon="github", role="img", xmlns="http://www.w3.org/2000/svg", viewBox="0 0 496 512",style="height: 3rem; width:3rem;")
                          path(fill="currentColor", d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z")
      .card
          .content.u-text-center.pt-3
              figure.avatar(style="height: 5rem; width:5rem;")
                  img(v-bind:src='xu_avatar_src')
              p#projectname.title.mt-2.mb-0 Zihang Xu  
                  span.chineseName 徐子航
              p.motto Good good learn, <br>day day up.
              div(align='center' style="max-height:4rem;")
                  a.smoothScroll(v-bind:href='xu_github' target="_blank" rel="noopener noreferrer" style="color:inherit;" )
                      svg.svg-inline--fa.fa-github.fa-w-16.fa-wrapper.small(aria-hidden="true", focusable="false", data-prefix="fab", data-icon="github", role="img", xmlns="http://www.w3.org/2000/svg", viewBox="0 0 496 512",style="height: 3rem; width:3rem;")
                          path(fill="currentColor", d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z")
      .card
          .content.u-text-center.pt-3
              figure.avatar(style="height: 5rem; width:5rem;")
                  img(v-bind:src='qing_avatar_src')
              p#projectname.title.mt-2.mb-0 Yunfan Qing 
                  span.chineseName  卿云帆
              p.motto A hunter of shadows,<br> himself a shade.
              div(align='center' style="max-height:4rem;")
                  a.smoothScroll(v-bind:href='qing_github' target="_blank" rel="noopener noreferrer" style="color:inherit;" )
                      svg.svg-inline--fa.fa-github.fa-w-16.fa-wrapper.small(aria-hidden="true", focusable="false", data-prefix="fab", data-icon="github", role="img", xmlns="http://www.w3.org/2000/svg", viewBox="0 0 496 512",style="height: 3rem; width:3rem;")
                          path(fill="currentColor", d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z")


</template>
<script>

export default {
  name: "Home",
  data() {
    return {
      state: "正在施工中...",
    //  
      jiang_github:'https://github.com/Victrid',
      jiang_words: 'We conjure the spirits of the computer with our spells.',
      jiang_avatar_src: 'images/jiang.jpg',
    //   
      tang_github:'https://github.com/JustQJ',
      tang_words: 'I will greet this day with love in my heart.',
      tang_avatar_src: 'images/tang.jpg',
    //   
      xu_github:'http://www.baidu.com',
      xu_words: 'Good good learn, day day up.',
      xu_avatar_src: 'images/xu.png',

      qing_github:'https://github.com/floudk',
      qing_words:"A hunter of shadows, himself a shade.",
      qing_avatar_src:'images/qing.png',
    };
  },
  components: {},
};
</script>

<style scoped>
.tile__title{
    font-size:20pt;
    margin-left: 4pt;
    color: rgb(6, 143, 206);
}
.tile__subtitle{
    font-size:12pt;
    margin-left: 4pt;
    color: black;
    font-weight: bold;
}
.card__body.content p{
    font-size:14pt;
    color: rgb(3, 129, 133);
}

#home-content .card.card--slide-up{
  width: 32%;
  height: 50%;
  left: 34%;
  margin-top: 5%;
}

.about-content{
  float: none;
  margin-top: 2%;
}
.about-content .desp p{
    max-width: 70%;
    color:white;
    font-size: 2em;
    line-height:normal;
}
.about-content .desp p.sub{
    max-width: 70%;
    color:white;
    font-size: 1.7em;
    line-height: 0.9em;
}
.about-content .intro p{
    color:white;
    font-size: 1.8em;
    line-height:0.8em;
}
.about-content .intro .compo{
    position: inherit;
    background-color:rgba(254, 254, 254, 0.501);
    max-height: 10em;
    max-width: 47%;
}
.about-content .intro .compo p{
    color: black;
    font-size: 1.1em;
    font-weight: bold;
    margin-left: 1em;
}
.about-content .sign{
    color: rgb(73, 222, 255);
    font-weight: bolder;
}
.about-content .crouseName{
    color: rgba(255, 73, 73, 0.841);
    font-weight: bold;
}
.about-content .link{
    color:rgb(0, 255, 242);
    font-style: italic;
}
.about-content .members{
    /* margin-right: 40%; */
    margin-left:8%;
    margin-right:8%;
}
.about-content .members .card{
    margin-right: 20px;
}
.about-content .chineseName{
    font-size: 0.6em;
    font-style: normal;
}
.about-content p.motto{
    font-weight: bold;
    font-size: 1em;
    margin-left: 3px;
    margin-right: 3px;
}
.about-content .members .card{
    height:35%;
    width: 22%;
    position:relative;
    display:inline-block;
}

</style>
