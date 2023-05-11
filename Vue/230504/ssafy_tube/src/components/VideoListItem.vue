<template>
  <div>
    <img :src="videoItem.snippet.thumbnails.default.url" alt="">
    <span>{{ videoItem.snippet.title }}</span>
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    videoItem: Object,
  },  
}
</script>

<style>

</style>