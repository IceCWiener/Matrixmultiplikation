import PySimpleGUI as sg
from utility import Utility
from gauss import Gauss

class GUI:
    def __init__(self) -> None:
        self.util = Utility()
        self.gauss = Gauss()

    def start_gui(self):
        """
        Starts the gui and runs an event-loop that blocks code from executing after this until the gui-window is closed
        """

        column_mat_a = [
            [sg.Text("Matrix A")],
            [sg.Multiline(key="-MATRIXA-", size=(20, 10))]
        ]

        column_mat_b = [
            [sg.Text("Matrix B")],
            [sg.Multiline(key="-MATRIXB-", size=(20, 10))]
        ]

        column_mat_l = [
            [sg.Text("Matrix L")],
            [sg.Multiline(key="-MATRIXL-", size=(20, 10))]
        ]

        column_mat_u = [
            [sg.Text("Matrix R")],
            [sg.Multiline(key="-MATRIXU-", size=(20, 10))]
        ]

        column_mat_lu = [
            [sg.Text("L&R kombiniert")],
            [sg.Multiline(key="-MATRIXLU-", size=(20, 10))]
        ]

        layout_multi = [
            [sg.Text("Matrixmultiplikation")],
            [sg.Text(
                "Geben Sie zwei Matrizen zum Multiplizieren ein, \nz. B. [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")],
            [sg.Column(column_mat_a), sg.VerticalSeparator(),
             sg.Column(column_mat_b)],
            [sg.Button("Multiplizieren")],
            [sg.Text("Ergebnis:")],
            [sg.Multiline(key="-RESULT-", size=(48, 8))]
        ]

        layout_lu_decomposition = [
            [sg.Text("LR-Zerlegung")],
            [sg.Text(
                "Geben Sie eine Matrix zum Zerlegen ein")],
            [sg.Multiline(key="-INPUTLU-", size=(48, 8))],
            [sg.Button("Zerlegen")],
            [sg.Text("Ergebnisse:")],
            [sg.Column(column_mat_l),
             sg.Column(column_mat_u),
             sg.Column(column_mat_lu)]
        ]

        layout = [[sg.Column(layout_multi), sg.VerticalSeparator(color="black"),
                  sg.Column(layout_lu_decomposition)], [sg.Button("Schließen")]]

        # Create the window
        window = sg.Window(
            "Matrixmultiplikation & LR-Zerlegung", layout, resizable=True)

        # Create an event loop
        while True:
            event, values = window.read()
            if event == "Schließen" or event == sg.WIN_CLOSED:
                break

            # Matrixmultiplication
            if event == "Multiplizieren":
                matrix_a = self.util.format_matrix_str_to_list(
                    values["-MATRIXA-"])
                matrix_b = self.util.format_matrix_str_to_list(
                    values["-MATRIXB-"])
                if matrix_a == None or matrix_b == None:
                    break

                if type(matrix_a) == str:
                    result = matrix_a
                elif type(matrix_b) == str:
                    result = matrix_b
                else:
                    result = self.util.get_products(matrix_a, matrix_b)

                window["-RESULT-"].update(
                    self.util.format_matrix_list_to_str(result))

            # LU-Decomposition
            # TODO: Update when decomposition works
            if event == "Zerlegen":
                input = self.util.format_matrix_str_to_list(
                    values["-INPUTLU-"])
                if input == None:
                    break
                try:
                    l_mat, u_mat = self.gauss.lu_decomposition(input)
                    window["-MATRIXL-"].update(
                        self.util.format_matrix_list_to_str(l_mat))
                    window["-MATRIXU-"].update(
                        self.util.format_matrix_list_to_str(u_mat))
                except ValueError:
                    window["-INPUTLU-"].print("\n Falsches Format, bitte neue Matrix eingeben")
        window.close()
