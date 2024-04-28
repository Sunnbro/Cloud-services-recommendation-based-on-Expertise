import transformers
import torch

# Load the BERT model and create a new tokenizer 
model = transformers.BertModel.from_pretrained("bert-base-uncased") 
tokenizer = transformers.BertTokenizer.from_pretrained("bert-base-uncased") 

# Tokenize and encode the text 
input_ids = tokenizer.encode("Though not without its faults, this software is amazingly accurate. I haven't tried voice recognition software in a long time, mainly because it used to take a lot of \"training\" (reading hour-long passages of text while the software learns my speech patterns) to get it to an acceptable level of accuracy.  A lot has changed in the last several years: improvements in voice recognition algorithms, and more powerful home computers have led to software that is impressively accurate right out of the box.  In under five minutes of reading to my computer, I found that the software was giving me near-perfect accuracy.  As a test, I read Walt Whitman's poem, \"When I Heard the Learn'd Astronomer\".  I read at a very natural pace (perhaps even a bit rushed), including punctuation, and the software scored 100% for accuracy.\n\nBesides its accuracy, Dragon NaturallySpeaking impressed me with its fairly intuitive set of commands, both for editing documents and for \"getting around\" in Windows and on the web.  Though references are provided to let you know the commands that are available, I found it pretty easy to guess correctly at the commands I needed.  For example, I said, \"search the web for computer science\".  A browser window quickly opened, and took me to the Bing search page to show me the results for \"computer science\".  Preferring Google results, I decided to try \"Search Google for computer science\".  Sure enough, it worked to (as did searching Yahoo).  Then I tried \"search computer for jpegs\" and immediately was presented with a list of jpeg files on my computer.  When I'm not sure what to say, I just need to say \"What can I say\", and Dragon NaturallySpeaking will give me a list of commands.  (And, apparently, I can teach it new commands, but I haven't tried that yet.)  All in all, I found that I could guess the right commands about 75% of the time.\n\nA NOTE ABOUT MULTIPLE USERS: I found it interesting that the software recognized my own voice almost perfectly.", add_special_tokens=True) 

# Use BERT to encode the meaning and context of the words and phrases in the text 
outputs = model(torch.tensor([input_ids])) 

# Use the attention weights of the tokens to identify the most important words and phrases 
attention_weights = outputs[-1] 
print("Attention weights shape:", attention_weights.shape)

# Calculate mean attention weights across all tokens 
mean_attention_weights = torch.mean(attention_weights, dim=1)  
print("Mean attention weights shape:", mean_attention_weights.shape)

# Get the indices of the top 3 tokens based on mean attention weights 
top_indices = mean_attention_weights.argsort(descending=True)[:3] 

# Remove indices corresponding to special tokens ([CLS] and [SEP])
top_indices = [idx for idx in top_indices if idx < len(input_ids) - 1]

# Get the tokens corresponding to the top indices
top_tokens = tokenizer.convert_ids_to_tokens([input_ids[i] for i in top_indices])

# Filter out special tokens
top_keywords = [token for token in top_tokens if token not in ['[CLS]', '[SEP]']]

# Print the top keywords
print("Top keywords:", top_keywords)
