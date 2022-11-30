const user = {
    state:{
      user:""
    },
    mutations:{
      USER_INFO(state,info){
        state.user = info
      }
    },
    actions:{
      saveUserInfo({ commit },data){
        commit('USER_INFO',data)
      }
    }
  };
  export default user