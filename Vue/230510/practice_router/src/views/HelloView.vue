<template>
  <div>
    <h1>Hello!! {{ userName }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloView',
  computed: {
    userName() {
      return this.$route.params.userName
    }
  },
  created() {
    console.log('created!!')
  },
  beforeRouteUpdate(to, from, next) {
    console.log(to.params.userName)
    console.log(from.name)
    next()
  }
}
</script>

<style>

</style>