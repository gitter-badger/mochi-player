'''
IPythonWidget gives us an interactive debugging console.
 Re-purposed from: https://github.com/jupyter/qtconsole/blob/master/examples/inprocess_qtconsole.py
'''

from PyQt5.Qt import QApplication
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager


class IPythonWidget(RichJupyterWidget):
    ''' Convenience class for a live IPython console widget. We can replace the standard banner using the customBanner argument '''

    def __init__(self, *args, **kwargs):
        super(IPythonWidget, self).__init__(*args, **kwargs)
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel(show_banner=False)
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            QApplication.instance().exit()
        self.exit_requested.connect(stop)

    def pushVariables(self, variableDict):
        ''' Given a dictionary containing name / value pairs, push those variables to the IPython console widget '''
        self.kernel_manager.kernel.shell.push(variableDict)

    def clearTerminal(self):
        ''' Clears the terminal '''
        self._control.clear()

    def printText(self, text):
        ''' Prints some plain text to the console '''
        self._append_plain_text(text)

    def executeCommand(self, command):
        ''' Execute a command in the frame of the console widget '''
        self._execute(command, False)
