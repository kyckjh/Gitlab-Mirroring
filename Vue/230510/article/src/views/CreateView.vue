<template>
  <div>
    <h1>글쓰기</h1>
    <form @submit.prevent="onSubmit">
      <p><label for="title">제목 : </label>
      <input type="text" id="title" v-model="title"></p>
      <p><label for="content">내용 :</label></p>
      <p><textarea v-model="content" id="content" cols="30" rows="10"></textarea></p>
      <p><input type="submit" value="작성하기"></p>
    </form>
    <router-link :to="{name:'home'}">목록으로</router-link>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  data() {
    return {
      title: '',
      content: '',

    }
  },
  methods: {
    // onSubmit(event) {
    //   event.preventDefault()
    //   console.log('우와!')
    // }    
    onSubmit() {
      const payload = {
        title: this.title,
        content: this.content,
      }
      this.$store.dispatch('addArticle', payload)
      this.$router.push({name:'home'})
    }
  }
}
</script>

<style>

</style>