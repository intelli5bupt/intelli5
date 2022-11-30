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
            <dv-border-box-8 style="margin-left: 0.5rem;width: 1.5rem;">
              <el-button type="text" @click="addVisible= true" style="margin-left: 0.5rem;">新增</el-button>
            </dv-border-box-8>
            <div class="bototm-box">
   
            <dv-border-box-10 style="height: 8rem;width: 21rem;margin-left: 0.5rem;">
            <div style="margin:0.75rem;" >
            <el-table
                ref="filterTable"
                :data="tableData"
                style="width: 100%">

            <el-table-column
                    prop="deviceName"
                    label="设备名称"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="deviceIP"
                    label="设备IP"
            >
            </el-table-column>
            <el-table-column
                    prop="devicePort"
                    label="设备代理端口"
            >
            </el-table-column>
            <el-table-column
                    prop="deviceStatus"
                    label="状态"
            >
            </el-table-column>
            <el-table-column
                    label="操作">
                <template slot-scope="scope">
                    <!-- <el-button type="text" @click="addVisible = true">新增</el-button>
                    <el-divider direction="vertical"></el-divider> -->

                    <el-button type="text" @click="handleEdit(scope.$index,scope.row)">修改</el-button>
                    <el-divider direction="vertical"></el-divider>

                    <template>
                        <el-popconfirm title="这是一段内容确定删除吗？" @confirm="handleDelete(scope.$index,scope.row)">
                            <el-button type="text" slot="reference">删除</el-button>
                        </el-popconfirm>
                    </template>

                </template>
            </el-table-column>

        </el-table>

        <!--新增对话框-->
        <el-dialog
                title="添加设备"
                :visible.sync="addVisible"
                width="600px">

            <el-form :model="addForm" :rules="addFormRules" ref="addForm" label-width="100px" class="demo-addForm">

                <el-form-item label="设备名称" prop="deviceName" label-width="100px">
                    <el-input v-model="addForm.deviceName" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="设备IP" prop="deviceIP" label-width="100px">
                    <el-input v-model="addForm.deviceIP" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="设备编号" prop="deviceNumber" label-width="100px">
                    <el-input v-model="addForm.deviceNumber" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="设备端口" prop="devicePort" label-width="100px">
                    <el-input v-model="addForm.devicePort" autocomplete="off"></el-input>
                </el-form-item>


                <el-form-item label="状态" prop="deviceStatus" label-width="100px">
                    <el-input v-model="addForm.deviceStatus" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="submitForm('addForm')">立即创建</el-button>
                    <el-button @click="resetForm('addForm')">重置</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
        <!--编辑对话框-->
        <el-dialog
                title="修改设备"
                :visible.sync="editVisible"
                width="600px">

            <el-form :model="editForm" :rules="editFormRules" ref="editForm" label-width="100px" class="demo-addForm">

                <el-form-item label="设备名称" prop="deviceName" label-width="100px">
                    <el-input v-model="editForm.deviceName" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="设备IP" prop="deviceIP" label-width="100px">
                    <el-input v-model="editForm.deviceIP" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="设备编号" prop="deviceNumber" label-width="100px">
                    <el-input v-model="editForm.deviceNumber" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="设备端口" prop="devicePort" label-width="100px">
                    <el-input v-model="editForm.devicePort" autocomplete="off"></el-input>
                </el-form-item>


                <el-form-item label="状态" prop="deviceStatus" label-width="100px">
                    <el-input v-model="editForm.deviceStatus" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="submitForm('editForm')">保存</el-button>
                </el-form-item>
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
    name: "Devicemanage",
    data() {
      return {
        addVisible:false,
                editVisible:false,
                username:'',
                tableData:[],
                addForm:{
                    deviceName: "",
                    deviceNumber: "",
                    deviceIP: "",
                    devicePort: "",
                    // deviceID: '',
                    deviceStatus: "",
                },
                addFormRules: {
                    deviceName: [
                        {required: true, message: '请输入设备名称', trigger: 'blur'}
                    ],
                    deviceIP: [
                        {required: true, message: '请输入设备IP', trigger: 'blur'}
                    ],
                    deviceNumber: [
                        {required: true, message: '请输入设备编号', trigger: 'blur'}
                    ],
                    devicePort: [
                        {required: true, message: '请输入设备代理端口', trigger: 'blur'}
                    ],
                    deviceStatus: [
                        {required: true, message: '请选择状态', trigger: 'blur'}
                    ]
                },
                editForm:{
                    deviceName: "",
                    deviceIP: "",
                    deviceNumber: "",
                    devicePort: "",
                    // deviceID: '',
                    deviceStatus: "",
                },
                editFormRules: {
                    deviceName: [
                        {required: true, message: '请输入设备名称', trigger: 'blur'}
                    ],
                    deviceIP: [
                        {required: true, message: '请输入设备IP', trigger: 'blur'}
                    ],
                    deviceNumber: [
                        {required: true, message: '请输入设备编号', trigger: 'blur'}
                    ],
                    devicePort: [
                        {required: true, message: '请输入设备代理端口', trigger: 'blur'}
                    ],

                    deviceStatus: [
                        {required: true, message: '请选择状态', trigger: 'blur'}
                    ]
                },
         }
        },
     mounted() {
          this.cancelLoading();
          this.$axios.get('/device/list').then(res => {
                if (res.data.code === 200) {
                    this.tableData = res.data.data
                    console.log(res)
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
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        if (formName === 'addForm') {
                          console.log(this.addForm)
                            this.$axios.post('/device/deviceCreate', this.addForm).then(res => {
                                console.log(res)
                                if (res.data.code === 200) {
                                    this.$message({
                                        message: res.data.message,
                                        type: 'success'
                                    })
                                    setTimeout(() => {
                                        this.resetForm(formName)
                                    }, 1000)
                                    this.addVisible = false
                                    this.getDevicelist()

                                } else {
                                    this.$message.error(res.data.message)
                                }
                            })
                        } else {
                            this.$axios.post('/device/deviceUpdate', this.editForm)
                                .then(res => {
                                    console.log(res)
                                    if (res.data.code === 200) {
                                        this.editVisible = false
                                        this.getDevicelist()
                                        this.$message({
                                            message: res.data.message,
                                            type: 'success'
                                        })
                                        setTimeout(() => {
                                        }, 1000)
                                    } else {
                                        this.$message.error(res.data.message)
                                    }
                                })
                        }
                    } else {
                        this.$message.error('error submit!!')
                        console.log('error submit!!')
                        return false
                    }
                })
            },
            handleEdit (index, row) {
                this.editVisible = true
                this.editForm = this.tableData[index]
                console.log(index, row)
            },
            handleDelete (index, row) {
                console.log(index, row)
                const data = {
                    id: row.id
                }
                console.log(data)
                this.$axios.post('/device/deviceDelete', data)
                    .then(res => {
                        if (res.data.code === 200) {
                            this.$message({
                                message: res.data.retMsg,
                                type: 'success'
                            })
                            this.getDevicelist()
                        } else {
                            this.$message.error(res.data.message)
                        }
                    })
            },
            resetForm (formName) {
                this.$refs[formName].resetFields()
            },
            getDevicelist(){
                this.$axios.get('/device/list').then(res => {
                    if (res.data.code === 200) {
                        this.tableData = res.data.data
                        console.log(res)
                    }
                })

            },
            cancelLoading() {
             setTimeout(() => {
            this.loading = false;
           }, 500);
      }
    }
  }
  
