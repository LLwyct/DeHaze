import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    drawer: false
  },
  mutations: {
    changeDrawerState (state) {
      state.drawer = !state.drawer
    }
  },
  actions: {
    changeDrawerState ({commit}) {
      commit('changeDrawerState')
    }
  }
})
