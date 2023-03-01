#!/usr/bin/env python
# coding: utf-8

# # Lab4
# 
# ___

# ### Running the Python Interpreter from a Terminal
# The Jupyter notebook is a popular software tool used by scientists to share their work. Jupyter and its predecessor IPython were developed by Fernando Perez when he was at CU Boulder as a graduate student in Physics, then postdoc in Applied Math. 
# 
# At times you may need to run Python from a Terminal. To run the Python interpreter, follow these steps:
# * Mac OS
#   * Open `Applications` $\to$ `Utilities` $\to$ `Terminal`. 
# * Windows 11
#   * Search for `cmd` on the toolbar, then select `Run as administrator`. 
# 
# After the Terminal opens,   
# * Make note of the current folder (displayed in the Terminal prompt).
# * Enter `python`.
# You should see the Python version number (3.8 or so) and the interpreter prompt `>>>`. (Note: If you see Python version 2.x, run `python3` instead of `python`.)

# **Enter code into the interpreter**: Try typing in Python commands. Press `return` or `enter` to execute. For example
# * `num = 7`
# * `10 * num`
# 
# **Enter this simple function definition**:
# ```
# def hello(name):
#     print('hello ' + name)
# ```
# Notice that the prompt changes to `...` until you enter a blank line which indicates the end of the function definition. (Within a function, to insert a blank line, enter a tab or space character.)
# 
# **Run the function**: Enter `hello('world!')`.
# 
# **Exit the interpreter**: Enter `exit()` to leave the interpreter and return to the Terminal.

# ___
# 
# ### Terminal Commands
# 
# **List contents of a folder**
# * Mac: `ls`
# * Windows: `dir`
# 
# **Change current folder**
# * `cd XXX` (or Windows: `chdir XXX`)
# 
# **Move up a level**
# * `cd ..`
# 
# **Autocomplete filenames**
# * Press the tab key
# 
# **Access command history**
# * Use up and down arrows

# ___
# 
# ### Running Python Code from a File
# Instead of entering code directly into the Python interpreter, you can write the code in any plain text editor (or Jupyter) and paste it into the interpreter. Another option is to save the code in a file, then execute the file.
# 
# **Open a plain text editor**
# * Mac: TextEdit (select `Format`$\to$`Make Plain Text`)
# * Windows: Notepad
# 
# **and save this Python code in a file** named `myfunc.py` (or any XXX.py filename) in an easily accessible folder (such as the Terminal current folder).:
# ```
# #!/usr/bin/env python
# 
# def hello(name):
#     print('hello ' + name)
#     
# hello('world!')
# ```
# 
# *Jupyter alternative*: Instead of using a plain text editor, you can write your code in a Jupyter notebook, then export to .py format.
# 
# **Execute the file in a Terminal**
# At a command prompt, enter `python myfunc.py`. You should see `Hello world!` as the output. 
# 
# **Note on filenames**: if the file is not saved in the current Terminal folder, the filename may need to include its full path, for example
# * Mac: `python /Users/Yourname/Desktop/myfunc.py`
# * Windows: `python C:\Users\Yourname\Desktop\myfunc.py`
# 
# 
# ___

# ### Importing Your Own Package
# User-defined functions can be imported as a module just like built-in modules like `math` and `numpy`.
# 
# **Open the Python interpreter** in a Terminal by entering `python`.
# 
# **Import your module** by entering `import myfunc`. You will see the `>>>` prompt.
# 
# **Run your function**: Enter `myfunc.hello('Gus')`.

# ___
# ___
# 
# ### Doubly Linked Lists
# 
# Below is a **`Node`** class with these attributes:
# * **`key`** identifier for the node
# * **`prev`** points to a previous node or equals `None` if there is no previous node.
# * **`next`** points to the next node or equals `None` if there is no next node.

# In[1]:


class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


# Create a **`DLinkedList`** class to represent a doubly linked list. Each list object has the following attribute:
# * **`head`** points to the first Node in the list or equals `None` if the list is empty.
# 
# Add the following methods:
# * **`insert(node)`** adds a new Node to the head of the list.
# * **`delete(node)`** removes a Node from the list. Assume that the Node is in the list.
# * **`search(value)`** traverses the list seeking a `key` value. If found, return the corresponding Node. If not found, return `None`.
# * **`keys()`** returns a Python `list` containing all the linked list keys in order.
# 
# Example:
# ```
# dl = DLinkedList()
# dl.insert(Node('frog'))
# dl.insert(Node('ladybug'))
# dl.insert(Node('cricket'))
# dl.keys()
# ```
# returns `['cricket', 'ladybug', 'frog']`. Then
# 
# ```
# ladynode = dl.search('ladybug')
# ladynode.key
# ```
# returns `'ladybug'` and
# 
# ```
# dl.delete(ladynode)
# dl.keys()
# ```
# returns `['cricket', 'frog']`.

# In[86]:


class DLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, node):
        node.prev = None
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        self.head = node
    def delete(self, node):
        if node.prev == None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
    def search(self, value):
        if self.head == None:
            return None
        else:
            node = self.head
            while node != None and node.key != value:
                node = node.next
            return node
    def keys(self):
        lst = []
        node = self.head
        while node != None:
            lst.append(node.key)
            node = node.next
        return lst


# In[81]:


dl = DLinkedList()
dl.insert(Node('frog'))
dl.insert(Node('ladybug'))
dl.insert(Node('cricket'))
dl.keys()


# In[82]:


ladynode = dl.search('ladybug')
ladynode.key


# In[83]:


dl.delete(ladynode)
dl.keys()


# In[ ]:




