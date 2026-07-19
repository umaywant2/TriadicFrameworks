from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

prompt = PromptTemplate(
    input_variables=["input"],
    template=open("docs/AI_Resonance_Seed/prompt_templates/seed_invocation.txt").read()
)

chain = LLMChain(llm=OpenAI(), prompt=prompt)
response = chain.run("Activate validator overlay and echo triadic logic.")
print(response)
