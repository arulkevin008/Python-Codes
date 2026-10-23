import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

print("\n========== MATPLOTLIB PLOT MENU ==========")
print(" Line Plot - 1")
print(" Scatter Plot - 2")
print(" Bar Chart - 3")
print(" Histogram - 4")
print(" Pie Chart - 5")
print(" Box Plot - 6")
print(" Contour Plot - 7")
print(" Density Plot - 8")

plot_type = int(input("\nEnter Plot plot_type: "))

if plot_type not in range(1, 9):
    print("Invalid plot_type")
    exit()

title = input("Enter Plot Title: ")

if plot_type != 5:
    grid = input("Enable Grid (y/n): ").lower()

if plot_type not in [5, 7]:
    xlabel = input("Enter X-axis Label: ")
    ylabel = input("Enter Y-axis Label: ")

if plot_type == 1:

    x = np.array(input("Enter X values: ").split(), dtype=float)
    y = np.array(input("Enter Y values: ").split(), dtype=float)

    color = input("Line Color: ")
    linestyle = input("Line Style: ")
    marker = input("Marker: ")
    width = float(input("Line Width: "))

    plt.plot(x, y,color=color,linestyle=linestyle,marker=marker,linewidth=width)

elif plot_type == 2:

    x = np.array(input("Enter X values: ").split(), dtype=float)
    y = np.array(input("Enter Y values: ").split(), dtype=float)

    color = input("Marker Color: ")
    size = int(input("Marker Size: "))

    plt.scatter(x,y,color=color,s=size)

elif plot_type == 3:

    x = np.array(input("Enter X values: ").split())
    y = np.array(input("Enter Y values: ").split(), dtype=float)

    color = input("Bar Color: ")
    edge = input("Edge Color: ")
    width = float(input("Bar Width: "))

    orientation = input("Vertical or Horizontal (v/h): ").lower()

    if orientation == "v":
        plt.bar(x,y,color=color,edgecolor=edge,width=width)
    else:
        plt.barh(x,y,color=color,edgecolor=edge,height=width)

elif plot_type == 4:

    x = np.array(input("Enter Values: ").split(), dtype=float)

    color = input("Bar Color: ")
    edge = input("Edge Color: ")
    bins = int(input("Number of Bins: "))

    plt.hist(x,bins=bins,color=color,edgecolor=edge)

elif plot_type == 5:

    values = np.array(input("Enter Values: ").split(), dtype=float)
    labels = input("Enter Labels: ").split()

    radius = float(input("Radius: "))
    explode = list(map(float, input("Explode Values: ").split()))

    shadow = input("Shadow (y/n): ").lower() == "y"

    plt.pie(values,labels=labels,explode=explode,shadow=shadow,radius=radius,autopct="%1.1f%%")

elif plot_type == 6:

    values = np.array(input("Enter Values: ").split(), dtype=float)

    width = float(input("Box Width: "))
    orientation = input("Vertical or Horizontal (v/h): ").lower()
    notch = input("Notched Box (y/n): ").lower() == "y"

    if orientation == "v":
        plt.boxplot(values,widths=width,notch=notch,vert=True)
    else:
        plt.boxplot(values,widths=width,notch=notch,vert=False)

elif plot_type == 7:

    rows = int(input("Number of Rows: "))
    cols = int(input("Number of Columns: "))

    print("Enter Z Matrix:")

    z = []

    for i in range(rows):
        row = list(map(float, input().split()))
        z.append(row)

    z = np.array(z)

    levels = int(input("Contour Levels: "))
    cmap = input("Colormap (viridis/plasma/jet/inferno): ")

    filled = input("Filled Contour (y/n): ").lower()

    if filled == "y":
        cp = plt.contourf(z,levels=levels,cmap=cmap)
    else:
        cp = plt.contour(z,levels=levels,cmap=cmap)

        labels = input("Show Contour Labels (y/n): ").lower()

        if labels == "y":
            plt.clabel(cp,inline=True,fontsize=10)

    if input("Show Colorbar (y/n): ").lower() == "y":
        plt.colorbar(cp)

elif plot_type == 8:

    values = np.array(input("Enter Values: ").split(), dtype=float)

    color = input("Plot Color: ")
    fill = input("Fill Curve (y/n): ").lower() == "y"
    width = float(input("Line Width: "))

    sns.kdeplot(values,color=color,fill=fill,linewidth=width)

plt.title(title, fontsize=16)

if plot_type not in [5, 7]:
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

if plot_type != 5 and grid == "y":
    plt.grid()

plt.show()
