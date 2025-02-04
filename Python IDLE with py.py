import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import sys
import io
import os
from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator
import pdb

class PythonIDLE:
    def __init__(self, root):
        self.root = root
        self.root.title("Python IDLE")
        
        # Current file path
        self.current_file = None
        
        # Text Widget for Code Editor
        self.editor = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.editor.pack(fill=tk.BOTH, expand=1)
        Percolator(self.editor).insertfilter(ColorDelegator())

        # Text Widget for Output
        self.output = scrolledtext.ScrolledText(self.root, height=10, wrap=tk.WORD, state='disabled')
        self.output.pack(fill=tk.BOTH, expand=1)
        
        # Menu Bar
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu.add_cascade(label="File", menu=file_menu)
        
        run_menu = tk.Menu(self.menu, tearoff=0)
        run_menu.add_command(label="Run", command=self.run_code)
        self.menu.add_cascade(label="Run", menu=run_menu)
        
        debug_menu = tk.Menu(self.menu, tearoff=0)
        debug_menu.add_command(label="Set Breakpoint", command=self.set_breakpoint)
        debug_menu.add_command(label="Start Debugger", command=self.start_debugger)
        self.menu.add_cascade(label="Debug", menu=debug_menu)
    
    def new_file(self):
        self.editor.delete('1.0', tk.END)
        self.current_file = None
        self.root.title("Python IDLE")
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                code = file.read()
                self.editor.delete('1.0', tk.END)
                self.editor.insert('1.0', code)
            self.current_file = file_path
            self.root.title(f"Python IDLE - {os.path.basename(file_path)}")
    
    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                code = self.editor.get('1.0', tk.END)
                file.write(code)
        else:
            self.save_as_file()
    
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                code = self.editor.get('1.0', tk.END)
                file.write(code)
            self.current_file = file_path
            self.root.title(f"Python IDLE - {os.path.basename(file_path)}")
    
    def run_code(self):
        code = self.editor.get('1.0', tk.END)
        self.output.config(state='normal')
        self.output.delete('1.0', tk.END)
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        try:
            exec(code, {})
        except Exception as e:
            self.output.insert(tk.END, redirected_error.getvalue())
        finally:
            self.output.insert(tk.END, redirected_output.getvalue())
            sys.stdout = old_stdout
            sys.stderr = old_stderr
        self.output.config(state='disabled')
    
    def set_breakpoint(self):
        index = self.editor.index(tk.INSERT)
        self.editor.mark_set("breakpoint", index)
        self.editor.tag_add("breakpoint", index, f"{index} +1c")
        self.editor.tag_config("breakpoint", background="red")
    
    def start_debugger(self):
        code = self.editor.get('1.0', tk.END)
        self.output.config(state='normal')
        self.output.delete('1.0', tk.END)
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        try:
            debugger = pdb.Pdb()
            debugger.reset()
            debugger.run(code)
        except Exception as e:
            self.output.insert(tk.END, redirected_error.getvalue())
        finally:
            self.output.insert(tk.END, redirected_output.getvalue())
            sys.stdout = old_stdout
            sys.stderr = old_stderr
        self.output.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonIDLE(root)
    root.mainloop()
