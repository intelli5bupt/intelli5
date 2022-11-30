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
          <dv-border-box-8 style="margin-left: 0.5rem;width: 1.5rem;">
              <el-button type="text" @click="addVisible= true" style="margin-left: 0.5rem;">新增</el-button>
            </dv-border-box-8>
          <div class="bototm-box">

            <dv-border-box-10 style="height: 8rem;width: 21rem;margin-left: 0.5rem;">
      
              <div  style="margin:0.5rem;">
                  <el-table
                          ref="filterTable"
                          :data="tableData"
                          style="width: 100%;">
                      <el-table-column
                              prop="deviceIP"
                              label="设备IP"
                              width="180"
                              column-key="date"
                      >
                      </el-table-column>
                      <el-table-column
                              prop="devicePort"
                              label="设备端口"
                              width="180">
                      </el-table-column>
                      <el-table-column
                              prop="datasetName"
                              label="数据名称">
                      </el-table-column>
                      <el-table-column
                              prop="datasetAddress"
                              label="数据地址">
                      </el-table-column>
                      <el-table-column
                              prop="supportJob"
                              label="支持业务">
                      </el-table-column>
                      <el-table-column label="操作">
                          <template slot-scope="scope">
                              <el-button type="text" @click="addVisible= true">新增</el-button>
                              <el-divider direction="vertical"></el-divider>
                              <el-button type="text" @click="handleEdit(scope.$index, scope.row)">修改</el-button>
                              <el-divider direction="vertical"></el-divider>
                              <template>
                                  <el-popconfirm title="这是一段内容确定删除吗？" @confirm="handleDelete(scope.$index, scope.row)">
                                      <el-button type="text" slot="reference">删除</el-button>
                                  </el-popconfirm>
                              </template>
                              <el-divider direction="vertical"></el-divider>
                              <a :href="dataLink" style="color:#409EFF" >详情</a>
                          </template>
                      </el-table-column>
                      <el-button type="text" @click="addVisible= true">新增</el-button>

                  </el-table>
                  

                  <el-dialog
                          title="添加数据"
                          :visible.sync="addVisible"
                          width="600px"
                  >
                      <el-form :model="addForm" :rules="addFormRules" ref="addForm" label-width="100px" class="demo-addForm">
                          <el-form-item label="设备IP" prop="deviceIP" label-width="100px">
                              <el-input v-model="addForm.deviceIP" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item label="设备端口" prop="devicePort" label-width="100px">
                              <el-input v-model="addForm.devicePort" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item label="数据名称" prop="datasetName" label-width="100px">
                              <el-input v-model="addForm.datasetName" autocomplete="off"></el-input>
                          </el-form-item>
                          <el-form-item label="数据地址" prop="datasetAddress" label-width="100px">
                              <el-input v-model="addForm.datasetAddress" autocomplete="off"></el-input>
                          </el-form-item>
                          <el-form-item label="支持业务" prop="supportJob" label-width="100px">
                              <!-- <el-input v-model="addForm.supportJob" autocomplete="off"></el-input> -->
                              <el-select v-model="addForm.supportJob" placeholder="请选择">
                                <el-option
                                        v-for="item in options1"
                                        :key="item.id"
                                        :label="item.supportJob"
                                        :value="item.supportJob">
                                </el-option>
                            </el-select>
                          </el-form-item>

                          <el-form-item>
                              <el-button type="primary" @click="submitForm('addForm')">立即创建</el-button>
                              <el-button @click="resetForm('addForm')">重置</el-button>
                          </el-form-item>
                      </el-form>
                  </el-dialog>

                  <el-dialog
                          title="编辑数据"
                          :visible.sync="editVisible"
                          width="600px"
                  >
                      <el-form :model="editForm" :rules="editFormRules" ref="editForm" label-width="100px" class="demo-addForm">
                          <el-form-item label="设备IP" prop="deviceIP" label-width="100px">
                              <el-input v-model="editForm.deviceIP" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item label="设备端口" prop="devicePort" label-width="100px">
                              <el-input v-model="editForm.devicePort" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item label="数据名称" prop="datasetName" label-width="100px">
                              <el-input v-model="editForm.datasetName" autocomplete="off"></el-input>
                          </el-form-item>
                          <el-form-item label="数据地址" prop="datasetAddress" label-width="100px">
                              <el-input v-model="editForm.datasetAddress" autocomplete="off"></el-input>
                          </el-form-item>
                          <el-form-item label="支持业务" prop="supportJob" label-width="100px">
                              <!-- <el-input v-model="editForm.supportJob" autocomplete="off"></el-input> -->
                              <el-select v-model="addForm.supportJob" placeholder="请选择">
                                <el-option
                                        v-for="item in options1"
                                        :key="item.id"
                                        :label="item.supportJob"
                                        :value="item.supportJob">
                                </el-option>
                            </el-select>
                          </el-form-item>

                          <el-form-item>
                              <el-button type="primary" @click="submitForm('editForm')">保存</el-button>
                          </el-form-item>
                      </el-form>
                  </el-dialog>

              </div>

            </dv-border-box-10>

          </div>
          <!-- <template>
              <div>
                  <el-table
                          ref="filterTable"
                          :data="tableData"
                          style="width: 100%">
                      <el-table-column
                              prop="deviceIP"
                              label="设备IP"
                              width="180"
                              column-key="date"
                      >
                      </el-table-column>
                      <el-table-column
                              prop="devicePort"
                              label="设备端口"
                              width="180">
                      </el-table-column>
                      <el-table-column
                              prop="datasetName"
                              label="数据名称">
                      </el-table-column>
                      <el-table-column
                              prop="datasetAddress"
                              label="数据地址">
                      </el-table-column>
                      <el-table-column
                              prop="supportJob"
                              label="支持业务">
                      </el-table-column>
                      <el-table-column label="操作">
                          <template slot-scope="scope">
                              <el-button type="text" @click="addVisible= true">新增</el-button>
                              <el-divider direction="vertical"></el-divider>
                              <el-button type="text" @click="handleEdit(scope.$index, scope.row)">修改</el-button>
                              <el-divider direction="vertical"></el-divider>
                              <template>
                                  <el-popconfirm title="这是一段内容确定删除吗？" @confirm="handleDelete(scope.$index, scope.row)">
                                      <el-button type="text" slot="reference">删除</el-button>
                                  </el-popconfirm>
                              </template>
                          </template>
                      </el-table-column>
                  </el-table>

                  <el-dialog
                          title="添加数据"
                          :visible.sync="addVisible"
                          width="600px"
                  >
                      <el-form :model="addForm" :rules="addFormRules" ref="addForm" label-width="100px" class="demo-addForm">
                          <el-form-item label="设备IP" prop="deviceIP" label-width="100px">
                              <el-input v-model="addForm.deviceIP" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item label="设备端口" prop="devicePort" label-width="100px">
                              <el-input v-model="addForm.devicePort" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item label="数据名称" prop="datasetName" label-width="100px">
                              <el-input v-model="addForm.datasetName" autocomplete="off"></el-input>
                          </el-form-item>
                          <el-form-item label="数据地址" prop="datasetAddress" label-width="100px">
                              <el-input v-model="addForm.datasetAddress" autocomplete="off"></el-input>
                          </el-form-item>
                          <el-form-item label="支持业务" prop="supportJob" label-width="100px">
                              <el-input v-model="addForm.supportJob" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item>
                              <el-button type="primary" @click="submitForm('addForm')">立即创建</el-button>
                              <el-button @click="resetForm('addForm')">重置</el-button>
                          </el-form-item>
                      </el-form>
                  </el-dialog>

                  <el-dialog
                          title="编辑数据"
                          :visible.sync="editVisible"
                          width="600px"
                  >
                      <el-form :model="editForm" :rules="editFormRules" ref="editForm" label-width="100px" class="demo-addForm">
                          <el-form-item label="设备IP" prop="deviceIP" label-width="100px">
                              <el-input v-model="editForm.deviceIP" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item label="设备端口" prop="devicePort" label-width="100px">
                              <el-input v-model="editForm.devicePort" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item label="数据名称" prop="datasetName" label-width="100px">
                              <el-input v-model="editForm.datasetName" autocomplete="off"></el-input>
                          </el-form-item>
                          <el-form-item label="数据地址" prop="datasetAddress" label-width="100px">
                              <el-input v-model="editForm.datasetAddress" autocomplete="off"></el-input>
                          </el-form-item>
                          <el-form-item label="支持业务" prop="supportJob" label-width="100px">
                              <el-input v-model="editForm.supportJob" autocomplete="off"></el-input>
                          </el-form-item>

                          <el-form-item>
                              <el-button type="primary" @click="submitForm('editForm')">保存</el-button>
                          </el-form-item>
                      </el-form>
                  </el-dialog>

              </div>
              </template> -->

          
          </div>

      
      </div>
    </dv-full-screen-container>
  </div>
