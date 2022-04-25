<template lang='pug'>
h1.headline-2(style="color:white" align='center') Help
.desp(align='center')
    p Here is a manual to help you understand and use 
        span.sign Aurchestra.
.sub-desp
    div
        .card.question-card
            div(class="card__header")
                p.font-bold How to submit a new package request?
            .content
                p If a package needed can not be found in the corresponding OS page, 
                    span you can click the&nbsp
                    span.apply-btn  APPLY 
                    span &nbsp button in the uppre right corner to submit a new package compilation request.
                p Once checked by admin, it will be added into page together with its current state.
                p However, it is not available for installing until the compilation is complete, 
                    span which can be comfirmed if the state shows "
                    span(style="color:green;font-weight:bold") Available
                    span ".
    div
        .card.question-card
            div(class="card__header")
                p.font-bold How to configure in Arch Operating System?
            .content
                p.tbd TBD...
</template>

<script>
export default {
  name: 'Help',
  data() {
      return{
      }
  },
  components:{
  }
}
</script>

<style scoped>
.desp p{
    max-width: 70%;
    color:white;
    font-size: 2em;
    line-height:normal;
}
.sign{
    color: rgb(73, 222, 255);
    font-weight: bolder;
}
.card__header p{
    font-size:1.4em;
    color: rgb(199, 0, 0);
    font-weight: bold;
}
.question-card{
    position: relative;
    left:2%;
    max-width: 95%;
    max-height: 30%;
    margin-bottom: 3%;
}
.card .content p{
    font-size: 0.8em;
    line-height: 1.2em;
}
.apply-btn{
    color:rgb(192, 112, 0);
    font-weight: bold;
    background: rgba(175, 175, 175, 0.812);
    border-radius: 5px;
}
.tbd{
    color:red;

}
</style>
