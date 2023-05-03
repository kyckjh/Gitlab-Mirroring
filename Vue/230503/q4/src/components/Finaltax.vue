<template>
  <div class="income">
    <h2>결정세액 : {{ max(0, calculatedAmount - reduction) }} 만원 </h2>

  </div>
</template>

<script>

export default {
  name: 'FinalTax',
  props: {
    reduction: Number,
    calculatedAmount: Number,
  },
  methods: {
    max(a, b) {
      return Math.max(a, b)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