</script>
<style lang="scss">
@import "../assets/scss/index.scss";
@import "../assets/scss/index_demo.scss";
</style>
<style lang="scss" scoped>
  .table-wrapper {
    width: 100%;
}
  
.table-wrapper ::v-deep .el-table {
    /* 表格字体颜色 */
    color: white;
    /* 表格边框颜色 */
    border: 0.5px solid #fcfcfc00;
    height: 80%;
  }
  
  /* 删除表格下横线 */
  .table-wrapper ::v-deep .el-table::before {
    left: 0;
    bottom: 0;
    width: 100%;
    height: 0px;
  }
  /* 删除单元格底部横线 */
  .table-wrapper ::v-deep .el-table td {
    border-bottom: 0px solid #dfe6ec !important;
  }
  
  .table-wrapper ::v-deep .el-table--fit {
    padding: 20px;
  }
  .table-wrapper ::v-deep .el-table,
  .el-table__expanded-cell {
    background-color: transparent;
  }
  
  .table-wrapper ::v-deep .el-table tr {
    background-color: transparent !important;
  }
  
.table-wrapper ::v-deep .el-table--enable-row-transition .el-table__body td,
.el-table .cell {
    background-color: transparent;
}
  </style>
  
  <style>
    .el-table,
      .el-table__expanded-cell {
        background-color: transparent !important;
        color: #FFF;
      }
      /* 表格内背景颜色 */
      .el-table th,
      .el-table tr,
      .el-table td {
        background-color: transparent !important;
        color: #FFF;
      }
  
  
</style>