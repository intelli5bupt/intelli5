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
          <div class="bototm-box">
            <dv-border-box-10 style="height: 8.5rem;width: 19rem;margin-left: 3rem; margin-top: 0.2rem;">
              <div style="margin:0.6rem; margin-left: 3.5rem;" >


                <el-form :inline="true" :model="addForm" :label-position="labelPosition"  :rules="addFormRules" ref="addForm" class="demo-ruleFrom">
                  <!-- 第一行 -->

                  <el-row>
 <el-col :span="8"><div>
            <el-form-item label="业务名称  " prop="jobName">
                <el-input   v-model="addForm.jobName" autocomplete="off"></el-input>
               </el-form-item>
              
                <el-form-item  label="业务描述" prop="jobDescription">
                <el-input type="textarea"  v-model="addForm.jobDescription" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item  label="业务类型">
                      <el-select style="width:90%; margin-left:0.05rem;" :popper-append-to-body="false"  v-model="addForm.jobType" placeholder="请选择">
                          <el-option
                                  v-for="item in options"
                                  :key="item.id"
                                  :label="item.label"
                                  :value="item.label">
                          </el-option>
                      </el-select>
              </el-form-item> 
                    
              <el-form-item  label="类型描述" prop="jobTypeDescription" >
              <el-input type="textarea"  v-model="addForm.jobTypeDescription" autocomplete="off"></el-input>
             </el-form-item>

             <el-form-item  label="模型名称">
                  <el-select style="width:90%; margin-left:0.05rem;" v-model="addForm.jobModelName" placeholder="请选择">
                      <el-option
                              v-for="item in options1"
                              :key="item.id"
                              :label="item.modelName"
                              :value="item.modelName">
                      </el-option>
                  </el-select>
              </el-form-item> 
</div></el-col>
  <el-col :span="8" ><div >
    <el-form-item   label="聚合策略　　　">
                          <el-select  v-model="addForm.modelDeployStrategy" placeholder="请选择">
                              <el-option
                                      v-for="item in options2"
                                      :key="item.id"
                                      :label="item.label"
                                      :value="item.label">
                              </el-option>
                          </el-select>
                  </el-form-item>

                  <el-form-item  label='预　算　　　' prop="budget">
                   <el-input   v-model="addForm.budget" autocomplete="off"></el-input>
                   </el-form-item>

                   <el-form-item  label="安全策略　　">
             
             <el-select  v-model="addForm.jobSafetyStrategy" placeholder="请选择">
                 <el-option
                         v-for="item in options3"
                         :key="item.id"
                         :label="item.label"
                         :value="item.label">
                 </el-option>
             </el-select>
          </el-form-item>
          <el-form-item  label="可支持数据集" prop="jobDatasetDescription" >
           <el-input    type="textarea" v-model="addForm.jobDatasetDescription" autocomplete="off"></el-input>
          </el-form-item>
          <dv-border-box-8 style="margin-left: 1.5rem;width: 1.5rem;">
             <el-button type="text" style="margin-left: 0.5rem;"  @click="submitForm('addForm')">创建</el-button>
              </dv-border-box-8 >
  </div></el-col>
  </el-row>
             </el-form>
             <div>

             </div>
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
  name:'AddJob',
  data() {
    return {
      labelPosition: 'right',
      loading: true,
      username:'',
      addForm:{
                    jobName:'',
                    jobDescription:'',
                    jobType:'',
                    jobTypeDescription:'',
                    jobModelName:'',
                    budget:'',
                    modelDeployStrategy:'',
                    jobSafetyStrategy:'',
                    jobDatasetDescription:'',
                    
                },
                addFormRules: {
                    jobName: [
                        {required: true, message: '请输入业务名称', trigger: 'blur'},
                    ],
                    jobDescription:[{required: true, message: '请输入业务描述', trigger: 'blur'},],
                    jobType: [
                        {required: true, message: '请输入业务类型', trigger: 'blur'},
                    ],
                    budget: [
                        {required: true, message: '请输入预算', trigger: 'blur'},
                    ],
                    jobDatasetDescription: [
                        {required: true, message: '请输入业务数据集描述', trigger: 'blur'},
                    ],

                },
                hasFile:false,
                options: [{
                    id: '1',
                    label: '钢铁缺陷检测'
                }, {
                    id: '2',
                    label: '路面裂缝检测'
                }, {
                    id: '3',
                    label: '瓷砖缺陷检测'
                }, {
                    id: '4',
                    label: '口罩穿戴识别'
                }, {
                    id: '5',
                    label: '安全帽穿戴识别'
                },{
                  id:'6',
                  label:'工作服穿戴识别'
                },
              ],
                options1: [{
                    id: '1',
                    modelName: 'CNN'
                }, {
                    id: '2',
                    modelName: '基于'
                },],
                options2: [{
                    id: '1',
                    label: '能耗优化策略'
                }, {
                    id: '2',
                    label: '参与度激励策略'
                },],
                options3: [{
                    id: '1',
                    label: '多方安全计算'
                }, {
                    id: '2',
                    label: '秘钥传输'
                },],

      }
  },
  mounted() {
    this.cancelLoading();
    this.$axios.get('/job/existModelList').then(res => {
                console.log(res)
                if (res.data.code === 200) {
                    this.options1 = res.data.data
                    console.log(res)
                    //console.log(res.message)
                }
            })
    
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
    submitForm (formName) {
                console.log(this.addForm)
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.$axios.post('/job/jobCreate', this.addForm).then(res => {
                            if(res.data.code ===200){
                                this.$message({message: res.data.message,
                                    type: 'success'})
                                setTimeout(() => {this.resetForm(formName)}, 1000)
                            }else{
                                console.log(res)
                                this.$message.error(res.data.message)
                            }
                        })

                    }}
                )
     },  
    cancelLoading() {
      setTimeout(() => {
        this.loading = false;
      }, 500);
    }
  }
};

</script>

<style lang="scss">
@import "../assets/scss/index.scss";
@import "../assets/scss/index_demo.scss";
</style>


<style lang="scss" scoped>
// ::v-deep .el-input__inner {
//   background-color: transparent !important;
//   //   border-color: rgba(255, 255, 255, 0.5);
//   color: #d9d9d9;
//   height: 40px;
// }
// /**修改边框和字体颜色 */
// ::v-deep .el-select {
//   position: relative;
//   width: 450px;
//   .el-input {
//     input {
//       height: 40px;
//       border-color: rgba(44, 137, 229, 0.5);
//       color: #fff;
//     }
//   }
// }
/**修改下拉图标颜色 */
::v-deep .el-input__suffix {
  .el-input__suffix-inner {
    .el-icon-arrow-up:before {
      color: rgba(44, 137, 229, 0.5);
      padding-left: 0.11rem;
    }
  }
  .el-select-dropdown__item {
  font-size: 7px;
  line-height: 19px;
  color: #fff;
  font-weight: 200;
  background-color: #00083e;
}
// 新增的
::deep.el-select-dropdown {
  background-color: transparent;
  border: 1px solid blue;
}
::deep.el-select-dropdown__list {
  padding: 0;
}
::deep.el-popper[x-placement^="bottom"] {
  margin-top: 0px;
}
::deep.el-popper .popper__arrow,
::deep.el-popper .popper__arrow::after {
  display: none;
}
.el-select-dropdown__item:hover {
  background-color: rgba(0, 225, 219, 0.690196078431373);
}


}
</style>

