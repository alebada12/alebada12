import requests
import beautifulsoup4
import csv

import tkinter as tk

def data_scraping():
    r_car1 = requests.get('https://www.iihs.org/ratings/vehicle/honda/accord-4-door-sedan/2022')

    soup1 = beautifulsoup4(r_car1.content, 'html.parser')
    ratings_car1 = soup1.find('div', class_='ratings-overview')
    rating_name1 = ratings_car1.find_all('a', href=True)
    rating_grade1 = ratings_car1.find_all('strong')
    model_car1 = soup1.find('h1', class_='head')


    #   Car 2 (2022 Dodge Charger)- Scraping data using Requests and BeautifulSoup
    #   Stores data into 3 lists: Model, Rating Names, Grades

    r_car2 = requests.get('https://www.iihs.org/ratings/vehicle/dodge/charger-4-door-sedan/2022')

    soup2 = BeautifulSoup(r_car2.content, 'html.parser')
    ratings_car2 = soup2.find('div', class_='ratings-overview')
    rating_name2 = ratings_car2.find_all('a', href=True)
    rating_grade2 = ratings_car2.find_all('strong')
    model_car2 = soup2.find('h1', class_='head')


    #   Extracts the text for all elements extracted using .text
    #   Stores the text information into 3 new lists (Model, Rating Names, Grades) for each car

    names_car1 = []
    grades_car1 = []
    car1_model = []

    names_car2 = []
    grades_car2 = []
    car2_model = []


    a = 0
    while a < len(rating_name1):
        names_car1.append(rating_name1[a].text)
        a = a + 1


    b = 0
    while b < len(rating_grade1):
        grades_car1.append(rating_grade1[b].text)
        b = b + 1


    car1_model.append(model_car1.text)


    c = 0
    while c < len(rating_name2):
        names_car2.append(rating_name2[c].text)
        c = c + 1


    d = 0
    while d < len(rating_grade2):
        grades_car2.append(rating_grade2[d].text)
        d = d + 1


    car2_model.append(model_car2.text)


    #   Small overlap front: passenger-side is commonly not tested
    #   Adds it to the list if it is not found along with 'Not Tested' for the grade

    if names_car1[1] != 'Small overlap front: passenger-side':
        names_car1.insert(1, 'Small overlap front: passenger-side')
        grades_car1.insert(1, 'Not Tested')

    if names_car2[1] != 'Small overlap front: passenger-side':
        names_car2.insert(1, 'Small overlap front: passenger-side')
        grades_car2.insert(1, 'Not Tested')


    #   Converts the data into a CSV file

    titles = ['Crashworthiness']
    legend = ['Legend:', 'G = Good', 'A = Acceptable', 'M = Marginal', 'P = Poor']

    with open('Safety Comparison.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(legend)
        filewriter.writerow([titles[0], car1_model[0], car2_model[0]])
        filewriter.writerow([names_car1[0], grades_car1[0], grades_car2[0]])
        filewriter.writerow([names_car1[1], grades_car1[1], grades_car2[1]])
        filewriter.writerow([names_car1[2], grades_car1[2], grades_car2[2]])
        filewriter.writerow([names_car1[3], grades_car1[3], grades_car2[3]])
        filewriter.writerow([names_car1[4], grades_car1[4], grades_car2[4]])
        filewriter.writerow([names_car1[5], grades_car1[5], grades_car2[5]])

urls = []

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.car = {'Toyota': ['Corolla'],
                    'Buick': ["Enclave", "Encore", "Encore GX", "Envision"]}

        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)

        self.variable_a.trace('w', self.update_options)

        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.car.keys())
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, '')

        self.buttonAddComparison = tk.Button(root, text="Add Car", command=lambda:[self.show(), self.url()]).pack()

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
        car_str = 'https://www.iihs.org/ratings/vehicle/' + make + "/" + model + "/2022"
        urls.append(car_str)
        print(urls[0])

    def data_scraping1(self):
        r_car1 = requests.get(str(urls[0]))

        soup1 = BeautifulSoup(r_car1.content, 'html.parser')
        ratings_car1 = soup1.find('div', class_='ratings-overview')
        rating_name1 = ratings_car1.find_all('a', href=True)
        rating_grade1 = ratings_car1.find_all('strong')
        model_car1 = soup1.find('h1', class_='head')

        #   Car 2 (2022 Dodge Charger)- Scraping data using Requests and BeautifulSoup
        #   Stores data into 3 lists: Model, Rating Names, Grades

        r_car2 = requests.get(str(urls[1]))

        soup2 = BeautifulSoup(r_car2.content, 'html.parser')
        ratings_car2 = soup2.find('div', class_='ratings-overview')
        rating_name2 = ratings_car2.find_all('a', href=True)
        rating_grade2 = ratings_car2.find_all('strong')
        model_car2 = soup2.find('h1', class_='head')

        #   Extracts the text for all elements extracted using .text
        #   Stores the text information into 3 new lists (Model, Rating Names, Grades) for each car

        names_car1 = []
        grades_car1 = []
        car1_model = []

        names_car2 = []
        grades_car2 = []
        car2_model = []

        a = 0
        while a < len(rating_name1):
            names_car1.append(rating_name1[a].text)
            a = a + 1

        b = 0
        while b < len(rating_grade1):
            grades_car1.append(rating_grade1[b].text)
            b = b + 1

        car1_model.append(model_car1.text)

        c = 0
        while c < len(rating_name2):
            names_car2.append(rating_name2[c].text)
            c = c + 1

        d = 0
        while d < len(rating_grade2):
            grades_car2.append(rating_grade2[d].text)
            d = d + 1

        car2_model.append(model_car2.text)

        #   Small overlap front: passenger-side is commonly not tested
        #   Adds it to the list if it is not found along with 'Not Tested' for the grade

        if names_car1[1] != 'Small overlap front: passenger-side':
            names_car1.insert(1, 'Small overlap front: passenger-side')
            grades_car1.insert(1, 'Not Tested')

        if names_car2[1] != 'Small overlap front: passenger-side':
            names_car2.insert(1, 'Small overlap front: passenger-side')
            grades_car2.insert(1, 'Not Tested')

        #   Converts the data into a CSV file

        titles = ['Crashworthiness']
        legend = ['Legend:', 'G = Good', 'A = Acceptable', 'M = Marginal', 'P = Poor']

        with open('Safety Comparison.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(legend)
            filewriter.writerow([titles[0], car1_model[0], car2_model[0]])
            filewriter.writerow([names_car1[0], grades_car1[0], grades_car2[0]])
            filewriter.writerow([names_car1[1], grades_car1[1], grades_car2[1]])
            filewriter.writerow([names_car1[2], grades_car1[2], grades_car2[2]])
            filewriter.writerow([names_car1[3], grades_car1[3], grades_car2[3]])
            filewriter.writerow([names_car1[4], grades_car1[4], grades_car2[4]])
            filewriter.writerow([names_car1[5], grades_car1[5], grades_car2[5]])



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()





#   Car 1 (2022 Honda Accord) - Scraping data using Requests and BeautifulSoup
#   Stores data into 3 lists: Model, Rating Names, Grades
