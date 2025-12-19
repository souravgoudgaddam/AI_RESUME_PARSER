from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from App.models.resume_schema import Resume
import os
llm=ChatMistralAI(api_key=os.getenv('MISTRAL_API_KEY'))

parser=PydanticOutputParser(pydantic_object=Resume)

prompt=PromptTemplate(
    template=""" You are an expert resume parser.
Extract structured information from the resume text.
Skills must be short normalized terms.
Do not hallucinate.
follw the format instructions

{format_instructions}

Resume text:
{resume_text}

""",
input_variables=['resume_text'],
partial_variables={
    'format_instructions':parser.get_format_instructions()
},
)

def parse_resume(resume_text:str) -> Resume:
    chains=prompt | llm | parser
    return chains.invoke({
        "resume_text":resume_text
    })
