# llm 基础:
# token 词元,context windows上下文,temperature温度

"""
完成本阶段后，你可以：

- 用 Ollama 的本地模型完成第一次 API 调用，再与 Anthropic 做对照。
- 说出模型从 Pre-training、Post-training 到 Inference 的顺序。
- 用简单例子解释 token、context window 和 temperature。
- 从响应的 usage 字段读出输入和输出 token。
- 用输入／输出价格、延迟和数据敏感度解释模型选择。
"""

"""
1 token 词元
token是 model 读写文字时使用的计量单位.也常是llm api的计价单位.

可以把它想象成句子切开后的小积木;一个英文单词可能是一块;也可能被切成几块;中文字也不保证只是一块;


2 context window 上下文窗口
context window模型处理一次请求时可用的token空间;

比如桌面,你的prompt+历史对话先占位置,模型还要留位置写答案;
模型还可能设定一个最大的输出限制;
在决定是否需要裁剪,总结或者批量处理长文档时,会用到这个概念.

3. 温度temperature
温度控制着采样变化的幅度.

想象下:从几个候选项中选择下一个块:较低的值更倾向于选择最有可能成功的候选者,这适合用于分类+固定格式的处理;
较高的值,则更频繁的尝试不太可能的候选者,这有助于激发创意,但可能不稳定.

这一阶段将温度视为一种用于提高输出稳定的调节因素.它不会增加额外的知识,也无法保证结果的精确可复制性.
"""

"""
temperature 温度可以理解成:模型回答时有多浪.

一个这样的问题: 给python程序员一句自我介绍

假设模型最后会出现以下3个选项:
我是一名python工程师 70%
我用python构建可靠的软件 20%
人生苦短,我拿python搞事情 10%

温度不同,大概会这样:
- 温度=0,基本逮着概率最高的选
    - 我是一名python工程师
- 温度=0.3,比较稳,但允许一点变化
    - 我是一名专注后端开发的python工程师
- 温度=1.0 正常发挥,变化明显
    - 我用python把业务需求变成能跑的代码
- 温度=1.5,就放飞自我了.
    - 别人用python写代码,我用python给服务器续命


温度高 = 模型更聪明 ❌
温度高= 低概率token更容易被抽中 = 输出更多样,但也更不稳定.

低温的时候
    模型: 70%a 20%b 10%c 
        更偏向a

高温的时候
    模型: abc的差距被拉小
        bc反而更容易选中

---


实际agent的使用场景:

结构化输出 / 分类 / 调工具 / 写 SQL
        ↓
temperature 低
        ↓
稳，少整活

---
头脑风暴 / 文案 / 创意方案
        ↓
temperature 高一点
        ↓
允许整活

---

尤其记住一个：Agent 调 Tool 时，一般希望模型“别他妈自由发挥”，所以通常偏低温；创意 Agent 才更需要高温。
Temperature 只控制采样变化，不会给模型增加知识，而且低温也不保证 100% 每次一模一样。
"""


"""
模型如何从数据走到 Agent？

数据 -> pre-training -> base model -> post-training -> instruct model -> inference -> agent系统


pre-training: 预训练: 模型先从大量文字,图像或者代码中学习模式,这一步会改变模型权重.
post-training:后训练,在用示范,偏好或者反馈,教模型遵循指令并更安全的完成任务;这一步也会改变权重.
fine-tuning:微调.用较小,较专门的数据集继续改变权重模型.post-training是广义的后训练阶段.fine-tuning是其中一种常见的做法
inference: 训练完成后,模型接受一次输入,并产生一次输出.这是在使用模型;不是在重新训练它.


这里有一个很重要的概念:
    agent是一套系统,包含:prompt+rag+memory+tools+harness

agent不是训练流程中的下一个模型检查点.它是把模型.prompt.rag.memory.tools.harness连接起来的系统.
这些通常在模型外部工作,不会改变模型权重.
"""
