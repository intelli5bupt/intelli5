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
                <span class="title-text">工业智能协同隐私计算平台</span>
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
              <span class="text fw-b">设备管理</span>
              </router-link>
            </div>
            <div class="react-right  bg-color-blue mr-3">
              <router-link :to="{name:'Myjob'}">
              <span class="text fw-b">我的业务</span>
              </router-link>
            </div>
            <div class="react-right  bg-color-blue mr-3">
              <router-link :to="{name:'Addjob'}">
              <span class="text fw-b">业务接入</span>
              </router-link>
            </div>  
            
          </div>
          <div style="width: 40%" class="d-flex">
            <div class="react-left bg-color-blue mr-3">
              <router-link :to="{name:'Model'}">
              <span class="text fw-b">智能建模</span>
              </router-link>
            </div>
            <div class="react-left bg-color-blue mr-3">
              <router-link :to="{name:'Model_analysis'}">
              <span class="text fw-b">在线推理</span>
              </router-link>
            </div>
            <div class="react-left bg-color-blue mr-3">
              <router-link :to="{name:'Jobmanage'}">
                <span class="text fw-b">业务管理</span>
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

        <div class="body-box" >
          <!-- 第三行数据 -->
          <div class="content-box" >
            <div>
              <dv-border-box-13 style="height:8rem;width:6.5rem;padding: 0.5rem;">

                <div style="font-size:large;text-align: center;">
             
               <span class="title-text">数据上传</span>
             <dv-decoration-1
               class="title-bototm"
               :reverse="true"
               :color="['#50e3c2', '#67a1e5']"
               style="width:4.125rem;height:.1rem;margin-bottom: 0.12rem;"
             />
           </div>
    <el-upload action="#" list-type="picture-card" :auto-upload="false" :on-change="addFile">
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
<el-dialog :visible.sync="dialogVisible">
  <img width="100%" :src="dialogImageUrl" alt="">
</el-dialog> 

              </dv-border-box-13>   
            </div>

              <div class="arrows 100%"></div>

            <div style="margin-left: 2rem;">
              <dv-border-box-13 style="height:8rem;width:6.5rem;padding: 0.5rem;">

                <div style="font-size:large;text-align: center;">
             
               <span class="title-text">数据处理</span>
             <dv-decoration-1
               class="title-bototm"
               :reverse="true"
               :color="['#50e3c2', '#67a1e5']"
               style="width:4.125rem;height:.1rem;margin-bottom: 0.12rem;"
             />
  <!-- <dv-border-box-8 style="height:3rem;width:5rem;padding: 0.4rem;margin-left: 0.2rem;">
  <div style="margin:0.2rem;font-size: 0.25rem">
    <p style="margin-bottom:0.2rem;">推理节点</p>
    <p style="margin-bottom:0.2rem;">推理时长：{{time}} s</p>
  </div>
</dv-border-box-8>   -->
<dv-border-box-1 style="height:3.7rem;width:5rem;padding: 0.4rem;">
  <div style="margin-top:0.6rem;  margin-left:0.29rem; font-size: 0.25rem；">
    <!-- 提交表单 -->

   <el-select style="width: 3.5rem; height: 0.6rem; color: #0f1325;margin-left: 0.2rem;margin-bottom: 0.2rem;" v-model="jobModelName"  placeholder="请选择模型">
       <el-option
          v-for="item in options1"
          :key="item.id"
          :label="item.modelName"
          :value="item.modelName">
         </el-option>
    </el-select>

    <el-button v-on:click="reasoningStart()" type="primary" style="width: 3.5rem;color: #0f1325;margin-left: 0.2rem;margin-bottom: 0.25rem;">开始推理</el-button>
    <el-button type="primary" style="width: 3.5rem;color: #0f1325;margin-left: 0.2rem;margin-bottom: 0.1rem;">结果保存</el-button>
  </div>
</dv-border-box-1>  
           </div>
             

              </dv-border-box-13>   
            </div>

              <div class="arrows2 100%"></div>

            <div style="margin-left: 2rem;">
              <dv-border-box-13 style="height:8rem;width:6.5rem;padding: 0.5rem;">

                <div style="font-size:large;text-align: center;">
             
               <span class="title-text">推理结果</span>
             <dv-decoration-1
               class="title-bototm"
               :reverse="true"
               :color="['#50e3c2', '#67a1e5']"
               style="width:4.125rem;height:.1rem;margin-bottom: 0.12rem;"
             />
           </div>
  <!-- <dv-border-box-13 style="height:4rem;width:5rem;padding: 0.4rem;margin-left: 0.2rem;">
    <div class="block">
    <span class="demonstration">推理结果</span>
    <el-image :src="src"></el-image>
  </div>
</dv-border-box-13>  -->
<dv-border-box-10 style="height:3rem;width:5rem;padding: 0.4rem;margin-left: 0.2rem;">
  <div style="margin:0.2rem;font-size: 0.25rem">
    <p style="margin:0.2rem;" >推理结果：</p>
    <p style="margin-left: 0.1rem;word-break: break-all;word-wrap: break-word;" v-text="modelResult"></p>
  </div>
