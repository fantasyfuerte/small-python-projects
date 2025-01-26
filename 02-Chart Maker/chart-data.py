import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

method = input("""Want to read a CSV file or create chart from scratch?
1-Read CSV
2-Create from scratch
-----------------------
""")

while True:
    if (method=="1"):
        try:
            file = input("Write file route (without .csv extension):\n")
            df = pd.read_csv(f"{file}.csv")
            print(f"\n\n{df}\n\n")
        except:
            print("Unexpected error. Try again.")
            continue
        des = input("1-Bars chart\n2-Poligonal Chart\n")
        break
    else:
        xvalues = input("List the values of column X separated by a comma (,). The first one should be the column name.\n")
        yvalues = input("List the values of column Y separated by a comma (,). The first one should be the column name.\n")
        xvalues = xvalues.split(",")
        yvalues = yvalues.split(",")
        for i in range(1,len(yvalues)):
            yvalues[i]=int(yvalues[i])
            
        
        df = pd.DataFrame({xvalues[0]:xvalues[1:], yvalues[0]:yvalues[1:]})
        print(f"\n\n{df}\n\n")
        des = input("1-Bars chart\n2-Poligonal Chart\n")
        break

if des == "1":
     sns.barplot(x=df.columns[0],y=df.columns[1],data=df)
else:
     sns.lineplot(x=df.columns[0],y=df.columns[1],data=df)
plt.show()
        
