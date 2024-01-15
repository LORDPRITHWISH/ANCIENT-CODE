import emoji

def remove_emojis(text):
    return emoji.replace_emoji(text_with_emojis,'')

# Example usage
text_with_emojis = "Hello! 😃 This is a message with emojis 😊👍"
text_without_emojis = remove_emojis(text_with_emojis)
print(text_without_emojis)  # Output: Hello!  This is a message with emojis 