</dv-border-box-10>  
              </dv-border-box-13>    
              
            </div>
          </div>
        </div>
                  <!-- 第四行数据 -->
                  

      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>

export default {
  data() {
    return {
      loading: true,
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      files:[],
      jobModelName:'',
      username:'',
      time :0, 
      modelResult:'',
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
      options1: [{
                    id: '1',
                    modelName: 'CNN'
                }, {
                    id: '2',
                    modelName: '基于'
        },],
    };
  },
  components: {

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
    cancelLoading() {
      setTimeout(() => {
        this.loading = false;
        
      }, 500);
    },
    reasoningStart() {
      console.log("ffff")
      let formData =  new FormData();
      formData.append('files',this.files[0].raw)
      formData.append('jobModelName',this.jobModelName)  
      console.log(formData)  

      this.$axios.post('/steel', formData).then(res => {
        console.log(res)
        this.src=this.files.url
        this.modelResult=res.data
      }
    )
       
      
    },
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
        // this.files=file
        this.files.push(file)
      }
  }
};
</script>

<style lang="scss">
@import "../assets/scss/index.scss";
@import "../assets/scss/index_demo.scss";

.router-link-active {
  text-decoration: none;
  color: #fff;
}

a {
  text-decoration: none;
  color: #fff;
}
$size: 50px;
$speed: 3s;
$peakopacity:0.6;

body {
 
  .arrows {
    position: relative;
    /**/
    position: absolute;
    top:50%;
    left:30.5%;
    /**/
    width:$size;
    height:$size;
    transform:translate(-50%,-50%);
    &:before {
      content: '';
      position: absolute;
      width:100%;
      height:100%;
      border-left:$size/3 solid rgba(242,244,246,$peakopacity);
      border-bottom:$size/3 solid rgba(242,244,246,$peakopacity);
      transform:translate($size/3,$size*4/3)rotate(-135deg);
      animation: arrows $speed linear infinite;
    }
    &:after {
      content: '';
      position: absolute;
      width:100%;
      height:100%;
      border-left:$size/3 solid rgba(242,244,246,$peakopacity);
      border-bottom:$size/3 solid rgba(242,244,246,$peakopacity);
      transform:translate($size*2/3,0px)rotate(-135deg) ;
      animation: arrows $speed linear infinite $speed/-2;
    }
  }
}
.arrows2 {
    position: relative;
    /**/
    position: absolute;
    top:50%;
    left:67%;
    /**/
    width:$size;
    height:$size;
    transform:translate(-50%,-50%);
    &:before {
      content: '';
      position: absolute;
      width:100%;
      height:100%;
      border-left:$size/3 solid rgba(242,244,246,$peakopacity);
      border-bottom:$size/3 solid rgba(242,244,246,$peakopacity);
      transform:translate($size/3,$size*4/3)rotate(-135deg);
      animation: arrows $speed linear infinite;
    }
    &:after {
      content: '';
      position: absolute;
      width:100%;
      height:100%;
      border-left:$size/3 solid rgba(242,244,246,$peakopacity);
      border-bottom:$size/3 solid rgba(242,244,246,$peakopacity);
      transform:translate($size*2/3,0px)rotate(-135deg) ;
      animation: arrows $speed linear infinite $speed/-2;
    }
  }

@keyframes arrows {
  0% {
      border-left:$size/3 solid rgba(242,244,246,1);
      border-bottom:$size/3 solid rgba(242,244,246,1);
      transform:translate($size*5/-6,$size*4/-6)rotate(-135deg) ;
  }
  10%, 90% {
      border-left:$size/3 solid rgba(242,244,246,1);
      border-bottom:$size/3 solid rgba(242,244,246,1);
  }
  50% {
      border-left:$size/3 solid rgba(242,244,246,$peakopacity);
      border-bottom:$size/3 solid rgba(242,244,246,$peakopacity);
      transform:translate(0px,$size*4/-6)rotate(-135deg) ;
  }
  100% {
      border-left:$size/3 solid rgba(242,244,246,1);
      border-bottom:$size/3 solid rgba(242,244,246,1);
      transform:translate($size*5/6,$size*4/-6)rotate(-135deg) ;
  }
}
@keyframes arrows2 {
  0% {
      border-left:$size/3 solid rgba(242,244,246,1);
      border-bottom:$size/3 solid rgba(242,244,246,1);
      transform:translate($size*5/-6,$size*4/-6)rotate(-135deg) ;
  }
  10%, 90% {
      border-left:$size/3 solid rgba(242,244,246,1);
      border-bottom:$size/3 solid rgba(242,244,246,1);
  }
  50% {
      border-left:$size/3 solid rgba(242,244,246,$peakopacity);
      border-bottom:$size/3 solid rgba(242,244,246,$peakopacity);
      transform:translate(0px,$size*4/-6)rotate(-135deg) ;
  }
  100% {
      border-left:$size/3 solid rgba(242,244,246,1);
      border-bottom:$size/3 solid rgba(242,244,246,1);
      transform:translate($size*5/6,$size*4/-6)rotate(-135deg) ;
  }
}

</style>