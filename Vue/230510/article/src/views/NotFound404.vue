<template>
  <div>
    <h1>NOT FOUND 404</h1>
    <button @click="goHome">목록으로</button>
  </div>
</template>

<script>
export default {
  name: 'NotFound404',
  methods: {
    goHome() {
      this.$router.push({name:'home'})
    }
  }
}
</script>

<style>

</style>