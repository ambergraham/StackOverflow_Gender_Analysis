import pandas as pd
import plotly.plotly as py
import plotly.offline as offline
import cufflinks as cf
import plotly.graph_objs as go
cf.set_config_file(offline=False, world_readable=True, theme='pearl')


'''
Location of csv file I am analyzing.
In this case I'm looking at a survey performed by stackoverflow in 2018.
More information about the survey is located at:
https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey
'''
csv_file = 'stack-overflow-2018-developer-survey/survey_results_public.csv'

'''
Columns in the data set that I want to analyze.
Each AssessJob column represents a different question that was asked.
These questions were specifically about looking at potential job opportunities.
People were asked to rate on a scale of 1 - 10 how important certain aspects of
those job opportunities were.

I also included the Gender column so that I could analyze the differences in
responses of men and women.
'''
column_names = ['AssessJob1', 'AssessJob2', 'AssessJob3', 'AssessJob4', 
                'AssessJob5', 'AssessJob6', 'AssessJob7', 'AssessJob8', 
                'AssessJob9', 'AssessJob10', 'Gender']


'''
Labels for the x axes. These are the topics that people were
asked to rate based on importance to them on a scale of 1-10.
'''
x_label1 = 'industry'
x_label2 = 'financial performance of company'
x_label3 = 'team they would work on'
x_label4 = 'compensation and benefits'
x_label5 = 'languages and technology'
x_label6 = 'office environment and culture'
x_label7 = 'opportunity to work at home'
x_label8 = 'opportunity for professional development'
x_label9 = 'diversity of company'
x_label10 = 'impact/usage of product or service'


#This data frame contains only the columns specified in column_names
df = pd.read_csv(csv_file,  usecols = column_names, na_values="NA", dtype = object)

'''
Replaces 'Female' reponses in the Gender column with a 1, and 'Male'
responses in the Gender column with a 0. This will be neccessary if 
I ever want to explore doing some sort of scatter plot with gender as
one of the axes. But for the box plot it is unneccessary.
'''
df['Gender'].replace(['Female','Male'],[1,0],inplace=True)

'''
Seperates the data frame into two data frames: one for women and 
one for men.
'''
df_Women = df[df['Gender'] == 1]
df_Men = df[df['Gender'] == 0]


'''
In order to group the data correctly, I needed arrays of all of the 
xaxis labels repeated the number of times that there is data in the column
that it is associated with.

This is different for each column and for men and women because we don't know
if there were participants that didn't fill out certain questions, or left it
as NA.
'''
AJ1_M = [x_label1] * df_Men[column_names[0]].count()
AJ2_M = [x_label2] * df_Men[column_names[1]].count()
AJ3_M = [x_label3] * df_Men[column_names[2]].count()
AJ4_M = [x_label4] * df_Men[column_names[3]].count()
AJ5_M = [x_label5] * df_Men[column_names[4]].count()
AJ6_M = [x_label6] * df_Men[column_names[5]].count()
AJ7_M = [x_label7] * df_Men[column_names[6]].count()
AJ8_M = [x_label8] * df_Men[column_names[7]].count()
AJ9_M = [x_label9] * df_Men[column_names[8]].count()
AJ10_M = [x_label10] * df_Men[column_names[9]].count()

AJ1_W = [x_label1] * df_Women[column_names[0]].count()
AJ2_W = [x_label2] * df_Women[column_names[1]].count()
AJ3_W = [x_label3] * df_Women[column_names[2]].count()
AJ4_W = [x_label4] * df_Women[column_names[3]].count()
AJ5_W = [x_label5] * df_Women[column_names[4]].count()
AJ6_W = [x_label6] * df_Women[column_names[5]].count()
AJ7_W = [x_label7] * df_Women[column_names[6]].count()
AJ8_W = [x_label8] * df_Women[column_names[7]].count()
AJ9_W = [x_label9] * df_Women[column_names[8]].count()
AJ10_W = [x_label10] * df_Women[column_names[9]].count()


'''
I have two different traces of box plots for the graph. 
One for women and one for men -- they will be combined 
in the overall graph.

y: answers in the designated columns added together to form one big list,
    all of the values are integers.
x: array of a bunch of xasis labels. Each AJ's length should be equal to the number
    of data in the respective column to ensure that the data gets grouped correctly.
'''
trace0 = go.Box (
        y = df_Women[column_names[0]].tolist() + df_Women[column_names[1]].tolist()
            + df_Women[column_names[2]].tolist() + df_Women[column_names[3]].tolist()
            + df_Women[column_names[4]].tolist() + df_Women[column_names[5]].tolist()
            + df_Women[column_names[6]].tolist() + df_Women[column_names[7]].tolist()
            + df_Women[column_names[8]].tolist() + df_Women[column_names[9]].tolist(),
        x = AJ1_W + AJ2_W + AJ3_W + AJ4_W + AJ5_W + AJ6_W + AJ7_W + AJ8_W + AJ9_W + AJ10_W,
        name = 'Women',
        marker = dict (
            color = 'rgb(214, 12, 140)',
        ),
        boxmean=True
      
    )

trace1 = go.Box(
        y = df_Men[column_names[0]].tolist() + df_Men[column_names[1]].tolist()
            + df_Men[column_names[2]].tolist() + df_Men[column_names[3]].tolist()
            + df_Men[column_names[4]].tolist() + df_Men[column_names[5]].tolist()
            + df_Men[column_names[6]].tolist() + df_Men[column_names[7]].tolist()
            + df_Men[column_names[8]].tolist() + df_Men[column_names[9]].tolist() ,
        x = AJ1_M + AJ2_M + AJ3_M + AJ4_M + AJ5_M + AJ6_M + AJ7_M + AJ8_M + AJ9_M + AJ10_M,
        name = 'Men',
        marker = dict (
            color = 'rgb(0, 128, 128)',
        ) , 
        boxmean=True
    )

data = [trace0, trace1]

'''
layout is how the actual graph will look. This includes titles,
font sizes, fonts, margins, etc.
'''
layout = go.Layout(
    yaxis=dict(
        title='Importance Rating',
        zeroline=False
    ),
    title = 'Stack Overflow Survey -- Importance of Job Opportunity Aspects to Men and Women',
    
    boxmode='group',
    margin = go.Margin(
        t = 100,
        b = 220,
        l = 80,
        r = 220,
        pad = 0
    ),
    font = dict(size = 18)
   
)


fig = go.Figure(data = data, layout = layout)

#Plots the graph on the plot.ly website in the filename specified
#py.iplot(fig, filename = 'stackoverflow-chart1')
offline.plot(fig, filename='stackoverflow-chart1.html')