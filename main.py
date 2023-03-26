import tkinter as tk
from PIL import Image,ImageTk 
import requests
root = tk.Tk()

root.title("WEATHER APP")
root.geometry("600x500")


def format_response(weather):
    try:
        city = weather['name']
        Country= weather['sys']['country']
        Condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        Humidity= weather['main']['humidity']

        final_str ='City       :%s\nCountry  :%s\nCondition:%s\nTemp     :%s\nHumidity :%s'%(city,Country,Condition,(temp-32)*5//9,Humidity)
    except:
        final_str = "NETWORK ERROR"

    return final_str        

def get_weather(City):
        

    weather_key ='33f5d7bf66405197484c1dc7fa72ae99'
    url ='https://api.openweathermap.org/data/2.5/weather'
    
    params={'APPID':weather_key,'q':City,'units':'imperial'}
    response=requests.get(url,params)
    #print(response.json())

    weather = response.json()
    # print("City     :",weather['name'])
    # print("Country  :",weather['sys']['country'])
    # print("Weather  :",weather['weather'][0]['description'])
    # print("Temp     :",weather['main']['temp'])
    # print("Humidity :",weather['main']['humidity'])

    result['text']= format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon_name):
    size = int(frame_two.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon_name+'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img 





img= Image.open('./bg1.jpeg')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title = tk.Label(bg_lbl,text='Weather Report of 100,000 cities!',fg='#fdfdfd',bg='#81869a',font=('times new roman',16,'bold'))
heading_title.place(x=150,y=18)

frame_one = tk.Frame(bg_lbl,bg='#8d90a1',bd=5)
frame_one.place(x=80,y=60,width=450,height=50) 

txt_box= tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky= 'w')

btn=tk.Button(frame_one,text='Search',fg='#f3812f',font=('times new roman',16,'bold'),command= lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=40)

frame_two = tk.Frame(bg_lbl,bd=5)
frame_two.place(x=80,y=130,width=450,height=300) 

result = tk.Label(frame_two,font=40,bg='#abf2f7',justify='left',anchor='nw' )
result.place(relwidth=1,relheight=1)

weather_icon = tk.Canvas(result,bg='#abf2f7',bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)

root.mainloop()