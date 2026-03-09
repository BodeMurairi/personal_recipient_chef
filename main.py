#!/usr/bin/env python3

import os
import uuid
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.messages import AIMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

from web_search import web_search
from image_encoder import encode_image_for_AI

load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
    max_tokens=4000
)

# Memory configuration
memory_thread = {
    "thread_id": str(uuid.uuid4()),
    "memory": InMemorySaver()
}

# System prompt
system_prompt = (
    "You are an expert cooking chef. The user will provide a list of ingredients "
    "or food images. Provide the best recipes and step-by-step instructions for "
    "cooking those recipes. Use the web search API when needed to find "
    "up-to-date recipes."
)

# Create the agent
agent = create_agent(
    model=llm,
    checkpointer=memory_thread["memory"],
    system_prompt=system_prompt,
    tools=[web_search]
)

print("👨‍🍳 Welcome to Sam Cooking Chef!")

while True:
    human_question = input("\nEnter your message (or type 'quit' to exit): ").strip()

    if human_question.lower() in ["quit", "exit", "q", "esc", "e"]:
        print("Thank you for using our chef. Goodbye!")
        break

    upload_images = input(
        "Enter image file paths, separated by commas (or leave empty): "
    ).strip()

    image_paths = [path.strip() for path in upload_images.split(",") if path.strip()]

    images_for_ai = encode_image_for_AI(image_paths=image_paths)

    # Create multimodal message
    message_content = [{"type": "text", "text": human_question}]

    if images_for_ai:
        message_content.extend(images_for_ai)

    messages_to_send = [
        HumanMessage(content=message_content)
    ]

    try:
        response = agent.invoke(
            {"messages": messages_to_send},
            config={"configurable": {"thread_id": memory_thread["thread_id"]}}
        )

    except Exception as error:
        print(f"\nError invoking agent: {error}")
        continue

    # Extract AI messages
    ai_messages = [
        m for m in response.get("messages", []) if isinstance(m, AIMessage)
    ]

    for ai_msg in ai_messages:
        content = ai_msg.content

        if isinstance(content, list):
            text_output = "\n".join(
                c.get("text", "") for c in content if c.get("type") == "text"
            )
        else:
            text_output = content

        if text_output.strip():
            print("\nAI Response:\n")
            print(text_output)
