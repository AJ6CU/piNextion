# --------------------
# This file is used for defining Ttk styles.
# Use the 'style' object to define styles.

# Pygubu Designer will need to know which style definition file
# you wish to use in your project.

# To specify a style definition file in Pygubu Designer:
# Go to: Edit -> Preferences -> Ttk Styles -> Browse (button)

# In Pygubu Designer:
# Assuming that you have specified a style definition file,
# - Use the 'style' combobox drop-down menu in Pygubu Designer
#   to select a style that you have defined.
# - Changes made to the chosen style definition file will be
#   automatically reflected in Pygubu Designer.
# --------------------

# import tkinter as tk
import tkinter.ttk as ttk
#import sv_ttk


def setup_ttk_styles(master=None):
    
    style = ttk.Style(master)
    #sv_ttk.set_theme("dark"))
    style.theme_use('default')

    fontList = {'Heading1': ('Times New Roman',24, 'bold' ),
            'Heading1b': ('Arial', 20, 'bold'),
            'Heading2': ('Arial',18, 'bold' ),
            'Heading2b': ('Arial',14, 'bold' ),
            'Heading2bi': ('Arial', 14, 'bold', 'italic'),
            'Heading3': ('Arial',12, 'bold' ),
            'Heading3i': ('Arial', 12, 'bold', 'italic'),
            'Heading4': ('Arial',10, 'bold' ),
            'Heading5': ('Fixed', 6),
            'Normal': ('Default', 10),
            'HeadingVFO': ('Fixed',82, 'bold' ),
            'Emphasis': ('Default',12, 'bold'),
            'Symbol1': ('Symbol',18, 'bold'),
            'Symbol3': ('Symbol',12, 'bold')}

    style.configure('Heading1.TLabel',font=fontList['Heading1'], background='gray', foreground='white')
    style.configure('Heading1b.TLabel', font=fontList['Heading1b'], background='gray', foreground='white')
    style.configure('Heading2.TLabel',font=fontList['Heading2'])
    style.configure('Heading2b.TLabel',font=fontList['Heading2b'], background='gray', foreground='white')
    style.configure('Heading2bi.TLabel', font=fontList['Heading2bi'], background='gray', foreground='white')
    style.configure('Heading3b.TLabel',font=fontList['Heading3'], background='gray', foreground='white')
    style.configure('Heading3bi.TLabel', font=fontList['Heading3i'], background='gray', foreground='white')
    style.configure('Heading4b.TLabel',font=fontList['Heading4'], background='gray', foreground='white')
    style.configure('OffLED.TLabel', font=fontList['Heading5'], background='gray', foreground='gray')
    style.configure('OnLED.TLabel', font=fontList['Heading5'], background='green', foreground='green')
    style.configure('GreenLED.TLabel',font=fontList['Heading2'], background='green', foreground='white')
    style.configure('RedLED.TLabel',font=fontList['Heading2'], background='red', foreground='white')
    style.configure('VFO.TLabel',font=fontList['HeadingVFO'], background='gray', foreground='white')
    style.configure('Heading3.TLabel',font=fontList['Heading3'])
    style.configure('Heading4.TLabel',font=fontList['Heading4'])
    style.configure('Normal.TLabel',font=fontList['Normal'])
    style.configure('Symbol1.TLabel',font=fontList['Symbol1'])
    style.configure('Button1.TButton',font=fontList['Heading1'])
    style.configure('Button1Raised.TButton', font=fontList['Heading1'], relief='raised')
    style.configure('Button2.TButton',font=fontList['Heading2'])
    style.configure('Button2b.TButton',font=fontList['Heading2b'], justify='center')
    style.configure('Button2Raised.TButton', font=fontList['Heading2'], justify='center', relief='raised')
    style.configure('Button2bipressed.TButton', relief='sunken', font=fontList['Heading2bi'], justify='center')
    # style.configure('Button2bcentered.TButton', font=fontList['Heading2b'],justify='center')

    style.configure('RedButton2b.TButton',font=fontList['Heading2b'], background='red', foreground='white')
    style.configure('GreenButton2b.TButton', font=fontList['Heading2b'], background='green', foreground='white',justify='center')
    style.configure('Button3.TButton',font=fontList['Heading3'])
 #   style.configure('DarkButton3.TButton',font=fontList['Heading3'], background='black', foreground='white', boarderwidth=5, relief='raised')
    style.configure('Button4.TButton',font=fontList['Heading4'])
    style.configure('Button3Blue.TButton',font=fontList['Heading3'], foreground='blue')
    style.configure('Normal.TButton',font=fontList['Normal'])
    style.configure('Symbol1.TButton',font=fontList['Symbol1'])
    style.configure('Symbol3.TButton',font=fontList['Symbol3'])
    style.configure('ButtonEmphasis.TButton',font=fontList['Emphasis'])
    style.configure('RadioButton3.TRadiobutton',font=fontList['Heading3'])
    style.configure('RadioButton4.TRadiobutton',font=fontList['Heading4'])
    style.configure('RadioButtonNormal.TRadiobutton',font=fontList['Normal'])
    style.configure('RadioButtonEmphasis.TRadiobutton',font=fontList['Emphasis'])
    style.configure('Heading2b.TMenubutton',font=fontList['Heading2b'])
    style.configure('Submenu.TMenuitem.Command',font=fontList['Heading2b'])
    style.configure('Checkbox3.TCheckbutton',font=fontList['Heading3'])
    style.configure('Checkbox4.TCheckbutton',font=fontList['Heading4'])
    style.configure('CheckboxNormal.TCheckbutton',font=fontList['Normal'])
    style.configure('CheckboxNormalNoBorder.TCheckbutton',font=fontList['Normal'],highlightthickness=0, borderwidth=0, bd=0)
    style.configure('CheckboxEmphasis.TCheckbutton',font=fontList['Emphasis'])
    style.configure('ComboBox2.TCombobox',font=fontList['Heading2'])
    style.configure('ComboBox2b.TCombobox', font=fontList['Heading2b'])
    style.configure('ComboBox3.TCombobox', font=fontList['Heading3'])
    style.configure('ComboBox4.TCombobox',font=fontList['Heading4'])
    style.configure('ComboBox4White.TCombobox',font=fontList['Heading4'],foreground='white')
    style.configure('Normal.TEntry',font=fontList['Normal'])

    style.configure('Entry1b.TEntry', font=fontList['Heading1'])
    style.configure('Entry2b.TEntry', font=fontList['Heading2'])
    style.configure('NoBorder.TEntry',font=fontList['Normal'], highlightthickness=0, borderwidth=0, bd=0)

    style.configure('Title.TFrame', background='blue', foreground='white')
    style.configure('Heading2.TLabelframe.Label', background='gray', bd=4, font=fontList['Heading2'])
    style.configure('Heading2.TLabelframe', background='gray', bd=4)
    style.configure('Normal.TText', background='gray', foreground='white', font=fontList['Heading3'])

    style.configure('Highlight.TFrame', background='blue', bd=4 )
 #   style.configure('Dark.TFrame', background='black', bd=4, bordercolor='white')
    style.configure('Normal.TFrame', background='gray', bd=4,font=fontList['Heading2'])
    style.configure('NormalOutline.TFrame', background='gray', bd=4, bordercolor='white' ,relief='groove')

    style.configure('Fixed.TNotebook')
    style.configure('Fixed.TNotebook.Tab',padding=[5,2])
    style.configure('Red.TSeparator', background='red', height=25)



