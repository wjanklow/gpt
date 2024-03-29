import openai
import pandas as pd

# Set up OpenAI API key
openai.api_key = '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'

# Function to generate completion for a single prompt
def generate_completion(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can replace this with the appropriate model ID
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Function to read prompts from spreadsheet and generate completions
def fill_spreadsheet(input_csv, output_csv):
    # Read prompts from input CSV
    df = pd.read_csv(input_csv)
    
    # Iterate over rows and generate completions
    for index, row in df.iterrows():
        prompt = row['Prompt']  # Assuming 'Prompt' is the column name for prompts
        completion = generate_completion(prompt)
        # Fill in the completion in the corresponding column
        df.at[index, 'Completion'] = completion
    
    # Write back to output CSV
    df.to_csv(output_csv, index=False)

# Example usage
input_csv = 'input.csv'  # Input CSV file containing prompts
output_csv = 'output.csv'  # Output CSV file where completions will be filled
fill_spreadsheet(input_csv, output_csv)


