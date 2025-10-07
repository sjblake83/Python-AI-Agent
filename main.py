import os, sys
from dotenv import load_dotenv
from google.genai import types
from google import genai



def main():
    is_verbose = False
    
    load_dotenv()
    api_key = os.environ.get("GEMENI_API_KEY")
    client = genai.Client(api_key=api_key)
    args_count = len(sys.argv)
    
    if (args_count <= 1):
        print("Error: missing argument <Query>")
        sys.exit(1)
    
    if (args_count >= 3 and sys.argv[2] == "--verbose"):
        is_verbose = True
            
    
    # query = input("Please enter your prompt: ")
    user_prompt = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages
    )
    
    if (is_verbose):
        print(f"User prompt: {user_prompt}")
    print(f"\nAgent Response: {response.text}")
    if (is_verbose):
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()