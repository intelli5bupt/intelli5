<template>
  <div id="index">
    <dv-full-screen-container class="bg">
      <dv-loading v-if="loading">Loading...</dv-loading>
      <div v-else class="host-body">
        <div class="d-flex jc-center">
          <dv-decoration-10 style="width:33.3%;height:.0625rem;" />
          <div class="d-flex jc-center">
            <dv-decoration-8 :color="['#568aea', '#000000']" style="width:2.5rem;height:.625rem;" />
            <div class="title">
              <router-link :to="{name:'index'}">
              <span class="title-text" >工业智能协同隐私计算平台</span>
              </router-link>
              <dv-decoration-6
                class="title-bototm"
                :reverse="true"
                :color="['#50e3c2', '#67a1e5']"
                style="width:3.125rem;height:.1rem;"
              />
            </div>
            <dv-decoration-8
              :reverse="true"
              :color="['#568aea', '#000000']"
              style="width:2.5rem;height:.625rem;"
            />
          </div>
          <dv-decoration-10 style="width:33.3%;height:.0625rem; transform: rotateY(180deg);" />
        </div>

        <!-- 第二行 -->
        <div class="d-flex jc-between px-2">
          <div class="d-flex" style="width: 40%">
            <!-- <div
              class="react-right ml-4"
              style="width: 6.25rem; text-align: left;background-color: #0f1325;"
            >
              <span class="react-before"></span>
              <span class="text">数据接入</span>
            </div>
            <div class="react-right ml-3" style="background-color: #0f1325;">
              <span class="text colorBlue">数据处理</span>
            </div> -->
            <div class="react-right  bg-color-blue mr-3">
              <router-link :to="{name:'Datamanage'}">
              <span class="text fw-b">数据管理</span>
              </router-link>
            </div>  
            <div class="react-right  bg-color-blue mr-3">
              <router-link :to="{name:'Devicemanage'}">
              <span class="text fw-b" >设备管理</span>
              </router-link>
            </div>
            <div class="react-right  bg-color-blue mr-3">
              <router-link :to="{name:'Myjob'}">
              <span class="text fw-b">我的业务</span>
              </router-link>
            </div>
            <div class="react-right  bg-color-blue mr-3">
              <router-link :to="{name:'Addjob'}">
              <span class="text fw-b" >业务接入</span>
              </router-link>
            </div>  
            
          </div>
          <div style="width: 40%" class="d-flex">
            <div class="react-left bg-color-blue mr-3">
              <router-link :to="{name:'Model'}">
              <span class="text fw-b" >智能建模</span>
              </router-link>
            </div>
            <div class="react-left bg-color-blue mr-3">
              <router-link :to="{name:'Model_analysis'}">
              <span class="text fw-b">在线推理</span>
              </router-link>
            </div>
            <div class="react-left bg-color-blue mr-3">
              <router-link :to="{name:'Jobmanage'}">
              <span class="text fw-b" >业务管理</span>
              </router-link>
            </div>
            <div
              class="react-left mr-4"
              style="width: 6.25rem; background-color: #0f1325; text-align: right;"
            >
              <span class="react-after"></span>
              <span class="text">{{this.username}}</span>
            </div>
          </div>
        </div>

        <div class="body-box">
          <!-- 第三行数据 -->
          <div class="content-box">
            <dv-border-box-10 style="height: 8rem;width: 21rem;margin-left: 0.5rem;">
         <div  style="margin:0.75rem;">
        <el-form label-width="100px" class="demo-addForm">
          <div style="width: 300px;" >
            <el-form-item label="模型名称" prop="modelName" label-width="100px">
                <el-input v-model="modelName"  size=" mini"></el-input>
            </el-form-item>
          </div>
            <el-form-item label="模型上传" prop="modelFile" label-width="100px">
                <!-- <el-upload
                        class="upload-import"
                        ref="uploadImport"
                        :http-request ="httpRequest"
                        action=""
                        :on-preview="handlePreview"
                        :on-remove="handleRemove"
                        :limit="1">
                    <el-button v-show="!hasFile" slot="trigger" size="small" type="primary">点击上传</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传pt文件,且不超过500kb</div>
                </el-upload> -->
                <div>
                  <el-upload action="#" list-type="picture-card" :auto-upload="false" :file-list="files" :on-change="addFile">
                      <i slot="default" class="el-icon-plus"></i>
                      <div slot="file" slot-scope="{file}">
                        <img class="el-upload-list__item-thumbnail" :src="file.url" alt="">
                        <span class="el-upload-list__item-actions">
                          <span
                            class="el-upload-list__item-preview"
                            @click="handlePictureCardPreview(file)"
                          >
                            <i class="el-icon-zoom-in"></i>
                          </span>
                          <span
                            v-if="!disabled"
                            class="el-upload-list__item-delete"
                            @click="handleDownload(file)"
                          >
                            <i class="el-icon-download"></i>
                          </span>
                          <span
                            v-if="!disabled"
                            class="el-upload-list__item-delete"
                            @click="handleRemove(file)"
                          >
                            <i class="el-icon-delete"></i>
                          </span>
                        </span>
                      </div>
                  </el-upload>
                </div>

            </el-form-item>

            <el-form-item label="加密策略">
        
                    <el-select v-model="encryptAlgorithm" placeholder="请选择">
                        <el-option
                                v-for="item in options"
                                :key="item.id"
                                :label="item.label"
                                :value="item.label">
                            <!-- <el-tooltip class="item" effect="dark" content="Top Left 提示文字" placement="right">
                                <p>{{item.label}}</p>
                            </el-tooltip> -->
                        </el-option>
                    </el-select>
         

            </el-form-item>

            <el-form-item>
                <el-button type="primary"  @click="submit()">提交</el-button>
            </el-form-item>
             </el-form>

            
         </div>
         </dv-border-box-10>
          </div>
        
        </div>
      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>

