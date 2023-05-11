import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    number: 0,

  },
  getters: {
  },
  mutations: {
    ADD_NUMBER(state, num) {
      state.number = state.number + num
    }
  },
  actions: {
  },
  modules: {
  }
})
