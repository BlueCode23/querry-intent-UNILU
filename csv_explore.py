import os
import openai
import csv
import time

start = time.time()
openai.api_key = "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"

# Define the path to your CSV file here
input_csv_file_path = 'osfstorage-archive/Coded Queries.csv'

output_csv_file_path = 'osfstorage-archive/generated queries.csv'

# function that takes in string argument as parameter
def comp(PROMPT, MaxToken=50, outputs=3):
    # using OpenAI's Completion module that helps execute
    # any tasks involving text
    response = openai.Completion.create(
        # model name used here is text-davinci-003
        # there are many other models available under the
        # umbrella of GPT-3
        model="text-davinci-003",
        # passing the user input
        prompt=PROMPT,
        # generated output can have "max_tokens" number of tokens
        max_tokens=MaxToken,
        # number of outputs generated in one call
        n=outputs
        #between 0 and 1, where 1 is deterministic answers
        #temperature= temperature
    )
    # creating a list to store all the outputs
    output = list()
    for k in response['choices']:
        output.append(k['text'].strip())
    print(output)
    return output



# Open the CSV file
with open(input_csv_file_path, mode='r', encoding='utf-8') as infile, \
     open(output_csv_file_path, mode='w', encoding='utf-8', newline='') as outfile:
    # Create a CSV reader object
    csv_reader = csv.DictReader(infile)

    # Create a CSV writer object
    csv_writer = csv.writer(outfile)

    # Write the header to the output file
    csv_writer.writerow(['User Group', 'Scenario (Stimulus)', 'Query', 'Query Scope', 'Query Purpose', 'Response Format', 'Information Feature 1', 'Information Feature 2', 'Information Feature 3'])

    # Initialize a line counter
    line_count = 0

    # Read each row in the CSV file
    for row in csv_reader:
        # Check if we have read 5 lines already
        #if line_count == 5:
        #    break
        # Print the 'user' and 'query' in the requested format
        sentence = f"{row['User Group']} : {row['Query']}"
        print("original : " + row['Query'])
        user_group,scenario, query, scope, purpose, response_format, info_feature_1, info_feature_2, info_feature_3 = row['User Group'], row['Scenario (Stimulus)'], row['Query'],row['Query Scope'], row['Query Purpose'], row['Response Format'],row['Information Feature 1'], row['Information Feature 2'], row['Information Feature 3']
        PROMPT = f"""Rephrase the following query in the manner of an experienced user interface {user_group} "{query}
        " """
        response = comp(PROMPT, MaxToken=3000, outputs=3)
        for i in response:
            csv_writer.writerow([user_group, scenario, PROMPT,scope, purpose, response_format, info_feature_1, info_feature_2, info_feature_3])

        # Increment the line counter
        #csv_writer.writerow([PROMPT])
        #line_count += 1



