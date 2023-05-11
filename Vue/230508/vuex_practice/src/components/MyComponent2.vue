<template>
  <div>
    <h1>MyComponent2</h1>
    <h1>Number : {{ number }}</h1>
  </div>
</template>

<script>
export default {
  name: 'MyComponent2',
  computed: {
    number() {
      return this.$store.state.number
    }
  }
}
</script>

<style>

</style>