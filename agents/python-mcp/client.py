#!/usr/bin/env python3
import argparse
import asyncio
import os
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="?", default="What is the capital of France?")
    parser.add_argument("--provider", choices=["openai", "anthropic"], default="openai")
    parser.add_argument("--model", type=str)
    parser.add_argument("--max-steps", type=int, default=30)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int)
    parser.add_argument("--mcp-path", type=str, default="/tmp/")
    return parser.parse_args()

def create_llm(args):
    model = args.model or ("gpt-4o" if args.provider == "openai" else "claude-3-5-sonnet-20241022")
    
    kwargs = dict(model=model)
    # kwargs = {"model": model, "temperature": args.temperature}
    # if args.max_tokens:
    #     kwargs["max_tokens"] = args.max_tokens
    
    if args.provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(**kwargs)
    else:
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(**kwargs)

async def main():
    load_dotenv()
    args = parse_args()
    
    config = {
        "mcpServers": {
            "filesystem": {
                "command": "npx",
                "args": ["@modelcontextprotocol/server-filesystem", args.mcp_path]
            }
        }
    }
    
    client = MCPClient.from_dict(config)
    llm = create_llm(args)
    agent = MCPAgent(llm=llm, client=client, max_steps=args.max_steps)
    
    result = await agent.run(args.prompt)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
