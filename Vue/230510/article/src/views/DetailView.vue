<template>
  <div>
    <h1>상세화면</h1>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : </p>
    <p>
      {{ article?.content }}
    </p>
    <p>작성일 : {{ new Date(article?.createdAt).toString() }}</p>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
    }
  },
  methods: {
    getArticle() {
      const id = Number(this.$route.params.articleId)
      for (const article of this.$store.state.articles) {
        if(article.id === id) {
          return article
        }
      }
      this.$router.push({name:'notfound404'})
      //return null
    }
  },
  created() {
    this.article = this.getArticle()
  }
}
</script>

<style>

</style>