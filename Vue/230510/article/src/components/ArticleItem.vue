<template>
  <div>
    <p>제목: {{ article.title }}</p>
    <p>내용 : </p>
    <p>{{ article.content }}</p>
    <p>작성일 : {{ createAt }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  computed: {
    createAt() {
      return new Date(this.article.createdAt).toString()
    }
  }
}
</script>

<style>

</style>