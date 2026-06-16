# Import required Kivy modules
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class myApp(App):
    def build(self):
        # Create main vertical layout container
        root_widget = BoxLayout(orientation='vertical')

        # Create display label for showing input/output
        output_label = Label(size_hint_y=0.75, font_size=50)

        # Define button symbols in layout order
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')

        # Create grid layout for calculator buttons (4 columns)
        button_grid = GridLayout(cols=4, size_hint_y=2)

        # Add each button symbol to the grid
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))

        # Create Clear button with custom height
        clear_button = Button(text='Clear', size_hint_y=None, height=100)

        # Function to append button text to display label
        def print_button_text(instance):
            output_label.text += instance.text

        # Bind all buttons except the last one (=) to print their text
        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)

        # Function to resize font based on label height
        def resize_label_text(label, new_height):
            label.fontsize = 0.5 * label.height

        # Bind label height change to font resizing
        output_label.bind(height=resize_label_text)

        # Function to evaluate and display the result
        def evaluate_result(instance):
            try:
                # Use eval() to calculate the expression
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                # Handle invalid expressions
                output_label.text = 'Python Syntax error!'

        # Bind the = button (first child of grid) to evaluate function
        button_grid.children[0].bind(on_press=evaluate_result)

        # Function to clear the display
        def clear_label(instance):
            output_label.text = " "

        # Bind clear button to clear function
        clear_button.bind(on_press=clear_label)

        # Add all widgets to the main layout
        root_widget.add_widget(output_label)  # Display at top
        root_widget.add_widget(button_grid)  # Button grid in middle
        root_widget.add_widget(clear_button)  # Clear button at bottom

        return root_widget


# Run the application
myApp().run()
