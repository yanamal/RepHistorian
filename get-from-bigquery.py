from google.cloud import bigquery
import pandas

client = bigquery.Client()

dataset_ref = client.dataset('stackoverflow', project='bigquery-public-data')


answers_table_ref = dataset_ref.table('posts_answers')
answers_table = client.get_table(answers_table_ref)

answer_rows = client.list_rows(answers_table, start_index=0, max_results=10)
data_dump = answer_rows.to_dataframe()


questions_table_ref = dataset_ref.table('posts_questions')
questions_table = client.get_table(questions_table_ref)

question_rows = client.list_rows(questions_table, start_index=0, max_results=10)
data_dump = pandas.concat([data_dump, question_rows.to_dataframe()], ignore_index=True, sort=False)
print data_dump