#-------------------------------------------------------------------
# Libraries
#-------------------------------------------------------------------
import tkinter as tk
from tkinter import font
import requests
from PIL import ImageTk, Image

#-------------------------------------------------------------------
# Definitions
#-------------------------------------------------------------------

# Define the dimesions of the GUI
HEIGHT = 398
WIDTH = 460
# Key and URL to access the Weather API (Open Weather Map)
key = '09f181ebaaeb75a6a20a138c3299c403'
url = 'https://api.openweathermap.org/data/2.5/weather'


# Function to format the API response
def response_format(weather):
    try:
        name = weather['name']
        temp = weather['main']['temp']
        desc = weather['weather'][0]['description']
        final_string = 'City: %s \nConditions: %s \nTemperature(°C): %s' % (name, desc, temp)

    except:
        final_string = 'City not found'
    
    return final_string


# Function defining the request and response of the weather API
def Get_Weather(city, key, url):
    params = {'APPID':key, 'q':city, 'units':'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = response_format(weather)
 
#-------------------------------------------------------------------
# GUI Structure
#-------------------------------------------------------------------
    
# Canvas definition 
root = tk.Tk()
canvas = tk.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()

# Setting background image
path = "Background.jpg"
img = ImageTk.PhotoImage(Image.open(path))
background_label = tk.Label(root,image=img)
background_label.place(relwidth=1, relheight=1)

# Defining the frames of the GUI
upper_frame = tk.Frame(root,bg='black')
upper_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
down_frame = tk.Frame(root, bg='black')
down_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

# Defining the entry space for the city's name
entry = tk.Entry(upper_frame)
entry.place(relx=0, relheight=1, relwidth=0.7)

# Defining the search button
button = tk.Button(upper_frame, text="Search", bg='gray', fg= 'black', command= lambda: Get_Weather(entry.get(),key,url))
button.place(relx=0.7, relwidth = 0.3, relheight= 1)

# Defining the label where the weather is shown
label = tk.Label(down_frame, bg='white', fg='black', font=(20))
label.place(relwidth = 1, relheight= 1)

# Infinite loop to run the appication
root.mainloop()