import pandas as pd
df = pd.read_csv('dataset.csv')

new_df = pd.DataFrame()


new_df['question'] = df['question']
new_df['answer'] = df['answer']

new_df.to_csv('new_df.csv', index=False)