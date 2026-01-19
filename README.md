# AI-Driven Multi-Scale Composite Simulation (CompSim-Agent)

## 项目愿景 (Project Vision)
本项目旨在构建一个 AI Agent，用于连接复合材料的制造参数与细观（Meso-scale）力学性能。通过结合机器学习（RVE 代理模型）和参数化几何建模，快速预测不同制造工艺下的 Fibre Bundle 性能。

## 核心架构 (Core Architecture)

### 1. Micro-Scale (微观层)
- **输入**: 局部纤维体积含量 ($V_f$)、基体/纤维/界面属性。
- **模型**: 基于 ML 的 RVE 性能预测代理模型 (Surrogate Model)。
- **输出**: 局部均匀化的刚度 ($E_{ij}$) 与强度 ($S$).

### 2. Meso-Scale (细观层 - RUC)
- **挑战**: 制造参数（压力、张力）导致纤维束 (Fibre Bundle) 形状改变及内部 $V_f$ 分布不均。
- **解决方案**: 
    - **Structure Generator**: 将制造参数映射为几何形状和 $V_f(x,y)$ 分布图。
    - **Homogenization**: 将 RVE 模型在空间上积分，得到 RUC 的等效性能。

### 3. AI Agent (控制层)
- **Workflow**: 
    1. 接收用户输入的制造参数 / 设计目标。
    2. 驱动 Structure Generator 生成虚拟结构。
    3. 调用 RVE Surrogate 进行全场性能映射。
    4. 输出最终性能报告或优化建议。

## 目录结构 (Directory Structure)

- `src/`: 源代码
    - `micro_models/`: RVE 机器学习模型代码及权重。
    - `meso_structure/`: 纤维束几何生成算法。
    - `simulation/`: 性能集成与计算逻辑。
    - `agent/`: AI Agent 的逻辑控制与接口。
- `data/`: 数据集 (训练 RVE 模型的数据, 实验验证数据)。
- `notebooks/`: Jupyter Notebooks 用于原型验证和可视化。
- `config/`: 配置文件 (材料参数库, 默认制造参数)。

## 快速开始 (Getting Started)

*(待补充安装和运行指南)*