export default {
  name:'Model',
  data() {
    return {
      dialogVisible: false,
      loading: true,
      modelName:'',
      disabled: false,
      encryptAlgorithm:'',
      username:'',
      files:[],
      options: [{
                    id: '1',
                    label: '秘密共享'
                }, {
                    id: '2',
                    label: '私钥加密'
                },],
          }
  },
  mounted() {
    this.cancelLoading();
    this.$axios.get('/user/current').then(res => {
                console.log(res)
                if (res.data.code === 200) {
                    this.username = res.data.data
                    console.log(res)
                    //console.log(res.message)
                }
            })
  },
  methods: {
    handleRemove(file) {
        console.log(file);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      handleDownload(file) {
        console.log(file);
      },
      addFile(file){
        this.files=file
      },
      submit(){
        // console.log(this.modelName)
        // console.log(this.encrypAlgorithm)
        // console.log(this.files)
        const data ={
          modelName:this.modelName,
          encryptAlgorithm:this.encryptAlgorithm,
          files:this.files,
        }
        console.log(data)            
        this.$axios.post('/model/modelUpload',data).then(res => {
                    console.log(res)
                    if (res.data.code === 200) {
                        // this.tableData = res.data.data
                        console.log(res)
                        this.$message({
                                message: res.data.message,
                                type: 'success'
                            })
                        //console.log(res.message)
                    }else {
                            this.$message.error(res.data.message)
                        }
         })
      },

    
    // handleRemove(file, fileList) {
    //             console.log(file, fileList);
    //             if (!fileList.length) {
    //                 this.hasFile = false;
    //             }
    //             this.addForm.file = null;
    //         },
          //   handlePreview(file) {
          //       console.log(file);
          //   },
          //   submitForm (formName) {
          //       this.$refs[formName].validate((valid) => {
          //               if (valid) {
          //                 this.$axios.post('/model/mdoel_maker', this.addForm)
          //                       .then(res => {
          //                           console.log(res)
          //                           if (res.data.code === 200) {

          //                               // this.editVisible = false
          //                               // this.getDatalist()
          //                               this.$message({
          //                                   message: res.data.message,
          //                                   type: 'success'
          //                               })
          //                               setTimeout(() => {
          //                               }, 1000)
          //                           } else {
          //                               this.$message.error(res.data.message)
          //                           }
          //                       })
          //               }

          //           }
          //       )
          //   },
          //   httpRequest(param) {
          //       let fd = new FormData();
          //       fd.append('file', param.file); // 传文件
          //       let fd2 = new FormData();
          //       fd2.append('modelName', this.addForm.modelName);
          //       fd2.append('encrypAlgorithm',this.addForm.encrypAlgorithm)
          //       console.log(fd)
          //       //dataPar.file.raw
          //       this.$axios.post('/model/model_maker', fd2 , {
          //           // headers: {'Content-Type': 'multipart/form-data'},//定义内容格式,很重要
          //           timeout: 20000,
          //       }).then(res=> {
          //           console.log(res)
          //           //接口成功调用params上的onSuccess函数，会触发默认的successHandler函数
          //           //这样可以用自带的ui等
          //           ///params.onSuccess({name: 'eric'})
          //       })
          //   },
          // toindex(){
          //   this.$router.push("/")
          // },
          // todata(){
          //   this.$router.push("/datamanage")
          // },
          // todevice(){
          //   this.$router.push("/devicemanage")
          // },
          // tojob(){
          //   this.$router.push("/addjob")
          // },
          // tojobmanage(){
          //   this.$router.push("/jobmanage")
          // },
          // tomodel(){
          //   this.$router.push("/model")
          // },
          cancelLoading() {
            setTimeout(() => {
              this.loading = false;
            }, 500);
    },
    // handleRemove(file,fileList) {
		// 		console.log(file,fileList);
		// 	},
		// 	submitUpload() {
		// 		this.$refs.upload.submit();
		// 	},
		// 	// 文件上传成功时的函数
		// 	handleFilUploadSuccess (res,file,fileList) {
		// 		console.log(res,file,fileList)
		// 		this.$message.success("上传成功")
		// 	},
		// 	handleUpdate () {
		// 		this.dialogVisible = true;
		// 	},
		// 	// 处理文件上传的函数
		// 	handleUpload () {
		// 		// console.log(res,file)
		// 		this.submitUpload()
		// 		this.dialogVisible = false
		// 	}
  }
};
</script>

<style lang="scss">
@import "../assets/scss/index.scss";
@import "../assets/scss/index_demo.scss";
</style>