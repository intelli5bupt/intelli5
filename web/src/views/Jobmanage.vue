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
          <div class="bototm-box">
            <dv-border-box-10 style="height: 8rem;width: 21rem;margin-left: 0.5rem;">
              <div style="margin:0.75rem;" >
                <el-button type="primary" style="width:1.5rem" @click="addjob()">新增</el-button>
                <el-table
              ref="filterTable"
              :data="tableData"
              style="width: 100%">
              <el-table-column
                  prop="jobName"
                  label="业务名称"
                  width="180"
                  column-key="date"
               >
             </el-table-column>
             <el-table-column
                prop="jobModelName"
                label="模型名称"
                width="180">
              </el-table-column>
              <el-table-column
                 prop="jobSName"
                 label="业务池"
                 width="180">
              </el-table-column>
              <el-table-column
                  prop="jobUsername"
                  label="业务发起者">
              </el-table-column>
              <el-table-column label="操作">
                <template slot-scope="scope">
                <el-button type="text" @click="handledetails(scope.$index, scope.row)" >详情</el-button>
                 </template>
                </el-table-column>
              </el-table>
              <el-dialog
                title="详情"
                :visible.sync="addVisible"
                width="600px"
                >
                <el-form :model="addForm"  ref="addForm" label-width="100px" class="demo-addForm">
                 <el-form-item label="业务名称" prop="jobName" label-width="100px">
                   <el-tag>{{addForm.jobName}}</el-tag>
                  </el-form-item>
                  <el-form-item label="业务描述" prop="jobDescription" label-width="100px">
                     <el-tag >{{addForm.jobDescription}}</el-tag>
                   </el-form-item>
                  <el-form-item label="业务类型" prop="jobType" label-width="100px">
                    <el-tag >{{addForm.jobType}}</el-tag>
                    </el-form-item>
                   <el-form-item label="业务类型描述" prop="jobTypeDescription" label-width="100px">
                      <el-tag >{{addForm.jobTypeDescription}}</el-tag>
                    </el-form-item>
                    <el-form-item label="业务模型名称" prop="jobModelName" label-width="100px">
                        <el-tag>{{addForm.jobModelName}}</el-tag>
                     </el-form-item>
                     <el-form-item label="预算" prop="budget" label-width="100px">
                        <el-tag  >{{addForm.budget}}</el-tag>
                      </el-form-item>
                      <el-form-item label="业务池" prop="jobSName" label-width="100px">
                          <el-tag >{{addForm.jobSName}}</el-tag>
                      </el-form-item>
                      <el-form-item label="聚合策略" prop="modelDeployStrategy" label-width="100px">
                      <el-tag >{{addForm.modelDeployStrategy}}</el-tag>
                       </el-form-item>
                        <el-form-item label="业务安全策略" prop="jobSafetyStrategy" label-width="100px">
                          <el-tag >{{addForm.jobSafetyStrategy}}</el-tag>
                        </el-form-item>
                        <!-- <el-form-item label="业务数据集描述" prop="jobDatasetDescription" label-width="100px">
                           <el-tag >{{addForm.jobDatasetDescription}}</el-tag>
                         </el-form-item> -->
                        </el-form>
                </el-dialog>
        
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
  name:'Jobmanage',
  data() {
    return {
      loading: true,
      tableData:[],
      addVisible:false,
      username:'',
      addForm:{
        id:0,
        jobName:'',
        jobDescription:'',
        jobType:'',
        jobTypeDescription:'',
        jobModelName:'',
        budget:'',
        jobSName:'',
        modelDeployStrategy:'',
        jobSafetyStrategy:'',
        jobDatasetDescription:'',
      },
    };
  },
  mounted() {
    this.cancelLoading();
    this.$axios.get('/job/list').then(res => {
                if (res.data.code === 200) {
                    console.log(res)
                    this.tableData = res.data.data
                    console.log(res.data.message)
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
    handledetails(index,row){
      console.log(index,row)
      const data = {
        id:row.id
      }
      console.log(data)
      this.$axios.post('/job/detailList', data)
                    .then(res => {
                      console.log()
                        if (res.data.code === 200) {
                            this.$message({
                                message: res.data.message,
                                type: 'success'
                            })
                            this.addVisible = true
                            this.addForm = res.data.data[0]
                        } else {
                            this.$message.error(res.data.message)
                        }
                    })

    },
    addjob(){
      this.$router.push("/addjob")
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

// .table-wrapper {
//   width: 100%;
// }

// .table-wrapper ::v-deep .el-table {
//   /* 表格字体颜色 */
//   color: white;
//   /* 表格边框颜色 */
//   border: 0.5px solid #fcfcfc00;
//   height: 80%;
// }

// /* 删除表格下横线 */
// .table-wrapper ::v-deep .el-table::before {
//   left: 0;
//   bottom: 0;
//   width: 100%;
//   height: 0px;
// }
// /* 删除单元格底部横线 */
// .table-wrapper ::v-deep .el-table td {
//   border-bottom: 0px solid #dfe6ec !important;
// }

// .table-wrapper ::v-deep .el-table--fit {
//   padding: 20px;
// }
// .table-wrapper ::v-deep .el-table,
// .el-table__expanded-cell {
//   background-color: transparent;
// }

// .table-wrapper ::v-deep .el-table tr {
//   background-color: transparent !important;
// }

// .table-wrapper ::v-deep .el-table--enable-row-transition .el-table__body td,
// .el-table .cell {
//   background-color: transparent;
// }
</style>

<style>
	/* .el-table,
		.el-table__expanded-cell {
			background-color: transparent !important;
      color: #FFF;
		}
		/* 表格内背景颜色 */
		/* .el-table th,
		.el-table tr,
		.el-table td {
			background-color: transparent !important;
      color: #FFF;
		/* } */ 

</style>