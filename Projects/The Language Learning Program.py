import sqlite3
import tkinter as tk
from tkinter import simpledialog, messagebox

class User:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning Program")
        self.conn = sqlite3.connect('user_database_laraib.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        # Create a Canvas widget
        self.canvas = tk.Canvas(self.root, width=800, height=600, bd=0, highlightthickness=0)
        self.canvas.pack()

        # Draw the first half with a purple color
        self.canvas.create_rectangle(0, 0, 800, 200, fill="#6B3E80", outline='')

        # Display title in the upper half
        self.canvas.create_text(400, 100, text="Language Learning Platform", font=("Georgia", 24), fill="white")

        # Draw the second half with a different shade of purple
        self.canvas.create_rectangle(0, 200, 800, 600, fill="#D8D8FA", outline='')

        # Display menu options in the lower half
        self.input_bar = tk.Entry(self.root, font=("Georgia", 12))
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy, font=("Georgia", 12))

        self.create_widgets()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT,
                email TEXT,
                learnt_languages TEXT,
                learning_languages TEXT,
                lessons_completed_arabic INTEGER,
                lessons_completed_japanese INTEGER,
                lessons_completed_spanish INTEGER,
                lessons_completed_french INTEGER,
                lessons_completed_urdu INTEGER
                
            )
        ''')
        self.conn.commit()
#current_lesson TEXT  -- New column to store the current lesson
    def create_widgets(self):
        menu_options = (
            "1. Create a New User",
            "2. Enroll a user in Language",
            "3. Lessons for enrolled language",
            "4. Completed Language",
            "5. View User Progress in a specific language",
            "6. View Achievements",
            "7. Show All Users",
            "Enter your Choice Number"
        )

        for option_index, option_text in enumerate(menu_options, start=1):
            tk.Label(self.root, text=option_text, bg='#D8D8FA', fg='black', font=("Georgia", 16)).place(x=50, y=250 + (option_index - 1) * 40)

        self.exit_button.place(x=700, y=525)  # Adjusted exit button position
        self.input_bar.place(x=350, y=535)  # Adjusted input bar position
        self.input_bar.bind('<Return>', self.on_return_key)


    def on_return_key(self, event):
        user_input = self.input_bar.get().strip()
        self.input_bar.delete(0, tk.END)  # Clear the entry widget

        if user_input == '8':
            self.root.destroy()
        else:
            self.process_user_choice(user_input)

    def process_user_choice(self, choice):
        if choice == '1':
            self.new_user()
        elif choice == '2':
            username = simpledialog.askstring("Input", "Enter your username:", parent=self.root)
            self.enroll_user(username)
        elif choice == '3':
            username = simpledialog.askstring("Input", "Enter your username:", parent=self.root)
            completed_language = simpledialog.askstring("Input", "Enter the language you are learning:", parent=self.root)
            self.lessons_completed(username, completed_language)
        elif choice == '4':
            username = simpledialog.askstring("Input", "Enter your username:", parent=self.root)
            self._get_completed_languages(username)
        elif choice == '5':
            username = simpledialog.askstring("Input", "Enter your username:", parent=self.root)
            self.user_progress(username)
        elif choice == '6':
            username = simpledialog.askstring("Input", "Enter your username:", parent=self.root)
            self.display_achievements(username)
        elif choice == '7':
            self.show_all_users()
        else:
            messagebox.showerror("Error", "Invalid choice. Please enter a valid option.", parent=self.root)


#from here
    def new_user(self, username=None):
        if username is None:
            username = simpledialog.askstring("Input", "Enter your Username:", parent=self.root)

        if self._user_exists(username):
            messagebox.showinfo("Info", 'User already exists. Log in with your existing account.', parent=self.root)
        else:
        # Use show='*' to display '*' for password input
            password_dialog = PasswordDialog(self.root, "Enter Password")
            password = password_dialog.result
            email = simpledialog.askstring("Input", "Enter your email:", parent=self.root)

            user_data = (
                username,
                password,
                email,
                '', # Empty string for learnt_languages initially
                '',  # Empty string for learning_languages initially
                0,  # lessons_completed_arabic
                0,  # lessons_completed_japanese
                0,  # lessons_completed_spanish
                0,  # lessons_completed_french
                0   # lessons_completed_urdu
            )

            self.cursor.execute('''
                INSERT INTO users 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', user_data)

            self.conn.commit()
            messagebox.showinfo("Info", "User created successfully!")

    def _user_exists(self, username):
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone() is not None

