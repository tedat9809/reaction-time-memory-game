import random
import time
import tkinter as tk


def generate_sequence(length):
    """
    Generate a random sequence of digit strings for the memory test.

    Args:
        length (int): Number of digits to generate.

    Returns:
        list[str]: A list of random digit strings.
    """
    return [str(random.randint(0, 9)) for _ in range(length)]


def calculate_average(values):
    """
    Calculate the average of a list of numeric values.

    Args:
        values (list[float]): A list of numbers.

    Returns:
        float: The average value, or 0 if the list is empty.
    """
    if not values:
        return 0.0
    return sum(values) / len(values)


def check_memory_answer(user_answer, sequence):
    """
    Check whether the user's memory response matches the target sequence.

    Args:
        user_answer (str): The user's typed answer.
        sequence (list[str]): The original sequence.

    Returns:
        bool: True if correct, otherwise False.
    """
    cleaned_answer = user_answer.strip().split()
    return cleaned_answer == sequence


class ReactionTimeMemoryGameApp:
    """
    GUI application for a reaction time and short-term memory game.
    """

    def __init__(self, root):
        """
        Initialize the application window and game state.

        Args:
            root (tk.Tk): Main Tkinter window.
        """
        self.root = root
        self.root.title("Reaction Time Memory Game")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.reaction_rounds = 3
        self.current_round = 0
        self.reaction_times = []
        self.memory_score = 0
        self.memory_length = 5
        self.current_sequence = []
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
            text="Test your reaction speed and short-term memory.",
            font=("Arial", 14),
            wraplength=600,
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
            wraplength=600,
            justify="center"
        )
        self.results_label.pack(pady=20)

        self.root.bind("<space>", self.handle_space_press)
        self.root.bind("<Return>", self.handle_return_press)

    def clear_input_widgets(self):
        """
        Hide input widgets used during the memory task.
        """
        self.entry.pack_forget()
        self.secondary_button.pack_forget()

    def start_game(self):
        """
        Reset state and begin the reaction time portion of the game.
        """
        self.current_round = 0
        self.reaction_times = []
        self.memory_score = 0
        self.current_sequence = []
        self.start_time = None
        self.waiting_for_go = False
        self.ready_for_click = False

        self.main_button.pack_forget()
        self.clear_input_widgets()
        self.results_label.config(text="")
        self.start_reaction_round()

    def start_reaction_round(self):
        """
        Start a new reaction-time round or move to the memory task.
        """
        if self.current_round >= self.reaction_rounds:
            self.start_memory_test()
            return

        self.current_round += 1
        self.waiting_for_go = True
        self.ready_for_click = False

        self.info_label.config(
            text=(
                f"Reaction Round {self.current_round} of {self.reaction_rounds}\n\n"
                "Wait for GO, then press the SPACE BAR as fast as you can."
            )
        )
        self.results_label.config(text="Get ready...")

        wait_ms = random.randint(2000, 5000)
        self.root.after(wait_ms, self.show_go_signal)

    def show_go_signal(self):
        """
        Display the GO signal and start reaction timing.
        """
        if not self.waiting_for_go:
            return

        self.ready_for_click = True
        self.start_time = time.perf_counter()
        self.results_label.config(text="GO! Press SPACE now!")

    def handle_space_press(self, event):
        """
        Handle the user's SPACE BAR press during reaction rounds.

        Args:
            event: Tkinter event object.
        """
        if self.ready_for_click and self.start_time is not None:
            end_time = time.perf_counter()
            reaction_time = end_time - self.start_time
            self.reaction_times.append(reaction_time)

            self.waiting_for_go = False
            self.ready_for_click = False
            self.start_time = None

            self.results_label.config(
                text=f"Your reaction time was {reaction_time:.3f} seconds."
            )
            self.root.after(1500, self.start_reaction_round)

        elif self.waiting_for_go and not self.ready_for_click:
            self.results_label.config(
                text="Too early! Wait for GO before pressing SPACE."
            )

    def start_memory_test(self):
        """
        Begin the memory task by showing a number sequence.
        """
        self.clear_input_widgets()
        self.current_sequence = generate_sequence(self.memory_length)

        self.info_label.config(
            text=(
                "Memory Test\n\n"
                "Memorize the sequence below. You will have 3 seconds."
            )
        )
        self.results_label.config(text=" ".join(self.current_sequence))

        self.root.after(3000, self.hide_sequence_and_prompt)

    def hide_sequence_and_prompt(self):
        """
        Hide the memory sequence and prompt the user to enter it.
        """
        self.results_label.config(text="")
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
        """
        Check the user's memory answer and move to the results screen.
        """
        user_answer = self.entry.get()
        is_correct = check_memory_answer(user_answer, self.current_sequence)

        if is_correct:
            self.memory_score = 1
            memory_feedback = "Correct! You remembered the sequence."
        else:
            self.memory_score = 0
            memory_feedback = (
                "Incorrect.\n"
                f"The correct sequence was: {' '.join(self.current_sequence)}"
            )

        self.show_final_results(memory_feedback)

    def handle_return_press(self, event):
        """
        Submit the memory answer when Enter is pressed.

        Args:
            event: Tkinter event object.
        """
        if self.entry.winfo_ismapped():
            self.submit_memory_answer()

    def show_final_results(self, memory_feedback):
        """
        Display the user's final results.

        Args:
            memory_feedback (str): Feedback from the memory task.
        """
        self.clear_input_widgets()

        average_time = calculate_average(self.reaction_times)
        best_time = min(self.reaction_times) if self.reaction_times else 0.0

        self.info_label.config(text="Final Results")
        self.results_label.config(
            text=(
                f"Average reaction time: {average_time:.3f} seconds\n"
                f"Best reaction time: {best_time:.3f} seconds\n"
                f"Memory score: {self.memory_score}\n\n"
                f"{memory_feedback}"
            )
        )

        self.main_button.config(text="Play Again", command=self.start_game)
        self.main_button.pack(pady=20)


def main():
    """
    Create the application window and run the game.
    """
    root = tk.Tk()
    app = ReactionTimeMemoryGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()