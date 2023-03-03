import pandas as pd
import numpy as np

df = pd.read_csv('data_gantt.csv')
df = df.replace({None: "null"})

# format_date = lambda x: f"new Date({x.replace('-', ', ')})"
def format_date(x):
    x = x.split('-')
    return f"new Date({x[0]}, {int(x[1])-1}, {x[2]})"
check_nan = lambda x: f"'{x}'" if x is not None else "null"

for index, row in df.iterrows():
    task_id = f"'{row['Task ID']}'"
    task_name = f"'{row['Task Name']}'"
    resource = f"'{row['Resource']}'"
    start_date = format_date(row['Start Date'])
    end_date = format_date(row['End Date'])
    duration = f"{row['Duration']}"
    duration = duration.replace("nan", "null")
    percent_complete = f"{row['Percent Complete']}"
    dependencies = check_nan(row['Dependencies'])
    dependencies = dependencies.replace("'null'", "null")

    line = f"      [{task_id}, {task_name}, {resource}, {start_date}, {end_date}, {duration}, {percent_complete}, {dependencies}],"
    print(line)

"""OUTPUT:
      ['planning', 'Planning', 'Analysis', new Date(2023, 02, 13), new Date(2023, 02, 24), null, 100, null],
      ['data_acquisition', 'Get and store VVVX, Gaia data', 'Data', new Date(2023, 02, 20), new Date(2023, 03, 17), null, 40, null],
      ['get_labels', 'Get labels from StarHorse and RR Lyrae samples', 'Data', new Date(2023, 03, 20), new Date(2023, 03, 22), null, 0, 'data_acquisition'],
      ['quality_check', 'Explore and check the quality of the data', 'Data', new Date(2023, 03, 23), new Date(2023, 03, 24), null, 0, 'get_labels'],
      ['preprocesing_strategy', 'Define the preprocesing strategy', 'Data', new Date(2023, 03, 27), new Date(2023, 03, 28), null, 0, null],
      ['preprocesing_implementation', 'Code implementation of the preprocesing strategy', 'Data', new Date(2023, 03, 29), new Date(2023, 03, 31), null, 0, 'preprocesing_strategy'],
      ['data_unbalance', 'Determine how unbalanced the data is', 'Data', new Date(2023, 04, 03), new Date(2023, 04, 05), null, 0, null],
      ['metric_determination', 'Determine metric(s) works  for our case of study', 'ML', new Date(2023, 04, 06), new Date(2023, 04, 12), null, 0, 'data_unbalance'],
      ['upmask_implementation', 'Code implementaion of UPMASK ', 'ML', new Date(2023, 02, 27), new Date(2023, 04, 07), null, 20, null],
      ['upmask_training', 'Train UPMASK model', 'ML', new Date(2023, 04, 10), new Date(2023, 04, 21), null, 0, 'upmask_implementation'],
      ['upmask_test', 'Test UPMASK model', 'ML', new Date(2023, 04, 10), new Date(2023, 04, 21), null, 0, 'upmask_implementation'],
      ['upmask_tuning', 'Tune UPMAKS model', 'ML', new Date(2023, 04, 10), new Date(2023, 04, 21), null, 0, 'upmask_implementation'],
      ['upmask_results', 'Analysis of the UPMASK results ', 'ML', new Date(2023, 04, 10), new Date(2023, 04, 21), null, 0, 'upmask_implementation'],
      ['nn_implementation', 'Code implementaion of the NN ', 'ML', new Date(2023, 04, 24), new Date(2023, 05, 12), null, 0, 'metric_determination'],
      ['nn_training', 'Train NN model', 'ML', new Date(2023, 05, 15), new Date(2023, 05, 26), null, 0, 'nn_implementation'],
      ['nn_test', 'Test NN model', 'ML', new Date(2023, 05, 15), new Date(2023, 05, 26), null, 0, 'nn_implementation'],
      ['nn_tuning', 'Tune NN model', 'ML', new Date(2023, 05, 15), new Date(2023, 05, 26), null, 0, 'nn_implementation'],
      ['nn_results', 'Analysis of the NN results ', 'ML', new Date(2023, 05, 15), new Date(2023, 05, 26), null, 0, 'nn_implementation'],
      ['test_other_ml_methods', 'Explore other ML models to compare', 'ML', new Date(2023, 05, 29), new Date(2023, 06, 09), null, 0, null],
      ['results_analysis', 'Analysis of the results', 'Analysis', new Date(2023, 06, 12), new Date(2023, 07, 14), null, 0, null],
"""