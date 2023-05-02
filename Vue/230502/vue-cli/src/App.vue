<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class="page">
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <section>
        
        <button :class="[reservations.includes(time) ? 'clicked' : 'button']" 
        v-for="(time, index) in times" 
        :key="index"
        @click="onBtnClick(time)">{{ time }}</button>
        <br><br>
        <hr class="line">
        <div>
          <h3>선택 시간 : <span v-for="res in reservations" :key="res">{{ res }} </span></h3>
          

        </div>
      </section>
    </div>
    
    <!-- <MyComponent />
    <MyComponent /> -->
    <!-- <HelloWorld :msg="msg"/> -->
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
// import MyComponent from './components/MyComponent.vue'

export default {
  name: 'App',
  data() { return { times: [
  "00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30",
  "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", 
  "08:00", "08:30",
    "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
], 
reservations: [],
} },
  components: {
    //HelloWorld,
    //MyComponent,
  },
  methods: {
    onBtnClick(time) {
      if (this.reservations.includes(time))
      {
        const idx = this.reservations.indexOf(time)
        this.reservations.splice(idx, 1)
      } else {
        if (this.reservations.length === 5) {
          alert("5타임까지만 신청할 수 있습니다.")
        } else {
          this.reservations.push(time)
          this.reservations.sort()
        }
      }
    },
  }
}

</script>

<style>
.clicked {
  margin: 6px;
  background-color: #658dc63d;
  border: none;
  color: #0F4C81;
}
.button {
  margin: 6px;
  background-color: white;
  border: none;
  color: #84898C;
}
#app {  
  font-family: 'Noto Sans KR';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;  
}
@font-face {
  font-family: 'Noto Sans KR', sans-serif;
  src: url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500&display=swap')
}
.page {
  padding-top: 10px;
  padding-bottom: 50px;
  margin-left: auto;
  margin-right: auto;
  height: 350px;
  width: 500px;
  box-shadow: 5px 5px 10px rgb(192, 192, 192);
}
.line {
  width: 400px;
}
</style>
