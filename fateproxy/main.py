import json
import requests
from flask import Flask, request, render_template
from flask_cors import *
import os
import datetime
import random
from utils import train1
from utils import test1
import socket
from utils import face

from requests_toolbelt import MultipartEncoder

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
finally:
    s.close()
server_ip = "10.128.173.86"
server_name = 509509
default_ip = "10.128.173.86"
default_name = 506506
default_job_view = {"Edd-steel-v1-in_built-Wnet": 0,
                    "Edd-crack-v1-in_built-Wnet": 1,
                    "Edd-tile-v1-in_built-Wnet": 2,
                    "Od-safehat-v1-in_built-Gnet": 3,
                    "Od-mask-v1-in_built-Gnet": 4,
                    "Od-fire-v1-in_built-Gnet": 5,
                    }
default_job_id = 10000

app = Flask(__name__)


@app.route('/data/upload', methods=['POST'])
def data_upload():
    print(request.get_data())

    dataaddress = (json.loads(request.get_data()))['dataaddress']
    print(dataaddress)
    job_type = (json.loads(request.get_data()))['job_type']
    print(job_type)
    device_ip = (json.loads(request.get_data()))['device_ip']
    print(device_ip)
    base_url = "http://" + device_ip + ":9380/v1"
    print(dataaddress)

    type = default_job_view.get(job_type)
    if (type == None):
        redata = {
            "success": 404,
            "message": "未知的业务类型",
            "why_not_success": "未知的业务类型",
            "table_name": "None"
        }
        return json.dumps(redata)

    if type == 0:
        uri = "/data/upload"
        key = random.randint(0, 1)
        if key == 0:
            file_name = "uploadff3.csv"
        else:
            file_name = "uploadff3.csv"

        current_time = datetime.datetime.now()
        tablename = ip + dataaddress + str(current_time)
        # tablename = "table509509"
        with open(file_name, 'rb') as fp:
            data = MultipartEncoder(
                fields={'file': (os.path.basename(file_name), fp, 'application/octet-stream')}
            )
            config_data = {
                "file": file_name,
                "id_delimiter": ",",
                "head": 1,
                "partition": 4,
                "namespace": "bupt",
                "table_name": tablename,

            }

            response = requests.post(
                url=base_url + uri,
                data=data,
                params=json.dumps(config_data),
                headers={'Content-Type': data.content_type}
            )
            print(response.text)
        redata = {
            "success": 200,
            "message": "数据上传成功",
            "why_not_success": "success",
            "table_name": tablename
        }


    else:
        redata = {
            "success": 404,
            "message": "数据上传失败",
            "why_not_success": "数据不存在",
            "table_name": "fail"
        }
    print(json.dumps(redata))
    return json.dumps(redata)

@app.route('/api/jobjob',methods=['POST'])
def job():
    a=os.popen("docker exec -it fate bash -c 'python /fate/python/fate_flow/fate_flow_client.py -f submit_job -c /fate/runrunrun.json -d /fate/dslffffff.json'").read()
    b=json.loads(a)
    c=b["jobId"]
    data={
        "job_id":c
    }
    return(json.dumps(c))
