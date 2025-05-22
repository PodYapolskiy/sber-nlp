# %%
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.prompts.loading import load_prompt
import yaml
# from pathlib import Path

model = GigaChat(credentials="")

prompt = load_prompt("template.yaml")
print(prompt)


# %%
def ask_llm_for_ner(text, categories):
    prompt = "Извлеки все сущности из следующего текста. Укажи тип ({}).".format(
        ", ".join(categories)
    )
    system_message = SystemMessage(prompt=prompt, text=text)
    chain = prompt | model
    return chain.generate_text()  # load_prompt


# %% [markdown]
#
