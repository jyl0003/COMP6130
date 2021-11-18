import sys
import re
import time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget, QProgressBar)
from PyQt5.QtCore import QProcess

from proj2 import Ui_MainWindow
from qt_material import apply_stylesheet

projectName = ""
projectPath = ""
# A regular expression, to extract the % complete.
progress_re = re.compile("Total complete: (\d+)%")



class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        #QProcess variable 
        self.p = None
        self.counter = 0
        
        #Stacked widget
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        
        #stacked widget for effectiveness pages
        self.ui.effectivenessBox.currentTextChanged.connect(self.text_changed)
        
        #Stacked widget for effectiveness run
        self.ui.progressBar.setValue(0)
        
        #back button widget
        self.ui.back_btn.clicked.connect(self.goBack)
        self.ui.back_btn_2.clicked.connect(self.goBack)
        
        
        self.ui.pushButton.clicked.connect(self.generateDataset)
        # self.ui.pushButton_2.clicked.connect(self.showYellow)
        # self.ui.pushButton_3.clicked.connect(self.showRed)
        
    def show(self):
        self.main_win.show()
    
    def text_changed(self, s):
        if (s == "Data-Free Knowledge"):
           # projectPath = 
            self.ui.stackedWidget.setCurrentWidget(self.ui.effectivenessPage)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
            
    def goBack(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        
    def generateDataset(self):
        # self.ui.stackedWidget.setCurrentWidget(self.ui.effRunPage)
        dataset = self.ui.eff_dataset_combobox.currentText()
        print(dataset)
        if (dataset == "MNIST"):
            dataset = "Mnist"
        else:
            dataset = "EMnist"
            
        projectPath = f"FedGen/data/{dataset}/generate_niid_dirichlet.py"
        sampling_ratio = self.ui.ratio_line.text()
        alpha = self.ui.alpha_line.text()
        num_clients = self.ui.client_line.text()
        arguments = [projectPath, "--n_class", "10", "--sampling_ratio", sampling_ratio, "--alpha", alpha, "--n_user", num_clients]
        self.start_process(arguments)
        
    def start_process(self, arguments):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            # self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            # self.arguments = [" /training.py" , "--name" , "mnist" , "--params" , "backdoors101/configs/mnist_params.yaml" , "--commit" , "none"]
            self.p.start("python", arguments)
            
    def runEffectiveness(self):
        projectPath = f"FedGen/main.py"
        arguments = [projectPath, "--dataset", "FedGen/Mnist-alpha0.1-ratio0.5", "--algorithm", "FedGen", "--batch_size", "32", "--num_glob_inter", "10", 
                     "local_epochs", "20", "--num_users", "10", "--lamda", "1", "--learning_rate", "0.01", "--model", "cnn", "--personal_learning_rate",
                     "0.01", "--times", "3"]
        self.start_process(arguments)
    def message(self, s):
        print(s)
        # self.ui.updateLabel.setText(s)
        if(s.find("Starting") != -1):
            self.counter = 0
            self.ui.updateLabel_2.setText(str(self.counter) + "%")
            self.ui.updateLabel.setText("Process started...")
        if (s.find("Reading source dataset.") != -1):
            self.counter = 10
            self.ui.updateLabel_2.setText(str(self.counter) + "%")
            self.ui.updateLabel.setText("Downloading dataset...")
        
        if (s.find("Loading data from storage") != -1):
            self.counter = 25
            self.ui.updateLabel_2.setText(str(self.counter) + "%")
            self.ui.updateLabel.setText("Loading data from storage...")
        
        if (s.find("TRAIN SET") != -1):
            self.counter = 34
            self.ui.updateLabel_2.setText(str(self.counter) + "%")
            self.ui.updateLabel.setText("Rearranged train set...")
        
        if (s.find("TEST SET") != -1):
            self.counter = 43
            self.ui.updateLabel_2.setText(str(self.counter) + "%")
            self.ui.updateLabel.setText("Rearranged Test set...")
        
        if (s.find("processing users...".lower()) != -1):
            self.counter = 63
            self.ui.updateLabel_2.setText(str(self.counter) + "%")
            self.ui.updateLabel.setText("Processing users...")
            
        # if (s.find("training samples for user [".lower()) != -1):
        #     if (self.counter < 90):
        #         self.counter += 1
        #         self.ui.updateLabel_2.setText(str(self.counter) + "%")
        #         self.ui.updateLabel.setText("Processing users...")
        if(s.find("Process finished.") != -1):
            self.counter = 100
            self.ui.updateLabel_2.setText(str(self.counter) + "%")
            self.ui.updateLabel.setText("Finished generating dataset!")
            time.sleep(5)
            self.ui.stackedWidget.setCurrentWidget(self.ui.effectivenessRunSetup)
        # self.text.appendPlainText(s)
        
    # def handle_stderr(self):
    #     data = self.p.readAllStandardError()
    #     stderr = bytes(data).decode("utf8")
    #     # Extract progress if it is in the data.
    #     progress = simple_percent_parser(stderr)
    #     print("TEST: " + str(progress))
    #     if progress:
    #         # self.progress.setValue(progress)
    #         self.ui.updateLabel_2.setText(str(progress) + "%")
    #     self.message(stderr)

    def handle_stdout(self):
        sys.stdout.flush()
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None
        
    # def showRed(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.red)
        
    # def showYellow(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.yello)
        
# def simple_percent_parser(output):
#     """
#     Matches lines using the progress_re regex,
#     returning a single integer for the % progress.
#     """
#     m = progress_re.search(output)
#     if m:
#         pc_complete = m.group(1)
#         return int(pc_complete)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
