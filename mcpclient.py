import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    # Read prompt from args or use a default 
    prompt = "What is the capital of France?"
    if len(os.sys.argv) > 1:
        prompt = os.sys.argv[1]

    # Print the extracted prompt
    print(f"Prompt: {prompt}")

    # Create configuration dictionary
    config = {
      "mcpServers": {
        "filesystem": {
          "command": "npx",
          "args": ["@modelcontextprotocol/server-filesystem", "/tmp/"]
        }
      }
    }

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatOpenAI(model="gpt-4o")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        prompt
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())