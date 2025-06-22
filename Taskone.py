from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(text, max_length=200, min_length=100):
    """
    Summarizes a long text using the BART model.
    """
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    
    article = medium_article = """
The evolution of smartphones over the past decade has been extraordinary. Initially used for simple tasks
like calling and texting, smartphones have now become powerful handheld computers. With advancements in
technology, phones now feature high-resolution cameras, AI-driven assistants, facial recognition, and 5G
connectivity. These features have changed the way we communicate, shop, and even access healthcare.

The app ecosystem has grown tremendously, providing tools for everything from social networking and banking
to learning and fitness. Companies like Apple and Samsung lead the market with innovative designs and
features. Meanwhile, newer players from countries like China are rapidly gaining ground with competitive
prices and high-performance devices.

However, with great power comes concerns. Data privacy, screen addiction, and e-waste are emerging challenges
that manufacturers and users alike must address. The future of smartphones may lie in foldable screens,
augmented reality integration, and even brain-computer interfaces. As the technology continues to evolve,
it's clear that smartphones are no longer just communication devices—they're essential tools shaping the
modern lifestyle.
"""


    
    summary = summarize_article(article)
    
   
    print("\n📄 Original Article:\n", article)
    print("\n📝 Summary:\n", summary)
