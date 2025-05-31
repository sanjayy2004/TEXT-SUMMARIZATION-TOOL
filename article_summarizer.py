from transformers import pipeline

def summarize_text(text, max_length=130, min_length=30):
    print("\n⏳ Summarizing...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

def main():
    print("📄 Article Summarizer using BART Model")
    print("--------------------------------------")

    # Ask user for input method
    choice = input("Enter '1' to paste text manually, or '2' to load from a .txt file: ").strip()

    if choice == '1':
        print("\nPaste your article text (end with an empty line):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        article_text = "\n".join(lines)
    elif choice == '2':
        filepath = input("Enter path to the .txt file: ").strip()
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                article_text = f.read()
        except FileNotFoundError:
            print("❌ File not found.")
            return
    else:
        print("❌ Invalid choice.")
        return

    # Check if article is long enough
    if len(article_text.split()) < 50:
        print("⚠️ Please provide a longer article (at least 50 words).")
        return

    # Perform summarization
    summary = summarize_text(article_text)

    # Show results
    print("\n✅ Summary:")
    print("--------------------------------------")
    print(summary)

if __name__ == "__main__":
    main()
