import os, sys
from dotenv import load_dotenv
from google import genai



def main():
    load_dotenv()
    api_key = os.environ.get("GEMENI_API_KEY")
    
    client = genai.Client(api_key=api_key)
    
    # query = input("Please enter your prompt: ")
    query = sys.argv[1]
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=query
    )
    
    print(f"Agent Response: {response.text}")
    print("\n\nUsage data:")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()