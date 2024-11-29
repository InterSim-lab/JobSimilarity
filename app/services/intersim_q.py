import torch 
from unsloth import FastLanguageModel

class InterSimQ:
    def __init__(self, model_name="app/tuning/intersim-model-v1.1.0"):
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(model_name, 
                                                       device_map="auto", 
                                                       load_in_4bit=True,

                                                      )
        FastLanguageModel.for_inference(self.model)

    def generator(self, prompt: str):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        ouputs = self.model.generate(**inputs, 
                                     max_length=2048, 
                                     num_return_sequences=1, 
                                     do_sample=True, 
                                     temperature=0.7,
                                     top_p=0.9,
                                     top_k=50,
                                     repetition_penalty=1.1
                                    )
        response = self.tokenizer.decode(ouputs[0], skip_special_tokens=True)
        return response.split("### Answer:")[-1]
    