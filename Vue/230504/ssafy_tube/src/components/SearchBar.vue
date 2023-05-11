<template>
  <div>
    <input type="text" v-model.trim="keyword">
    <button @click="onSearch">검색</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      keyword: '',
    }
  },
  methods: {
    onSearch() {
      // 검색어를 상위 모듈로 전달
      if (this.keyword) {
        this.$emit('search', this.keyword)
        this.keyword = ''        
      } else {
        alert('검색어를 입력하세요')
      }
    },
  },
  
}
</script>

<style>

</style>