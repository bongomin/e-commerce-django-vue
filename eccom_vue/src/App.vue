<template>
  <div id="wrapper">
    <nav class="navbar is-light">
      <div class="navbar-brand">
        <router-link to="/" class ="navbar-item">
        <strong>Daniel's Vue Eccomm</strong>
        </router-link>

        <a class="navbar-burger" aria-label="menu"
        arial-expanded="false"
        data-target="navbar-menu"
        @click="showMobileMenu = !showMobileMenu">
          <span arial-hidden="true"></span>
          <span arial-hidden="true"></span>
          <span arial-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'isActive':showMobileMenu}">
        <div class="navbar-end">
           <router-link to="/summer" class ="navbar-item">Summer</router-link>
           <router-link to="/winter" class ="navbar-item">Winter</router-link>

           <div class="navbar-item">
             <div class="buttons" >
               <router-link to="/login" class ="button is-light">Login</router-link>
               <router-link to="/cart" class ="button is-success">
               <span class="icon"><i class="fa fa-shopping-basket"></i></span>
               <span>Cart</span>
               </router-link>
             </div>
           </div>

        </div>
      </div>
    </nav>
    <div class="section">
        <router-view/>
    </div>
    <div class="footer">
      <p class="has-text-centered">copyright (c) 2021 </p>
    </div>
  </div>
</template>

<script>
export default ({
  data() {
    return {
    showMobileMenu: false,
    }
  },
})
</script>


<style lang="scss">
@import '../node_modules/bulma'

</style>
