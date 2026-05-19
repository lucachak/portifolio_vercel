import re

with open("core/views.py", "r") as f:
    content = f.read()

# Replace "title": "..." with "title": _("...")
content = re.sub(r'("title":\s*)("[^"]+")', r'\1_\2', content)

# Replace "description": (\n            "..."\n            "..."\n        ),
# This is tricky with regex, let's write a targeted replace for description and terminal_lines text
def wrap_in_lazy(match):
    return f'_({match.group(0)})'

# we can just use a simple regex for descriptions
descriptions = re.findall(r'"description":\s*\((.*?)\),', content, re.DOTALL)
for desc in descriptions:
    content = content.replace(f'"description": ({desc}),', f'"description": _({desc}),')

# terminal_lines text
texts = re.findall(r'("text":\s*)("[^"]+")', content)
for prefix, text in texts:
    content = content.replace(f'{prefix}{text}', f'{prefix}_{text}')

with open("core/views.py", "w") as f:
    f.write(content)

print("done")
