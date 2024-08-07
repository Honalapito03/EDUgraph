#from transformers import AutoModelForCausalLM, AutoTokenizer
#import torch
import abc
import ai71


from IPython.display import display
from IPython.display import Markdown

class AI_API(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractclassmethod
    def messenge(self, promt:tuple[str, str], **kwargs) -> tuple[str, list[dict[str, str]]]:
        """kwargs: 
                history
                name
                parameters (temp, stb),
                """
        pass

    def create_input(self, promt:tuple[str, str], history:list[dict[str, str]]) -> list[dict[str, str]]:
        history.append({"role": "system", "content": promt[0]})
        history.append({"role": "user", "content": promt[1]}) #később alakítsd
        return(history)


    def create_output(self, output:str, history:list[dict[str, str]]) -> tuple[str, list[dict[str, str]]]:
        history.append({"role": "assistant", "content": output}) #később alakítsd
        return(output, history)



    

class AI71_api(AI_API):
    def __init__(self) -> None:
        self.client = ai71.AI71("ai71-api-6d918339-00a5-4fe6-8422-027b0e6f6089")

    async def messenge(self, promt:str, **kwargs):
        print("fut")
        mes = self.create_input(promt, kwargs["history"] if "history" in kwargs.keys() else [])
        res = self.client.chat.completions.create(
            model="tiiuae/falcon-180b-chat",
            messages=mes,
            top_k=5000,
            temperature=0.1
        )
        resstr = res.choices[0].message.content
        return(self.create_output(res.choices[0].message.content, mes))
    




