<template>
  <div>
    <p>
      <span>연봉 입력 (만원): </span> 
      <input v-model.number="totalAmount" 
        type="number"
        @input="calc"
        > 
    </p>
    <p>
      <span>세액감면액 (만원): </span> 
      <input v-model.number="reduction" type="number"> 
    </p>
    <div class="income">
      <hr>
      <h2>종합소득금액 : {{ totalAmount }} 만원</h2>
      <h2>종합소득공제 : (-) {{ deduction }} 만원</h2>
      <h2>과세표준 : {{ standard }} 만원</h2>
      <hr>
      <Taxrate
      :standard="standard"
      :reduction="reduction"
      />
    </div>

  </div>
</template>

<script>
import Taxrate from '@/components/Taxrate'

export default {
  name: 'InCome',
  components: {
    Taxrate,
  },
  data() {
    return {
      totalAmount: 0,
      deduction: 0,
      reduction: 0,
      standard: 0,
    }
  },
  methods: {
    calc() {
      if (this.totalAmount < 150) {
        this.deduction = this.totalAmount
      } else {
        this.deduction = 150
      }      
      this.standard = this.totalAmount - this.deduction
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.income {
  text-align: left;
}
input {
  border: none;
  background: rgb(206, 219, 255);
}
</style>
