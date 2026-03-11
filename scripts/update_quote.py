import urllib.request
import json
import re

def update_quote():
    url = "https://zenquotes.io/api/random"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode('utf-8'))
            quote = data[0]['q']
            author = data[0]['a']
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return
    
    quote_text = f"*{quote}* — **{author}**"
    
    with open("README.md", "r", encoding="utf-8") as file:
        readme = file.read()
        
    # Replace content between <!-- BEGIN QUOTE --> and <!-- END QUOTE -->
    pattern = r'(<!-- BEGIN QUOTE -->\s*)(.*?)(\s*<!-- END QUOTE -->)'
    if re.search(pattern, readme, re.DOTALL):
        readme = re.sub(pattern, rf'\1{quote_text}\3', readme, flags=re.DOTALL)
    else:
        print("Quote markers not found in README.md")
        return
        
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme)
        
    print("Updated quote:", quote_text)

if __name__ == "__main__":
    update_quote()
