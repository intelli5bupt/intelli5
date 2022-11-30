<template>

	<el-row type="flex" class="row-bg" justify="center">
		<el-col :xl="6" :lg="7">
			<h2>工业智能协同隐私计算平台</h2>
			<br/>
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
			<el-form :model="logintForm" :rules="rules" ref="logintForm" label-width="80px">
				<el-form-item label="用户名" prop="username" style="width: 380px;">
					<el-input v-model="logintForm.username"></el-input>
				</el-form-item>
				<el-form-item label="密码" prop="passwd"  style="width: 380px;">
					<el-input v-model="logintForm.passwd" type="password"></el-input>
				</el-form-item>
			    
				<el-form-item>
					<el-button type="primary" @click="submitForm()">注册</el-button>
					<el-button @click="submittForm('logintForm')">登录</el-button>
				</el-form-item>
			</el-form>
		</el-col>
	</el-row>

</template>

<script>
import axios from 'axios';

	export default {
		name: "Login",
		data() {
			return {
				logintForm: {
					username: 'Intelli5',
					passwd: 'yongzhaiguiguan',
					
				},
				rules: {
					username: [
						{ required: true, message: '请输入用户名', trigger: 'blur' }
					],
					password: [
						{ required: true, message: '请输入密码', trigger: 'blur' }
					]
				
				},
				
			};
		},
		methods: {
			submitForm() {
				this.$router.push("/register")
			},
			submittForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$axios.post('/user/login', this.logintForm).then(res => {
							if(res.data.code === 200){
								console.log(axios.defaults.withCredentials)
								console.log("111111111")
								this.$message({
                                        message: res.data.message,
                                        type: 'success'
                                })
								this.$router.push("/index")
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
				
			}
			
		}
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