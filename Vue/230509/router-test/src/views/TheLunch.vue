<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="PickMenu">Pick Lunch</button>
    <h3>{{ menu }}</h3>
    <br>
    <h2>로또를 뽑아보자</h2>
    <router-link to="/lotto/6"><button>Pick Lotto</button></router-link>
  </div>
</template>

<script>
export default {
  name: 'TheLunch',
  data() {
    return {
      menu: '',
      menuList: ['국밥', '짜장면', '치킨', '파스타', '햄버거',
                 '짬뽕', '칼국수', '라면', '비빔밥', '김밥',
                 '제육덮밥', '텐동', '떡볶이', '찜닭', '스테이크',
                 '마라탕', '스팸덮밥', '김치찌개', '순두부찌개']
    }
  },
  methods: {
    PickMenu() {
      let num = Math.ceil(Math.random()*this.menuList.length)
      this.menu = this.menuList[num]
    }
  }
}
</script>

<style>

</style>