import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class MyApp(toga.App):
    def startup(self):
        main_box = toga.Box()
        button_box = toga.Box()
        
        text_input = toga.MultilineTextInput()
        saved_text = toga.MultilineTextInput(readonly=True)
        def dbg_value(widget):
            print(text_input.value)
            print(type(text_input.value))
        def clear_text(widget):
            text_input.value = ""
        
        def save_text(widget):
            if saved_text.value =="":
                saved_text.value += f"{text_input.value} "
            else:
                saved_text.value +=f"\n{text_input.value}"
                
        
        clear_button = toga.Button("Очистить", on_press=clear_text)
        save_button = toga.Button("Добавить текст", on_press=save_text)
        
        debug_button = toga.Button("check txt value console",on_press=dbg_value)
        
        button_box.add(debug_button)
        button_box.add(clear_button)
        button_box.add(save_button)
        
        main_box.add(text_input)
        main_box.add(toga.Label("Сохранненый текст"))
        main_box.add(saved_text)
        main_box.add(button_box)
        
        
        main_box.style.update(direction=COLUMN, padding=10, gap=5)
        button_box.style.update(direction=ROW, padding_top=5, gap=5)
        
        text_input.style.update(flex=1, height=100)
        saved_text.style.update(flex=1, height=100)
        clear_button.style.update(width=100)
        save_button.style.update(width=100)
        
        self.main_window = toga.MainWindow()
        self.main_window.content = main_box
        self.main_window.show()
    
    


if __name__ == "__main__":
    app = MyApp("app","eshkere")
    app.main_loop()