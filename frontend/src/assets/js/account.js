import store from '@/store'
import router from '@/router'
import axios from 'axios'

// 로그인 기능을 적용할 요소 ID를 받고, 로그인 이후 동작을 정의한다.
const userLogin = function(elemID) {
  const clientID = store.state.clientID
  // 로그인 기능을 적용할 요소
  const element = document.getElementById(elemID)
  // OAuth2 기능을 활성화한다.
  const auth2 = gapi.auth2.init({
    client_id: clientID,
  })

  // 로그인 기능을 적용한다. 1: 적용할 요소, 2: 옵션, 3: 성공시 콜백함수
  auth2.attachClickHandler(element, {}, function(googleUser) {
    const serverURL = store.state.serverURL
    const authResponse = googleUser.getAuthResponse()
    const loggedIn = true
    const idToken = ''
    const email = googleUser.getBasicProfile().getEmail()
    const name = googleUser.getBasicProfile().getName()
    const expiresAt = authResponse.expires_at

    axios.post(serverURL['login'], {email, idToken})
    .then( res => {
      // 로그인 거부된 경우
      if (!res.data.flag) {
        alert(res.data.msg)
        router.push({name:'Home'})
        return
      // 로그인 성공한 경우
      } else {
        // 유저 정보를 Vuex에 담고, Manage 페이지로 포워딩
        store.commit('setUserInfo', {loggedIn, idToken, email, name, expiresAt})
        router.push({name: 'Manage'})
      }
      console.log(res)
    }).catch( ex => {
      console.log(ex)
    })
  })
}

const userLogout = function() {
  const payload = {loggedIn: false, idToken: '', email: '', name: '', expiresAt: null}

  // 유저 정보 초기화 후 Main 페이지로 이동
  store.commit('setUserInfo', payload)
  router.push({name: 'Main'})
}

export { userLogin, userLogout }