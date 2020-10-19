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
  // 사용자 동의 후 실행할 함수
  const signInCallback = function(authResult) {
    const serverURL = store.state.serverURL
    const loggedIn = true

    if (authResult['code']) {
      // 일회성 코드를 서버로 보낸다.
      axios.post(serverURL['login'], {code: authResult['code']}, {
        headers: {
          'X-Requested-With': 'XMLHttpRequest' // CSRF 공격 방지
        }
      }).then(res => {
        // 로그인 거부된 경우
        if (!res.data.flag) {
          alert(res.data.msg)
          router.push({name:'Home'})
        // 로그인 성공한 경우
        } else {
          const email = res.data['email']
          const name = res.data['name']
          console.log(res)
          // 유저 정보를 Vuex에 담고, Manage 페이지로 포워딩
          store.commit('setUserInfo', {loggedIn, email, name})
          router.push({name: 'Manage'})
        }
      }).catch( ex => {
          console.log(ex)
      })
    } else {
      alert("An Error Occurred!")
    }
  }

  // 로그인 기능을 적용한다.
  // grantOfflineAccess: auth2에 설정된 스코프에 대한 사용자의 동의를 얻은 후
  //   서버측 핸드쉐이크를 위한 일회성 코드를 then으로 반환한다.
  element.addEventListener("click", function() {
    auth2.grantOfflineAccess().then(signInCallback)
  })
}

const userLogout = function() {
  const payload = {loggedIn: false, idToken: '', email: '', name: '', expiresAt: null}

  // 유저 정보 초기화 후 Main 페이지로 이동
  store.commit('setUserInfo', payload)
  router.push({name: 'Main'})
}

export { userLogin, userLogout }