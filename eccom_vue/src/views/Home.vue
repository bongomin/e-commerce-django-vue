<template>
  <div class="home">
     <section class="hero is-medium is-dark mb-6">
       <div class="hero-body has-text-centered">
         <p class="title mb-6">
           Welcome to Daniel's Online Store
         </p>
         <p class="subtitle">
           The Best vue eccomerce store online
         </p>
       </div>
     </section>
     <div class="columns is-multiline">
       <div class="column is-12">
         <h2 class="is-size-2 has-text-centered">
           Latest Products
         </h2>
       </div>
       <div class="column is-3"
        v-for="product in latestProducts"
        :key="product.id"
        >
          <div class="box">
            <figure class="image mb-4">
              <img :src="product.get_thumbnail">
            </figure>
            <h3 class="is-size-4">{{product.name}}</h3>
            <p class="is-size-6">${{product.price}}</p>
            view details
          </div>
       </div>
     </div>
  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
  },

  data() {
    return {
      latestProducts: []
    }
  },

  mounted() {
    this.getLatestProducts()
  },

  methods: {
    // http: // localhost: 8000/api/v1/latest-products/
    getLatestProducts() {
      axios
      .get('http://localhost:8000/api/v1/latest-products/')
      .then(response=> {
        this.latestProducts = response.data
      })
      .catch(error => console.error('error has occured'))
    }

  }
}
</script>
<style scoped>
.image {
  margin-top: -1.25em;
  margin-left: -1.25em;
  margin-right: -1.25em;
}
</style>