@app.route('/job/submit', methods=['POST'])
def job_submit():
    global default_job_id
    redata = {}
    job_type = (json.loads(request.get_data()))['job_type']
    initiator_party_id = (json.loads(request.get_data()))['initiator_party_id']
    initiator_tablename = (json.loads(request.get_data()))['initiator_tablename']
    others_party_id = (json.loads(request.get_data()))['others_party_id']
    others_tablename = (json.loads(request.get_data()))['others_tablename']
    initiator_ip = (json.loads(request.get_data()))['initiator_ip']
    type = default_job_view.get(job_type)
    print(type)
    if (type == None):
        redata = {
            "success": 404,
            "message": "无效的任务类型",
            "job_id": "无"
        }
        return json.dumps(redata)
    base_url = "http://" + server_ip + ":9380/v1"
    configdata = {
        "dsl": {
            "components": {
                "reader_0": {
                    "module": "Reader",
                    "output": {
                        "data": ["data"]
                    }
                },
                "dataio_0": {
                    "module": "DataIO",
                    "input": {
                        "data": {
                            "data": ["reader_0.data"]
                        }
                    },
                    "output": {
                        "data": ["data"],
                        "model": ["model"]
                    }
                },
                "homo_nn_0": {
                    "module": "HomoNN",
                    "input": {
                        "data": {
                            "train_data": ["dataio_0.data"]
                        }
                    },
                    "output": {
                        "data": ["data"],
                        "model": ["model"]
                    }
                },
                "evaluation_0": {
                    "module": "Evaluation",
                    "input": {
                        "data": {
                            "data": ["homo_nn_0.data"]
                        }
                    },
                    "output": {
                        "data": ["data"]
                    }
                }
            }
        },
        "runtime_conf": {
            "dsl_version": 2,
            "initiator": {
                "role": "guest",
                "party_id": 506506
            },
            "role": {
                "arbiter": [506506],
                "host": [509509],
                "guest": [506506]

            },
            # "job_parameters": {
            #     "common": {
            #         "work_mode": 0,
            #         "backend": 0
            #     }
            # },
            "component_parameters": {
                "common": {
                    "dataio_0": {
                        "with_label": True

                    },
                    "homo_nn_0": {
                        "encode_label": True,
                        "max_iter": 50,
                        "batch_size": 128,
                        "early_stop": {
                            "early_stop": "diff",
                            "eps": 0.0001
                        },
                        "optimizer": {
                            "learning_rate": 0.0015,
                            "decay": 0.0,
                            "beta_1": 0.9,
                            "beta_2": 0.999,
                            "epsilon": 1e-07,
                            "amsgrad": False,
                            "optimizer": "Adam"
                        },
                        "loss": "categorical_crossentropy",
                        "metrics": ["accuracy", "AUC"],
                        "nn_define":
                            {"class_name": "Sequential", "config": {"name": "sequential", "layers": [
                                {"class_name": "InputLayer",
                                 "config": {"batch_input_shape": [None, 10800], "dtype": "float32", "sparse": False,
                                            "ragged": False, "name": "reshape_input"}}, {"class_name": "Reshape",
                                                                                         "config": {"name": "reshape",
                                                                                                    "trainable": True,
                                                                                                    "batch_input_shape": [
                                                                                                        None, 10800],
                                                                                                    "dtype": "float32",
                                                                                                    "target_shape": [60,
                                                                                                                     60,
                                                                                                                     3]}},
                                {"class_name": "Conv2D",
                                 "config": {"name": "conv2d", "trainable": True, "batch_input_shape": [None, 60, 60, 3],
                                            "dtype": "float32", "filters": 16, "kernel_size": [3, 3], "strides": [1, 1],
                                            "padding": "valid", "data_format": "channels_last", "dilation_rate": [1, 1],
                                            "groups": 1, "activation": "relu", "use_bias": True,
                                            "kernel_initializer": {"class_name": "GlorotUniform",
                                                                   "config": {"seed": None}},
                                            "bias_initializer": {"class_name": "Zeros", "config": {}},
                                            "kernel_regularizer": None, "bias_regularizer": None,
                                            "activity_regularizer": None, "kernel_constraint": None,
                                            "bias_constraint": None}}, {"class_name": "MaxPooling2D",
                                                                        "config": {"name": "max_pooling2d",
                                                                                   "trainable": True,
                                                                                   "dtype": "float32",
                                                                                   "pool_size": [2, 2],
                                                                                   "padding": "valid",
                                                                                   "strides": [2, 2],
                                                                                   "data_format": "channels_last"}},
                                {"class_name": "Conv2D",
                                 "config": {"name": "conv2d_1", "trainable": True, "dtype": "float32", "filters": 32,
                                            "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid",
                                            "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1,
                                            "activation": "relu", "use_bias": True,
                                            "kernel_initializer": {"class_name": "GlorotUniform",
                                                                   "config": {"seed": None}},
                                            "bias_initializer": {"class_name": "Zeros", "config": {}},
                                            "kernel_regularizer": None, "bias_regularizer": None,
                                            "activity_regularizer": None, "kernel_constraint": None,
                                            "bias_constraint": None}}, {"class_name": "MaxPooling2D",
                                                                        "config": {"name": "max_pooling2d_1",
                                                                                   "trainable": True,
                                                                                   "dtype": "float32",
                                                                                   "pool_size": [2, 2],
                                                                                   "padding": "valid",
                                                                                   "strides": [2, 2],
                                                                                   "data_format": "channels_last"}},
                                {"class_name": "GlobalAveragePooling2D",
                                 "config": {"name": "global_average_pooling2d", "trainable": True, "dtype": "float32",
                                            "data_format": "channels_last"}}, {"class_name": "Dense",
                                                                               "config": {"name": "dense",
                                                                                          "trainable": True,
                                                                                          "dtype": "float32",
                                                                                          "units": 4,
                                                                                          "activation": "softmax",
                                                                                          "use_bias": True,
                                                                                          "kernel_initializer": {
                                                                                              "class_name": "GlorotUniform",
                                                                                              "config": {"seed": None}},
                                                                                          "bias_initializer": {
                                                                                              "class_name": "Zeros",
                                                                                              "config": {}},
                                                                                          "kernel_regularizer": None,
                                                                                          "bias_regularizer": None,
                                                                                          "activity_regularizer": None,
                                                                                          "kernel_constraint": None,
                                                                                          "bias_constraint": None}}]},
                             "keras_version": "2.5.0", "backend": "tensorflow"},

                        "config_type": "keras"
                    }
                },
                "role": {
                    "host": {
                        "0": {
                            "reader_0": {
                                "table": {
                                    "name": "10.112.76.172111112022-11-25 21:40:00.975055",
                                    "namespace": "bupt"
                                }
                            },
                            "dataio_0": {
                                "with_label": True,
                                "output_format": "dense"
                            }
                        }
                    },
                    "guest": {
                        "0": {
                            "reader_0": {
                                "table": {
                                    "name": "table1",
                                    "namespace": "bupt"
                                }
                            },
                            "dataio_0": {
                                "with_label": True,
                                "output_format": "dense"
                            }
                        }

                    }

                }
            }

        }
    }
    # configdata["runtime_conf"]["initiator"]["party_id"] =server_name
    # configdata["runtime_conf"]["role"]["guest"].append(server_name)
    # configdata["runtime_conf"]["role"]["arbiter"].append(server_name)
    # configdata["runtime_conf"]["role"]["guest"].append(default_name)
    # configdata["runtime_conf"]["component_parameters"]["role"]["guest"].update(
    #     {
    #         "0": {
    #             "reader_0": {
    #                 "table": {
    #                     "name": "10.112.76.172111112022-11-25 20:17:04.925833",
    #                     "namespace": "bupt"
    #                 }
    #             },
    #             "dataio_0": {
    #                 "with_label": True,
    #                 "output_format": "dense"
    #             }
    #         }
    #     }
    #
    # )
    # configdata["runtime_conf"]["component_parameters"]["role"]["guest"].update(
    #     {
    #         "1": {
    #             "reader_0": {
    #                 "table": {
    #                     "name": "10.112.76.172111112022-11-25 20:12:32.868163",
    #                     "namespace": "bupt"
    #                 }
    #             },
    #             "dataio_0": {
    #                 "with_label": True,
    #                 "output_format": "dense"
    #             }
    #         }
    #     }
    #
    # )
    print(job_type, initiator_party_id, initiator_tablename, others_party_id, others_tablename)

    uri = "/job/submit"
    if type == 0:
        rundata = {
            "dsl": {
                "components": {
                    "reader_0": {
                        "module": "Reader",
                        "output": {
                            "data": ["data"]
                        }
                    },
                    "dataio_0": {
                        "module": "DataIO",
                        "input": {
                            "data": {
                                "data": ["reader_0.data"]
                            }
                        },
                        "output": {
                            "data": ["data"],
                            "model": ["model"]
                        }
                    },
                    "homo_nn_0": {
                        "module": "HomoNN",
                        "input": {
                            "data": {
                                "train_data": ["dataio_0.data"]
                            }
                        },
                        "output": {
                            "data": ["data"],
                            "model": ["model"]
                        }
                    },
                    "evaluation_0": {
                        "module": "Evaluation",
                        "input": {
                            "data": {
                                "data": ["homo_nn_0.data"]
                            }
                        },
                        "output": {
                            "data": ["data"]
                        }
                    }
                }
            },
            "runtime_conf": {
                "dsl_version": 2,
                "initiator": {
                    "role": "guest",
                    "party_id": initiator_party_id
                },
                "role": {
                    "arbiter": [],
                    "guest": []
                },
                "job_parameters": {
                    "common": {
                        "work_mode": 0,
                        "backend": 0
                    }
                },
                "component_parameters": {
                    "common": {
                        "dataio_0": {
                            "with_label": True

                        },
                        "homo_nn_0": {
                            "encode_label": True,
                            "max_iter": 50,
                            "batch_size": 128,
                            "early_stop": {
                                "early_stop": "diff",
                                "eps": 0.0001
                            },
                            "optimizer": {
                                "learning_rate": 0.0015,
                                "decay": 0.0,
                                "beta_1": 0.9,
                                "beta_2": 0.999,
                                "epsilon": 1e-07,
                                "amsgrad": False,
                                "optimizer": "Adam"
                            },
                            "loss": "categorical_crossentropy",
                            "metrics": ["accuracy", "AUC"],
                            "nn_define":
                                {"class_name": "Sequential", "config": {"name": "sequential", "layers": [
                                    {"class_name": "InputLayer",
                                     "config": {"batch_input_shape": [None, 10800], "dtype": "float32", "sparse": False,
                                                "ragged": False, "name": "reshape_input"}}, {"class_name": "Reshape",
                                                                                             "config": {
                                                                                                 "name": "reshape",
                                                                                                 "trainable": True,
                                                                                                 "batch_input_shape": [
                                                                                                     None, 10800],
                                                                                                 "dtype": "float32",
                                                                                                 "target_shape": [60,
                                                                                                                  60,
                                                                                                                  3]}},
                                    {"class_name": "Conv2D",
                                     "config": {"name": "conv2d", "trainable": True,
                                                "batch_input_shape": [None, 60, 60, 3],
                                                "dtype": "float32", "filters": 16, "kernel_size": [3, 3],
                                                "strides": [1, 1],
                                                "padding": "valid", "data_format": "channels_last",
                                                "dilation_rate": [1, 1],
                                                "groups": 1, "activation": "relu", "use_bias": True,
                                                "kernel_initializer": {"class_name": "GlorotUniform",
                                                                       "config": {"seed": None}},
                                                "bias_initializer": {"class_name": "Zeros", "config": {}},
                                                "kernel_regularizer": None, "bias_regularizer": None,
                                                "activity_regularizer": None, "kernel_constraint": None,
                                                "bias_constraint": None}}, {"class_name": "MaxPooling2D",
                                                                            "config": {"name": "max_pooling2d",
                                                                                       "trainable": True,
                                                                                       "dtype": "float32",
                                                                                       "pool_size": [2, 2],
                                                                                       "padding": "valid",
                                                                                       "strides": [2, 2],
                                                                                       "data_format": "channels_last"}},
                                    {"class_name": "Conv2D",
                                     "config": {"name": "conv2d_1", "trainable": True, "dtype": "float32",
                                                "filters": 32,
                                                "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid",
                                                "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1,
                                                "activation": "relu", "use_bias": True,
                                                "kernel_initializer": {"class_name": "GlorotUniform",
                                                                       "config": {"seed": None}},
                                                "bias_initializer": {"class_name": "Zeros", "config": {}},
                                                "kernel_regularizer": None, "bias_regularizer": None,
                                                "activity_regularizer": None, "kernel_constraint": None,
                                                "bias_constraint": None}}, {"class_name": "MaxPooling2D",
                                                                            "config": {"name": "max_pooling2d_1",
                                                                                       "trainable": True,
                                                                                       "dtype": "float32",
                                                                                       "pool_size": [2, 2],
                                                                                       "padding": "valid",
                                                                                       "strides": [2, 2],
                                                                                       "data_format": "channels_last"}},
                                    {"class_name": "GlobalAveragePooling2D",
                                     "config": {"name": "global_average_pooling2d", "trainable": True,
                                                "dtype": "float32",
                                                "data_format": "channels_last"}}, {"class_name": "Dense",
                                                                                   "config": {"name": "dense",
                                                                                              "trainable": True,
                                                                                              "dtype": "float32",
                                                                                              "units": 4,
                                                                                              "activation": "softmax",
                                                                                              "use_bias": True,
                                                                                              "kernel_initializer": {
                                                                                                  "class_name": "GlorotUniform",
                                                                                                  "config": {
                                                                                                      "seed": None}},
                                                                                              "bias_initializer": {
                                                                                                  "class_name": "Zeros",
                                                                                                  "config": {}},
                                                                                              "kernel_regularizer": None,
                                                                                              "bias_regularizer": None,
                                                                                              "activity_regularizer": None,
                                                                                              "kernel_constraint": None,
                                                                                              "bias_constraint": None}}]},
                                 "keras_version": "2.5.0", "backend": "tensorflow"},

                            "config_type": "keras"
                        }
                    },
                    "role": {
                        "guest": {

                        }
                    }
                }

            }
        }
        rundata["runtime_conf"]["initiator"]["party_id"] = initiator_party_id
        rundata["runtime_conf"]["role"]["guest"].append(initiator_party_id)
        rundata["runtime_conf"]["role"]["arbiter"].append(initiator_party_id)
        for k in others_party_id:
            rundata["runtime_conf"]["role"]["guest"].append(k)
        rundata["runtime_conf"]["component_parameters"]["role"]["guest"].update(
            {
                "0": {
                    "reader_0": {
                        "table": {
                            "name": initiator_tablename,
                            "namespace": "bupt"
                        }
                    },
                    "dataio_0": {
                        "with_label": True,
                        "output_format": "dense"
                    }
                }
            }

        )
        for inx, tablename in enumerate(others_tablename):
            rundata["runtime_conf"]["component_parameters"]["role"]["guest"].update(
                {str(inx + 1): {
                    "reader_0": {
                        "table": {
                            "name": tablename,
                            "namespace": "bupt"
                        }
                    },
                    "dataio_0": {
                        "with_label": True,
                        "output_format": "dense"
                    }
                }
                })

        print(configdata)
        # res = requests.post(base_url + uri, json=configdata)

        # print(res.text)
        train1()
        default_job_id = default_job_id + 1
        ret = {
            "success": 200,
            "message": "任务开始",
            "job_id": default_job_id
        }
        return json.dumps(ret)
    if type == 3:
        print("sa")

@app.route('/api/steel', methods=[ 'POST'])
def steela():
    print("init")
    img = request.files.get('files')
    print(img)
    # print(img)
    img.save("steel.jpg")
    # print("sa")
    h=test1("steel.jpg")
    # print("h")
    
    # print("adasaa")
    ww=request.form.get('jobModelName')
    print(ww)
    
    data={
        "code":200,
        "message":"sssss",
        "data":str(h)
    }
    return json.dumps(h)


@app.route('/face', methods=['POST'])
def face_detete():
    face()
    data = {
        "success": 200
    }
    return json.dumps(data)


@app.route('/fateserving', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('fateserving.html')

    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobby")
        city = request.form.get("city")
        skill_list = request.form.getlist("skill")
        more = request.form.get("more")
        print(user, pwd, gender, hobby_list, city, skill_list, more)
        # 将用户信息写入文件中实现注册、写入到excel中实现注册、写入数据库中实现注册

        # 2.给用户再返回结果
        return "注册成功"


if __name__ == '__main__':
    app.run(host=ip, port=43999, debug=True)