#from here
    def enroll_user(self, username):
        if self._user_exists(username):
            enrolled_language = self._get_enrolled_language_choice()

            # Ask the user for the lesson they want to enroll in
            #enrolled_lesson = simpledialog.askstring("Input", f'In which lesson of {enrolled_language} do you want to enroll?', parent=self.root)

            # Update the current_lesson column in the database
            self.cursor.execute('''
                UPDATE users
                SET learning_languages = ?
                WHERE username = ?
            ''', (enrolled_language, username))

            self.conn.commit()

            messagebox.showinfo("Info", f'You have successfully enrolled into {enrolled_language}!!!')
        else:
            messagebox.showerror("Error", 'User does not exist!')


    def _add_learning_language(self, username, enrolled_language):
        try:
            if self._user_exists(username):
                current_learning_languages = self.user_record(username)['learning_languages']
                current_learning_languages.append(enrolled_language)
                learning_languages_str = ','.join(current_learning_languages)

                self.cursor.execute('''
                    UPDATE users
                    SET learning_languages = ?
                    WHERE username = ?
                ''', (learning_languages_str, username))

                self.conn.commit()
            else:
                raise UserNotFoundException(f'User {username} does not exist!', parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in add learning language: {e}")

    def _get_enrolled_language_choice(self):
        languages = Languages().get_language_choices()
        return simpledialog.askstring("Input", f'In which language do you want to enroll?\nLanguages: \n{languages}\n(Enter their name)', parent=self.root)

# to here

    #from here
    def lessons_completed(self, username, enrolled_language):
        try:
            if self._user_exists(username):
                user_data = self.user_record(username)

                if enrolled_language in user_data['learning_languages']:
                    lessons_completed = user_data['lessons_completed'].get(enrolled_language, 0)

                    if lessons_completed == 0:
                        messagebox.showinfo("Info", 'Welcome to your first lesson!', parent=self.root)

                    self._complete_lessons(username, enrolled_language, lessons_completed)
                else:
                    messagebox.showinfo("Info", f"You are not currently learning {enrolled_language}.", parent=self.root)
            else:
                raise UserNotFoundException(f'User {username} does not exist!', parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in lessons completed: {e}")

    def _complete_lessons(self, username, enrolled_language, starting_lesson):
        messagebox.showinfo("Info", f'Your language learning journey includes 10 lessons.', parent=self.root)

        for i in range(starting_lesson, 10):
            while True:
                stage = simpledialog.askstring("Input", f'This is your Lesson {i+1}. Please enter "DONE" to complete the lesson or "QUIT" to exit lessons: ', parent=self.root)
                stage = stage.strip().upper()

                if stage == 'DONE':
                    messagebox.showinfo("Info", f'Lesson {i+1} completed!', parent=self.root)
                    self._update_lessons_completed(username, enrolled_language)
                    break
                elif stage == 'QUIT':
                    messagebox.showinfo("Info", 'Exiting lessons.', parent=self.root)
                    return
                else:
                    messagebox.showerror("Error", 'Invalid input. Please enter "DONE" or "QUIT".', parent=self.root)

        messagebox.showinfo("Info", f'Congratulations! You have completed all 10 lessons for {enrolled_language}', parent=self.root)
        self._remove_learning_language(username , enrolled_language)

    def _remove_learning_language(self, username, completed_language):
        try:
            user_data = self.user_record(username)
            learning_languages_list = user_data['learning_languages']

            if completed_language in learning_languages_list:
                learning_languages_list.remove(completed_language)

                learning_languages_str = ','.join(learning_languages_list)

                self.cursor.execute('''
                    UPDATE users
                    SET learning_languages = ?
                    WHERE username = ?
                ''', (learning_languages_str, username))

                self.conn.commit()
            else:
                messagebox.showinfo("Info", f"OOPS! You have not completeted learning {completed_language} yet!", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in removing language: {e}")



    def _update_lessons_completed(self, username, enrolled_language):
        try:
            current_lessons_completed = self.user_record(username)['lessons_completed'].get(enrolled_language, 0)
            current_lessons_completed += 1

            column_name = f'lessons_completed_{enrolled_language.lower()}'

            self.cursor.execute(f'''
                UPDATE users
                SET {column_name} = ?
                WHERE username = ?
            ''', (current_lessons_completed, username))

            # Check if all lessons for the language are completed
            if current_lessons_completed == 10:
                self._add_learnt_language(username, enrolled_language)

            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in updating lessons completed: {e}")

    def _add_learnt_language(self, username, completed_language):
        try:
            user_data = self.user_record(username)
            current_learnt_languages = user_data['learnt_languages']

            if completed_language not in current_learnt_languages:
                current_learnt_languages.append(completed_language)
                learnt_languages_str = ','.join(current_learnt_languages)

                self.cursor.execute('''
                    UPDATE users
                    SET learnt_languages = ?
                    WHERE username = ?
                ''', (learnt_languages_str, username))

                self.conn.commit()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in adding learnt language: {e}")

#to here
        #from here
    def _get_completed_languages(self, username):
        try:
            user_data = self.user_record(username)
            return user_data.get('learnt_languages', [])
        except UserNotFoundException as e:
            messagebox.showerror("Error", f"Error: {e}")
            return []



    def user_progress(self, username):
        try:
            if self._user_exists(username):
                user_data = self.user_record(username)  # Using the user_record method that fetches data from the database
                enrolled_languages = user_data.get('learning_languages', [])

                if not enrolled_languages:
                    messagebox.showinfo("Info", f"{username} has not enrolled in any language.", parent=self.root)
                else:
                    for language in enrolled_languages:
                        lessons_completed = user_data['lessons_completed'].get(language, 0)
                        total_lessons = 10
                        points_earned = lessons_completed * 10
                        remaining_lessons = max(0, total_lessons - lessons_completed)
                        remaining_points = max(0, (total_lessons - lessons_completed) * 10)

                        progress_info = (
                            f"Progress for {username} in {language}:\n"
                            f"Lessons Completed: {lessons_completed}/{total_lessons}\n"
                            f"Points Earned: {points_earned}/100\n"
                            f"Remaining Lessons: {remaining_lessons}\n"
                            f"Remaining Points: {remaining_points}\n\n"
                        )
                        messagebox.showinfo("Info", progress_info)
            else:
                raise UserNotFoundException('User does not exist!', parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in user progress: {e}")

    def user_record(self, username):
        try:
            self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            result = self.cursor.fetchone()
            if result:
                return {
                    'username': result[0],
                    'password': result[1],
                    'email': result[2],
                    'learnt_languages': result[3].split(',') if result[3] else [],
                    'learning_languages': result[4].split(',') if result[4] else [],
                    'lessons_completed': {
                        'Arabic': result[5],
                        'Japanese': result[6],
                        'Spanish': result[7],
                        'French': result[8],
                        'Urdu': result[9]
                    }
                }
            else:
                raise UserNotFoundException('User does not exist!', parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in user record: {e}")

    def _calculate_points(self, username):
        try:
            user_data = self.user_record(username)
            total_points = 0
            for language in user_data.get('learning_languages', []):
                lessons_completed = user_data['lessons_completed'].get(language, 0)
                total_points += lessons_completed * 10
            return total_points
        except UserNotFoundException as e:
            messagebox.showerror("Error", f"Error: {e}")

    def _get_enrolled_languages(self, username):
        try:
            user_data = self.user_record(username)
            return user_data.get('learning_languages', [])
        except UserNotFoundException as e:
            messagebox.showerror("Error", f"Error: {e}")
            return []

    def display_achievements(self, username):
        try:
            if self._user_exists(username):
                user_data = self.user_record(username)
                achievements_info = (
                    f"{username}'s Achievements:\n"
                    f"Points: {self._calculate_points(username)}\n"
                    "Completed Lessons:\n"
                )
                for language in self._get_enrolled_languages(username):
                    lessons_completed = user_data['lessons_completed'].get(language, 0)
                    total_lessons = 10
                    points_earned = lessons_completed * 10
                    remaining_lessons = max(0, total_lessons - lessons_completed)
                    remaining_points = max(0, (total_lessons - lessons_completed) * 10)

                    progress_info = (
                        f"\nProgress for {username} in {language}:\n"
                        f"Lessons Completed: {lessons_completed}/{total_lessons}\n"
                        f"Points Earned: {points_earned}/100\n"
                        f"Remaining Lessons: {remaining_lessons}\n"
                        f"Remaining Points: {remaining_points}\n"
                    )
                    achievements_info += progress_info

                messagebox.showinfo("Info", achievements_info, parent=self.root)

            else:
                raise UserNotFoundException('User does not exist!')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in display achievements: {e}")

    def show_all_users(self):
        try:
            self.cursor.execute('SELECT * FROM users')
            all_users = self.cursor.fetchall()

            all_users_info = ""
            for user in all_users:
                # Fetch current_lesson information
                current_lesson = user[-1] if user[-1] else "Not enrolled in any lesson"

                learning_languages_index = self._get_language_index('learning_languages')
                learning_languages = str(user[learning_languages_index]).split(',') if user[learning_languages_index] else []

                learnt_languages = str(user[3]).split(',') if user[3] else []

                user_info = (
                    f"Username: {user[0]}\n"
                    f"Email: {user[2]}\n"
                    f"Learnt Languages: {', '.join(map(str, learnt_languages))}\n"

                    f"Current Lesson: {current_lesson}\n"
                    "Lessons Completed:\n"
                )

                for lang in learning_languages:
                    user_info += f"{lang}: {user[6 + self._get_language_index(str(lang))]}\n"

                user_info += "\n"
                all_users_info += user_info

            messagebox.showinfo("Info", all_users_info)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in show all users: {e}")

    def _get_language_index(self, language):
        # Helper function to get the index of the language in the database columns
        languages_columns = ['Arabic', 'Japanese', 'Spanish', 'French', 'Urdu']
        try:
            return languages_columns.index(language)
        except ValueError:
            return -1


    def __del__(self):
        self.conn.close()
class PasswordDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Password:").grid(row=0)
        self.entry = tk.Entry(master, show='*')
        self.entry.grid(row=0, column=1)
        return self.entry

    def apply(self):
        self.result = self.entry.get()


class Languages:
    def __init__(self):
        self.languages = {1 : 'Arabic',
                          2 : 'Japanese',
                          3 : 'Spanish',
                          4 : 'French',
                          5 : 'Urdu'
                          }
    def get_language(self, language_key):
        return self.languages.get(language_key, 'Unknown Language')

    def get_language_choices(self):
        return "\n".join([f"{key}) {value}" for key, value in self.languages.items()])

# ... (Previous code for the User and Languages classes)

class Achievements:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def update_achievements(self, username, language):
        try:
            if self.user_manager._user_exists(username):
                user_data = self.user_manager.user_record(username)
                lessons_completed = user_data['lessons_completed'].get(language, 0)

                if lessons_completed == 10:
                    self._add_achievement(username, language)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in updating achievements: {e}")

    def _add_achievement(self, username, language):
        try:
            # Implement the logic to add the achievement for the user and language
            pass
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in adding achievement: {e}")


class LessonTracker:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def track_lesson_completion(self, username, language, lesson_number):
        try:
            if self.user_manager._user_exists(username):
                user_data = self.user_manager.user_record(username)

                if language in user_data['learning_languages']:
                    lessons_completed = user_data['lessons_completed'].get(language, 0)

                    if lessons_completed == 0:
                        messagebox.showinfo("Info", 'Welcome to your first lesson!', parent=self.root)

                    self._complete_lesson(username, language, lessons_completed, lesson_number)
                else:
                    messagebox.showinfo("Info", f"You are not currently learning {language}.", parent=self.root)
            else:
                raise UserNotFoundException(f'User {username} does not exist!', parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in tracking lesson completion: {e}", parent=self.root)

    def _complete_lesson(self, username, language, starting_lesson, lesson_number):
        try:
            # Implement the logic to handle lesson completion and update lessons_completed
            pass
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred in completing lesson: {e}")



class UserNotFoundException(Exception):
    pass

def main():
    root = tk.Tk()
    user_manager = User(root)
    root.geometry("800x600")
    user_manager.create_widgets()
    root.mainloop()

if __name__ == "__main__":
    main()

