import os
import json

notebooks_data = [
    {
        "filename": "01_what_is_ai_vs_ml_vs_genai_vs_agentic_ai.ipynb",
        "title": "Section 1: What is AI vs ML vs GenAI vs Agentic AI (2 hours)",
        "links": [
            ("AI vs. machine learning vs. deep learning vs. neural networks", "https://www.ibm.com/topics/ai-vs-machine-learning-vs-deep-learning-vs-neural-networks"),
            ("AI agent orchestration patterns", "https://anthropic.com/research/building-effective-agents")
        ],
        "summary": """### Key Learnings
* **Artificial Intelligence (AI):** Broad field of computer science focused on building smart machines.
* **Machine Learning (ML):** Subset of AI where models learn patterns from data without explicit programming.
* **Deep Learning (DL):** ML subset using multi-layered neural networks for complex pattern recognition.
* **Generative AI (GenAI):** Models capable of generating text, images, or audio based on input prompts.
* **Agentic AI:** Autonomous systems capable of planning, using tools, and executing multi-step workflows to achieve goals.""",
        "code": """# Python Conceptual Comparison: Rule-Based AI vs ML vs GenAI Mock

def rule_based_classifier(text):
    return 'Spam' if 'buy now' in text.lower() else 'Ham'

def ml_classifier_mock(features):
    return 'Spam' if features['spam_score'] > 0.8 else 'Ham'

def agentic_loop_mock(task):
    print(f"Agent planning steps for: '{task}'")
    steps = ["Search DB", "Analyze Data", "Generate Report"]
    for step in steps:
        print(f"Executing action: {step}")
    return "Task completed successfully."

print(rule_based_classifier("Buy now for free!"))
print(agentic_loop_mock("Synthesize Q3 Sales Report"))"""
    },
    {
        "filename": "02_llm_fundamentals_and_providers.ipynb",
        "title": "Section 2: LLM fundamentals, major LLMs & providers (6 hours)",
        "links": [
            ("How do Transformers work?", "https://jalammar.github.io/illustrated-transformer/"),
            ("Transformer Architectures", "https://huggingface.co/docs/transformers/index"),
            ("OpenAI Platform", "https://platform.openai.com/docs/"),
            ("Start building with Claude", "https://docs.anthropic.com/"),
            ("Google Gemini Docs", "https://ai.google.dev/docs"),
            ("Meta Llama", "https://www.llama.com/"),
            ("Hugging Face", "https://huggingface.co/"),
            ("Attention-based Models", "https://arxiv.org/abs/1706.03762")
        ],
        "summary": """### Key Learnings
* **Transformer Architecture:** Based on self-attention mechanisms that weigh token importance regardless of position.
* **Encoder-Decoder vs Decoder-Only:** Decoder-only architectures (e.g., GPT, Claude, Llama) dominate generative tasks.
* **Provider Ecosystem:** Proprietary leaders (OpenAI, Anthropic, Google) vs Open-Weights leaders (Meta Llama, Mistral) hosted on Hugging Face.""",
        "code": """# Example: Comparing API Call Schemas across major providers (Mock client concept)
class LLMProviderClient:
    def __init__(self, provider):
        self.provider = provider
        
    def generate(self, prompt):
        if self.provider == "openai":
            return f"[OpenAI GPT-4o Response to]: {prompt}"
        elif self.provider == "claude":
            return f"[Anthropic Claude 3.5 Response to]: {prompt}"
        elif self.provider == "gemini":
            return f"[Google Gemini 1.5 Response to]: {prompt}"
        else:
            return f"[HuggingFace Local Llama Response to]: {prompt}"

client = LLMProviderClient("claude")
print(client.generate("Explain self-attention in 1 sentence."))"""
    },
    {
        "filename": "03_tokens_embeddings_prompts_context_windows.ipynb",
        "title": "Section 3: Tokens, embeddings, prompts, context windows (4 hours)",
        "links": [
            ("Tokenizer", "https://platform.openai.com/tokenizer"),
            ("Vector Embeddings", "https://www.pinecone.io/learn/vector-embeddings/"),
            ("Prompt Engineering Guide", "https://www.promptingguide.ai/"),
            ("Context windows", "https://anthropic.com")
        ],
        "summary": """### Key Learnings
* **Tokens:** Sub-word chunks processed by models (roughly ~4 characters or 0.75 words in English).
* **Embeddings:** High-dimensional vector representations capturing semantic relationships between text.
* **Context Window:** Maximum token capacity an LLM can process in a single prompt + completion cycle.""",
        "code": """import numpy as np

# Simulating Cosine Similarity between Embeddings
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

emb_king = np.array([0.25, 0.88, 0.12])
emb_queen = np.array([0.24, 0.85, 0.15])
emb_apple = np.array([-0.50, 0.10, 0.90])

print("King vs Queen Similarity:", round(cosine_similarity(emb_king, emb_queen), 4))
print("King vs Apple Similarity:", round(cosine_similarity(emb_king, emb_apple), 4))"""
    },
    {
        "filename": "04_rag_architecture_databricks_cortex.ipynb",
        "title": "Section 4: RAG architecture, DataBricks Vector Search and Cortex Search (4 hours)",
        "links": [
            ("Retrieval-Augmented Generation (RAG) - I", "https://research.ibm.com/blog/retrieval-augmented-generation-RAG"),
            ("Retrieval Augmented Generation (RAG) - II", "https://docs.databricks.com/en/generative-ai/retrieval-augmented-generation.html"),
            ("Cortex Search", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview")
        ],
        "summary": """### Key Learnings
* **RAG Architecture:** Grounding LLM responses on retrieved external data to minimize hallucinations.
* **Components:** Ingestion -> Chunking -> Embedding -> Vector Indexing -> Search Retrieval -> Context Synthesis.
* **Enterprise Platforms:** DataBricks Vector Search and Snowflake Cortex Search bring managed search directly to data warehouses.""",
        "code": """# End-to-End Conceptual RAG Query Flow
def mock_retriever(query):
    knowledge_base = {
        "company policy": "Employees get 20 days of paid leave annually.",
        "ai policy": "All LLM usage must be audited by data security."
    }
    for key, val in knowledge_base.items():
        if key in query.lower():
            return val
    return "No relevant context found."

def rag_pipeline(user_query):
    context = mock_retriever(user_query)
    augmented_prompt = f"Context: {context}\\n\\nQuestion: {user_query}\\nAnswer:"
    return f"[LLM Generation based on Prompt]:\\n{augmented_prompt}"

print(rag_pipeline("What is our company policy on leave?"))"""
    },
    {
        "filename": "05_vector_embeddings_and_chunking.ipynb",
        "title": "Section 5: Vector Embeddings and Chunking (4 hours)",
        "links": [
            ("Chunking Strategies for LLM Applications", "https://www.pinecone.io/learn/chunking-strategies/"),
            ("Vector Search", "https://docs.databricks.com/en/generative-ai/vector-search.html"),
            ("Cortex Search", "https://docs.snowflake.com/")
        ],
        "summary": """### Key Learnings
* **Chunking Strategies:** Fixed-size, sentence-based, recursive character, and semantic chunking.
* **Overlap:** Crucial to prevent loss of context across chunk boundaries.
* **Impact on Embeddings:** Smaller chunks improve precision; larger chunks improve context breadth.""",
        "code": """# Fixed-size Chunking with Overlap
def chunk_text(text, chunk_size=50, overlap=10):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

sample_text = "Retrieval Augmented Generation works best when documents are split into clean semantic chunks."
chunks = chunk_text(sample_text, chunk_size=30, overlap=10)
for i, c in enumerate(chunks):
    print(f"Chunk {i+1}: '{c}'")"""
    },
    {
        "filename": "06_vector_databases_and_major_providers.ipynb",
        "title": "Section 6: Vector Databases and major providers (4 hours)",
        "links": [
            ("Pinecone Docs", "https://docs.pinecone.io/"),
            ("Milvus Docs", "https://milvus.io/docs"),
            ("Weaviate Docs", "https://weaviate.io/developers/weaviate"),
            ("Chroma DB Docs", "https://docs.trychroma.com/")
        ],
        "summary": """### Key Learnings
* **Vector Databases:** Specialized engines for storing high-dimensional vectors and querying via Approximate Nearest Neighbor (ANN) search.
* **Indexing Algorithms:** HNSW (Hierarchical Navigable Small World), IVF (Inverted File Index).
* **Providers:** Pinecone (Managed SaaS), Milvus (High-scale distributed), Weaviate (Hybrid search), Chroma (Local embedded).""",
        "code": """import numpy as np

class SimpleVectorDB:
    def __init__(self):
        self.storage = {}
        
    def insert(self, doc_id, vector, metadata):
        self.storage[doc_id] = {"vector": np.array(vector), "metadata": metadata}
        
    def query(self, query_vector, top_k=1):
        results = []
        for doc_id, data in self.storage.items():
            score = np.dot(query_vector, data["vector"])
            results.append((doc_id, score, data["metadata"]))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]

vdb = SimpleVectorDB()
vdb.insert("doc1", [0.1, 0.9], {"text": "AI Policy"})
vdb.insert("doc2", [0.8, 0.1], {"text": "Sales Report"})
print("Search Result:", vdb.query([0.05, 0.95]))"""
    },
    {
        "filename": "07_ai_agents_and_workflows.ipynb",
        "title": "Section 7: AI agents and workflows (4 hours)",
        "links": [
            ("Building Effective Agents", "https://anthropic.com/research/building-effective-agents"),
            ("AI agent orchestration patterns", "https://langchain-ai.github.io/langgraph/"),
            ("Agent Bricks - Production AI Agents", "https://docs.databricks.com/")
        ],
        "summary": """### Key Learnings
* **Agent Core Components:** Planning, Memory, Tools, and Action execution.
* **Orchestration Patterns:** Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer loops.
* **ReAct Framework:** Reasoning + Acting iteratively to solve complex queries.""",
        "code": """def execute_tool(action, query):
    if action == "calculator":
        return eval(query)
    return "Tool not found"

def react_agent(user_prompt):
    print(f"User: {user_prompt}")
    print("Thought: I need to calculate 15% of 250 using the calculator tool.")
    action = "calculator"
    action_input = "250 * 0.15"
    observation = execute_tool(action, action_input)
    print(f"Observation: {observation}")
    print(f"Final Answer: 15% of 250 is {observation}")

react_agent("What is 15% of 250?")"""
    },
    {
        "filename": "08_memory_and_langchain.ipynb",
        "title": "Section 8: Memory & Langchain (2 hours)",
        "links": [
            ("LangChain Overview", "https://python.langchain.com/docs/get_started/introduction")
        ],
        "summary": """### Key Learnings
* **LangChain Framework:** Standardized interface for chaining LLMs, prompts, and vector stores.
* **Types of Memory:** ConversationBufferMemory, ConversationSummaryMemory, VectorStore-backed memory.
* **Context Management:** Persisting conversation state across multiple turns.""",
        "code": """class ConversationBufferMemory:
    def __init__(self):
        self.history = []
        
    def add_user_message(self, msg):
        self.history.append(f"User: {msg}")
        
    def add_ai_message(self, msg):
        self.history.append(f"AI: {msg}")
        
    def get_formatted_history(self):
        return "\\n".join(self.history)

memory = ConversationBufferMemory()
memory.add_user_message("Hi, I'm Alex.")
memory.add_ai_message("Hello Alex! How can I assist you?")
memory.add_user_message("What's my name?")

print(memory.get_formatted_history())"""
    },
    {
        "filename": "09_model_context_protocol.ipynb",
        "title": "Section 9: Model Context Protocol (MCP) (2 hours)",
        "links": [
            ("What is Model Context Protocol", "https://modelcontextprotocol.io/")
        ],
        "summary": """### Key Learnings
* **Model Context Protocol (MCP):** Open standard connecting AI models cleanly to local/remote data sources and tools.
* **Architecture:** MCP Client (LLM Application) <-> MCP Server (Data sources, APIs, Tools).
* **Benefits:** Eliminates custom tool integrations; provides dynamic capability discovery.""",
        "code": """import json

# Conceptual Model of MCP Client/Server Request
mcp_request_payload = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "name": "query_database",
        "arguments": {"sql": "SELECT * FROM sales LIMIT 5"}
    },
    "id": 1
}

print("MCP Client Tool Call Payload:")
print(json.dumps(mcp_request_payload, indent=2))"""
    },
    {
        "filename": "10_tool_calling.ipynb",
        "title": "Section 10: Tool calling (2 hours)",
        "links": [
            ("Tool / Function Calling", "https://platform.openai.com/docs/guides/function-calling"),
            ("Tool use with Claude", "https://docs.anthropic.com/en/docs/build-with-claude/tool-use")
        ],
        "summary": """### Key Learnings
* **Function/Tool Calling:** Structured output schema (JSON) where the model outputs tool parameters rather than prose.
* **Execution Loop:** Model chooses tool -> Code executes tool -> Result sent back to Model -> Final Answer generated.""",
        "code": """import json

weather_tool_schema = {
    "name": "get_weather",
    "description": "Fetch real-time weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "City name"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
    }
}

llm_response_tool_call = {
    "tool": "get_weather",
    "arguments": {"location": "San Francisco", "unit": "celsius"}
}

print("Tool Definition Schema:", json.dumps(weather_tool_schema, indent=2))
print("LLM Generated Call:", json.dumps(llm_response_tool_call, indent=2))"""
    },
    {
        "filename": "11_responsible_ai_governance_hallucinations.ipynb",
        "title": "Section 11: Responsible AI, governance, hallucinations (4 hours)",
        "links": [
            ("Responsible AI at Microsoft", "https://www.microsoft.com/en-us/ai/responsible-ai"),
            ("Optimizing LLM Accuracy", "https://platform.openai.com/docs/guides/optimizing-llm-accuracy")
        ],
        "summary": """### Key Learnings
* **Responsible AI Pillars:** Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, Accountability.
* **Hallucinations:** Confident generation of incorrect facts. Mitigated via RAG, guardrails, and lower temperature settings.
* **Governance Frameworks:** Auditing prompts, tracking line-of-sight metrics, content moderation, PII redaction.""",
        "code": """def verify_groundedness(fact_statement, retrieved_sources):
    matches = [src for src in retrieved_sources if src in fact_statement]
    groundedness_score = len(matches) / len(retrieved_sources)
    return {
        "statement": fact_statement,
        "score": groundedness_score,
        "is_grounded": groundedness_score > 0.5
    }

sources = ["Revenue grew by 15%", "New product launches in Q4"]
print(verify_groundedness("The company revenue grew by 15% this quarter.", sources))"""
    },
    {
        "filename": "12_system_prompts.ipynb",
        "title": "Section 12: System prompts (2 hours)",
        "links": [
            ("Prompting best practices", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts"),
            ("Prompt engineering guide", "https://www.promptingguide.ai/")
        ],
        "summary": """### Key Learnings
* **System Prompts:** Top-level instructions framing persona, constraints, guidelines, and output structures for the model.
* **Best Practices:** Use explicit XML/Markdown tags, specify output formats (JSON/Markdown), define fallback behavior.""",
        "code": """def build_system_prompt(role, task, output_format):
    return f\"\"\"<system>
Role: {role}
Task: {task}
Rules:
1. Adhere strictly to facts provided.
2. Do not invent information.
Format Requirements:
{output_format}
</system>\"\"\"

sys_prompt = build_system_prompt(
    role="Senior Financial Analyst",
    task="Summarize quarterly earnings call transcripts.",
    output_format="Respond only in a JSON object with keys 'summary' and 'key_metrics'."
)
print(sys_prompt)"""
    },
    {
        "filename": "13_few_shot_prompting.ipynb",
        "title": "Section 13: Few-shot prompting (1 hours)",
        "links": [
            ("Few-Shot Prompting", "https://www.promptingguide.ai/techniques/fewshot"),
            ("Prompt engineering", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview")
        ],
        "summary": """### Key Learnings
* **In-Context Learning:** Teaching the model tasks without fine-tuning by providing exemplar input-output pairs.
* **Zero-shot vs Few-shot:** Zero-shot provides no examples; Few-shot provides 1 to 5 exemplar pairs.""",
        "code": """examples = [
    {"input": "The service was terribly slow.", "output": "Negative"},
    {"input": "Food was amazing and staff was friendly!", "output": "Positive"}
]

def build_few_shot_prompt(new_input, exemplar_list):
    prompt = "Classify sentiment as Positive or Negative based on examples:\\n\\n"
    for ex in exemplar_list:
        prompt += f"Input: {ex['input']}\\nOutput: {ex['output']}\\n---\\n"
    prompt += f"Input: {new_input}\\nOutput:"
    return prompt

print(build_few_shot_prompt("The atmosphere was quiet and pleasant.", examples))"""
    },
    {
        "filename": "14_chain_of_thought.ipynb",
        "title": "Section 14: Chain-of-thought (1 hours)",
        "links": [
            ("Chain-of-Thought Prompting", "https://www.promptingguide.ai/techniques/cot")
        ],
        "summary": """### Key Learnings
* **Chain-of-Thought (CoT):** Encourages LLMs to output intermediate reasoning steps before delivering a final answer.
* **Zero-Shot CoT:** Adding phrases like *\"Let's think step by step\"* dramatically improves complex arithmetic & logic accuracy.""",
        "code": """def cot_prompt(problem):
    return f\"\"\"Solve the following problem by breaking it down step by step.
    
Problem: {problem}

Let's think step by step:
1. \"\"\"

print(cot_prompt("A store has 35 apples. It sells 12 in the morning and receives a shipment of 20. How many apples remain?"))"""
    },
    {
        "filename": "15_python_for_ai.ipynb",
        "title": "Section 15: Python for AI (2 hours)",
        "links": [
            ("OpenAI Python API library", "https://github.com/openai/openai-python")
        ],
        "summary": """### Key Learnings
* **OpenAI SDK:** Primary client for interacting with GPT models programmatically.
* **Patterns:** Initializing client, streaming responses, error handling, structured output parsing.""",
        "code": """code_snippet = '''
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "your_api_key_here"))

try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a python function to calculate Fibonacci numbers."}
        ],
        temperature=0.7
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"API Error: {e}")
'''

print("Executable Python SDK Pattern:")
print(code_snippet)"""
    }
]

def create_jupyter_notebook(title, links, summary, code):
    cells = []
    
    # Header & Links Cell
    header_md = f"# {title}\n\n### Material Links & Prerequisites\n"
    for label, url in links:
        header_md += f"* [{label}]({url})\n"
    
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [header_md]
    })
    
    # Summary Cell
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [summary]
    })
    
    # Code Example Cell
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [code]
    })
    
    notebook = {
        "cells": cells,
        "metadata": {
            "language_info": {"name": "python"}
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    return notebook

output_dir = "ai_course_notebooks"
os.makedirs(output_dir, exist_ok=True)

for nb in notebooks_data:
    nb_json = create_jupyter_notebook(nb["title"], nb["links"], nb["summary"], nb["code"])
    path = os.path.join(output_dir, nb["filename"])
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb_json, f, indent=2)

print(f"Successfully created 15 Jupyter Notebooks in directory '{output_dir}/'")