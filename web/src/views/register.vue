<template>
	<el-row type="flex" class="row-bg" justify="center">
		<el-col :xl="6" :lg="7">
			<h2>工业智能协同计算平台</h2>
			<br/>
			<br/>
			<el-image :src="require('@/assets/flipped-aurora.png')" style="height: 200px; width: 200px;"></el-image>

		</el-col>

		<el-col :span="1">
			<el-divider direction="vertical"></el-divider>
		</el-col>

		<el-col :xl="6" :lg="7">
		<br/>
		<br/>
		<br/>
		<br/>
		<br/>
		<br/>
			<el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="80px">
				<el-form-item label="用户名" prop="username" style="width: 380px;">
					<el-input v-model="loginForm.username"></el-input>
				</el-form-item>
				<el-form-item label="密码" prop="password"  style="width: 380px;">
					<el-input v-model="loginForm.password" type="password"></el-input>
				</el-form-item>
				<el-form-item label="验证密码" prop="checkPassword"  style="width: 380px;">
					<el-input v-model="loginForm.checkPassword" type="password"></el-input>
				</el-form-item>
				<el-form-item label="邮箱" prop="email"  style="width: 380px;">
					<el-input v-model="loginForm.email" ></el-input>
				</el-form-item>
				<el-form-item label="公司" prop="company"  style="width: 380px;">
					<el-input v-model="loginForm.company" ></el-input>
				</el-form-item>
				<el-form-item label="电话" prop="phone"  style="width: 380px;">
					<el-input v-model="loginForm.phone" ></el-input>
				</el-form-item>

				<el-form-item>
					<el-button type="primary" @click="submitForm('loginForm')">注册</el-button>
				</el-form-item>
			</el-form>
		</el-col>
	</el-row>

</template>

<script>
	export default {
		name: "Register",
		data() {
			return {
				loginForm: {
					username: '',
					password: '',
					checkPassword: '',
					email:'',
					company:'',
					phone:'',
				},
				rules: {
					username: [
						{ required: true, message: '请输入用户名', trigger: 'blur' }
					],
					password: [
						{ required: true, message: '请输入密码', trigger: 'blur' }
					],
					checkPassword: [
						{ required: true, message: '请输入验证密码', trigger: 'blur' }
					],
					email: [
						{ required: true, message: '请输入邮箱', trigger: 'blur' }
					],
					company: [
						{ required: true, message: '请输入公司名', trigger: 'blur' }
					],
					phone: [
						{ required: true, message: '请输入电话', trigger: 'blur' }
					],
				},
			};
		},
		methods: {
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$axios.post('/user/register', this.loginForm).then(res => {

							if(res.data.code === 200){
								this.$message({
                                        message: res.data.message,
                                        type: 'success'
                                })
								this.$router.push("/login")
							}
							else{
							    console.log(res)
								this.$message.error(res.data.message)
							}
						})

					} else {
						console.log('error submit!!');
						return false;
					}
				});
			},
			
		},
		
	}
</script>

<style scoped>

	.el-row {
		background-color: #fafafa;
		height: 100%;
		display: flex;
		align-items: center;
		text-align: center;
		justify-content: center;
	}

	.el-divider {
		height: 350px;
	}

	.captchaImg {
		float: left;
		margin-left: 8px;
		border-radius: 4px;
	}

</style>