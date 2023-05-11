<template>
  <div id="app">
    <div>
      <SearchBar @search="onSearch"/>
    </div>
    <div class="d-flex flex-row justify-content-around">
      <VideoDetail/>
      <VideoList :video-list="videoList"/>
    </div>
    <ul>
      <li v-for="video in videoList" :key="video.id.videoId">
        <img :src="video.snippet.thumbnails.default.url" alt="">
      </li>
    </ul>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import VideoDetail from '@/components/VideoDetail.vue'
import VideoList from '@/components/VideoList.vue'
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      videoList: [],
    }
  },
  components: {
    SearchBar,
    VideoDetail,
    VideoList
  },
  methods: {
    onSearch(keyword) {
      this.search(keyword)
    },
    search(keyword) {
      //api 요청해서 데이터 받아와서 this.videoList에 추가
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      axios({
        url: API_URL,
        params: {
          key: 'AIzaSyDXwqkf_7BJOhVrWmEKyes_uxo-AEEEWwU', 
          part: 'snippet',
          type: 'video',
          q: keyword,
        }
      })
      .then((response)=>{
        console.log(response.data.items)
        this.videoList = response.data.items
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
