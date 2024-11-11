# EAHistoriChat

**EAHistoriChat** (*E*arly *A*merican) is a chatbot designed to respond in the style of Early American written texts. This project draws significant inspiration from Pierre-Carl Langlais' [Monad-GPT](https://huggingface.co/Pclanglais/MonadGPT), which pioneered the use of 17th-century writing styles in AI responses. Similarly, EAHistoriChat is a fine-tuned version of [Mistral-Hermes 2](https://huggingface.co/teknium/OpenHermes-2-Mistral-7B), trained on synthetic question-answer pairs to replicate Early American prose.

To build the training dataset, we curated paragraphs from the [Evans-TCP](https://textcreationpartnership.org/tcp-texts/evans-tcp-evans-early-american-imprints/) corpus and used a quantized version of [Mistral-Nemo-Instruct](https://huggingface.co/neuralmagic/Mistral-Nemo-Instruct-2407-FP8) to generate questions for which these paragraphs serve as appropriate answers. Fine-tuning was conducted using the Axolotl framework on this custom dataset.

- Idea: [Mark L. Thompson](https://www.rug.nl/staff/m.l.thompson)
- Design and implementation: [Michiel van der Ree](https://www.rug.nl/staff/michiel.van.der.ree/)

For more details see our [repository](https://github.com/UG-Team-Data-Science/ea-historichat).

## Known Limitations
- **Limited multi-turn capabilities**: The bot struggles with multi-turn conversations. For the best experience, clear the chat history before asking a new question.
- **Text formatting**: Since the training data retained newlines, the bot's responses may include line breaks after approximately a manuscript's width of characters.
