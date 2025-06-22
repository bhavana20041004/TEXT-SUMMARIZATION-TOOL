# TEXT-SUMMARIZATION-TOOL

*COMPANY* : CODTECH IT SOLUTION

*NAME* : TALARI BHAVANA

*INTERN ID* : CT04DF313

*DOMAIN* : Artificial Intelligence

*DURATION* : 4 weeks 

*MENTOR* : NEELA SANTOSH

*DISCRIPTION* : The provided Python script implements a **text summarization tool** using the **transformers library** from Hugging Face and specifically utilizes the **pre-trained BART (Bidirectional and Auto-Regressive Transformers) model – `facebook/bart-large-cnn`** for abstractive summarization. This tool is designed to generate concise summaries of lengthy textual content, making it highly useful for processing articles, reports, and other long-form documents. At its core, the script leverages Hugging Face’s `pipeline` abstraction, which simplifies access to powerful NLP models without requiring complex configurations. The summarization pipeline automatically loads the `facebook/bart-large-cnn` model, which was fine-tuned on the CNN/DailyMail dataset, known for news summarization tasks. The script defines a function `summarize_article` that takes the input text and optional parameters such as `max_length` and `min_length` to control the size of the output summary. These parameters ensure the summary is neither too short to miss key points nor too long to defeat the purpose of summarization. In the `__main__` block, a sample article about the evolution of smartphones is provided as input. The function is called to generate the summary, which is then printed alongside the original article for comparison. The tool demonstrates how transformer-based architectures can effectively condense large bodies of information while retaining meaning and context. The BART model combines the capabilities of both autoencoder and autoregressive models, allowing it to understand the full context of the input text and generate coherent and fluent summaries. Tools used include Python as the programming language, the `transformers` library for accessing pre-trained models, and the `pipeline` method for quick deployment. This approach abstracts away the need to manually tokenize input, feed it into the model, and decode the output. Moreover, the use of a command-line script format with the `__main__` guard makes the tool modular and easily integrable into larger applications. This kind of summarization is **abstractive**, meaning it does not just extract sentences verbatim from the input, but rather generates new sentences that capture the essence of the input text. It differs from **extractive summarization**, which only pulls key sentences directly. In practical terms, such tools are valuable for students, researchers, content creators, and professionals who deal with large volumes of textual data and need to grasp core ideas quickly. As AI and NLP continue to evolve, tools like this exemplify how cutting-edge research can be turned into user-friendly applications.
