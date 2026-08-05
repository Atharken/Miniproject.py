import sqlite3
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.metrics import dp, sp

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect("gym_data_v2.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            category TEXT NOT NULL,
            is_bodyweight INTEGER DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workout_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            routine_name TEXT DEFAULT 'General',
            exercise_name TEXT DEFAULT '',
            set_number INTEGER NOT NULL,
            weight REAL NOT NULL,
            reps INTEGER NOT NULL
        )
    ''')
    DEFAULT_EXERCISES = [
        ("Pull ups", "Pull", 1), ("Push ups", "Push", 1), ("Alternate crunch", "Core", 1),
        ("Leg raises", "Core", 1), ("Hyper extension", "Legs", 1), ("Lat pulldown wide", "Pull", 0),
        ("Reverse peck deck", "Pull", 0), ("T bar rowing", "Pull", 0), ("Preacher curl", "Pull", 0),
        ("Chin pull down", "Pull", 0), ("Face pull", "Pull", 0), ("Hammer curl", "Pull", 0),
        ("Uwu curl", "Pull", 0), ("Reverse curl", "Pull", 0), ("Incline bench", "Push", 0),
        ("Incline dumbbell", "Push", 0), ("Tricep push down", "Push", 0), ("Shoulder press", "Push", 0),
        ("Lateral raises", "Push", 0), ("Peck deck", "Push", 0), ("Dumbbell overhead extension", "Push", 0),
        ("Lunges", "Legs", 0), ("Leg extension", "Legs", 0), ("Calves", "Legs", 0), ("Standing calves", "Legs", 0)
    ]
    for name, cat, bw in DEFAULT_EXERCISES:
        cursor.execute("INSERT OR IGNORE INTO exercises (name, category, is_bodyweight) VALUES (?, ?, ?)", (name, cat, bw))
    conn.commit()
    conn.close()

init_db()

ROUTINES = {
    "Pull 1": ["Pull ups", "Lat pulldown wide", "Reverse peck deck", "T bar rowing", "Preacher curl"],
    "Push 1": ["Incline bench", "Incline dumbbell", "Tricep push down", "Shoulder press", "Lateral raises", "Peck deck", "Alternate crunch"],
    "Legs": ["Lunges", "Leg extension", "Hyper extension", "Calves", "Standing calves", "Uwu curl", "Reverse curl"],
    "Pull 2": ["Pull ups", "Chin pull down", "T bar rowing", "Face pull", "Hammer curl", "Leg raises"],
    "Push 2": ["Push ups", "Dumbbell overhead extension", "Lateral raises", "Peck deck"]
}

# --- TAB 1: LOG SET ---
class LogTab(BoxLayout):
    def __init__(self, **kwargs):
        super(LogTab, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(10)

        self.add_widget(Label(text="Select Routine:", font_size=sp(18), size_hint_y=None, height=dp(30)))
        self.routine_spinner = Spinner(text='Pull 1', values=list(ROUTINES.keys()), font_size=sp(18), size_hint_y=None, height=dp(50))
        self.routine_spinner.bind(text=self.update_exercises)
        self.add_widget(self.routine_spinner)

        self.add_widget(Label(text="Select Exercise:", font_size=sp(18), size_hint_y=None, height=dp(30)))
        self.exercise_spinner = Spinner(text='Pull ups', values=ROUTINES['Pull 1'], font_size=sp(18), size_hint_y=None, height=dp(50))
        self.add_widget(self.exercise_spinner)

        self.add_widget(Label(text="Weight (kg) [0 for BW]:", font_size=sp(18), size_hint_y=None, height=dp(30)))
        self.weight_input = TextInput(text='0', font_size=sp(20), multiline=False, size_hint_y=None, height=dp(50), input_type='number')
        self.add_widget(self.weight_input)

        self.add_widget(Label(text="Reps:", font_size=sp(18), size_hint_y=None, height=dp(30)))
        self.reps_input = TextInput(text='', font_size=sp(20), multiline=False, size_hint_y=None, height=dp(50), input_type='number')
        self.add_widget(self.reps_input)

        save_btn = Button(text="SAVE SET", background_color=(0.1, 0.7, 0.1, 1), font_size=sp(22), size_hint_y=None, height=dp(60))
        save_btn.bind(on_press=self.save_set)
        self.add_widget(save_btn)
        
        self.add_widget(Widget()) 

    def update_exercises(self, spinner, text):
        if text in ROUTINES:
            self.exercise_spinner.values = ROUTINES[text]
            if ROUTINES[text]:
                self.exercise_spinner.text = ROUTINES[text][0]

    def save_set(self, instance):
        routine = self.routine_spinner.text
        exercise = self.exercise_spinner.text
        weight_str = self.weight_input.text
        reps_str = self.reps_input.text

        if not reps_str.isdigit():
            return 

        conn = sqlite3.connect("gym_data_v2.db")
        cursor = conn.cursor()
        today = datetime.now().strftime("%Y-%m-%d")
        
        cursor.execute("SELECT MAX(set_number) FROM workout_logs WHERE date=? AND exercise_name=?", (today, exercise))
        last_set = cursor.fetchone()[0]
        set_num = (last_set or 0) + 1

        cursor.execute("INSERT INTO workout_logs (date, routine_name, exercise_name, set_number, weight, reps) VALUES (?, ?, ?, ?, ?, ?)",
                       (today, routine, exercise, set_num, float(weight_str), int(reps_str)))
        conn.commit()
        conn.close()

        self.reps_input.text = "" 

# --- TAB 2: ADD EXERCISE ---
class AddTab(BoxLayout):
    def __init__(self, **kwargs):
        super(AddTab, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(10)

        self.add_widget(Label(text="New Exercise Name:", font_size=sp(18), size_hint_y=None, height=dp(30)))
        self.name_input = TextInput(font_size=sp(20), multiline=False, size_hint_y=None, height=dp(50))
        self.add_widget(self.name_input)

        self.add_widget(Label(text="Is it Bodyweight?", font_size=sp(18), size_hint_y=None, height=dp(30)))
        self.bw_spinner = Spinner(text='No', values=['Yes', 'No'], font_size=sp(18), size_hint_y=None, height=dp(50))
        self.add_widget(self.bw_spinner)

        self.add_widget(Label(text="Add to Routine:", font_size=sp(18), size_hint_y=None, height=dp(30)))
        self.routine_spinner = Spinner(text='None', values=['None'] + list(ROUTINES.keys()), font_size=sp(18), size_hint_y=None, height=dp(50))
        self.add_widget(self.routine_spinner)

        save_btn = Button(text="ADD EXERCISE", background_color=(0.2, 0.5, 0.8, 1), font_size=sp(20), size_hint_y=None, height=dp(60))
        save_btn.bind(on_press=self.save_new_ex)
        self.add_widget(save_btn)

        self.add_widget(Widget()) 

    def save_new_ex(self, instance):
        name = self.name_input.text.strip()
        if not name:
            return
            
        is_bw = 1 if self.bw_spinner.text == 'Yes' else 0
        routine = self.routine_spinner.text

        try:
            conn = sqlite3.connect("gym_data_v2.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO exercises (name, category, is_bodyweight) VALUES (?, ?, ?)", (name, "Custom", is_bw))
            conn.commit()
            conn.close()

            if routine != "None":
                ROUTINES[routine].append(name)

            self.name_input.text = ""
        except sqlite3.IntegrityError:
            pass 

# --- TAB 3: HISTORY ---
class HistoryTab(BoxLayout):
    def __init__(self, **kwargs):
        super(HistoryTab, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(10)

        # Create a layout for the two top buttons to sit side-by-side
        btn_layout = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))

        refresh_btn = Button(text="REFRESH", font_size=sp(18), background_color=(0.3, 0.3, 0.3, 1))
        refresh_btn.bind(on_press=self.load_history)
        btn_layout.add_widget(refresh_btn)

        clear_btn = Button(text="CLEAR HISTORY", font_size=sp(18), background_color=(0.8, 0.2, 0.2, 1))
        clear_btn.bind(on_press=self.clear_history)
        btn_layout.add_widget(clear_btn)

        self.add_widget(btn_layout)

        scroll = ScrollView(size_hint=(1, 1))
        self.history_label = Label(text="Press Refresh to load data.", font_size=sp(16), size_hint_y=None, halign='left', valign='top')
        
        self.history_label.bind(width=lambda *x: self.history_label.setter('text_size')(self.history_label, (self.history_label.width, None)),
                                texture_size=lambda *x: self.history_label.setter('height')(self.history_label, self.history_label.texture_size[1]))
        
        scroll.add_widget(self.history_label)
        self.add_widget(scroll)
        self.load_history()

    def load_history(self, *args):
        conn = sqlite3.connect("gym_data_v2.db")
        cursor = conn.cursor()
        cursor.execute('''
            SELECT l.date, l.routine_name, l.exercise_name, l.set_number, l.weight, l.reps, e.is_bodyweight 
            FROM workout_logs l
            LEFT JOIN exercises e ON l.exercise_name = e.name
            ORDER BY l.id DESC LIMIT 30
        ''')
        logs = cursor.fetchall()
        conn.close()

        if not logs:
            self.history_label.text = "No workouts logged yet."
            return

        display_text = ""
        for date, routine, ex, set_num, weight, reps, is_bw in logs:
            weight_str = f"BW + {weight}kg" if is_bw and weight > 0 else ("BW" if is_bw else f"{weight}kg")
            display_text += f"{date} | {ex}\nSet {set_num}: {weight_str} x {reps} reps\n------------------------\n"
            
        self.history_label.text = display_text

    def clear_history(self, instance):
        # This deletes everything from the workout_logs table
        conn = sqlite3.connect("gym_data_v2.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM workout_logs")
        conn.commit()
        conn.close()
        
        self.history_label.text = "History cleared!"

# --- MAIN APP ---
class GymAppMain(TabbedPanel):
    def __init__(self, **kwargs):
        super(GymAppMain, self).__init__(**kwargs)
        self.do_default_tab = False
        self.tab_width = dp(120) 

        tab1 = TabbedPanelItem(text='Log Set')
        tab1.add_widget(LogTab())
        self.add_widget(tab1)

        tab2 = TabbedPanelItem(text='Add Ex')
        tab2.add_widget(AddTab())
        self.add_widget(tab2)
        
        tab3 = TabbedPanelItem(text='History')
        tab3.add_widget(HistoryTab())
        self.add_widget(tab3)

class GymApp(App):
    def build(self):
        return GymAppMain()

if __name__ == '__main__':
    GymApp().run()
