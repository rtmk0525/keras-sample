# keras-sample

## サンプルコードのクローン
terminalで
```shell
cd YOUR_DIRECTORY
git clone https://github.com/rtmk0525/keras-sample.git
```
- YOUR_DIRECTORYの例: /share/USERNAME

## 仮想環境構築
上と同じterminal上で
```shell
. /home/user?/set-anaconda.sh
conda create -n ENV_NAME python=3.10
. activate ENV_NAME
pip install "tensorflow==2.11" keras numpy
```
- user?の?は1桁の数字
- ENV_NAMEは自由
- pythonのバージョンは3.11未満にする必要あり（tensorflow2.11非対応のため([参考](https://www.tensorflow.org/install/source?hl=ja#gpu))）
- tensorflowのバージョンは2.11を指定([参考](https://github.com/tensorflow/text/issues/554#:~:text=%40JainRohan%2C%20downgrading%20tensorflow%20to%202.11.1%20solved%20the%20issue%20in%20my%20case.%0Apip%20install%20tensorflow%3D%3D2.11.1%0AInstalling%20another%20cudnn%20version%20should%20be%20another%20solution%2C%20yet%20a%20more%20complex%20one%2C%20as%20you%20will%20still%20need%20to%20rebuild%20tensorflow.))
  - 先程試したところ`pip install tensorflow keras numpy`(tensorflow==2.12)でも動作を確認。ただしpython=3.10は必要

## 実行
```shell
jupyter notebook
```