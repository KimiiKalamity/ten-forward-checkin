import random

prompts = [
    "What would make tonight feel complete?"
    "What am I avoiding that might actually be small?"
    "What would Picard do today?"
    "What am I making this mean about myself?",
    "What feels heavy right now?",
    "What feels quietly hopeful right now?",
    "What would help Future Kimberly?",
    "What is one kind thing I can do before the day ends?"
]

chosen_prompt = random.choice(prompts)

print("Ten Forward Prompt of the Day:")
print(chosen_prompt)
