import pdb
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import (HumanMessage, SystemMessage)
import numpy as np

script_path = r'C:\Users\hly\PyCharmMiscProject\知乎\营销原理\001.2022，如何用营销应对危机？.txt'
model = 'Qwen/Qwen3-32B'
block_lst = []
range_length = 1000

chat = ChatOpenAI(
    api_key='XXX',  # get keys from siliconflow.com
    base_url="https://api.siliconflow.cn/v1",
    model=model
)

with open(script_path, 'r', encoding='utf-8') as file:

    script = file.read()

    for ii in np.arange(0, len(script), range_length):
        block_lst.append(script[ii:ii+range_length])


for sentence in block_lst:

    response = chat(
        [
            SystemMessage(
                content='你现在是一名语文老师，请对输入的文字添加标点符号。'
            ),
            HumanMessage(
                content=sentence
            )
        ]
    )
    print(response.content)
    print('==' * 80)




