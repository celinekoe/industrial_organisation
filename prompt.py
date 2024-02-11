import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
#csv_file_path = 'your_file.csv'

# Read the CSV file into a DataFrame
#df = pd.read_csv(csv_file_path)

# Define a function to create a prompt from a row
def create_prompt_from_row(row):
    # Assuming your CSV has columns 'Name' and 'Action'
    #return f"Generate a story about {row['Name']} who is trying to {row['Action']}."
    return "Find the key technology of Austin Biosciences Corp"

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    prompt = create_prompt_from_row(row)
    # Here you can send the prompt to ChatGPT or do something else with it
    print(prompt)


curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'