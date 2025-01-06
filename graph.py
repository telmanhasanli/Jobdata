import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys



def graph (argv):
    y_var = argv[1]
    province = argv[2]
    y_axis = ''
    statistics = ''
    y_title = ''
    if y_var == 'w':
       y_var = 'Wage'
       y_title = 'Wage'
       y_axis = 'Wage, CA ($)'
       statistics = 'wage'
    elif y_var == 'v':
       y_var = 'Count'
       y_title = 'Job Vacancies'
       y_axis = 'Vacancies (number of jobs available)'
       statistics = 'vacancies'
    else:
       print("Error: invalid input, only acccept w for wage or v for vacancies", file=sys.stdout)
       sys.exit(1)
    dataset_path = f'q4_processed_{statistics}_{province}.csv'
    data = pd.read_csv(dataset_path)

    data['Date'] = pd.to_datetime(data['Date'])

    # Create the line plot using Seaborn
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Date', y=y_var, color='#47DE55')
    plt.title(f'Software Engineering {y_title} in {province.capitalize()}', fontdict={'fontsize': 16, 'fontweight': 'bold'}, pad = 16)
    plt.xlabel('Dates', fontdict={'fontsize': 13, 'fontweight': 'bold'}, labelpad = 14)
    plt.ylabel(f'{y_axis}', fontdict={'fontsize': 13, 'fontweight': 'bold'}, labelpad = 14)
    plt.grid(True) 
    plt.savefig("file.png", dpi = 400)

    #show_ticks = data['Date'][::4]
    #plt.xticks(show_ticks, rotation=30)  
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 3:
      print(f"Usage: graph.py <v/w> <province>", file=sys.stdout)
      sys.exit(1)
    
    graph(sys.argv)