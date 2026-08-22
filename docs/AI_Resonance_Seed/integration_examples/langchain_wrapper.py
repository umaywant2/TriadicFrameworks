from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Load the TriadicFrameworks seed invocation prompt
seed_prompt_text = open(
    "docs/AI_Resonance_Seed/prompt_templates/seed_invocation.txt"
).read()

prompt = PromptTemplate(
    input_variables=["input"],
    template=seed_prompt_text
)

# Standard LC chain using OpenAI backend
chain = LLMChain(
    llm=OpenAI(),
    prompt=prompt
)

# Example invocation
response = chain.run(
    "Activate validator overlay and echo triadic logic."
)

print(response)
