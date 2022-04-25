<template>
  <div class="card card--slide-up"
  style="max-width: 520px;
         max-height 320px;
         "
  >
    <div class="card__container" >
      <div
        class="card__image"
        style="
          background-image: url('/images/arch.png');
          background-size: 280px 280px;
          background-position: center 10px;
          
        "
      ></div>
    </div>
    <div class="card__mobile-title">
      <div class="content">
        <div class="tile">
          <div class="tile__container">
            <p class="tile__title">Aurchestra</p>
            <p class="tile__subtitle">Aurchestra is an automated package build orchestration system.</p>
          </div>
        </div>
      </div>
    </div>
    <div class="card__body content">
      <p>
        Designed to establish a distributed, reproducible, and easy-to-manage
    software package build process.
      </p>
    </div>
  </div>

</template>
<script>
export default {
  name: "Home",
  data() {
    return {
      state: "正在施工中...",
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
</style>
