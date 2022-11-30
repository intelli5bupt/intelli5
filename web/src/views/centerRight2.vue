<template>
  <div id="centreRight2" style="height:4rem!important;">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span style="color:#5cd9e8">
          <icon name="align-left"></icon>
        </span>
        <span class="fs-xl text mx-2">节点参与度分析</span>
      </div>
      <div class="d-flex jc-center body-box" style=" margin-top: 1.4rem;">
        <dv-capsule-chart :config="config" style="width: 100%;height:2rem" />
        <!-- ---------------------------------------- -->
    
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      config: {
        data: [
          {
            name: "node1",
            value: 167
          },
          {
            name: "node3",
            value: 142
          },
          {
            name: "node4",
            value: 123
          },
          {
            name: "node11",
            value: 98
          },
          {
            name: "node23",
            value: 95
          }
        ]
      }
    };
  },
  mounted() {},
  methods: {}
};
</script>

<style lang="scss">
#centreRight2 {
  padding: 0.0625rem;
  height: 5rem;
  min-width: 3.75rem;
  border-radius: 0.0625rem;
  .bg-color-black {
    padding: 0.0625rem;
    height: 5.0625rem;
    border-radius: 0.125rem;
  }
  .text {
    color: #c3cbde;
  }
  .body-box {
    border-radius: 0.125rem;
    overflow: hidden;
  }
}
</style>