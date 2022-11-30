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
            <dv-border-box-8 style="margin-left: 0.6rem;width:4rem;">
              <el-row>
                <el-button type="text" @click="getMyjob()" style="margin-left: 0.5rem;">我的业务</el-button>
                <el-button type="text" @click="getMyjoinjob()" style="margin-left: 0.5rem;">我参与的业务</el-button>
              </el-row>
            </dv-border-box-8>
            <div class="bototm-box">
              <dv-border-box-10 style="height: 8rem;width: 21rem;margin-left: 0.5rem;">
                <div style="margin:0.75rem;" >
                  <el-table
                ref="filterTable"
                :data="tableData"
                :key="certinfoKey"
                :row-class-name="tableRowClassName"
                style="width: 100%">
                <el-table-column
                    prop="myJob"
                    label="业务名称"
                    width="180"
                    column-key="date"
                 >
               </el-table-column>
               <el-table-column  
               style="padding-left: 2rem;"
                prop="myJobJoinUserName"
                label="参与者"
                width="180">
              </el-table-column>
                <el-table-column style="padding-left:2rem;" label="操作">
                <template slot-scope="scope">
                 <el-button type="text" @click="start(scope.row)">启动</el-button>
                  </template>
                </el-table-column>
                <el-table-column
                    prop="myJobLink"
                    label="超链接"
                    width="180"
                    column-key="date"
                 >
                 <template slot-scope="scope">
                  <a :href="scope.row.myJobLink">{{scope.row.myJobLink}}</a>
                  </template>
                
                 </el-table-column>
              </el-table>
                  </div>
              </dv-border-box-10>


              <el-dialog
                    title="模型训练进度"
                    :visible.sync="dialogVisible"
                    width="30%"
                    :before-close="handleClose"
                    >
                   
                  <!-- 旋转按钮-->
                  <!-- <el-progress type="circle" :percentage="0"></el-progress> -->
                  <template>
                    <el-row>
                      <el-col :span="10" style="margin-left: 2.7rem ;" >
                        <el-progress
                        :color = "colorLine"
                         type="circle" 
                         :percentage="percentage">
                        </el-progress>
                      </el-col>
                    </el-row>

                  </template>

                    <span slot="footer" class="dialog-footer">
                      <el-button @click=end()>取 消</el-button>
                      <el-button type="primary" @click =end()>确 定</el-button>
                    </span>
                  </el-dialog>
                  <el-dialog
                      title="我参与的业务"
                      :visible.sync="dialogVisible1"
                      width="30%"
                      :before-close="handleClose">
                 <el-form :model="addForm"  ref="addForm" label-width="100px" class="demo-addForm">
                 <el-form-item  prop="jobJobListName" label-width="100px">
                   <p>{{addForm.jobJobListName}}</p>
                  </el-form-item>
                  </el-form>


                    </el-dialog>



  
            </div>
          </div>
        </div>
      </dv-full-screen-container>
    </div>
  </template>
  
  <script>
  export default {
    name:'Jobmanage',
    data() {
      return {
        loading: true,
        certinfoKey:true,
        dialogVisible:false,
        dialogVisible1:false,
        percentage:0,
        username:'',
        colorLine:"#409eff",
        colr:'#409eff',
        tableData:[{
          myJob:'业务1',
          myJobJoinUserName:'用户1,用户2,用户3',
          myJobLink:''
        },],
        addForm:[{
          jobJobListName:''
        },]
      };
    },
    mounted() {
      this.cancelLoading();
      this.$axios.get('/job/myJobList').then(res => {
                  if (res.data.code === 200) {
                      // console.log(res)
                      this.tableData = res.data.data
                      // console.log(res.data.message)
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
      getMyjob(){
        this.$router.push("/myjob")
      },
      getMyjoinjob(){
        this.$axios.get('/job/myJoinJobList').then(res => {
                  if (res.data.code === 200) {
                      console.log(res.data.data)

                      this.addForm = res.data.data[0]
                      this.dialogVisible1 = true
                      console.log(res.data.message)
                  }
           })

      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(() => {
            done();
          })
          .catch(() => {});
      },
      
      start(row){

        const data = {
          myJob : row.myJob
        }
           console.log(data)
                this.$axios.post('/job/jobSubmit', data)
                    .then(res => {
                      console.log(res)
                      console.log(row.tableId-1)
                      this.tableData[row.tableId-1]['myJobLink']=res.data.data
                      this.$refs['filterTable'].doLayout();
                      this.certinfoKey = !this.certinfoKey
                      console.log("ssss")
                      console.log(row['myJobLink'])
                        // if (res.data.data.code === 200) {
                        //   console.log(res.data.data)
                        //   this.tableData[row]['myJobLink'] =res.data.data
      
                        //     this.$message({
                        //         message: res.data.message,
                        //         type: 'success'
                        //     })
                            
                        // } else {
                        //     this.$message.error(res.data.message)
                        // }
                    })


      //  this.dialogVisible=true
      //  setInterval(()=>{
      //   if(this.percentage >= 93){
      //     this.percentage =100
      //      return
      //   }else{
      //   this.percentage=this.percentage + Math.round(Math.random()*10)
      //   this.colorLine = this.getRandomColor()
      //   this.color = this.getRandomColor()}
      //  },2000)

      },
      // end(){
      //   // this.dialogVisible=false
      //   // this.percentage =0
      // } ,
      // getRandomColor(){
      //   return "#" + '0123456789abcdef'.split('').map(function(v,i,a){
      //     return i > 5 ? null : a[Math.floor(Math.random()*16)]
      //   }).join('')

      // },
      cancelLoading() {
        setTimeout(() => {
          this.loading = false;
        }, 500);
      },
      tableRowClassName({row, rowIndex}) {
        row.tableId = rowIndex+1;
},
    }
  };
  </script>
  
  <style lang="scss">
  @import "../assets/scss/index.scss";
  @import "../assets/scss/index_demo.scss";
  
  </style>
  <style lang="scss" scoped>
  </style>
  