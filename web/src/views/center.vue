<template>
  <div id="center">
    <div class="up">
      <div class="bg-color-black item" v-for="item in titleItem" :key="item.title">
        <p class="ml-3 colorBlue fw-b">{{item.title}}</p>
        <div>
          <dv-digital-flop :config="item.number" style="width:1.25rem;height:.625rem;" />
        </div>
      </div>
    </div>
    <div class="down">
      <div class="ranking bg-color-black">
        <span style="color:#5cd9e8">
          <icon name="align-left"></icon>
        </span>
        <span class="fs-xl text mx-2 mb-1">年度业务盈利榜</span>
        <dv-scroll-ranking-board :config="ranking" style="height:2.75rem" />
      </div>
      <div class="percent">
        <div class="item bg-color-black">
          <span>今日任务通过率</span>
          <centerChart :id="rate[0].id" :tips="rate[0].tips" :colorObj="rate[0].colorData" />
        </div>
        <div class="item bg-color-black">
          <span>今日任务达标率</span>
          <centerChart :id="rate[1].id" :tips="rate[1].tips" :colorObj="rate[1].colorData" />
        </div>
        <div class="water">
          <dv-water-level-pond :config="water" style="height: 1.5rem" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import centerChart from "@/components/echart/center/centerChartRate";

export default {
  data() {
    return {
      titleItem: [
        {
          title: "今年累计任务建次数",
          number: {
            number: [120],
            toFixed: 1,
            content: "{nt}"
          }
        },
        {
          title: "本月累计任务次数",
          number: {
            number: [18],
            toFixed: 1,
            content: "{nt}"
          }
        },
        {
          title: "今日累计任务次数",
          number: {
            number: [2],
            toFixed: 1,
            content: "{nt}"
          }
        },
        {
          title: "今年失败任务次数",
          number: {
            number: [14],
            toFixed: 1,
            content: "{nt}"
          }
        },
        {
          title: "今年成功任务次数",
          number: {
            number: [106],
            toFixed: 1,
            content: "{nt}"
          }
        },
        {
          title: "今年达标任务个数",
          number: {
            number: [100],
            toFixed: 1,
            content: "{nt}"
          }
        }
      ],
      ranking: {
        data: [
          {
            name: "新乡一电厂智慧巡检",
            value: 55
          },
          {
            name: "新乡二电厂负荷预测",
            value: 120
          },
          {
            name: "西峡车辆装配厂故障监测",
            value: 78
          },
          {
            name: "驻马店光伏厂缺陷检测",
            value: 66
          },
          {
            name: "驻马店二电厂负荷预测",
            value: 80
          },
          {
            name: "新乡光伏厂异常行为检测",
            value: 80
          },
          {
            name: "新乡光伏厂负荷预测",
            value: 80
          },
          {
            name: "驻马店三电厂负荷预测",
            value: 80
          }
        ],
        waitTime: 4000,
        carousel: "page",
        unit: "份"
      },
      water: {
        data: [24, 45],
        shape: "roundRect",
        formatter: "{value}%",
        waveNum: 3
      },
      // 通过率和达标率的组件复用数据
      rate: [
        {
          id: "centerRate1",
          tips: 60,
          colorData: {
            textStyle: "#3fc0fb",
            series: {
              color: ["#00bcd44a", "transparent"],
              dataColor: {
                normal: "#03a9f4",
                shadowColor: "#97e2f5"
              }
            }
          }
        },
        {
          id: "centerRate2",
          tips: 40,
          colorData: {
            textStyle: "#67e0e3",
            series: {
              color: ["#faf3a378", "transparent"],
              dataColor: {
                normal: "#ff9800",
                shadowColor: "#fcebad"
              }
            }
          }
        }
      ]
    };
  },
  components: {
    centerChart
    // centerChart1,
    // centerChart2
  }
};
</script>

<style lang="scss" scoped>
#center {
  display: flex;
  flex-direction: column;
  .up {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    .item {
      border-radius: 0.0625rem;
      padding-top: 0.2rem;
      margin-top: 0.1rem;
      width: 32%;
      height: 0.875rem;
    }
  }
  .down {
    padding: 0.07rem 0.05rem;
    padding-bottom: 0;
    width: 100%;
    display: flex;
    height: 3.1875rem;
    justify-content: space-between;
    .bg-color-black {
      border-radius: 0.0625rem;
    }
    .ranking {
      padding: 0.125rem;
      width: 59%;
    }
    .percent {
      width: 40%;
      display: flex;
      flex-wrap: wrap;
      .item {
        width: 50%;
        height: 1.5rem;
        span {
          margin-top: 0.0875rem;
          display: flex;
          justify-content: center;
        }
      }
      .water {
        width: 100%;
      }
    }
  }
}
</style>