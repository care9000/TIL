<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading.....</span>
    </div>

    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디를 입력바랍네다."
        v-model="credentials.username"
        >
        
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input 
        type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호 입력바랍네다."
        v-model="credentials.password"
        >
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        passowrd: '',
      },
      // loading: false, 위에서 관리할거임 
      errors: [],
    }
  },
  computed: {
    loading: function() {
      return this.$store.state.loading //이렇게 상태 관리를 시작할 거임 
    }
  },
  methods: {
    //1. 로그인 유효성 검사가 끝나면
    login() {
      if (this.checkForm()) {
        //2. loading의 상태가 true로 변경하고(spinner-border 돈다.)
        // this.loading = true 바로밑에서 할거니깐 주석 처리할거임 ㅇㅋ?
        this.$store.dispatch('startLoading')
        
        //3. credentials(username, password) 정보를 담아 Django 서버로 로그인 요청을 보낸다.
        axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
        .then(res => {
          // this.$session.start() 바로밑에서 다른걸 로 바꿀거임
          this.$store.dispatch('endLoading')
          // this.$session.set('jwt', res.data.token) 필요없어지고 바로밑에서 다른걸로 작성
          this.$store.dispatch('login', res.data.token)
          router.push('/')
          // console.log(res)
        })
        .catch(err => {
          // this.loading = false 바로밑에서 상태정보로 변경
          this.$store.dispatch('endLoading')  
          console.log(err)
        })
      } else {
        console.log('로그인 실패')
      }
    },
    checkForm() {
      this.errors = []
      //1. 사용자가 아이디를 입력하지 않은 경우
      if (!this.credentials.username){
        this.errors.push("아이디를 입력해주세요.")
      }
      //2. 패스워드가 8글자 미만인 경우
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 입력해주세요.")
      }
      //3. 아이디와 패스워드 모두 잘 입력한 경우
      if (this.errors.length === 0) {
        return true
      }
    }
  }
}
</script>

<style>

</style>