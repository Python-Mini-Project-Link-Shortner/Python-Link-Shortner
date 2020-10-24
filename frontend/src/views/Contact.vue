<template>
	<v-container class="pt-0 px-0" :class="{'limit-width': isMain}">
		<div class="polygon white--text">
			<div class="pt-5 mb-3 text-h5 font-weight-medium">
				E-Mail Us
			</div>
			<div class="px-3 text-subtitle-1">
				If you have questions or issues with using our service, 
				use the form below.
				<br>
				We would be happy to answer your questions 
				and watch your problems solved!
			</div>
		</div>

		<v-form 
			ref="form"
			class="mx-auto px-5 mt-10 mb-5"
		>
			<!-- 첫 줄: 이름과 성-->
			<v-row justify="center">
				<v-col class="pb-0" cols="12" sm="5">
					<v-text-field
						outlined
						v-model="firstName"
						label="First Name"
					/>
				</v-col>
				<v-col class="pb-0" cols="12" sm="5">
					<v-text-field
						outlined
						v-model="lastName"
						label="Last Name*"
						:rules="nameRules"
					/>
				</v-col>
			</v-row>

			<!-- 둘째 줄: 받을 이메일-->
			<v-row justify="center">
				<v-col class="pb-0" cols="12" sm="10">
					<v-text-field
						outlined
						v-model="email"
						label="E-mail*"
						:rules="emailRules"
						:disabled="emailDisabled"
					/>
				</v-col>
			</v-row>

			<!-- 셋째 줄: 제목 -->
			<v-row justify="center">
				<v-col class="pb-0" cols="12" sm="10">
					<v-text-field
						outlined
						v-model="subject"
						label="Subject"
					/>
				</v-col>
			</v-row>

			<!-- 넷째 줄: 내용 -->
			<v-row justify="center">
				<v-col class="pb-0" cols="12" sm="10">
					<v-textarea
						outlined
						v-model="message"
						name="message"
						label="Your Message*"
						counter="800"
						:rules="messageRules"
					/>
				</v-col>
			</v-row>

			<v-btn
				outlined
				class="mb-5 px-8"
				color="primary"
				@click="sendMessage"
			>
				Send
			</v-btn>
		</v-form>
	</v-container>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'

export default {
	name: 'Contact',
	data: () => ({
		firstName: '',
		lastName: '',
		nameRules: [
			v => !!v || 'Name is required'
		],
		email: '',
		emailDisabled: false,
		emailRules: [
			v => !!v || 'E-mail is required',
			v => /.+@.+\..+/.test(v) || 'E-mail must be valid'
		],
		subject: '',
		message: '',
		messageRules: [
			v => !!v || 'Message is required',
			v => v.length <= 800 || 'Message must be less than 800 characters',
		],
		isMain: null
	}),
	computed: {
		...mapState(['userInfo', 'serverURL'])
	},
	methods: {
		sendMessage() {
			// 서버에 내용을 전송한다.
			const isValid = this.$refs.form.validate()

			if (isValid) {
				const name = (this.firstName) ? 
					this.firstName + " " + this.lastName : this.lastName
				const email = this.email
				const subject = this.subject
				const message = this.message
				const sendData = {name, email, subject, message}

				axios.post(this.serverURL['contact'], sendData)
					.then( res => {
						alert('Email successfully sent!')
					}).catch( ex => {
						alert('An error occurred during sending email.')
					})
			} else {
				alert("Please fill in the required forms.")
			}
		}
	},
	created() {
		// Main 페이지일 경우 isMain = True
		const mainReg = /\/main.*/
		const fullPath = this.$route.fullPath

		if (mainReg.test(fullPath)) {
			this.isMain = true
		}

		// 로그인되어 있는 경우 Email 고정 (Manage 페이지)
		const loggedIn = this.userInfo.loggedIn
		
		if (loggedIn) {
			this.email = this.userInfo.email
			this.emailDisabled = true
		}
	}
}
</script>

<style scoped>
.polygon {
	background: linear-gradient(to bottom, rgb(55,115,165), #67D7F5);
	width: inherit;
	height: 250px;
	-webkit-clip-path: polygon(0 0, 100% 0, 100% 59%, 49% 100%, 0 59%);
	clip-path: polygon(0 0, 100% 0, 100% 59%, 50% 100%, 0 59%);
}
.v-form {
	max-width: 700px;
}
</style>