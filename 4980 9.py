# I would say that the most useful thing I learned from this course was data scraping.
# My understanding of data scraping is still elementary level.
# It's part of my group and individual project. If I can fully complete my individual project
# then my buddy and I will quite literally use it weekly to make our budgeting process easier.
# At this point, I haven't really got much done in terms of code for my individual project
# since the group project was a higher priority.

# I'm going to submit the group project code and hope that it counts.

# If it doesn't, I will add something else that I learned.


import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk

urls = []


class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.car = {
            'Buick': ['LaCrosse', 'Park-Avenue'],
            'Chevrolet': ['Impala', 'Malibu', 'Sonic', 'Volt'],
            'Dodge': ['Avenger', 'Charger', 'Dart'],
            'Ford': ['Fiesta', 'Fusion', 'Focus'],
            'Honda': ['Accord', 'Civic', 'Insight'],
            'Subaru': ['Impreza', 'Legacy', 'WRX'],
            'Tesla': ['Model-3'],
            'Toyota': ['Avalon', 'Camry', 'Corolla'],
        }

        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)

        self.variable_a.trace('w', self.update_options)

        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.car.keys())
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, '')

        self.buttonAddComparison = tk.Button(root, text="Add Car", command=lambda: [self.show(), self.url()]).pack()

        self.buttonSave = tk.Button(root, text="Save CSV", command=self.data_scraping1).pack()

        self.variable_a.set('')

        self.optionmenu_a.pack()
        self.optionmenu_b.pack()
        self.pack()

    def update_options(self, *args):
        cars = self.car[self.variable_a.get()]
        self.variable_b.set(cars[0])

        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')

        for acar in cars:
            menu.add_command(label=acar, command=lambda make=acar: self.variable_b.set(make))

    def show(self):
        labelFrame = tk.LabelFrame(root, text="Cars", padx=10, pady=10)
        labelFrame.pack(padx=10, pady=10)
        tk.Label(labelFrame, text=self.variable_a.get()).pack()
        tk.Label(labelFrame, text=self.variable_b.get()).pack()

    def url(self):
        make = self.variable_a.get()
        model = self.variable_b.get() + '-4-door-sedan'
        car_str = 'https://www.iihs.org/ratings/vehicle/' + make + "/" + model
        urls.append(car_str)
        print(urls[0])

    def data_scraping1(self):

        print('Exporting ...')

        names_car1 = []
        grades_car1 = []
        car1_model = []

        names_car2 = []
        grades_car2 = []
        car2_model = []

        names_car3 = []
        grades_car3 = []
        car3_model = []

        names_car4 = []
        grades_car4 = []
        car4_model = []
        #   Car 1 - Scraping data using Requests and BeautifulSoup
        #   Stores data into 3 lists: Model, Rating Names, Grades

        try:
            r_car1 = requests.get(str(urls[0]))

            soup1 = BeautifulSoup(r_car1.content, 'html.parser')
            ratings_car1 = soup1.find('div', class_='ratings-overview')
            rating_name1 = ratings_car1.find_all('a', href=True)
            rating_grade1 = ratings_car1.find_all('strong')
            model_car1 = soup1.find('h1', class_='head')

            a = 0
            while a < len(rating_name1):
                names_car1.append(rating_name1[a].text)
                a = a + 1

            b = 0
            while b < len(rating_grade1):
                grades_car1.append(rating_grade1[b].text)
                b = b + 1

            car1_model.append(model_car1.text)

            if names_car1[1] != 'Small overlap front: passenger-side':
                names_car1.insert(1, 'Small overlap front: passenger-side')
                grades_car1.insert(1, 'Not Tested')
        except:
            pass

        #   Car 2 - Scraping data using Requests and BeautifulSoup
        #   Stores data into 3 lists: Model, Rating Names, Grades

        try:
            r_car2 = requests.get(str(urls[1]))

            soup2 = BeautifulSoup(r_car2.content, 'html.parser')
            ratings_car2 = soup2.find('div', class_='ratings-overview')
            rating_name2 = ratings_car2.find_all('a', href=True)
            rating_grade2 = ratings_car2.find_all('strong')
            model_car2 = soup2.find('h1', class_='head')

            c = 0
            while c < len(rating_name2):
                names_car2.append(rating_name2[c].text)
                c = c + 1

            d = 0
            while d < len(rating_grade2):
                grades_car2.append(rating_grade2[d].text)
                d = d + 1

            car2_model.append(model_car2.text)

            if names_car2[1] != 'Small overlap front: passenger-side':
                names_car2.insert(1, 'Small overlap front: passenger-side')
                grades_car2.insert(1, 'Not Tested')
        except:
            pass

        #   Car 3 - Scraping data using Requests and BeautifulSoup
        #   Stores data into 3 lists: Model, Rating Names, Grades

        try:
            r_car3 = requests.get(str(urls[2]))

            soup3 = BeautifulSoup(r_car3.content, 'html.parser')
            ratings_car3 = soup3.find('div', class_='ratings-overview')
            rating_name3 = ratings_car3.find_all('a', href=True)
            rating_grade3 = ratings_car3.find_all('strong')
            model_car3 = soup3.find('h1', class_='head')

            a1 = 0
            while a1 < len(rating_name3):
                names_car3.append(rating_name3[a1].text)
                a1 = a1 + 1

            b1 = 0
            while b1 < len(rating_grade3):
                grades_car3.append(rating_grade3[b1].text)
                b1 = b1 + 1

            car3_model.append(model_car3.text)

            if names_car3[1] != 'Small overlap front: passenger-side':
                names_car3.insert(1, 'Small overlap front: passenger-side')
                grades_car3.insert(1, 'Not Tested')
        except:
            pass

        try:
            r_car4 = requests.get(str(urls[3]))

            soup4 = BeautifulSoup(r_car4.content, 'html.parser')
            ratings_car4 = soup4.find('div', class_='ratings-overview')
            rating_name4 = ratings_car4.find_all('a', href=True)
            rating_grade4 = ratings_car4.find_all('strong')
            model_car4 = soup4.find('h1', class_='head')

            c1 = 0
            while c1 < len(rating_name4):
                names_car4.append(rating_name4[c1].text)
                c1 = c1 + 1

            d1 = 0
            while d1 < len(rating_grade4):
                grades_car4.append(rating_grade4[d1].text)
                d1 = d1 + 1

            car4_model.append(model_car4.text)

            if names_car4[1] != 'Small overlap front: passenger-side':
                names_car4.insert(1, 'Small overlap front: passenger-side')
                grades_car4.insert(1, 'Not Tested')
        except:
            pass

        range1 = len(names_car1)
        while len(names_car1) < 6:
            names_car1.append('')
            grades_car1.append('')
            car1_model.append('')
            range1 = len(names_car1)

        range2 = len(names_car2)
        while len(names_car2) < 6:
            names_car2.append('')
            grades_car2.append('')
            car2_model.append('')
            range2 = len(names_car2)

        range3 = len(names_car3)
        while len(names_car3) < 6:
            names_car3.append('')
            grades_car3.append('')
            car3_model.append('')
            range3 = len(names_car3)

        range4 = len(names_car4)
        while len(names_car4) < 6:
            names_car4.append('')
            grades_car4.append('')
            car4_model.append('')
            range4 = len(names_car4)

        #   Converts the data into a CSV file

        titles = ['Crashworthiness']
        legend = ['Legend:', 'G = Good', 'A = Acceptable', 'M = Marginal', 'P = Poor']

        with open('Safety Comparison.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(legend)
            filewriter.writerow([titles[0], car1_model[0], car2_model[0], car3_model[0], car4_model[0]])
            filewriter.writerow([names_car1[0], grades_car1[0], grades_car2[0], grades_car3[0], grades_car4[0]])
            filewriter.writerow([names_car1[1], grades_car1[1], grades_car2[1], grades_car3[1], grades_car4[1]])
            filewriter.writerow([names_car1[2], grades_car1[2], grades_car2[2], grades_car3[2], grades_car4[2]])
            filewriter.writerow([names_car1[3], grades_car1[3], grades_car2[3], grades_car3[3], grades_car4[3]])
            filewriter.writerow([names_car1[4], grades_car1[4], grades_car2[4], grades_car3[4], grades_car4[4]])
            filewriter.writerow([names_car1[5], grades_car1[5], grades_car2[5], grades_car3[5], grades_car4[5]])


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()

#   Car 1 (2022 Honda Accord) - Scraping data using Requests and BeautifulSoup
#   Stores data into 3 lists: Model, Rating Names, Grades

# Regardless! Another useful thing I learned from this class was just general knowledge of python.
# I took a Matlab course and Python seems night & day way easier to pick up and use.

# In terms of specific lectures/lessons, Lecture 14 and 15 where you talked about GUI & API more specifically.

# Another topic I learned that will be useful to me in the near future is the ability to move files from
# one directory to another.
# Once my individual project is complete I will use this to move those newly created csv files into a specific
# location so I'm not getting clutter everytime I run the program.

f = os.path.join('/home/anthonylebada/Downloads', 'Default.txt')
f2 = os.path.join('/home/anthonylebada/Downloads', 'NewDefault.txt')
# rename(first file, second file)
os.rename(f, f2)
# new location path
newlocation = '/home/anthonylebada/Desktop'
# shutil module that move file location
mover = shutil.move(f2, newlocation)
print("NewDefault.txt moved from /Downloads to:", mover)

