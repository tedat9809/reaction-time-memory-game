import random
import time
import tkinter as tk


def generate_sequence(length):
    """Generate a random sequence of digit strings"""
    return [str(random.randint(0, 9)) for _ in range(length)]


def calculate_average(values):
    """Calculate the average of a list of numbers"""
    if not values:
        return 0.0
    return sum(values) / len(values)


def check_memory_answer(user_answer, sequence):
    """Check if the user's typed sequence matches the original sequence"""
    cleaned_answer = user_answer.strip().split()
    return cleaned_answer == sequence


def check_stroop_answer(user_answer, correct_color):
    """Check if the user's answer matches the displayed text color"""
    return user_answer.strip().lower() == correct_color.lower()


class ReactionTimeMemoryGameApp:
    """Run the reaction time, memory, and Stroop task GUI"""

    def __init__(self, root):
        """set up the window, game state, labels etc"""
        self.root = root
        self.root.title("Reaction Time Memory Game")
        self.root.geometry("750x560")
        self.root.resizable(False, False)

        self.reaction_rounds = 3
        self.current_round = 0
        self.reaction_times = []

        self.memory_score = 0
        self.memory_length = 4
        self.current_sequence = []
        self.memory_game_active = False

        self.stroop_score = 0
        self.current_stroop_color = ""
        self.color_words = ["red", "blue", "green", "purple", "orange"]
        self.stroop_time_left = 30
        self.stroop_game_active = False

        self.start_time = None
        self.waiting_for_go = False
        self.ready_for_click = False

        self.title_label = tk.Label(
            self.root,
            text="Reaction Time Memory Game",
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=20)

        self.info_label = tk.Label(
            self.root,
            text=(
                "Welcome to the Reaction Time Memory Game!\n\n"
                "Round 1: Reaction Time\n"
                "Wait for the GO signal, then press SPACE as fast as possible.\n\n"
                "Round 2: Memory Challenge\n"
                "Memorize a number sequence. Each time you get it correct, "
                "the next sequence gets longer. The round ends when you make "
                "a mistake.\n\n"
                "Round 3: Stroop Attention Task\n"
                "Type the COLOR of the word, not the word itself. Try to get "
                "as many correct as possible in 30 seconds."
            ),
            font=("Arial", 13),
            wraplength=680,
            justify="center"
        )
        self.info_label.pack(pady=10)

        self.main_button = tk.Button(
            self.root,
            text="Start Game",
            font=("Arial", 14),
            width=20,
            command=self.start_game
        )
        self.main_button.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 14), width=30)

        self.secondary_button = tk.Button(
            self.root,
            text="Submit",
            font=("Arial", 12),
            width=15,
            command=self.submit_memory_answer
        )

        self.results_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 13),
            wraplength=650,
            justify="center"
        )
        self.results_label.pack(pady=20)

        self.root.bind("<space>", self.handle_space_press)
        self.root.bind("<Return>", self.handle_return_press)

    def clear_input_widgets(self):
        """Hide the text entry box and submit button"""
        self.entry.pack_forget()
        self.secondary_button.pack_forget()

    def start_game(self):
        """Reset all game variables and start the reaction time round"""
        self.current_round = 0
        self.reaction_times = []

        self.memory_score = 0
        self.memory_length = 4
        self.current_sequence = []
        self.memory_game_active = False

        self.stroop_score = 0
        self.current_stroop_color = ""
        self.stroop_time_left = 30
        self.stroop_game_active = False

        self.start_time = None
        self.waiting_for_go = False
        self.ready_for_click = False

        self.main_button.pack_forget()
        self.clear_input_widgets()
        self.results_label.config(text="", fg="black")
        self.start_reaction_round()

    def start_reaction_round(self):
        """Start the next reaction round or move to the memory task"""
        if self.current_round >= self.reaction_rounds:
            self.start_memory_test()
            return

        self.current_round += 1
        self.waiting_for_go = True
        self.ready_for_click = False

        self.info_label.config(
            text=(
                "Round 1: Reaction Time\n\n"
                f"Reaction Round {self.current_round} of {self.reaction_rounds}\n\n"
                "Wait for GO, then press the SPACE BAR as fast as you can."
            )
        )
        self.results_label.config(text="Get ready...", fg="black")

        wait_ms = random.randint(2000, 5000)
        self.root.after(wait_ms, self.show_go_signal)

    def show_go_signal(self):
        """show the GO signal and begin timing the reaction"""
        if not self.waiting_for_go:
            return

        self.ready_for_click = True
        self.start_time = time.perf_counter()
        self.results_label.config(text="GO! Press SPACE now!", fg="black")

    def handle_space_press(self, event):
        """Record the user's reaction time when they press SPACE"""
        if self.ready_for_click and self.start_time is not None:
            end_time = time.perf_counter()
            reaction_time = end_time - self.start_time
            self.reaction_times.append(reaction_time)

            self.waiting_for_go = False
            self.ready_for_click = False
            self.start_time = None

            self.results_label.config(
                text=f"Your reaction time was {reaction_time:.3f} seconds.",
                fg="black"
            )
            self.root.after(1500, self.start_reaction_round)

        elif self.waiting_for_go and not self.ready_for_click:
            self.results_label.config(
                text="Too early! Wait for GO before pressing SPACE.",
                fg="black"
            )

    def start_memory_test(self):
        """show a new memory sequence that gets longer after each correct answer"""
        self.clear_input_widgets()
        self.memory_game_active = True
        self.current_sequence = generate_sequence(self.memory_length)

        self.info_label.config(
            text=(
                "Round 2: Memory Challenge\n\n"
                f"Current sequence length: {self.memory_length}\n"
                "Memorize the sequence below. You will have 3 seconds."
            )
        )
        self.results_label.config(text=" ".join(self.current_sequence), fg="black")

        self.root.after(3000, self.hide_sequence_and_prompt)

    def hide_sequence_and_prompt(self):
        """Hide the sequence and ask the user to type it from memory"""
        self.secondary_button.config(command=self.submit_memory_answer)
        self.results_label.config(text="", fg="black")
        self.info_label.config(
            text=(
                "Enter the sequence exactly as shown before.\n"
                "Separate each number with a space."
            )
        )

        self.entry.delete(0, tk.END)
        self.entry.pack(pady=10)
        self.secondary_button.pack(pady=10)
        self.entry.focus_set()

    def submit_memory_answer(self):
        """Check the memory answer and continue or move to the Stroop task"""
        user_answer = self.entry.get()
        is_correct = check_memory_answer(user_answer, self.current_sequence)

        self.clear_input_widgets()

        if is_correct:
            self.memory_score += 1
            self.memory_length += 1
            self.results_label.config(
                text=(
                    "Correct! The next sequence will be one digit longer.\n"
                    f"Memory score so far: {self.memory_score}"
                ),
                fg="black"
            )
            self.root.after(1500, self.start_memory_test)
        else:
            self.memory_game_active = False
            self.results_label.config(
                text=(
                    "Incorrect. The memory round is over.\n"
                    f"The correct sequence was: {' '.join(self.current_sequence)}\n"
                    f"Final memory score: {self.memory_score}"
                ),
                fg="black"
            )
            self.root.after(2500, self.start_stroop_test)

    def start_stroop_test(self):
        """Start the 30-second Stroop attention task"""
        self.clear_input_widgets()
        self.stroop_score = 0
        self.stroop_time_left = 30
        self.stroop_game_active = True

        self.info_label.config(
            text=(
                "Round 3: Stroop Attention Task\n\n"
                "Type the COLOR of the word, not what the word says.\n"
                "Get as many correct as possible in 30 seconds."
            )
        )

        self.update_stroop_timer()
        self.show_stroop_question()

    def update_stroop_timer(self):
        """update the Stroop countdown timer every second"""
        if not self.stroop_game_active:
            return

        if self.stroop_time_left <= 0:
            self.stroop_game_active = False
            self.show_final_results()
            return

        self.info_label.config(
            text=(
                "Round 3: Stroop Attention Task\n\n"
                f"Time left: {self.stroop_time_left} seconds\n"
                f"Current Stroop score: {self.stroop_score}\n\n"
                "Type the COLOR of the word, not what the word says."
            )
        )

        self.stroop_time_left -= 1
        self.root.after(1000, self.update_stroop_timer)

    def show_stroop_question(self):
        """display a new Stroop word with a mismatched color"""
        if not self.stroop_game_active:
            return

        word = random.choice(self.color_words)
        color = random.choice(self.color_words)

        while color == word:
            color = random.choice(self.color_words)

        self.current_stroop_color = color

        self.results_label.config(text=word.upper(), fg=color)

        self.entry.delete(0, tk.END)
        self.entry.pack(pady=10)
        self.secondary_button.config(command=self.submit_stroop_answer)
        self.secondary_button.pack(pady=10)
        self.entry.focus_set()

    def submit_stroop_answer(self):
        """check the Stroop answer and quickly show the next question"""
        if not self.stroop_game_active:
            return

        user_answer = self.entry.get()

        if check_stroop_answer(user_answer, self.current_stroop_color):
            self.stroop_score += 1
            feedback = "Correct!"
        else:
            feedback = f"Incorrect. Correct color: {self.current_stroop_color}"

        self.results_label.config(text=feedback, fg="black")
        self.root.after(400, self.show_stroop_question)

    def handle_return_press(self, event):
        """submit the active answer when the user presses Enter"""
        if self.entry.winfo_ismapped():
            self.secondary_button.invoke()

    def show_final_results(self):
        """Show the user's final scores for all three tasks"""
        self.clear_input_widgets()

        average_time = calculate_average(self.reaction_times)
        best_time = min(self.reaction_times) if self.reaction_times else 0.0

        self.info_label.config(text="Final Results")
        self.results_label.config(
            text=(
                f"Average reaction time: {average_time:.3f} seconds\n"
                f"Best reaction time: {best_time:.3f} seconds\n"
                f"Memory score: {self.memory_score} correct sequences\n"
                f"Longest sequence attempted: {self.memory_length} digits\n"
                f"Stroop score: {self.stroop_score} correct in 30 seconds\n\n"
                "Great job! You completed the reaction time, memory, "
                "and attention tasks."
            ),
            fg="black"
        )

        self.main_button.config(text="Play Again", command=self.start_game)
        self.main_button.pack(pady=20)


def main():
    """create the Tkinter window and run the game"""
    root = tk.Tk()
    app = ReactionTimeMemoryGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()