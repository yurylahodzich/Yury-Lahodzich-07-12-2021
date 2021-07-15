import Vue from 'vue'
import Vuex from 'vuex'

import MessagesModule from '../store/modules/messages-module'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {},
    mutations: {},
    actions: {},
    modules: {
        MessagesModule
    }
})