</template>
<script>
import { cornflowerblue } from 'color-name';


export default {
  data() {
    return {
      loading: true,
      name: 'Datamanage',
      addVisible: false,
      editVisible: false,
      username:'',
      dataLink:"",
      tableData: [],
      addForm: {
                id:0,
                deviceIP: '',
                devicePort: '',
                datasetName: '',
                datasetAddress: '',
                supportJob: ''
      },
      options1: [{
                    id: '1',
                    supportJob: 'CNN'
                },],
      addFormRules: {
        deviceIP: [
                  {required: true, message: '请输入设备IP', trigger: 'blur'}
                  ],
        devicePort: [
          {required: true, message: '请输入设备代理端口', trigger: 'blur'}
                    ],
        datasetName: [
          {required: true, message: '请输入数据名称', trigger: 'blur'}
                    ],
        datasetAddress: [
          {required: true, message: '请输入数据地址', trigger: 'blur'}
          ],
        supportJob: [
          {required: true, message: '请输入支持业务', trigger: 'blur'}
            ]
          },
        editForm: {
          deviceIP: '',
          devicePort: '',
          datasetName: '',
          datasetAddress: '',
          supportJob: ''
          },
        editFormRules: {
          deviceIP: [
          {required: true, message: '请输入设备IP', trigger: 'blur'}
          ],
          devicePort: [
            {required: true, message: '请输入设备代理端口', trigger: 'blur'}
           ],
          datasetName: [
           {required: true, message: '请输入数据名称', trigger: 'blur'}],
          datasetAddress: [
          {required: true, message: '请输入数据地址', trigger: 'blur'}],
          supportJob: [
          {required: true, message: '请输入支持业务', trigger: 'blur'}
          ]
        }
       }
      },
      mounted() {
        this.cancelLoading();
        this.$axios.get('/data/list').then(res => {
                console.log(res)
                if (res.data.code === 200) {
                    this.tableData = res.data.data
                    console.log(res)
                    //console.log(res.message)
                }
            })
            this.$axios.get('/data/supportJob').then(res => {
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
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        if (formName === 'addForm') {
                            this.$axios.post('/data/data_register', this.addForm).then(res => {
                              console.log(addForm)
                              this.dataLink = res.data.dataLink
                                if (res.data.code === 200) {

                                    this.$message({
                                        message: res.data.message,
                                        type: 'success'
                                    })
                                    setTimeout(() => {
                                        this.resetForm(formName)
                                    }, 1000)
                                    this.addVisible = false
                                    this.getDatalist()
                                } else {
                                    // alert(res.message)
                                    console.log(res)
                                    this.$message.error(res.data.message)
                                }
                            })

                        } else {
                            this.$axios.post('/data/dataUpdate', this.editForm)
                                .then(res => {
                                    console.log(res)
                                    if (res.data.code === 200) {

                                        this.editVisible = false
                                        this.getDatalist()
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
                this.$axios.post('/data/dataDelete', data)
                    .then(res => {
                        if (res.data.code === 200) {
                            this.$message({
                                message: res.data.message,
                                type: 'success'
                            })
                            this.getDatalist()
                        } else {
                            this.$message.error(res.data.message)
                        }
                    })
            },
            resetForm (formName) {
                this.$refs[formName].resetFields()
            },
            getDatalist(){
                this.$axios.get('/data/list').then(res => {
                    console.log(res)
                    if (res.data.code === 200) {
                        this.tableData = res.data.data
                        console.log(res)
                        //console.log(res.message)
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
<!-- <style lang="scss" scoped>
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

</style> -->