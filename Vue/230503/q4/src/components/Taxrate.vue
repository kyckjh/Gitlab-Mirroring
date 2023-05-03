<template>
  <div class="income">
    <h2>산출세액 : {{ calculatedAmount }} 만원</h2>
    <h2>세액감면 : (-) {{ Math.min(reduction, calculatedAmount) }} 만원</h2>
    <hr>
    <Finaltax 
    :reduction="reduction" 
    :calculatedAmount="calculatedAmount"
    />

  </div>
</template>

<script>
import Finaltax from '@/components/Finaltax'

export default {
  name: 'TaxRate',
  components: {
    Finaltax,
  },
  props: {
    standard: Number,
    reduction: Number,
  },
  data() {
    return {
      calculatedAmount: 0,
    }
  },
  watch: {
    standard: function() {
      if (this.standard <= 1200) {
        this.calculatedAmount = this.standard*0.06
      }
      else if (this.standard <= 4600) {
        this.calculatedAmount = this.standard*0.15 - 108
      }
      else if (this.standard <= 8800) {
        this.calculatedAmount = this.standard*0.24 - 522
      }
      else if (this.standard <= 15000) {
        this.calculatedAmount = this.standard*0.35 - 1490
      }
      else if (this.standard <= 30000) {
        this.calculatedAmount = this.standard*0.38 - 1940
      }
      else if (this.standard <= 50000) {
        this.calculatedAmount = this.standard*0.40 - 2540
      }
      else if (this.standard <= 100000) {
        this.calculatedAmount = this.standard*0.42 - 3540
      }
      else {
        this.calculatedAmount = this.standard*0.45 - 6540
      }
      this.calculatedAmount = Math.round(this.calculatedAmount)
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
