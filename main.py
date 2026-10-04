from core.router import handle
import skills.basic 

def main():
    print("Assistant ready. Type 'exit' to quit.")
    while True:
        text = input("You: ").strip()
        if text.lower() in ("exit", "quit"):
            break
        print("Assistant:", handle(text))

if __name__ == "__main__":
    main()