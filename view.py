from controller import Controller
from tkinter import *
from tkinter import ttk


class AppWindow():
    def __init__(self, controller: Controller):
        self.controller = controller
        self.window = Tk()
        self.window.title('Hospital System')
        self.childrens = []

    def run(self):
        self.startWindow()
        self.window.mainloop()

    def clear(self):
        for children in self.childrens:
            children.destroy()
        self.childrens = []
    
    def registrationWindow(self):
        self.clear()
        self.window.geometry('300x300')
        label = Label(self.window, text='Регистрация')
        name_sur = Label(self.window, text='ФИО:')
        mail_label = Label(self.window, text='Почта:')
        login = Label(self.window, text = 'Логин:')
        
        login_entry = Entry(self.window)
        mail_entry = Entry(self.window)
        name_sur_entry = Entry(self.window)
        btn = Button(self.window, text='Зарегистрироваться', command = self.mainMenuWindow)
        self.childrens.append(label)
        self.childrens.append(name_sur)
        self.childrens.append(mail_label)
        self.childrens.append(login)
        self.childrens.append(name_sur_entry)        
        self.childrens.append(login_entry)
        self.childrens.append(mail_entry)
        self.childrens.append(btn)

        label.pack()
        name_sur.place(x = 50, y = 50)
        mail_label.place(x = 50 , y = 75)
        login.place(x = 50, y = 100)
        name_sur_entry.place(x =150, y = 50)
        login_entry.place(x =150, y = 100)
        mail_entry.place(x = 150, y = 75)
        btn.place(x = 150, y= 125, anchor = N)

    def mainMenuWindow(self):
        self.clear()
        self.window.geometry('300x400')
        bt1 = Button(self.window, text = 'Поиск', width = 25, height = 4, bg='#729dc5', command= self.Search)
        bt2 = Button(self.window, text = 'Профиль', width = 25, height = 4, bg='#729dc5', command = self.profile_window)
        bt3 = Button(self.window, text = 'Выход', width = 25, height = 4, bg='#729dc5', command = self.window.destroy)
    
        label = Label(text='Меню')

        self.childrens.append(label)
        self.childrens.append(bt1)
        self.childrens.append(bt2)
        self.childrens.append(bt3)

        label.pack()
        bt1.place(x=50, y=70)
        bt2.place(x=50, y=160)
        bt3.place(x=50, y=250)


    def loginWindow(self):
        self.clear()
        self.window.geometry('300x300')
        label = Label(self.window, text='Вход')
        login_label = Label(self.window, text='Логин:')
        password_label = Label(self.window, text='Пароль:')
        login_entry = Entry(self.window)
        password_entry = Entry(self.window)
        btn = Button(self.window, text='Войти', command = self.mainMenuWindow)
        self.childrens.append(label)
        self.childrens.append(login_label)
        self.childrens.append(password_label)
        self.childrens.append(login_entry)
        self.childrens.append(password_entry)
        self.childrens.append(btn)

        label.pack()
        login_label.place(x = 50, y = 50)
        login_entry.place(x = 150, y = 50)
        password_label.place(x = 50, y = 100)
        password_entry.place(x = 150, y = 100)
        btn.place(x = 150, y = 125, anchor = N)

    def startWindow(self):
        self.clear()
        self.window.geometry('300x400')
        bt1 = Button(self.window, text = 'Войти', width = 25, height = 4, bg='#729dc5', command=self.loginWindow)
        bt1.place(x=50, y=70)
        bt2 = Button(self.window, text = 'Регистрация', width = 25, height = 4, bg='#729dc5', command = self.registrationWindow)
        bt2.place(x=50, y=160)
        bt3 = Button(self.window, text = 'Выход', width = 25, height = 4, bg='#729dc5', command = self.window.destroy)
        bt3.place(x=50, y=250)
        self.childrens.append(bt1)
        self.childrens.append(bt2)
        self.childrens.append(bt3)

    def popup_window(self, text):
        win = Toplevel(self.window)
        Label(win, text=text).pack()
        Button(win, text='OK', command = win.destroy).pack()


    def profile_window(self):
        self.clear()
        self.window.geometry('500x300')
        profile = self.controller.model.profile[0]
        label = Label(self.window, text='Профиль')
        name_sur = Label(self.window, text='ФИО: ' + profile.name + ' ' + profile.last_name)
        mail_label = Label(self.window, text='Почта: ' + profile.mail)
        login = Label(self.window, text = 'Логин: ' + profile.login)

        def confirm_delete_window():
            win = Toplevel()
            Label(win, text = 'Точно хотите удалить\n профиль?').place(y = 50, x = 100, anchor = N)
            def delete_ok():
                win.destroy()
                self.startWindow()
            Button(win, text='да', command = delete_ok).place(y = 90, x = 125)
            Button(win, text='нет', command = win.destroy).place(y = 90, x = 55)

        btn = Button(self.window, text='Удалить профиль', command = confirm_delete_window)
        btn1 = Button(self.window, text='Изменить информацию', command = self.EditWindow)
        btn2 = Button(self.window, text='История посещений', command = self.history_of_visit)

        self.childrens.append(label)
        self.childrens.append(name_sur)
        self.childrens.append(mail_label)
        self.childrens.append(login)
        self.childrens.append(btn)
        self.childrens.append(btn1)
        self.childrens.append(btn2)

        label.pack()
        name_sur.place(x = 50, y = 50)
        mail_label.place(x = 50 , y = 75)
        login.place(x = 50, y = 100)
    
        btn.place(x = 50, y= 125)
        btn1.place(x = 175, y = 125)
        btn2.place(x = 345, y = 125)


    def DoctorWindow(self, doctor):
        self.clear()
        self.window.geometry('300x300')
        label = Label(self.window, text='Врач')
        name_sur = Label(self.window, text='ФИО: ' + doctor.name + ' ' + doctor.last_name )
        speciality_label = Label(self.window, text='Специальность: ' + doctor.speciality)
        category = Label(self.window, text = 'Категория:' + doctor.category )
        cabinet = Label(self.window, text = 'Кабинет: ' + str(doctor.room))
        visit_time = Label(self.window, text = 'время приема: ' + str(doctor.reception_time[0]))

        btn = Button(self.window, text='Записаться на приём', command = self.registration_on_appointment)

        self.childrens.append(label)
        self.childrens.append(name_sur)
        self.childrens.append(speciality_label)
        self.childrens.append(category)
        self.childrens.append(cabinet)        
        self.childrens.append(visit_time)
        self.childrens.append(btn)

        label.pack()
        name_sur.place(x = 25, y = 50)
        speciality_label.place(x = 25 , y = 75)
        category.place(x = 25, y = 100)
        cabinet.place(x =25, y = 125)
        visit_time.place(x =25, y = 150)
        btn.place(x = 150, y= 175, anchor = N)



    def Search(self):
        self.clear()
        self.window.geometry('300x300')
        label = Label(self.window, text='Поиск')
        search_info = Label(self.window, text='ФИО/Название')
       
        search = Entry(self.window)
       
        btn = Button(self.window, text='Поиск врача', command = lambda: self.DoctorWindow(self.controller.model.list_doctor[0]))
        btn1 = Button(self.window, text = 'Поиск больницы', command = self.HospitalWindow)
        self.childrens.append(label)
        self.childrens.append(search_info)
        self.childrens.append(search) 
        self.childrens.append(btn)
        self.childrens.append(btn1)

        label.pack()
        search_info.place(x = 50, y = 50)
        search.place(x = 150, y = 50)
        btn.place(x = 50, y = 150)
        btn1.place(x = 150, y = 150)

    def HospitalWindow(self):
        self.clear()
        self.window.geometry('900x500')
        hospital = self.controller.model.list_hospital[0]
        label = Label(self.window, text='Больница')
        name = Label(self.window, text='Название: ' + hospital.name)
        contact = Label(self.window, text='Контакты: ' + hospital.contact_info)
        work_time = Label(self.window, text = 'Время работы:' + hospital.work_time )
        adres = Label(self.window, text = 'Адрес: ' + hospital.adress)
        doctors = Label(self.window, text = 'Врачи')
        def create_table_doctors(hospital):
            columns = ('#1', '#2', '#3', '#4')
            table = ttk.Treeview(show='headings', columns=columns)
            table.heading('#1', text='ФИО')
            table.heading('#2', text='специальность')
            table.heading('#3', text='категория')
            table.heading('#4', text='кабинет')
            ysb = ttk.Scrollbar(orient = VERTICAL, command = table.yview)
            table.configure(yscroll=ysb)
            for doctor in hospital.doctor:
                value = [doctor.name + ' ' + doctor.last_name, doctor.speciality, doctor.category, str(doctor.room)]
                table.insert("", END, values = value)

            def search_doctor(doctor_data):
                for doctor in hospital.doctor:
                    if doctor.name + ' ' + doctor.last_name == doctor_data[0] and doctor.speciality == doctor_data[1] and doctor.category == doctor_data[2] and str(doctor.room) == doctor_data[3]:
                        return doctor
                    return hospital.doctor[0]
            
            def item_selected(event):
                for selected_item in table.selection():
                    item = table.item(selected_item)
                    info = item['values']
                    self.DoctorWindow(search_doctor(info))

            table.bind('<<TreeviewSelect>>', item_selected)
            return table

        doctors_table = create_table_doctors(hospital)

        self.childrens.append(label)
        self.childrens.append(name)
        self.childrens.append(contact)
        self.childrens.append(work_time)
        self.childrens.append(adres)        
        self.childrens.append(doctors_table)
        self.childrens.append(doctors)

        label.pack()
        name.place(x = 25, y = 50)
        contact.place(x = 25 , y = 75)
        work_time.place(x = 25, y = 100)
        adres.place(x =25, y = 125)
        doctors.place(x=25,y = 150 )
        doctors_table.place(x = 25, y = 175)

    def registration_on_appointment(self):
        self.clear()
        self.window.geometry('300x300')
        label = Label(self.window, text='Запись на приём')
        name_sur_label = Label(self.window, text='ФИО:')
        day_label = Label(self.window, text='Дата:')
        day_entry =Entry(self.window) 
        name_sur_entry = Entry(self.window)
        time = Label(self.window, text ='Время: ')
        time_entry = Entry(self.window)
        btn = Button(self.window, text='Записаться на приём', command = self.mainMenuWindow)
        self.childrens.append(label)
        self.childrens.append(name_sur_label)
        self.childrens.append(name_sur_entry)
        self.childrens.append(day_label)
        self.childrens.append(day_entry)
        self.childrens.append(time)
        self.childrens.append(time_entry)
        self.childrens.append(btn)

        label.pack()
        name_sur_label.place(x = 50, y = 50)
        name_sur_entry.place(x = 150, y = 50)
        day_label.place(x = 50, y = 75)
        day_entry.place(x = 150, y = 75)
        time.place(x = 50, y = 100)
        time_entry.place(x = 150, y = 100)
        btn.place(x = 170, y = 125, anchor = N)


    def history_of_visit(self):
        self.clear()
        self.window.geometry('900x400')
        label = Label(self.window, text='История посещений')
        visit = Label(self.window, text = 'Последние приёмы:')
        btn = Button(self.window, text='Профиль', command = self.profile_window)

        def create_table_of_visit():
            columns = ('#1', '#2', '#3', '#4', '#5')
            table = ttk.Treeview(show='headings', columns=columns)
            table.heading('#1', text='ФИО')
            table.heading('#2', text='специальность')
            table.heading('#3', text='категория')
            table.heading('#4', text='кабинет')
            table.heading('#5', text='дата')
    
            doctor = list(self.controller.model.profile[0].history_of_visit.keys())[0]
            reception = list(self.controller.model.profile[0].history_of_visit.values())[0]
        
            ysb = ttk.Scrollbar(orient = VERTICAL, command = table.yview)
            table.configure(yscroll=ysb)
            value = [doctor.name + ' ' + doctor.last_name, doctor.speciality, doctor.category, str(doctor.room), str(reception)]
            table.insert("", END, values = value)

            return table

        visits_table = create_table_of_visit()

        self.childrens.append(visit)
        self.childrens.append(label)
        self.childrens.append(btn)
        self.childrens.append(visits_table)
        label.pack()
        visits_table.pack()
        btn.place(x = 400, y = 300)

    
    def EditWindow(self):
        self.clear()
        self.window.geometry('300x300')
        label = Label(self.window, text='Окно изменений данных')
        name_sur = Label(self.window, text='ФИО:')
        mail_label = Label(self.window, text='Почта:')
        login = Label(self.window, text = 'Логин:')
        
        login_entry = Entry(self.window)
        mail_entry = Entry(self.window)
        name_sur_entry = Entry(self.window)
        btn = Button(self.window, text='Изменить', command = self.profile_window)
        self.childrens.append(label)
        self.childrens.append(name_sur)
        self.childrens.append(mail_label)
        self.childrens.append(login)
        self.childrens.append(name_sur_entry)        
        self.childrens.append(login_entry)
        self.childrens.append(mail_entry)
        self.childrens.append(btn)

        label.pack()
        name_sur.place(x = 50, y = 50)
        mail_label.place(x = 50 , y = 75)
        login.place(x = 50, y = 100)
        name_sur_entry.place(x =150, y = 50)
        login_entry.place(x =150, y = 100)
        mail_entry.place(x = 150, y = 75)
        btn.place(x = 150, y= 125, anchor = N)

