<template>
  <div class="home">
    <h1>Home</h1>
    <button @click="goCreate">글쓰기</button>
    <ArticleItem v-for="article in articles" :key="article.id" :article="article"/>
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem'
export default {
  name: 'HomeView',
  components: {
    ArticleItem
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  methods: {
    goCreate() {
      this.$router.push({name:'create'})
    }
  }
}
</script>
