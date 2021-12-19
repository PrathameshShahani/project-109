import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].to_list()

mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
std_deviation=statistics.stdev(data)

first_std_dev_start,first_std_dev_end=mean-std_deviation,mean+std_deviation
second_std_dev_start,second_std_dev_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_dev_start,third_std_dev_end=mean-(3*std_deviation),mean+(3*std_deviation)

fig=ff.create_distplot([data],["Reading Scores"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines",name="1 standard deviation start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines",name="1 standard deviation end"))

fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines",name="2 standard deviation start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines",name="2 standard deviation end"))

fig.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_start],y=[0,0.17],mode="lines",name="3 standard deviation start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end,third_std_dev_end],y=[0,0.17],mode="lines",name="3 standard deviation end"))

fig.show()

list_within_1_std_dev=[result for result in data if result>first_std_dev_start and result<first_std_dev_end]
list_within_2_std_dev=[result for result in data if result>second_std_dev_start and result<second_std_dev_end]
list_within_3_std_dev=[result for result in data if result>third_std_dev_start and result<third_std_dev_end]

print("mean of the data is {}".format(mean))
print("median of the data is {}".format(median))
print("mode of the data is {}".format(mode))
print("Standard Deviation of data is {}".format(std_deviation))

print("{}% of data lies within one standard deviation".format(len(list_within_1_std_dev)*100.0/len(data)))
print("{}% of data lies within two standard deviation".format(len(list_within_2_std_dev)*100.0/len(data)))
print("{}% of data lies within three standard deviation".format(len(list_within_3_std_dev)*100.0/len(data)))
