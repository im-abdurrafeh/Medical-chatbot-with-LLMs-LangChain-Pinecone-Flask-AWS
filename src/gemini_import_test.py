from dotenv import load_dotenv
import os

load_dotenv()

def main():
    key = os.getenv("GOOGLE_API_KEY")
    print("GOOGLE_API_KEY present:", bool(key))
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        print("Imported ChatGoogleGenerativeAI OK")
    except Exception as e:
        print("Import error for langchain_google_genai.ChatGoogleGenerativeAI:", repr(e))
        raise

if __name__ == "__main__":
    main()
