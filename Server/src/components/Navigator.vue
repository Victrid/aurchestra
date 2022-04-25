<template class="content">
<div class="header header-fixed u-unselectable header-animated u-fixed">
    <div class="header-brand">
        <div class="nav-item no-hover">
            <a href="/"><h6 class="title" >Aurchestra</h6></a>
        </div>
    </div>
    <div class="header-nav" id="header-menu">
        <div class="nav-left">
            <!-- <div class="nav-item text-center">
                <a href="#">
                    <span class="icon">
                        <i class="fab fa-wrapper fa-github" aria-hidden="true"></i>
                    </span>
                </a>
            </div> -->
            <div class="nav-item has-sub toggle-hover" id="dropdown">
                <a class="nav-dropdown-link">Supported OS</a>
                <ul class="dropdown-menu dropdown-animated" role="menu">
                    <li role="menu-item"><a href="arch">Arch Linux</a></li>
                    <li role="menu-item" ><a>Coming soon...</a></li>
                </ul>
            </div>
        </div>

        <div class="nav-right">
            <div class="nav-item">
                <a href="about">About</a>
            </div>
            <div class="nav-item">
                <a href="help">Help</a>
            </div>
            <div class="nav-item active">
                <a href="admin">Aadministrator</a>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'Navi',
  data() {
      return{
         
      }
  }
}
</script>

<style>

</style>

