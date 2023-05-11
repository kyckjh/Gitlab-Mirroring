<template>
  <div>
    <ul>
      <VideoListItem 
        v-for="video in videoList" 
        :key="video.id.videoId"
        :video-item="video"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videoList: Array,
  },
}
</script>

<style>

</style>