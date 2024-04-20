import tkinter as tk
from tkinter import ttk, filedialog, messagebox,simpledialog
import subprocess
import os
import time
import shutil
import psutil
import webbrowser
import string
import random
import webbrowser
import urllib.request  # For downloading files
from tkinter import filedialog  # For browsing folders
import requests
import logging


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="black")
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.pack()
        self.new_vm_path = None  # Initialize new_vm_path to None

        # Create a canvas and add scrollbars to it
        self.canvas = tk.Canvas(self,bg="black")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # This frame will contain the widgets
        self.frame = tk.Frame(self.canvas,bg="black")
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # Add scrollbars
        self.scrollbar_y = tk.Scrollbar(self,bg="black", orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = tk.Scrollbar(self,bg="black", orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

        # Update scrollregion after all widgets are added
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.create_widgets()

    def create_widgets(self):
        # Setup the main application window
        self.master.title("ForensicFusion")
        self.master.configure(bg="black")
        self.current_step = "WELCOME"
        self.create_welcome_page()
        
                    
 
    def create_welcome_page(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Add widgets for the welcome page
        self.welcome_lable = tk.Label(self.frame, text="ForensicFusion: Automated Memory Analysis tool!\n", bg="black", fg="#aaff33", font=("Terminal",35))
        
        self.welcome_lable.grid(row=0, column=1,pady=50)


        self.note_label1 = tk.Label(self.frame, text=" Information ", bg="#b91919", fg="#ccff33",font=("Terminal",28), wraplength=1000, justify="center")
        self.note_label1.grid(row=2, column=1, pady=20)
        
        
        self.welcome_lable = tk.Label(self.frame,text="The automated Memory Analysis tool facilitates the creation of virtual machines on various operating systems such as Windows, Linux, macOS, and Android, allowing users to run potentially harmful scripts within these isolated environments. Subsequently, users can take memory dumps of these virtual machines and analyze them using the Volatility tool for further investigation. ",
            bg="black", fg="#43af1c",font=("Terminal",18),wraplength=1300, justify="left")
        self.welcome_lable.grid(row=3, column=1,pady=50, padx=30)
        
        self.welcome_lable = tk.Label(self.frame, text="Click the button below to start the process", bg="black", fg="#A5D732",font=("Terminal",20))
        self.welcome_lable.grid(row=4, column=1,pady=20)

         # Button to start VM creation
        self.welcome_button=tk.Button(self.frame, text="start",bg="#aaff33", fg="#f22525" , font=("Terminal",30), command=self.info_page)
        self.welcome_button.grid(row=5, column=1,pady=20)

        
##############################################################################################################################################################################################################
##############################################################################################################################################################################################################
    def info_page(self):
        
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.note_labe = tk.Label(self.frame, text="  Information " , bg="#b91919", fg="#ccff33",font=("Terminal",28), wraplength=1000, justify="center")
        self.note_labe.grid(row=0, column=1,columnspan=3,pady=(50,50))
   

        self.note_label = tk.Label(self.frame,text="Before you start creating your Virtual Machine make sure that you have installed Virtual Box setup in your Host Machine.\n\nIf not then please click on below buttons as per your host machine and see the process download the Virtual box.\n\nAnd If you already have Virtual Box and Virtual machine and want to analye it please proceed with next step ",bg="black", fg="#ccff33",font=("Terminal",20), wraplength=1100, justify="left")
        self.note_label.grid(row=2, column=1,columnspan=3, pady=(20,20))

        self.note_labe = tk.Label(self.frame, text=" \n\n", bg="black",font=("Terminal",20), justify="center")
        self.note_labe.grid(row=3, column=1, columnspan=3,pady=(5))


        # Button for Windows 
        self.windows_button = tk.Button(self.frame, text="\nWindows\n", bg="#ccff33", fg="black", font=("Terminal", 20), command=self.show_windows_Vm_install)
        self.windows_button.grid(row=4, column=1, sticky='ew', pady=(20,50),padx=30)

        # Button for Linux
        self.Linux_button = tk.Button(self.frame, text="\nLinux\n", bg="#ccff33", fg="black", font=("Terminal", 20), command=self.show_Linux_Vm_install)
        self.Linux_button.grid(row=4, column=2, sticky='we',pady=(20,50),padx=30)

        # Button for Mac-os 
        self.Macos_button = tk.Button(self.frame, text="\nMacOS\n", bg="#ccff33", fg="black", font=("Terminal", 20), command=self.show_macos_install)
        self.Macos_button.grid(row=4, column=3, sticky='ew', pady=(20,50), padx=30)

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="Next",bg="#ccff33", fg="#b21e1e", font=("Terminal",20), command=self.iso_Download)
        self.next_button.grid(row=8, column=4, sticky='ew', pady=(50, 0))

        # Back Button
        self.back_button = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),command=self.create_welcome_page)
        self.back_button.grid(row=8, column=0, sticky='w',pady=(50, 0))  

##############################################################################################################################################################################################################
########################zz######################################################################################################################################################################################   
        

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.vm_folder_path.set(folder_selected)

##############################################################################################################################################################################################################
##############################################################################################################################################################################################################

    def show_windows_Vm_install(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.note_label = tk.Label(self.frame, text="The general steps to download and install VirtualBox for Windows System", bg="black", fg="#ccff33", font=("Terminal", 25), wraplength=1000, justify="center")
        self.note_label.pack(pady=(30,20))
        instructions = (
		"1. Go to the VirtualBox website: https://www.virtualbox.org/\n\n"
		"2. Click on the Downloads menu at the top of the page.\n\n"
		"3. Under VirtualBox platform packages click on Windows hosts to download the installer.\n\n"
		"4. Once the installer is downloaded, double-click on it to start the installation process.\n\n"
		"5. Follow the on-screen instructions in the installer.\n\n"
		"6. After the installation is complete you can launch VirtualBox from the Start menu.\n"
    	)
        self.note_text = tk.Text(self.frame, bg="black", fg="#b91919",height=10, width=100,font=("Terminal", 12))
        self.note_text.insert("end", instructions)
        self.note_text.config(state="disabled")
        self.note_text.pack(fill="both", expand=True)
    	#Back Button
        self.windows_back_button = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal", 20), command=self.info_page)
        self.windows_back_button.pack(side="bottom", pady=(20, 10))


    def show_Linux_Vm_install(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
    	    widget.destroy()
            
        self.note_label = tk.Label(self.frame, text="The general steps to download and install VirtualBox for Linux System", bg="black", fg="#ccff33", font=("Terminal", 25), wraplength=1000, justify="center")
        self.note_label.pack(pady=(30,20))

        instructions = (
		"1. Open a terminal window.\n\n"
		"2. Depending on your Linux distribution you can either use a package manager to install\n"
		"VirtualBox or download the installer from the VirtualBox website.\n\n"
		"3. If using a package manager (Example: apt for Debian-based systems):\n"
		"    $ sudo apt update\n"
		"    $ sudo apt install virtualbox\n\n"
		"4. If downloading from the website:\n"
		"    - Go to the VirtualBox website: https://www.virtualbox.org/\n"
		"    - Click on the Downloads menu at the top of the page.\n"
		"    - Under VirtualBox platform packages select the appropriate\n" 
		"      package for your Linux distribution and architecture.\n"
		"    - Download the package.\n\n"
		"5. Once downloaded, follow the installation instructions provided for your distribution.\n\n"
		"6. After the installation is complete you can launch VirtualBox from the Applications\n"
		"menu or by running 'virtualbox' in the terminal.\n\n"
    	)
        self.note_text = tk.Text(self.frame, bg="black", fg="#b91919", height=15, width=100, font=("Terminal", 12))
        self.note_text.insert("end", instructions)
        self.note_text.config(state="disabled")
        self.note_text.pack(fill="both", expand=True)
    	 # Back Button
        self.linux_back_button = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal", 20), command=self.info_page)
        self.linux_back_button.pack(side="bottom", pady=(20, 10))


    def show_macos_install(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
        	widget.destroy()

        self.note_label = tk.Label(self.frame, text="The general steps to download and install VirtualBox for Mac-OS ", bg="black", fg="#ccff33", font=("Terminal", 25), wraplength=1000, justify="center")
        self.note_label.pack(pady=(30,20))


        instructions = (
		"1. Go to the VirtualBox website: https://www.virtualbox.org/\n\n"
		"2. Click on the Downloads menu at the top of the page.\n\n"
		"3. Under VirtualBox platform packages, click on 'OS X hosts' to download the installer.\n\n"
		"4. Once the installer is downloaded, double-click on it to mount the disk image.\n\n"
		"5. Open the mounted disk image and double-click on the VirtualBox.pkg file to start the installation process.\n\n"
		"6. Follow the on-screen instructions in the installer.\n\n"
		"7. After the installation is complete, you can launch VirtualBox from the Applications folder."
    	)

        self.note_text = tk.Text(self.frame, bg="black", fg="#b91919", height=15, width=100, font=("Terminal", 12))
        self.note_text.insert("end", instructions)
        self.note_text.config(state="disabled")
        self.note_text.pack(fill="both", expand=True)

    	# Back Button
        self.macos_back_button = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal", 20), command=self.info_page)
        self.macos_back_button.pack(side="bottom", pady=(20, 10))


##############################################################################################################################################################################################################
##############################################################################################################################################################################################################
    def iso_Download(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.os_version_label = tk.Label(self.frame, text="\nProcess 1 : Download The Image File\n",bg="#ffecce", fg="#b21e1e", wraplength=1000, font=("Terminal",25))
        self.os_version_label.grid(row=0, column=1, columnspan=3,sticky='ew', pady=25, padx=60)

        self.os_version_label = tk.Label(self.frame, text="\nBefore creating your virtual machine, let's download the image file (.iso) file as per your VM\n\n",bg="black", fg="#9cb344", wraplength=1000,justify="center", font=("Terminal",20))
        self.os_version_label.grid(row=1, column=1, sticky='we',columnspan=3, pady=5,padx=60)
       
        # OS Type Selection
        self.create_vmpage1 =tk.Label(self.frame, text="Setp 1: Choose your operating System(OS):", bg="black", fg="#9cb344", justify= "left",wraplength=500,font=("Terminal",15)).grid(row=2, column=0, columnspan=3,padx=15, pady=5, sticky='w')
        self.os_types = ["Windows", "Linux", "MAC-os", "Android"]
        self.os_type = tk.StringVar()
        self.os_type.set("Select OS")
        self.os_type_dropdown = ttk.Combobox(self.frame, background="#ffecce", foreground="#b21e1e",font=("Terminal", 15),textvariable=self.os_type, width=50, height=5, values=self.os_types,state="readonly")
        self.os_type_dropdown.grid(row=2, column=1, sticky='e',pady=25, padx=60,columnspan=3)
        self.os_type_dropdown.bind("<<ComboboxSelected>>", self.update_os_version_options)

        # OS Version Selection
        self.os_version_label = tk.Label(self.frame, text="\nStep 2: Choose OS Version:",bg="black", wraplength=1000, fg="#9cb344", font=("Terminal",15))
        self.os_version_label.grid(row=6, column=1, sticky='w', columnspan=3,pady=5,padx=15)
        self.os_version = tk.StringVar()
        self.os_version_dropdown = ttk.Combobox(self.frame,background="#fff2cc", foreground="#b21e1e", width=50, font=("Terminal", 15), height=5, textvariable=self.os_version, state="readonly")
        self.os_version_dropdown.grid(row=6, column=1, sticky='e', columnspan=3,pady=25,padx=60)

 
        # ISO file download
        self.os_version_label = tk.Label(self.frame, text="\nSetp 3: Please click on Download button to \nDownload the .iso file to create Vm ",bg="black", fg="#9cb344",justify="left", font=("Terminal",15))
        self.os_version_label.grid(row=9, column=1, sticky='w',columnspan=3,pady=25, padx=0)
        self.create_vm_button = tk.Button(self.frame, text="\n     Download      \n", bg="#ccff33", fg="black",justify="right",font=("Terminal",25), command=self.download_iso)
        self.create_vm_button.grid(row=9, column=3, sticky='w',columnspan=4, pady=15,padx=60)
        self.note_labe = tk.Label(self.frame, text="  Note " , bg="#b91919", fg="#ccff33",font=("Terminal",20), wraplength=300, justify="left")
        self.note_labe.grid(row=10, column=2,columnspan=3,pady=15,padx=5)
        
        self.label = tk.Label(self.frame, text="1.If you want to create VM using other .iso files please installed your required  .iso file and use it for creating VM.\n\n2. If you are facing issue while downloading the above .iso files please installed it externally from authorized platform.", wraplength=1200, justify="left",bg="black", fg="#b21e1e", font=("Terminal",12))
        self.label.grid(row=11, column=2, sticky='w', columnspan=3,pady=15,padx=60)

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="  Next  ",bg="#ccff33", fg="#b21e1e", font=("Terminal",20), command=self.android_genymotion)
        self.next_button.grid(row=15, column=3, sticky='e',columnspan=3, pady=10,padx=25)

        # Back Button
        self.back_button = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),command=self.info_page)
        self.back_button.grid(row=15, column=0, sticky='w',columnspan=3,pady=10, padx=25) 

    def update_os_version_options(self, event):
        os_versions = {
            "Windows": ["Windows 8", "Windows 11", "Windows Server 2012"],
            "Linux": ["Kali Linux", "Ubuntu", "Fedora", "Parrot"],
            "MAC-os": ["macOS Ventura", "macOS Big Sur", "macOS  Sonoma"],
            "Android": ["genymotion"]
        }
        selected_os = self.os_type.get()
        if selected_os in os_versions:
            self.os_version_dropdown.config(values=os_versions[selected_os], state="readonly")
            self.os_version.set(os_versions[selected_os][0])  # Set the default version
        else:
            print("Invalid OS type selected.")


    def download_iso(self):
        selected_os = self.os_type.get().lower()  # Convert to lowercase for case-insensitive matching
        selected_version = self.os_version.get()

        print("Selected OS:", selected_os)
        print("Selected Version:", selected_version)

        os_version_to_iso = {
            "windows": {
                "Windows 8": r"https://drive.google.com/file/d/1wFSTj2-vsEi3tIhWmkF4qqPOIIqlv0Ak/view?usp=sharing",
                "Windows 11": r"https://drive.google.com/file/d/1ZBmPgEr2fRs90j3aipoYVzyR6R8fhMDA/view?usp=sharing",
                "Windows Server 2012": r"https://go.microsoft.com/fwlink/p/?LinkID=2195443&clcid=0x409&culture=en-us&country=US"
            },
            "linux": {
                "Kali Linux": r"https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-installer-amd64.iso",
                "Ubuntu": r"https://releases.ubuntu.com/jammy/ubuntu-22.04.4-desktop-amd64.iso",
                "Fedora": r"https://download.fedoraproject.org/pub/fedora/linux/releases/39/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-39-1.5.iso",
                "Parrot": r"https://deb.parrot.sh/parrot/iso/6.0/Parrot-security-6.0_amd64.iso"
            },
            "mac-os": {
                "macOS Ventura": r"https://www.mediafire.com/file/dcji26zay7s3p8r/macOS%20Ventura%20ISO%20for%20VM%20by%20techrechard.com.iso/file#",
                "macOS Big Sur": r"https://download2392.mediafire.com/zt0oedepncmgqj7Kq3FpLWtQB7jX7CUrFAfrVdXp1F93HvgfyBRXJRmPYwlguoeNza95jwYqEmiCUmUXfyZkgqyNP9Z_INF1InUi2c7rIvo4wRlsuyH6Cyo_2t3d-CkUlf9sWGDqU1M03GqDT2KEyzl_WJ5nPWtH1LVKaXipsjMP/irna8hwybkhl41f/BigSur13-3-1.iso",
                "macOS  Sonoma": r"https://www.mediafire.com/file/vku90kjifs1fmu0/macOS%20Sonoma%20ISO%20by%20techrechard.com.iso/file#"
            },
            "android": {
                "genymotion": r"https://dl.genymotion.com/releases/genymotion-3.6.0/genymotion-3.6.0.exe",
            }
        }

        selected_os_dict = os_version_to_iso.get(selected_os)
        if selected_os_dict:
            if selected_version in selected_os_dict:
                iso_path = selected_os_dict[selected_version]
                print("ISO Path:", iso_path)  # Check if the ISO path is correct

                if iso_path:
                    # Open the ISO file download link in the default web browser
                    webbrowser.open(iso_path)
                    print("ISO file download link opened in the default web browser.")
                else:
                    print("ISO path not found for the selected version.")
            else:
                print("Invalid version selected for the chosen OS.")
        else:
            print("Invalid OS selected.")


##############################################################################################################################################################################################################
############################################################################################################################################################################################################## 
    def android_genymotion(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.note_labe = tk.Label(self.frame, text="  Information " , bg="#b91919", fg="#ccff33",font=("Terminal",28), wraplength=1000, justify="center")
        self.note_labe.grid(row=0, column=1,pady=50,padx=5)

        # Display Docker setup instructions for Windows
        self.note_label = tk.Label(self.frame,text="For android once you download the genymotion app you have to access it and need to select your android platform as per your need.\n\nPlease click on below button to see the step by step process"
                                   , bg="black", fg="#ccff33",font=("Terminal",18), wraplength=900, justify="left")
        self.note_label.grid(row=2, column=1, pady=(20))
        

        self.browse_button = tk.Button(self.frame, text="\n  Sample Document  \n",bg="#84ac28", fg="black", font=("Terminal",20), command=self.Sample_Document)
        self.browse_button.grid(row=3, column=1, sticky="w", pady=10,padx=200)
        
        self.note_labe = tk.Label(self.frame, text="\n" , bg="black", font=("Terminal",28), wraplength=1000, justify="center")
        self.note_labe.grid(row=4, column=1)


        self.note_label1 = tk.Label(self.frame,text="NOTE : Please Skip this step if you are not working on Android", bg="black", fg="#b21e1e",font=("Terminal",25), wraplength=800, justify="left")
        self.note_label1.grid(row=5, column=1,pady=(30))

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="  Next  ",bg="#ccff33", fg="#b21e1e", font=("Terminal",20), command=self.create_vm_page)
        self.next_button.grid(row=15, column=3,sticky="e",pady=10,padx=0)

        # Back Button
        self.back_button = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),command=self.iso_Download)
        self.back_button.grid(row=15, column=0, sticky='w',pady=10, padx=25)  

##############################################################################################################################################################################################################
        
    def Sample_Document(self):
        doucumet_path=r"https://docs.genymotion.com/desktop/Get_started/014_Basic_steps/"

        webbrowser.open(doucumet_path)

##############################################################################################################################################################################################################            
##############################################################################################################################################################################################################
    def create_vm_page(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.os_version_label = tk.Label(self.frame, text="\n  Process 2: Creation of Virtual Machine.  \n ",bg="#ffecce", fg="#b21e1e", wraplength=1200, font=("Terminal",25))
        self.os_version_label.grid(row=0, column=2, columnspan=5,sticky='ew',  pady=50, padx=150)

        self.os_version_label = tk.Label(self.frame, text="Once you donload the image file i.e (.iso file), please follow the below steps\n",bg="black", fg="#9cb344", wraplength=1200,justify="center", font=("Terminal",20))
        self.os_version_label.grid(row=1, column=1, sticky='we',columnspan=5, pady=15,padx=150)
        
        # Chose .ISO file 
        self.create_isopage =tk.Label(self.frame, text="Step 1: Please select path to where you downloaded .iso file",bg="black", fg="#9cb344", wraplength=350,font=("Terminal",15),justify="left")
        self.create_isopage.grid(row=2, column=1,  columnspan=4,pady=10,padx=50,sticky='w')
        self.iso_path_var = tk.StringVar()
        self.ISO_file_entry = tk.Entry(self.frame,bg="#fff2cc", fg="#b21e1e",font=("Terminal",15),textvariable=self.iso_path_var, highlightthickness=5,width=30,justify="left")
        self.ISO_file_entry.grid(row=2, column=2, sticky="e",columnspan=3,pady=10,padx=400)
        self.browse_button = tk.Button(self.frame, text="Browse",bg="#84ac28", fg="black", font=("Terminal",20), command=self.browse_iso)
        self.browse_button.grid(row=2, column=3, sticky="e", pady=10,padx=0)
        
        # VM Folder Path
        self.create_vmpage =tk.Label(self.frame, text="Step 2:Select Path where you want to store your VM, otherwise it will store in default path.\nNOTE: You can skip this step",bg="black", fg="#9cb344", wraplength=350, font=("Terminal",15),justify="left")
        self.create_vmpage.grid(row=4, column=1,columnspan=4,pady=10,padx=50,sticky='w')
        self.vm_folder_path_var = tk.StringVar()
        self.vm_folder_entry = tk.Entry(self.frame,bg="#fff2cc", fg="#b21e1e",font=("Terminal",15),textvariable=self.vm_folder_path_var, highlightthickness=5, width=30, justify="left")
        self.vm_folder_entry.grid(row=4, column=2 ,sticky="e",columnspan=3,pady=10,padx=400)
        self.browse_button = tk.Button(self.frame, text="Browse",bg="#84ac28", fg="black", font=("Terminal",18), justify="right",command=self.browse_vm_folder)
        self.browse_button.grid(row=4, column=3, sticky="e",pady=10,padx=0)
        
       
        # Create VM Button
        self.os_version_label = tk.Label(self.frame, text="Setp 3: Now Click on Create Vm button",bg="black", fg="#9cb344",wraplength=350, justify="left", font=("Terminal",15))
        self.os_version_label.grid(row=9, column=1, columnspan=3,pady=10,padx=50,sticky="w")
        self.create_vm_button = tk.Button(self.frame, text="\n  Create VM  \n", bg="#ccff33", width=15, fg="black",justify="left",font=("Terminal",25), command=self.perform_create_vm)
        self.create_vm_button.grid(row=9,column=3,sticky="e",pady=10,padx=0)
      
      
        self.note_labe = tk.Label(self.frame, text=" \n", bg="black",font=("Terminal",20), justify="center")
        self.note_labe.grid(row=12, column=1, columnspan=3,pady=10, padx=5)
 
        
        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="  Next  ",bg="#ccff33", fg="#b21e1e", font=("Terminal",20), command=self.Introduction_page)
        self.next_button.grid(row=15, column=3, columnspan=3,sticky="e",pady=10,padx=0)

        # Back Button
        self.back_button = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),command=self.android_genymotion)
        self.back_button.grid(row=15, column=0, sticky='w',columnspan=3,pady=10, padx=25)  

    
##############################################################################################################################################################################################################

    def browse_iso(self):
        """Browse and select the ISO file."""
        iso_path = filedialog.askopenfilename(title="Select ISO file", filetypes=[("ISO files", "*.*")])
        if iso_path:
            self.iso_path_var.set(iso_path)

    def browse_vm_folder(self):
        """Browse and select the folder for VM."""
        folder_path = filedialog.askdirectory(title="Select Destination Folder for VM")
        if folder_path:
            self.vm_folder_path_var.set(folder_path)

    def perform_create_vm(self):
        iso_path = self.iso_path_var.get()
        vm_folder = self.vm_folder_path_var.get()

        base_name = "admin"
        i = 0
        while os.path.exists(os.path.join(vm_folder, f"{base_name}{i}")):
            i += 1
        new_vm_name = f"{base_name}{i}"
        vdipath = os.path.join(vm_folder, f"{new_vm_name}\\{new_vm_name}.vdi")

        vbox_manage_path =  r"/Applications/VirtualBox.app/Contents/MacOS/VBoxManage"

        ram_size = 2048
        num_cpus = 2


        subprocess.run([vbox_manage_path, "createvm", "--name", new_vm_name, "--ostype", "Random", "--register"])
        subprocess.run([vbox_manage_path, "createhd", "--filename", vdipath, "--size", "20480"])

        subprocess.run([vbox_manage_path, "storagectl", new_vm_name, "--name", "SATA Controller", "--add", "sata", "--controller", "IntelAHCI"])
        subprocess.run([vbox_manage_path, "storageattach", new_vm_name, "--storagectl", "SATA Controller", "--port", "0", "--device", "0", "--type", "hdd", "--medium", vdipath])

        subprocess.run([vbox_manage_path, "storagectl", new_vm_name, "--name", "IDE Controller", "--add", "ide"])
        subprocess.run([vbox_manage_path, "storageattach", new_vm_name, "--storagectl", "IDE Controller", "--port", "1", "--device", "0", "--type", "dvddrive", "--medium", iso_path])

        subprocess.run([vbox_manage_path, "modifyvm", new_vm_name, "--nic1", "nat"])
        subprocess.run([vbox_manage_path, "modifyvm", new_vm_name, "--memory", str(ram_size)])
        subprocess.run([vbox_manage_path, "modifyvm", new_vm_name, "--cpus", str(num_cpus)])

        subprocess.run([vbox_manage_path, "startvm", new_vm_name])




        # Optionally wait for the VM to start (adjust the sleep time accordingly)
        time.sleep(30)


        print("Congratulations on creating your VM!")

        print(f"Creating VM: OS={self.os_type.get()}, Version={self.os_version.get()}, Path={self.vm_folder_path_var.get()}")
        # Simulate VM creation
        time.sleep(2)  # Simulate time delay for VM creation
        print("VM creation successful.")
        self.next_button.config(state="normal")
        return os.path.join(vm_folder, new_vm_name)  # Return the path of the new VM
    




##############################################################################################################################################################################################################
##############################################################################################################################################################################################################
    def Introduction_page(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        #Information 
        self.note_label1 = tk.Label(self.frame, text=" Information: ", bg="#b91919", fg="#ccff33",font=("Terminal",30), wraplength=1000, justify="center")
        self.note_label1.grid(row=0, column=1, columnspan=4,pady=(20,10))

        self.note_label1 = tk.Label(self.frame, text="Let's Understand what is memory dump", bg="black", fg="#ccff33",font=("Terminal",25), wraplength=1000, justify="center")
        self.note_label1.grid(row=1, column=1, columnspan=4,pady=(20,10))



        self.note_label1 = tk.Label(self.frame, text="A memory dump is a snapshot of the contents of a computer's memory at a specific point in time. It captures the state of running processes, system configurations, and data stored in RAM. Memory dumps are commonly used for diagnosing system crashes, debugging software, and analyzing security incidents. They provide valuable insights into the state of a system when an issue occurs, aiding in troubleshooting and resolving problems.\n\nAdditionally, a memory dump enable the safe execution of malicious scripts within isolated virtual machine environments, allowing analysts to study their effects on the system without risking damage to the underlying infrastructure. This approach facilitates a deeper understanding of malware behavior, enabling the development of effective countermeasures and proactive defense strategies.\n\n"
                                    , bg="black", fg="#b91919",font=("Terminal",15), wraplength=1100, justify="left")
        self.note_label1.grid(row=2, column=1,columnspan=4, pady=(20,20))
        
        self.note_label1 = tk.Label(self.frame, text=" Note: ", bg="#b91919", fg="#ccff33",font=("Terminal",20), wraplength=1000, justify="center")
        self.note_label1.grid(row=4, column=1, columnspan=4,pady=(20,20))

        self.note_label1 = tk.Label(self.frame, text="You can execute a malicious script within your virtual machine to observe its impact on the system. Afterward, utilizing tools like Volatility, you can analyze the effects of the script on the virtual machine.\n\nTo view a few examples, click on the Reference Script button. Ensure that when installing or running any script, you do so within the virtual machine and not on your host machine."
                                    , bg="black", fg="#b91919",font=("Terminal",15), wraplength=1100, justify="left")
        self.note_label1.grid(row=5, column=1,columnspan=4, pady=(10))


        # Back Button
        self.back_button = tk.Button(self.frame, text="\n  Reference Script  \n", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right",command=self.Reference_Script)
        self.back_button.grid(row=7, column=2, sticky='e' ,pady=(20,20))

        
        # Back Button
        self.back_button = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right",command=self.create_vm_page)
        self.back_button.grid(row=10, column=0, sticky='ew' ,pady=(20,10))

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="  Next  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right", command=self.create_memory_dump_page)
        self.next_button.grid(row=10, column=4, sticky='e', pady=(20,10))

##############################################################################################################################################################################################################
    def Reference_Script (self):

        try:
            document_url = 'https://nekraj.medium.com/notepad-virus-script-a6d60a8174a5'
            webbrowser.open(document_url)
        except Exception as e:
            logging.error(f"Failed to open the URL {document_url}: {e}")

        
##############################################################################################################################################################################################################
##############################################################################################################################################################################################################
        
    def create_memory_dump_page(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()


        # Available VMs
        self.available_vms_label = tk.Label(self.frame, text="\nProcess 3 : Click on Refresh button to see \n\nAvailable Virtual Machines in your Virtual box:\n",bg="#ffecce", fg="#b21e1e", wraplength=1200, font=("Terminal",25))
        self.available_vms_label.grid(row=0, column=1, sticky='ew',columnspan=5,padx=10 ,pady=20)
        self.available_vms_listbox = tk.Listbox(self.frame, height=11, width=50 ,bg="#fffdf4", fg="black",font=("Terminal",20))
        self.available_vms_listbox.grid(row=1, column=1, columnspan=5, sticky='e', padx=200, pady=15)

        # Refresh Button
        self.refresh_button = tk.Button(self.frame, text="\n Refresh \n",bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right", command=self.refresh_available_vms)
        self.refresh_button.grid(row=1, column=4, sticky='e', columnspan=5, padx=10, pady=0)

        #Path to save Memory dump
        self.create_vmpage =tk.Label(self.frame, text="Select Path where you want to store your Memory dump file :",bg="black", fg="#9cb344", wraplength=300, font=("Terminal",15),justify="right")
        self.create_vmpage.grid(row=2, column=0, columnspan=3,sticky='w', padx=10, pady=0)
        self.vm_folder_path = tk.StringVar()
        self.vm_folder_entry = tk.Entry(self.frame,bg="#fff2cc", fg="#b21e1e",font=("Terminal",15),textvariable=self.vm_folder_path, width=60, highlightthickness=5, justify="left")
        self.vm_folder_entry.grid(row=2, column=2 ,columnspan=3, sticky="w", padx=10, pady=5)
        self.browse_button = tk.Button(self.frame, text=" Browse ",bg="#84ac28", fg="black", font=("Terminal",20), command=self.browse_folder)
        self.browse_button.grid(row=2, column=4, sticky="e",columnspan=5, padx=10, pady=5)


        self.note_labe = tk.Label(self.frame, text="Note: Make sure your VM is ON while taking memory dump" , bg="black", fg="#b91919",font=("Terminal",15), wraplength=1000, justify="left")
        self.note_labe.grid(row=3, column=2,columnspan=3, sticky="we" ,padx=5, pady=5)

        # Snapshot Button
        self.snapshot_button = tk.Button(self.frame, text="Take Memory Dump",bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="center", command=self.take_dump)
        self.snapshot_button.grid(row=4, column=2, sticky='we',columnspan=3, padx=10, pady=25)
        
       

        self.create_vmpage =tk.Label(self.frame, text="\n",bg="black", fg="#9cb344")
        self.create_vmpage.grid(row=10, column=2)

        # Back Button
        self.back_button = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right",command=self.Introduction_page)
        self.back_button.grid(row=14, column=0, sticky='w' ,pady=(10, 0))

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="  Next  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right", command=self.create_Volatility_page)
        self.next_button.grid(row=14, column=4, sticky='e', columnspan=5,padx=50, pady=15)


        
##############################################################################################################################################################################################################

    def refresh_available_vms(self):
        vbox_manage_path = r"/Applications/VirtualBox.app/Contents/MacOS/VBoxManage"
        try:
            result = subprocess.run([vbox_manage_path, "list", "vms"], capture_output=True, text=True)
            output = result.stdout.strip()
            available_vms = output.split('\n')
            self.available_vms_listbox.delete(0, tk.END)
            for vm in available_vms:
                self.available_vms_listbox.insert(tk.END, vm)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve available VMs: {e}")

    def take_dump(self):
        selected_vm_info = self.available_vms_listbox.get(tk.ACTIVE)
        # Extract the VM name from the selected_vm_info, assuming it's in the format: "VM_NAME" {UUID}
        selected_vm_name = selected_vm_info.split(' ')[0].strip('"')
        print("Selected VM:", selected_vm_name)  # Print selected VM name for debugging
        vbox_manage_path = r"/usr/bin/vboxmanage"
        try:# Generate a random 5-letter filename
            dump_filename = ''.join(random.choices(string.ascii_letters, k=5))
            # Get the selected folder path
            selected_folder = self.vm_folder_path.get()
            if not selected_folder:
                messagebox.showerror("Error", "Please select a folder to store the memory dump.")
                return
            # Construct the full path for the dump file
            dump_file_path = os.path.join(selected_folder, dump_filename)
            # Construct the command
            cmd = [vbox_manage_path, "debugvm", selected_vm_name, "dumpvmcore", "--filename", dump_file_path]
            subprocess.run(cmd, check=True)
            messagebox.showinfo("Success", f"Dump file '{dump_filename}' created for VM: {selected_vm_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create dump file for VM: {selected_vm_name}: {e}")

    def goto_memory_dump_option(self):
        self.create_memory_dump_page()
    
##############################################################################################################################################################################################################
##############################################################################################################################################################################################################

    def create_Volatility_page(self):
    # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()


        #Information 
        self.note_label1 = tk.Label(self.frame, text=" Information: ", bg="#b91919", fg="#ccff33",font=("Terminal",28), wraplength=1300, justify="center")
        self.note_label1.grid(row=0, column=1, columnspan=4,pady=(20,10))

        # Add widgets for the Docker installation page
        self.Volatility_label=tk.Label(self.frame, text="Let's Analyze the memory dump ",bg="black", fg="#43af1c",wraplength=1000, font=("Terminal",25))
        self.Volatility_label.grid(row=1, column=1, sticky='ew',padx=10, pady=20)

        self.Volatility_label2=tk.Label(self.frame, text="To Anlayze the memory dump we can use volatality2 or Volatility3.",bg="#fff2cc", fg="#b80808",wraplength=1000, font=("Terminal",20))
        self.Volatility_label2.grid(row=2, column=1, sticky='ew', padx=10, pady=10)
        self.Volatility_label3=tk.Label(self.frame, text="Before starts let's understand what is Volatality and \nhow we can use it to analyze any memory dump file:\n  ", bg="black", fg="#ffff11",wraplength=1300, font=("Terminal",21),justify="center")
        self.Volatility_label3.grid(row=3, column=1,padx=5, pady=10,sticky='ew')
        
        # Add widgets for the Docker setup page
        self.Volatility_label4=tk.Label(self.frame, text="1.Volatility is a critical tool in cybersecurity and digital forensics specializing in the analysis of volatile memory (RAM) to uncover insightsinto system state malware behavior and security incidents.\n", 
                                    bg="black", fg="#ccff33", font=("Terminal",13),wraplength=1000, justify="left")
        self.Volatility_label4.grid(row=4, column=1,sticky='ew')

        # Add widgets for the Docker setup page
        self.Volatility_label5=tk.Label(self.frame, text="2.By examining processes network connections and system artifacts in memory Volatility aids in malware detection incidentresponse forensic investigations threat hunting and proactive defense.\n", 
                                    bg="black", fg="#ccff33", wraplength=1000,font=("Terminal",13), justify="left")
        self.Volatility_label5.grid(row=5, column=1,sticky='ew')
        self.Volatility_label5=tk.Label(self.frame, text="3.Its modular architecture allows for extensibility empowering analysts to develop custom plugins and adapt the tool to evolving security challenges.\n", 
                                    bg="black", fg="#ccff33", wraplength=1000,font=("Terminal",13), justify="left")
        self.Volatility_label5.grid(row=6, column=1,sticky='ew')

        self.Volatility_label5=tk.Label(self.frame, text="4.With its open-source nature and active community support Volatility remains an indispensable resource for uncovering evidence identifying threats and mitigating cybersecurity risks.\n", 
                                    bg="black", fg="#ccff33", wraplength=1000,font=("Terminal",13), justify="left")
        self.Volatility_label5.grid(row=7, column=1,sticky='ew')

        self.Volatility_label6= tk.Label(self.frame, text=" NOTE: ", bg="#b91919", fg="#ccff33",font=("Terminal",20), wraplength=1300, justify="center")
        self.Volatility_label6.grid(row=8, column=1, pady=(10))

        self.Volatility_label7=tk.Label(self.frame, text="Before you dive into Volatility, make sure docker or any platform that supports volatility tool is Installed! \n\nIf you have trouble installing docker make sure you follow our guide on next page!", 
                                    bg="black", fg="#b80808",wraplength=1300, font=("Terminal",15), justify="center")
        self.Volatility_label7.grid(row=9, column=1,sticky='w')


        # Add a button to go back to the previous page
        self.Volatility_back=tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right",command=self.goto_memory_dump_option)
        self.Volatility_back.grid(row=13, column=0,sticky='w' ,pady=(10, 0))

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="Next", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right", command=self.create_docker_page)
        self.next_button.grid(row=13, column=2, sticky='ew', pady=(10, 0))


##############################################################################################################################################################################################################

    def create_docker_page(self):
    # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()



        # Add widgets for the Docker installation page
        self.docker_label2=tk.Label(self.frame, text="\n   Process 4 : Please Select the Docker as per your Host Machine \n",bg="#ffecce", fg="#b21e1e", wraplength=1500, font=("Terminal",28), justify="center")
        self.docker_label2.grid(row=0, column=0, columnspan=4, sticky='ew', padx=30, pady=50)

        self.docker_label2=tk.Label(self.frame, text="NOTE: Host Machine means current operating system of your laptop or system where you will analyse the memory dump",bg="black", fg="#ccff33",wraplength=1000, font=("Terminal", 15), justify="left")
        self.docker_label2.grid(row=4, column=0,  columnspan=4,sticky='ew', padx=10, pady=10)

        # Button for Windows
        self.windows__button=tk.Button(self.frame, text="\nWindows\n", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="left",command=self.windows_docker_selction)
        self.windows__button.grid(row=7, column=1,sticky='we', padx=50)

        # Button for Linux
        self.linux__button=tk.Button(self.frame, text="\nLinux\n", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="left", command=self.linux_docker_selction)
        self.linux__button.grid(row=7, column=2,sticky='ew' ,padx=50)

        # Button for macOS
        self.macos__button=tk.Button(self.frame, text="\nMac-OS\n", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="left",command=self.MacOs_docker_selction)
        self.macos__button.grid(row=15, column=1,sticky='ew' ,padx=50)
        

        
        # Button for macOS
        self.macos__button=tk.Button(self.frame, text="\nDocker Creation\n", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="left",command=self.Docker_creation_sample_file)
        self.macos__button.grid(row=15, column=2,sticky='ew' ,padx=50)

        self.docker_label2=tk.Label(self.frame, text=" \n  ",bg="black", fg="#ccff33", font=("Terminal",10))
        self.docker_label2.grid(row=17, column=0, sticky='ew')

        # Add a button to go back to the previous page
        self.docker_back=tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right",command=self.create_Volatility_page)
        self.docker_back.grid(row=20, column=0,sticky='w' ,pady=(10, 10))


    
        # Column headers1
        columns = [" For Windows system  ","  For linux system  "]
        for i, column in enumerate(columns):
            header_label = tk.Label(self.frame, text=column, bg="black", fg="#990000", font=("Terminal", 20), justify="center")
            header_label.grid(row=5, column=i+1, sticky='ew', padx=0, pady=20)

        # Sample Data for the Cheatsheet (you would populate this with actual data)
        commands_info = []
        # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (windows,linux, mac_os,docker) in enumerate(commands_info):
            current_row = row_offset + i
            tk.Label(self.frame, text=windows, bg="black", fg="#ccff33", font=("Terminal",11), justify="center").grid(row=current_row, column=0, sticky='ew', padx=5)
            tk.Label(self.frame, text=linux, bg="black", fg="#ccff33", font=("Terminal", 11), justify="center").grid(row=current_row, column=1, sticky='ew', padx=5)
            
        # Column headers2
        columns = ["  For Mac-OS system  ", "Learn how to create\nyour own docker"]
        for i, column in enumerate(columns):
            header_label = tk.Label(self.frame, text=column, bg="black", fg="#990000", font=("Terminal", 20), justify="center")
            header_label.grid(row=10, column=i+1, sticky='ew', padx=0, pady=20)

        # Sample Data for the Cheatsheet (you would populate this with actual data)
        commands_info = []
        # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (windows,linux, mac_os,docker) in enumerate(commands_info):
            current_row = row_offset + i
            tk.Label(self.frame, text=mac_os, bg="black", fg="#ccff33", font=("Terminal", 11), justify="center").grid(row=current_row, column=2, sticky='ew', padx=5)
            tk.Label(self.frame, text=docker, bg="black", fg="#ccff33", font=("Terminal", 11), justify="center").grid(row=current_row, column=2, sticky='ew', padx=5)



#########################################################################################################################################################################################################
########################################################################################################################################################################################################        

    def windows_docker_selction(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        # Add widgets for the Docker installation page
        self.docker_label=tk.Label(self.frame, text=" Select your mode of \n\nDocker implementation !! \n\n ",bg="black", fg="#ccff33", font=("Terminal",28),justify="center")
        self.docker_label.grid(row=0, column=1, sticky='ew',columnspan=3,padx=10, pady=10)

        self.docker_button=tk.Button(self.frame, text="\n  Automated \n  Docker Installation  \n", bg="#ccff33", fg="black",font=("Terminal",20), justify="center",command=self.show_windows_docker_info)
        self.docker_button.grid(row=2, column=1, sticky='ew',padx=10,pady=10)


        self.docker_button=tk.Button(self.frame, text="\n  Manual \n  Docker Installation   \n", bg="#ccff33", fg="black",font=("Terminal",20), justify="center",command=self.show_windows_docker_manual_info)
        self.docker_button.grid(row=2, column=2, sticky='ew',padx=10, pady=10)

        self.docker_button=tk.Button(self.frame, text="\n  Linux Profile  \n  creation  \n", bg="#ccff33", fg="black",font=("Terminal",20), justify="center",command=self.linux_profile_page)
        self.docker_button.grid(row=2, column=3, sticky='ew',padx=10, pady=10)


        self.docker_label=tk.Label(self.frame, text="\n\n \n\n ",bg="black", fg="#ccff33", font=("Terminal",30),justify="center")
        self.docker_label.grid(row=5, column=1, sticky='ew',padx=10, pady=10)

        self.windows_back = tk.Button(self.frame, text="  Back   ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.create_docker_page)
        self.windows_back.grid(row=10, column=0, sticky='w', pady=(10, 0))


        
########################################################################################################################################################################################################

    def show_windows_docker_info(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
       
        # Add widgets for the Docker installation page
        self.docker_label=tk.Label(self.frame, text=" Automated Docker Configuration for Windows\n" ,wraplength=1200, bg="black", fg="#ccff33", font=("Terminal",30),justify="center")
        self.docker_label.grid(row=0, column=1, sticky='ew',padx=10, pady=10)
        self.docker_label=tk.Label(self.frame, text=" \n ",bg="black", fg="#ccff33", font=("Terminal",20),justify="center")
        self.docker_label.grid(row=0, column=2, sticky='ew',padx=10, pady=10)

        self.docker_label2=tk.Label(self.frame, text="Note : Before start please check you have Docker Desktop Installed.\n\n",wraplength=1300,bg="black", fg="#b91919", font=("Terminal",20),justify="left")
        self.docker_label2.grid(row=2, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="Step1: If NO, then please click on Install Docker Desktop and run it after installation.Once done please select path to memory dump and click on pull docker button. ",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label4.grid(row=3, column=1, sticky='w',padx=5, pady=0)

        self.label3=tk.Label(self.frame, text="Note: When you Download the Docker Desktop for the 1st time Please retart your system after running the Docker Desktop to access the docker image otherwise you will face some error.\n" , bg="black", fg="#990000",font=("Terminal",15), wraplength=800, justify="left")
        self.label3.grid(row=4, column=1, sticky='w',padx=5, pady=0)


        # Add a button to install Docker Desktop
        self.install_docker_button = tk.Button(self.frame, text="       Install   \n    Docker     \n  Desktop     ", bg="#990000", fg="black", font=("Terminal",20), command=self.install_and_start_docker)
        self.install_docker_button.grid(row=3, column=2, sticky='w', pady=10)
        
        self.docker_label3=tk.Label(self.frame, text="Step2 :If YES, please select Memory Dump which you want to analyze using Volatility\n",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label3.grid(row=5, column=1, sticky='w',padx=5, pady=0)

        # Add a button to select the memory dump file
        self.select_dump_button = tk.Button(self.frame, text=" Select \n Memory Dump ", bg="#990000", fg="black", font=("Terminal",20), command=self.select_memory_dump)
        self.select_dump_button.grid(row=5, column=2, sticky='w', pady=(10, 10))

        self.docker_label3=tk.Label(self.frame, text="Step 3:Once done pull the Docker.\n",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label3.grid(row=7, column=1, sticky='w',padx=5, pady=0) 


        # Add a button to pull the Docker image and open it in terminal
        self.pull_docker_button = tk.Button(self.frame, text="Pull \n Docker Image", bg="#990000", fg="black", font=("Terminal",20), command=self.pull_docker_image)
        self.pull_docker_button.grid(row=7, column=2, sticky='w', pady=(10, 10))
 
        self.note_labe = tk.Label(self.frame, text=" \n", bg="black",font=("Terminal",20), justify="center")
        self.note_labe.grid(row=8, column=1,)

        self.docker_label3=tk.Label(self.frame, text="Once you pull the docker click on next to see the volatility commands",wraplength=200,bg="black", fg="#b21e1e", font=("Terminal",10),justify="left")
        self.docker_label3.grid(row=10, column=2, sticky='w',padx=10, pady=10)

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="  Next  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right", command=self.volatility_cheatsheet)
        self.next_button.grid(row=11, column=2, sticky='w', pady=(10, 0))

        # Add a button to go back to the previous page
        self.windows_docker_back = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.windows_docker_selction)
        self.windows_docker_back.grid(row=11, column=0, sticky='w', pady=(10, 0))
        
########################################################################################################################################################################################################

    def select_memory_dump(self):
        # Prompt the user to select the memory dump file
        self.selected_file_path = filedialog.askopenfilename(title="Select Memory Dump File", filetypes=[("Memory Dump Files", "*.*")])
        if self.selected_file_path:
            messagebox.showinfo("Selected File", f"Selected file: {self.selected_file_path}")
            # You can perform any additional actions here with the selected file

    def pull_docker_image(self):
        if self.selected_file_path:
            # Extract the file name from the file path
            file_name = self.selected_file_path.split("/")[-1]
            # Convert the file path to lowercase
            print(file_name)
            # Command to pull Docker image and mount selected file into container
            self.start_docker_desktop()
            time.sleep(30)
            pull_command = "docker pull pmeher/volatility"
            subprocess.Popen(["start", "cmd", "/k", pull_command], shell=True)
            volume = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
            print(self.selected_file_path)
            path_in_lowers=self.selected_file_path.lower().replace(' ','_')
            print(path_in_lowers)
            open_command = f'docker run -it --name {volume} -v {path_in_lowers}:/app/{file_name} pmeher/volatility'
            subprocess.Popen(['start', 'cmd', '/k', open_command], shell=True)
            
        else:
            messagebox.showwarning("File Not Selected", "Please select a memory dump file before pulling the Docker image.")




    def install_and_start_docker(self):
        # Install Docker Desktop
        self.install_docker_desktop()
        # Start Docker Desktop
        self.start_docker_desktop()

    def install_docker_desktop(self):
        # Download Docker Desktop installer
        webbrowser.open("https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module")

        # You can inform the user about the download and installation process
        print("Downloading Docker Desktop installer...")

        # You can use a message box to inform the user about the installation process
        messagebox.showinfo("Docker Desktop Installation", "Docker Desktop installer is being downloaded. Please run the installer after the download completes.")


    def start_docker_desktop(self):
        # Start Docker Desktop
        # Adjust the command based on your Docker Desktop installation path
        docker_desktop_command = "C:/Program Files/Docker/Docker/Docker Desktop.exe"
        subprocess.Popen([docker_desktop_command], shell=True)

##################################################################################################################################################################################################

    def show_windows_docker_manual_info(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()    
        # Manual Process

        self.docker_label1=tk.Label(self.frame, text="  Manual Docker Installation  ",bg="black", fg="#43af1c",font=("Terminal",35), justify="center")
        self.docker_label1.grid(row=1, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="Please follow the below steps :\n",bg="black", fg="#990000", font=("Terminal",25),justify="center")
        self.docker_label4.grid(row=2, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="1.Install the Docker Desktop from :  https://www.docker.com/products/docker-desktop/\n\n\n2.Please run the installer after the download completes.\n\n\n3.Open your terminal and dive into this path C:\Program Files\Docker\Docker and run this command : ",
                                    bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=3, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="$ .\DockerCli.exe -SwitchLinuxEngine",bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=4, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="4.Now pull the docker using :",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=5, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="$docker pull pmeher/volatility ",bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=6, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="5.Access your memory dump in docker using :",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=7, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="$docker run -it --name any_random_name -v C:\\Users\\path_of_your_memory_dump:/app/memory_dump_name pmeher/volatility \n\nExample : $docker run -it --name user -v C:\\Users\\admin\Desktop\memory_dump:/app/memory_dump pmeher/volatility ",bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=8, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="6.Click on next to see the volatility commands to analyze the memory dump file \n\n\n\n",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=9, column=1, sticky='w',padx=10, pady=10)


        self.windows_back = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.windows_docker_selction)
        self.windows_back.grid(row=13, column=0, sticky='w', pady=(10, 0))
     
        self.windows_next = tk.Button(self.frame, text="Next", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.volatility_cheatsheet)
        self.windows_next.grid(row=13, column=2, sticky='w', pady=(10, 0))
######################################################################################################################################
    def linux_profile_page(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
            
        # Add widgets for the Docker installation page
        self.docker_label=tk.Label(self.frame, text=" Profile creation for Linux virtual machine !! \n\n ",bg="black", fg="#ccff33", font=("Terminal",30),wraplength=1500,justify="center")
        self.docker_label.grid(row=0, column=1, sticky='ew',columnspan=2,padx=10, pady=20)
        
        # Add widgets for the Docker installation page
        self.docker_label=tk.Label(self.frame, text="Process of creating a custom Linux profile for Volatility3, a widely used framework for extracting digital artifacts from volatile memory (RAM) samples. Analyzing memory dumps of Linux systems is a crucial task for digital forensics and incident response. There are two references are given to shows the steps to create a custom profile.",bg="black", fg="#ccff33", font=("Terminal",20),wraplength=1200,justify="center")
        self.docker_label.grid(row=1, column=1, sticky='ew',columnspan=3,padx=30, pady=10)


        self.docker_button=tk.Button(self.frame, text="\n  Document  \n", bg="#990000", fg="black",font=("Terminal",20), justify="center",command=self.linux_profile_Document)
        self.docker_button.grid(row=2, column=1, sticky='e',padx=10, pady=20)
        self.docker_button=tk.Button(self.frame, text="\n Github Link\n ", bg="#990000", fg="black",font=("Terminal",20), justify="center",command=self.linux_profile_github)
        self.docker_button.grid(row=2, column=2, sticky='w',padx=10, pady=20)
        
        self.windows_back = tk.Button(self.frame, text="  Back   ", bg="#ccff33", fg="#b21e1e", font=("Terminal",25), justify="right", command=self.windows_docker_selction)
        self.windows_back.grid(row=6, column=2, sticky='e', pady=(15, 10))
        
    def linux_profile_Document(self):
        # Replace 'document_url' with the actual URL of the document
        document_url = 'https://drive.google.com/file/d/1Fld5bHlBQa8TYICfyqvBuSIPFZ51EvKH/view?usp=sharing'

        # Open the URL in the default web browser
        webbrowser.open(document_url)
        
    def linux_profile_github(self):
        # Replace 'document_url' with the actual URL of the document
        document_url = "https://github.com/Sandesh028/Tutorials-How-to.../blob/main/How%20to%20Create%20Linux%20Profile(Volatility%203).md"

        # Open the URL in the default web browser
        webbrowser.open(document_url)

######################################################################################################################################    


    def volatility_cheatsheet(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.cheatsheet_label = tk.Label(self.frame, text="VOLATILITY CHEATSHEET", bg="black", fg="#ccff33", font=("Terminal", 25), justify="left")
        self.cheatsheet_label.grid(row=0, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

        # Column headers
        columns = ["Use","Command Name", "Volatility 2 Command", "Volatility 3 Command"]
        for i, column in enumerate(columns):
            header_label = tk.Label(self.frame, text=column, bg="black", fg="#990000", font=("Terminal", 20), justify="left")
            header_label.grid(row=1, column=i, sticky='ew', padx=10, pady=20)


        # Sample Data for the Cheatsheet (you would populate this with actual data)
        commands_info = [
            ("OS INFORMATION",
            "IMAGEINFO", 
            'vol.py -f “dump_file” imageinfo\n', 
            'vol -f “dump_file” windows.info\n', 
            ),
            ("PROCESS INFORMATION",
            "PSLIST", 
            'vol.py -f “dump_file” --profile <profile> pslist\n', 
            'vol -f “dump_file” windows.pslist', 
            ),
            ("PROCESS INFORMATION","PSSCAN", 
            'vol.py -f “dump_file” --profile <profile> pslist\n', 
            'vol -f “dump_file” windows.psscan\n', 
            ),
            ("PROCESS INFORMATION","PSTREE", 
            'vol.py -f “dump_file” ‑‑profile <profile> pstree\n', 
            'vol -f “dump_file” windows.pstree\n', 
            ),
            ("PROCESS INFORMATION","PROCDUMP", 
            'vol.py -f “dump_file” ‑‑profile <profile> procdump \n-p <PID> ‑‑dump-dir=“/path/to/dir\n', 
            'vol -f “dump_file” -o “/path/to/dir” \nwindows.dumpfiles ‑‑pid <PID>', 
            ),
            ("PROCESS INFORMATION","MEMDUMP", 
            'vol.py -f “dump_file” ‑‑profile <profile> memdump \n-p <PID> ‑‑dump-dir=“/path/to/dir\n', 
            'vol -f “dump_file” -o “/path/to/dir” \nwindows.memmap ‑‑dump ‑‑pid <PID>\n', 
            ),
            ("PROCESS INFORMATION","DLLS", 
            'vol.py -f “dump_file” ‑‑profile <profile> dlllist \n-p <PID>\n', 
            'vol -f “dump_file” windows.dlllist ‑‑pid <PID>\n', 
            ),
            ("PROCESS INFORMATION","CMDLINE", 
            'vol.py -f “dump_file” ‑‑profile <profile> cmdline\n\nvol.py -f “dump_file” ‑‑profile <profile> cmdscan\n\nvol.py -f “dump_file” ‑‑profile <profile> consoles\n', 
            'vol -f “dump_file” windows.cmdline\n', 
            ),
            ("NETWORK INFORMATION","NETSCAN", 
            'vol.py -f “dump_file” ‑‑profile <profile> netscan\nvol.py -f “dump_file” ‑‑profile <profile> netstat\n', 
            'vol.py -f “dump_file” windows.netscan\n\nvol -f “dump_file” windows.netstat\n', 
            ),
            ("REGISTRY","HIVELIST", 
            'vol.py -f “dump_file” ‑‑profile <profile> hivescan\n\nvol.py -f “dump_file” ‑‑profile <profile> hivelist\n', 
            'vol.py -f “dump_file” windows.registry.hivescan\n\nvol -f “dump_file” windows.registry.hivelist\n', 
            ),

            ("REGISTRY","PRINTKEY", 
            'vol.py -f “dump_file” ‑‑profile <profile> printkey\n\nvol.py -f “dump_file” ‑‑profile <profile> printkey -K \n“Software\Microsoft\Windows\CurrentVersion\n', 
            'vol -f “dump_file” windows.registry.printkey\n\nvol -f “dump_file” windows.registry.printkey ‑‑key \n“Software\Microsoft\Windows\CurrentVersion\n', 
            ),

            ("REGISTRY","HIVEDUMP", 
            'vol.py -f “dump_file” ‑‑profile hivedump -o <offset>\n', 
            'I’m not sure if this capability exists in Vol3;however, \nyou may be able to extractregistry hives using \nfiledump with the offset\n', 
            ),
       
            ]

            # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (Use,cmd_name, vol2_cmd, vol3_cmd) in enumerate(commands_info):
            current_row = row_offset + i


            use_label = tk.Label(self.frame, text=Use, bg="black", fg="#ccff33", font=("Terminal",15), justify="left")
            use_label.grid(row=current_row, column=0, sticky='ew', padx=5)
    
            cmd_name_label = tk.Label(self.frame, text=cmd_name, bg="black", fg="#ccff33", font=("Terminal", 15), justify="center")
            cmd_name_label.grid(row=current_row, column=1, sticky='ew', padx=5)
    
            # Create Text widget for Volatility 2 command
            vol2_text_widget = tk.Text(self.frame, height=4, width=60, bg="black", fg="#ccff33",font=("Terminal", 11), wrap="none")
            vol2_text_widget.insert("1.0", vol2_cmd)
            vol2_text_widget.grid(row=current_row, column=2, sticky='w', padx=10)

            # Create Text widget for Volatility 3 command
            vol3_text_widget = tk.Text(self.frame, height=4, width=60, bg="black", fg="#ccff33", font=("Terminal", 11), wrap="none")
            vol3_text_widget.insert("1.0", vol3_cmd)
            vol3_text_widget.grid(row=current_row, column=3, sticky='w', padx=10)


        self.windows_docker_back = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.windows_docker_selction)
        self.windows_docker_back.grid(row=18, column=0, sticky='w', pady=(10, 0))
        self.windows_docker_NEXT = tk.Button(self.frame, text="next", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.volatility_cheatsheet1)
        self.windows_docker_NEXT.grid(row=18, column=3, sticky='e', pady=(10, 0))


############################################################################################################################################################################################################################################################################
        
    def volatility_cheatsheet1(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.cheatsheet_label = tk.Label(self.frame, text="VOLATILITY CHEATSHEET", bg="black", fg="#ccff33", font=("Terminal", 25), justify="left")
        self.cheatsheet_label.grid(row=0, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

        # Column headers
        columns = ["Use","Command Name", "Volatility 2 Command", "Volatility 3 Command"]
        for i, column in enumerate(columns):
            header_label = tk.Label(self.frame, text=column, bg="black", fg="#990000", font=("Terminal", 20), justify="left")
            header_label.grid(row=1, column=i, sticky='ew', padx=10, pady=20)

        # Sample Data for the Cheatsheet (you would populate this with actual data)
        commands_info = [
            
            ("FILES","FILESCAN", 
            'vol.py -f “dump_file” ‑‑profile <profile> filescan', 
            'vol -f “dump_file” windows.filescan', 
            ),
            
            ("FILES","FILEDUMP", 
            'vol.py -f “dump_file” ‑‑profile <profile> \ndumpfiles ‑‑dump-dir=“/path/to/dir\n\nvol.py -f “dump_file” ‑‑profile <profile> dumpfiles \n‑‑dump-dir=“/path/to/dir” -Q <offset>\n\nvol.py -f “dump_file” ‑‑profile <profile> dumpfiles \n‑‑dump-dir=“/path/to/dir” -p <PID>', 
            'vol -f ““dump_file”” -o ““dump_file”” windows.dumpfiles\n\nvol -f “dump_file” -o “/path/to/dir” \nwindows.dumpfiles ‑‑virtaddr <offset>\n\nvol -f “dump_file” -o “/path/to/dir”\nwindows.dumpfiles ‑‑physaddr <offset>', 
            ),
            ("MISCELLANEOUS","MALFIND", 
            'vol.py -f “dump_file” ‑‑profile <profile> malfind\n', 
            'vol.py -f “dump_file” windows.malfind\n', 
            ),
            ("MISCELLANEOUS","YARASCAN", 
            'vol.py -f “dump_file” ‑‑profile <profile> filescan\n', 
            'vol -f “dump_file” windows.filescan\n', 
            )
            
            
            ]

        # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (Use,cmd_name, vol2_cmd, vol3_cmd) in enumerate(commands_info):
            current_row = row_offset + i


            use_label = tk.Label(self.frame, text=Use, bg="black", fg="#ccff33", font=("Terminal",15), justify="left")
            use_label.grid(row=current_row, column=0, sticky='ew', padx=5)
    
            cmd_name_label = tk.Label(self.frame, text=cmd_name, bg="black", fg="#ccff33", font=("Terminal", 15), justify="center")
            cmd_name_label.grid(row=current_row, column=1, sticky='ew', padx=5)
    
            # Create Text widget for Volatility 2 command
            vol2_text_widget = tk.Text(self.frame, height=4, width=60, bg="black", fg="#ccff33",font=("Terminal", 11), wrap="none")
            vol2_text_widget.insert("1.0", vol2_cmd)
            vol2_text_widget.grid(row=current_row, column=2, sticky='w', padx=10)

            # Create Text widget for Volatility 3 command
            vol3_text_widget = tk.Text(self.frame, height=4, width=60, bg="black", fg="#ccff33", font=("Terminal", 11), wrap="none")
            vol3_text_widget.insert("1.0", vol3_cmd)
            vol3_text_widget.grid(row=current_row, column=3, sticky='w', padx=10)


        self.cheatsheet_label = tk.Label(self.frame, text="\n\n\n\n Note :If you want to try more plugins please try this coammnd:\n\n$ vol.py -h\n\n", bg="black", fg="#990000", font=("Terminal", 15), justify="left")
        self.cheatsheet_label.grid(row=10, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

        self.windows_docker_back = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.volatility_cheatsheet)
        self.windows_docker_back.grid(row=13, column=0, sticky='w', pady=(10, 0))

        self.windows_docker_sample = tk.Button(self.frame, text="Click hre to see \nsample Document", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.sample_Volatality_Document)
        self.windows_docker_sample.grid(row=11, column=2, sticky='e', pady=(10, 0))

#########################################################################################################################################################################################################
    def sample_Volatality_Document(self):
        # Replace 'document_url' with the actual URL of the document
        document_url = 'https://drive.google.com/file/d/15A2-x-lE822pvDxW7vceBvFG6Bl-alDa/view?usp=sharing'

        # Open the URL in the default web browser
        webbrowser.open(document_url)

#########################################################################################################################################################################################################
 #########################################################################################################################################################################################################
    def linux_docker_selction(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        # Add widgets for the Docker installation page
        self.docker_label=tk.Label(self.frame, text=" Select your mode of \n\nDocker implementation !! \n\n ",bg="black", fg="#ccff33", font=("Terminal",28),justify="center")
        self.docker_label.grid(row=0, column=1, sticky='ew',columnspan=3,padx=10, pady=10)
        

        self.docker_button=tk.Button(self.frame, text="\n  Automated \n  Docker Installation  \n", bg="#990000", fg="black",font=("Terminal",20), justify="center",command=self.show_linux_docker_info)
        self.docker_button.grid(row=2, column=1, sticky='ew',padx=10,pady=10)



        self.docker_button=tk.Button(self.frame, text="\n  Manual \n  Docker Installation   \n", bg="#990000", fg="black",font=("Terminal",20), justify="center",command=self.show_Linux_docker_manual_info)
        self.docker_button.grid(row=2, column=2, sticky='ew',padx=10, pady=10)
        
        
        self.docker_button=tk.Button(self.frame, text="\n  Linux Profile  \n  creation  \n", bg="#990000", fg="black",font=("Terminal",20), justify="center",command=self.linux_profile_page)
        self.docker_button.grid(row=2, column=3, sticky='ew',padx=10, pady=10)


        self.docker_label=tk.Label(self.frame, text="\n\n \n\n ",bg="black", fg="#ccff33", font=("Terminal",30),justify="center")
        self.docker_label.grid(row=5, column=1, sticky='ew',padx=10, pady=10)

        self.windows_back = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.create_docker_page)
        self.windows_back.grid(row=10, column=0, sticky='w', pady=(10, 0))


##################################################################################################################################################################################################
    def show_linux_docker_info(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
      
# Add widgets for the Docker installation page
        self.docker_label=tk.Label(self.frame, text=" Automated Docker Configuration for Windows\n" ,wraplength=1200, bg="black", fg="#ccff33", font=("Terminal",30),justify="center")
        self.docker_label.grid(row=0, column=1, sticky='ew',padx=10, pady=10)
        self.docker_label=tk.Label(self.frame, text=" \n ",bg="black", fg="#ccff33", font=("Terminal",20),justify="center")
        self.docker_label.grid(row=0, column=2, sticky='ew',padx=10, pady=10)

        self.docker_label2=tk.Label(self.frame, text="Note : Before start please check you have Docker Desktop Installed.\n\n",wraplength=1300,bg="black", fg="#b91919", font=("Terminal",20),justify="left")
        self.docker_label2.grid(row=2, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="Step1: If NO, then please click on Install Docker Desktop and run it after installation.Once done please select path to memory dump and click on pull docker button. ",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label4.grid(row=3, column=1, sticky='w',padx=5, pady=0)

        self.label3=tk.Label(self.frame, text="Note: When you Download the Docker Desktop for the 1st time Please retart your system after running the Docker Desktop to access the docker image otherwise you will face some error.\n" , bg="black", fg="#990000",font=("Terminal",10), wraplength=800, justify="left")
        self.label3.grid(row=4, column=1, sticky='w',padx=5, pady=0)


        # Add a button to install Docker Desktop
        self.install_docker_button = tk.Button(self.frame, text="  Install   \n  Docker  \n  Desktop  ", bg="#990000", fg="black", font=("Terminal",20), command=self.install_docker)
        self.install_docker_button.grid(row=3, column=2, sticky='w', pady=10)
        
        self.docker_label3=tk.Label(self.frame, text="Step2 :If YES, please select Memory Dump which you want to analyze using Volatility\n",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label3.grid(row=5, column=1, sticky='w',padx=5, pady=0)

        # Add a button to select the memory dump file
        self.select_dump_button = tk.Button(self.frame, text=" Select \n Memory Dump ", bg="#990000", fg="black", font=("Terminal",20), command=self.select_path)
        self.select_dump_button.grid(row=5, column=2, sticky='w', pady=(10, 10))

        self.docker_label3=tk.Label(self.frame, text="Step 3:Once done pull the Docker.\n",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label3.grid(row=7, column=1, sticky='w',padx=5, pady=0) 


        # Add a button to pull the Docker image and open it in terminal
        self.pull_docker_button = tk.Button(self.frame, text="Pull \n Docker Image", bg="#990000", fg="black", font=("Terminal",20), command=self.pull_linuxdocker_image)
        self.pull_docker_button.grid(row=7, column=2, sticky='w', pady=(10, 10))
 
        self.note_labe = tk.Label(self.frame, text=" \n", bg="black",font=("Terminal",20), justify="center")
        self.note_labe.grid(row=8, column=1,)

        self.docker_label3=tk.Label(self.frame, text="Once you pull the docker click on next to see the volatility commands",wraplength=200,bg="black", fg="#b21e1e", font=("Terminal",10),justify="left")
        self.docker_label3.grid(row=10, column=2, sticky='w',padx=10, pady=10)

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="  Next  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right", command=self.linux_volatility_cheatsheet)
        self.next_button.grid(row=11, column=2, sticky='w', pady=(10, 0))

        # Add a button to go back to the previous page
        self.windows_docker_back = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.linux_docker_selction)
        self.windows_docker_back.grid(row=11, column=0, sticky='w', pady=(10, 0))
        


################################################################################################################################################################################################## 
    def show_Linux_docker_manual_info(self):

        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()    
        # Manual Process

        self.docker_label1=tk.Label(self.frame, text="  Manual Docker Installation  ", wraplength=1500, bg="black", fg="#43af1c",font=("Terminal",35), justify="center")
        self.docker_label1.grid(row=1, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="Please follow the below steps :\n",bg="black", fg="#990000", font=("Terminal",25),justify="center")
        self.docker_label4.grid(row=2, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="1.Open your terminal and run the below command :",wraplength=1000, bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=3, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="$ sudo apt install docker-compose",wraplength=1000, bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=4, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="2.Once the docker is installed, we can verify that by running a sample docker image: :",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=5, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="$ sudo docker run hello-world",wraplength=1000, bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=6, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="3.Now pull the docker using :",wraplength=1000, bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=7, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="$docker pull pmeher/volatility ",wraplength=1000, bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=8, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="4.Access your memory dump in docker using :",wraplength=1000, bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=9, column=1, sticky='w',padx=10, pady=10)
        
        self.docker_label4=tk.Label(self.frame, text="$docker run -it --name any_random_name -v path_of_your_memory_dump:/app/memory_dump_name pmeher/volatility \n\nExample : $docker run -it --name user -v /media/kali/:/app/memory_dump pmeher/volatility ",bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=10, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="6.Click on next to see the volatility commands to analyze the memory dump file \n\n\n\n",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=11, column=1, sticky='w',padx=10, pady=10)



        self.windows_back = tk.Button(self.frame, text="Back",wraplength=1000,bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.linux_docker_selction)
        self.windows_back.grid(row=13, column=0, sticky='w', pady=(10, 0))
     
        self.windows_next = tk.Button(self.frame, text="Next",wraplength=1000, bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.linux_volatility_cheatsheet)
        self.windows_next.grid(row=13, column=2, sticky='w', pady=(10, 0))

##################################################################################################################################################################################################
    def install_docker(self):
        # Check if Docker is already installed
        docker_installed = subprocess.call(['docker', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
        
        if docker_installed:
            self.message_label.config(text="Docker is already installed.")
            return
        
        # Prompt for sudo password
        sudo_password = tk.simpledialog.askstring("Sudo Password", "Enter your root password:", show='*')
        
        if sudo_password:
            command = f'echo {sudo_password} | sudo -S apt-get update && echo {sudo_password} | sudo -S apt-get install docker.io -y'
            subprocess.call(command, shell=True)
            self.message_label.config(text="Docker installed successfully.")
        else:
            self.message_label.config(text="Installation cancelled.")

    def select_path(self):
      # Prompt the user to select the memory dump file
        self.selected_file_path = filedialog.askopenfilename(
            title="Select Memory Dump File", filetypes=[("All Files", "*")])
        if self.selected_file_path:
            messagebox.showinfo("Selected File", f"Selected file: {self.selected_file_path}")
            # You can perform any additional actions here with the selected file

    def pull_linuxdocker_image(self):
        if self.selected_file_path:
            # Extract the file name from the file path
            file_name = os.path.basename(self.selected_file_path)
            # Convert the file path to lowercase
            print(file_name)
            # Command to pull Docker image and mount selected file into container
            pull_command = "docker pull pmeher/volatility"
            subprocess.run(pull_command, shell=True)
            volume = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
            print(self.selected_file_path)
            #path_in_lower = self.selected_file_path.lower().replace(' ', '_')
            print(self.selected_file_path)
            open_command = f'docker run -it --name {volume} -v {self.selected_file_path}:/app/{file_name} pmeher/volatility'
            #subprocess.Popen(open_command, shell=True)
            os.system(f"x-terminal-emulator -e 'bash -c \"{open_command}; exec bash\"'")
            
        else:
            messagebox.showwarning("File Not Selected", "Please select a memory dump file before pulling the Docker image.")

######################################################################################################################################    

    def linux_volatility_cheatsheet(self):

        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.cheatsheet_label = tk.Label(self.frame, text="VOLATILITY CHEATSHEET", bg="black", fg="#ccff33", font=("Terminal", 25), justify="left")
        self.cheatsheet_label.grid(row=0, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

        # Column headers
        columns = ["Use","Command Name", "Volatility 2 Command", "Volatility 3 Command"]
        for i, column in enumerate(columns):
            header_label = tk.Label(self.frame, text=column, bg="black", fg="#990000", font=("Terminal", 20), justify="left")
            header_label.grid(row=1, column=i, sticky='ew', padx=10, pady=20)


                    # Sample Data for the Cheatsheet (you would populate this with actual data)
        commands_info = [
                ("OS INFORMATION",
                "IMAGEINFO", 
                'vol.py -f “dump_file” imageinfo\n', 
                'vol -f “dump_file” linux.info\n', 
                ),
                ("PROCESS INFORMATION",
                "PSLIST", 
                'vol.py -f “dump_file” --profile <profile> pslist\n', 
                'vol -f “dump_file” linux.pslist', 
                ),
                ("PROCESS INFORMATION","PSSCAN", 
                'vol.py -f “dump_file” --profile <profile> pslist\n', 
                'vol -f “dump_file” linux.psscan\n', 
                ),
                ("PROCESS INFORMATION","PSTREE", 
                'vol.py -f “dump_file” ‑‑profile <profile> pstree\n', 
                'vol -f “dump_file” linux.pstree\n', 
                ),
                ("PROCESS INFORMATION","PROCDUMP", 
                'vol.py -f “dump_file” ‑‑profile <profile> procdump \n-p <PID> ‑‑dump-dir=“/path/to/dir\n', 
                'vol -f “dump_file” -o “/path/to/dir” \nlinux.dumpfiles ‑‑pid <PID>', 
                ),
                ("PROCESS INFORMATION","MEMDUMP", 
                'vol.py -f “dump_file” ‑‑profile <profile> memdump \n-p <PID> ‑‑dump-dir=“/path/to/dir\n', 
                'vol -f “dump_file” -o “/path/to/dir” \nlinux.memmap ‑‑dump ‑‑pid <PID>\n', 
                ),
                ("PROCESS INFORMATION","DLLS", 
                'vol.py -f “dump_file” ‑‑profile <profile> dlllist \n-p <PID>\n', 
                'vol -f “dump_file” linux.dlllist ‑‑pid <PID>\n', 
                ),
                ("PROCESS INFORMATION","CMDLINE", 
                'vol.py -f “dump_file” ‑‑profile <profile> cmdline\nvol.py -f “dump_file” ‑‑profile <profile> cmdscan\nvol -f “dump_file” ‑‑profile <profile> consoles\n', 
                'vol -f “dump_file” linux.cmdline\n', 
                ),
                ("NETWORK INFORMATION","NETSCAN", 
                'vol.py -f “dump_file” ‑‑profile <profile> netscan\nvol.py -f “dump_file” ‑‑profile <profile> netstat\n', 
                'vol.py -f “dump_file” linux.netscan\nvol -f “dump_file” linux.netstat\n', 
                ),
                ("REGISTRY","HIVELIST", 
                'vol.py -f “dump_file” ‑‑profile <profile> hivescan\nvol.py -f “dump_file” ‑‑profile <profile> hivelist\n', 
                'vol.py -f “dump_file” linux.registry.hivescan\nvol -f “dump_file” linux.registry.hivelist\n', 
                ),

                ("REGISTRY","PRINTKEY", 
                'vol.py -f “dump_file” ‑‑profile <profile> printkey\nvol.py -f “dump_file” ‑‑profile <profile> printkey -K \n“Software\Microsoft\linux\CurrentVersion\n', 
                'vol -f “dump_file” linux.registry.printkey\nvol -f “dump_file” linux.registry.printkey ‑‑key\n“Software\Microsoft\linux\CurrentVersion\n', 
                ),

                ("REGISTRY","HIVEDUMP", 
                'vol.py -f “dump_file” ‑‑profile hivedump -o <offset>\n', 
                'I’m not sure if this capability exists in Vol3;\nhowever,you may be able to extractregistry\nhives using filedump with the offset\n', 
                ),
        ]

        # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (Use,cmd_name, vol2_cmd, vol3_cmd) in enumerate(commands_info):
            current_row = row_offset + i


            use_label = tk.Label(self.frame, text=Use, bg="black", fg="#ccff33", font=("Terminal",15), justify="left")
            use_label.grid(row=current_row, column=0, sticky='ew', padx=5)
    
            cmd_name_label = tk.Label(self.frame, text=cmd_name, bg="black", fg="#ccff33", font=("Terminal", 15), justify="center")
            cmd_name_label.grid(row=current_row, column=1, sticky='ew', padx=5)
    
            # Create Text widget for Volatility 2 command
            vol2_text_widget = tk.Text(self.frame, height=4, width=60, bg="black", fg="#ccff33",font=("Terminal", 11), wrap="none")
            vol2_text_widget.insert("1.0", vol2_cmd)
            vol2_text_widget.grid(row=current_row, column=2, sticky='w', padx=10)

            # Create Text widget for Volatility 3 command
            vol3_text_widget = tk.Text(self.frame, height=4, width=60, bg="black", fg="#ccff33", font=("Terminal", 11), wrap="none")
            vol3_text_widget.insert("1.0", vol3_cmd)
            vol3_text_widget.grid(row=current_row, column=3, sticky='w', padx=10)

        self.cheatsheet_label = tk.Label(self.frame, text="\n\n", bg="black", fg="#990000", font=("Terminal", 15), justify="left")
        self.cheatsheet_label.grid(row=17, column=0, columnspan=4, sticky='ew', padx=10, pady=10)
        
        
        self.linux_docker_back = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.linux_docker_selction)
        self.linux_docker_back.grid(row=18, column=0, sticky='w', pady=(15, 10))
        self.linux_docker_NEXT = tk.Button(self.frame, text="next", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.linux_volatility_cheatsheet1)
        self.linux_docker_NEXT.grid(row=18, column=3, sticky='e', pady=(10, 10))


        


######################################################################################################################################
    def linux_volatility_cheatsheet1(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.cheatsheet_label = tk.Label(self.frame, text="VOLATILITY CHEATSHEET", bg="black", fg="#ccff33", font=("Terminal", 25), justify="left")
        self.cheatsheet_label.grid(row=0, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

        # Column headers
        columns = ["Use","Command Name", "Volatility 2 Command", "Volatility 3 Command"]
        for i, column in enumerate(columns):
            header_label = tk.Label(self.frame, text=column, bg="black", fg="#990000", font=("Terminal", 20), justify="left")
            header_label.grid(row=1, column=i, sticky='ew', padx=10, pady=20)

       	# Sample Data for the Cheatsheet (you would populate this with actual data)
        commands_info = [
            
            ("FILES","FILESCAN", 
            'vol.py -f “dump_file” ‑‑profile <profile> filescan', 
            'vol -f “dump_file” linux.filescan', 
            ),
            
            ("FILES","FILEDUMP", 
            'vol.py -f “dump_file” ‑‑profile <profile> \ndumpfiles ‑‑dump-dir=“/path/to/dir\n\nvol.py -f “dump_file” ‑‑profile <profile> dumpfiles \n‑‑dump-dir=“/path/to/dir” -Q <offset>\n\nvol.py -f “dump_file” ‑‑profile <profile> dumpfiles \n‑‑dump-dir=“/path/to/dir” -p <PID>', 
            'vol -f ““dump_file”” -o ““dump_file”” linux.dumpfiles\n\nvol -f “dump_file” -o “/path/to/dir” \nlinux.dumpfiles ‑‑virtaddr <offset>\n\nvol -f “dump_file” -o “/path/to/dir”\nlinux.dumpfiles ‑‑physaddr <offset>', 
            ),
            ("MISCELLANEOUS","MALFIND", 
            'vol.py -f “dump_file” ‑‑profile <profile> malfind\n', 
            'vol -f “dump_file” linux.malfind\n', 
            ),
            ("MISCELLANEOUS","YARASCAN", 
            'vol.py -f “dump_file” ‑‑profile <profile> filescan\n', 
            'vol -f “dump_file” linux.filescan\n', 
            )
            
            
        ]
        # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (Use,cmd_name, vol2_cmd, vol3_cmd) in enumerate(commands_info):
            current_row = row_offset + i


            use_label = tk.Label(self.frame, text=Use, bg="black", fg="#ccff33", font=("Terminal",15), justify="left")
            use_label.grid(row=current_row, column=0, sticky='ew', padx=5)
    
            cmd_name_label = tk.Label(self.frame, text=cmd_name, bg="black", fg="#ccff33", font=("Terminal", 15), justify="center")
            cmd_name_label.grid(row=current_row, column=1, sticky='ew', padx=5)
    
            # Create Text widget for Volatility 2 command
            vol2_text_widget = tk.Text(self.frame, height=3, width=50, bg="black", fg="#ccff33",font=("Terminal", 11), wrap="none")
            vol2_text_widget.insert("1.0", vol2_cmd)
            vol2_text_widget.grid(row=current_row, column=2, sticky='w', padx=10)

            # Create Text widget for Volatility 3 command
            vol3_text_widget = tk.Text(self.frame, height=3, width=50, bg="black", fg="#ccff33", font=("Terminal", 11), wrap="none")
            vol3_text_widget.insert("1.0", vol3_cmd)
            vol3_text_widget.grid(row=current_row, column=3, sticky='w', padx=10)


        self.cheatsheet_label = tk.Label(self.frame, text="\n\n\n\n Note :If you want to try more plugins please try this coammnd:\n\n$ vol.py -h\n\n", bg="black", fg="#990000", font=("Terminal", 15), justify="left")
        self.cheatsheet_label.grid(row=10, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

        
        self.linux_docker_back = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.linux_volatility_cheatsheet)
        self.linux_docker_back.grid(row=13, column=0, sticky='w',  pady=10)

        self.linux_docker_sample = tk.Button(self.frame, text="Click hre to see \nsample Document", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.sample_Volatality_Document)
        self.linux_docker_sample.grid(row=11, column=2, sticky='e', pady=10)

##############################################################################################################################################################################################################
##############################################################################################################################################################################################################
    def Docker_creation_sample_file(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
        
         #Information 
        self.note_label1 = tk.Label(self.frame, text=" Information: ", bg="#b91919", fg="#ccff33",font=("Terminal",28), wraplength=1300, justify="center")
        self.note_label1.grid(row=0, column=1, columnspan=4,pady=(20,10))

   
        
        
        self.lable=tk.Label(self.frame, text="Below are the refrence documentation to create your own docker\n\n\n",bg="black", fg="#43af1c",wraplength=1000, font=("Terminal",25))
        self.lable.grid(row=1, column=1, columnspan=4,sticky='ew',padx=10, pady=20)


        # Button for Volatility3 
        self.lable=tk.Button(self.frame, text="\n   Referance 1   \n", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="left",command=self.referance_1)
        self.lable.grid(row=7, column=1,columnspan=4,sticky='w', padx=50)

        # Button for cyber tool 
        self.lable=tk.Button(self.frame, text="\n   Referance 2   \n", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="left", command=self.referance_2)
        self.lable.grid(row=7, column=2,columnspan=4,sticky='e' ,padx=50)

        self.label = tk.Label(self.frame, text="\n\n", bg="black", fg="#990000", font=("Terminal", 15), justify="left")
        self.label.grid(row=10, column=0, columnspan=4, sticky='ew', padx=10, pady=10)


        self.back = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.create_docker_page)
        self.back.grid(row=14, column=3, sticky='w',  pady=10)

        

    def  referance_1(self):
        # Download Docker Desktop installer
        webbrowser.open("https://drive.google.com/file/d/1VEnEZn_il36hRlcHnJZcvuYy_4tS-XdN/view?usp=sharing")
    
    def  referance_2(self):
        # Download Docker Desktop installer
        webbrowser.open("https://drive.google.com/file/d/1NKceEv7EgMSsApw3s0HEgeXyg5qei6ok/view?usp=sharing")





    ##############################################################################################################################################################################################################
    ##############################################################################################################################################################################################################
    def MacOs_docker_selction(self):
        # Clear the current view
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        # Add widgets for the Docker installation page
        self.docker_label=tk.Label(self.frame, text=" Select your mode of \n\nDocker implementation !! \n\n ",bg="black", fg="#ccff33", font=("Terminal",28),justify="center")
        self.docker_label.grid(row=0, column=1, sticky='ew',columnspan=3,padx=10, pady=10)
        

        self.docker_button=tk.Button(self.frame, text="\n  Automated \n  Docker Installation  \n", bg="#990000", fg="black",font=("Terminal",20), justify="center",command=self.show_macos_docker_info)
        self.docker_button.grid(row=2, column=1, sticky='ew',padx=10,pady=10)



        self.docker_button=tk.Button(self.frame, text="\n  Manual \n  Docker Installation   \n", bg="#990000", fg="black",font=("Terminal",20), justify="center",command=self.show_macos_docker_manual_info)
        self.docker_button.grid(row=2, column=2, sticky='ew',padx=10, pady=10)
        
        
        self.docker_button=tk.Button(self.frame, text="\n  Linux Profile  \n  creation  \n", bg="#990000", fg="black",font=("Terminal",20), justify="center",command=self.linux_profile_page)
        self.docker_button.grid(row=2, column=3, sticky='ew',padx=10, pady=10)


        self.docker_label=tk.Label(self.frame, text="\n\n \n\n ",bg="black", fg="#ccff33", font=("Terminal",30),justify="center")
        self.docker_label.grid(row=5, column=1, sticky='ew',padx=10, pady=10)

        self.windows_back = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.create_docker_page)
        self.windows_back.grid(row=10, column=0, sticky='w', pady=(10, 0))


##############################################################################################################################################################################################################

    def show_macos_docker_info(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()
      
# Add widgets for the Docker installation page
        self.docker_label=tk.Label(self.frame, text=" Automated Docker Configuration for Windows\n" ,wraplength=1200, bg="black", fg="#ccff33", font=("Terminal",30),justify="center")
        self.docker_label.grid(row=0, column=1, sticky='ew',padx=10, pady=10)
        self.docker_label=tk.Label(self.frame, text=" \n ",bg="black", fg="#ccff33", font=("Terminal",20),justify="center")
        self.docker_label.grid(row=0, column=2, sticky='ew',padx=10, pady=10)

        self.docker_label2=tk.Label(self.frame, text="Note : Before start please check you have Docker Desktop Installed.\n\n",wraplength=1300,bg="black", fg="#b91919", font=("Terminal",20),justify="left")
        self.docker_label2.grid(row=2, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="Step1: If NO, then please click on Install Docker Desktop and run it after installation.Once done please select path to memory dump and click on pull docker button. ",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label4.grid(row=3, column=1, sticky='w',padx=5, pady=0)

        self.label3=tk.Label(self.frame, text="Note: When you Download the Docker Desktop for the 1st time Please retart your system after running the Docker Desktop to access the docker image otherwise you will face some error.\n" , bg="black", fg="#990000",font=("Terminal",10), wraplength=800, justify="left")
        self.label3.grid(row=4, column=1, sticky='w',padx=5, pady=0)


        # Add a button to install Docker Desktop
        self.install_docker_button = tk.Button(self.frame, text="  Install   \n  Docker  \n  Desktop  ", bg="#990000", fg="black", font=("Terminal",20), command=self.install_macos_docker)
        self.install_docker_button.grid(row=3, column=2, sticky='w', pady=10)
        
        self.docker_label3=tk.Label(self.frame, text="Step2 :If YES, please select Memory Dump which you want to analyze using Volatility\n",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label3.grid(row=5, column=1, sticky='w',padx=5, pady=0)

        # Add a button to select the memory dump file
        self.select_dump_button = tk.Button(self.frame, text=" Select \n Memory Dump ", bg="#990000", fg="black", font=("Terminal",20), command=self.select_macos_path)
        self.select_dump_button.grid(row=5, column=2, sticky='w', pady=(10, 10))

        self.docker_label3=tk.Label(self.frame, text="Step 3:Once done pull the Docker.\n",wraplength=800,bg="black", fg="#ccff33", font=("Terminal",20),justify="left")
        self.docker_label3.grid(row=7, column=1, sticky='w',padx=5, pady=0) 


        # Add a button to pull the Docker image and open it in terminal
        self.pull_docker_button = tk.Button(self.frame, text="Pull \n Docker Image", bg="#990000", fg="black", font=("Terminal",20), command=self.pull_macos_docker_image)
        self.pull_docker_button.grid(row=7, column=2, sticky='w', pady=(10, 10))
 
        self.note_labe = tk.Label(self.frame, text=" \n", bg="black",font=("Terminal",20), justify="center")
        self.note_labe.grid(row=8, column=1,)

        self.docker_label3=tk.Label(self.frame, text="Once you pull the docker click on next to see the volatility commands",wraplength=200,bg="black", fg="#b21e1e", font=("Terminal",10),justify="left")
        self.docker_label3.grid(row=10, column=2, sticky='w',padx=10, pady=10)

        # Next Button (initially hidden)
        self.next_button = tk.Button(self.frame, text="  Next  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20),justify="right", command=self.macos_volatility_cheatsheet)
        self.next_button.grid(row=11, column=2, sticky='w', pady=(10, 0))

        # Add a button to go back to the previous page
        self.windows_docker_back = tk.Button(self.frame, text="  Back  ", bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.MacOs_docker_selction)
        self.windows_docker_back.grid(row=11, column=0, sticky='w', pady=(10, 0))
        
##############################################################################################################################################################################################################

    def install_macos_docker(self):
        # Check if Docker is already installed
        try:
            subprocess.run(['docker', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            messagebox.showinfo("Check Docker", "Docker is already installed.")
            return
        except subprocess.CalledProcessError:
            pass  # Docker is not installed

        # Update brew and install Docker Desktop
        try:
            subprocess.run(['brew', 'update'], check=True)
            subprocess.run(['brew', 'install', '--cask', 'docker'], check=True)
            messagebox.showinfo("Install Docker", "Docker installed successfully.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Install Docker", "Failed to install Docker.")

    def select_macos_path(self):
        # Prompt the user to select the memory dump file
        self.selected_file_path = filedialog.askopenfilename(
            title="Select Memory Dump File", filetypes=[("All Files", "*.*")])
        if self.selected_file_path:
            messagebox.showinfo("Selected File", f"Selected file: {self.selected_file_path}")

    def pull_macos_docker_image(self):
        if not self.selected_file_path:
            messagebox.showwarning("File Not Selected", "Please select a memory dump file before pulling the Docker image.")
            return

        # Extract the file name from the file path
        file_name = os.path.basename(self.selected_file_path)
        
        # Pull Docker image and create a volume
        try:
            subprocess.run(['docker', 'pull', 'pmeher/volatility'], check=True)
            volume = ''.join(random.choices(string.ascii_lowercase, k=3))
            docker_command = f'docker run -it --name {volume} -v "{self.selected_file_path}:/app/{file_name}" pmeher/volatility'
            escaped_docker_command = docker_command.replace('"', '\\"').replace('$', '\\$')
            script_command = f'tell application "Terminal" to do script "{escaped_docker_command}"'
            subprocess.run(['osascript', '-e', script_command], check=True)
        except subprocess.CalledProcessError:
            messagebox.showerror("Docker Error", "Failed to execute Docker command.")


        

##############################################################################################################################################################################################################

    def show_macos_docker_manual_info(self):

        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()    
        # Manual Process

        self.docker_label1=tk.Label(self.frame, text="  Manual Docker Installation  ", wraplength=1500, bg="black", fg="#43af1c",font=("Terminal",35), justify="center")
        self.docker_label1.grid(row=1, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="Please follow the below steps :\n",bg="black", fg="#990000", font=("Terminal",25),justify="center")
        self.docker_label4.grid(row=2, column=1, sticky='ew',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="1.Install the Docker Desktop from : https://docs.docker.com/desktop/install/mac-install/",wraplength=1000, bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=3, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="2.Double-click Docker.dmg to open the installer, then drag the Docker icon to the Applications folder.",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=4, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="3.Open Finder and go to your Applications folder, double-click on the Docker icon to launch Docker Desktop,\nyou may be prompted to grant permission to install additional components. \nFollow the on-screen instructions to complete the installation.",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=5, column=1, sticky='w',padx=10, pady=10)

        self.label3=tk.Label(self.frame, text="Note: When you Download the Docker Desktop for the 1st time Please retart your system after running the Docker Desktop to access the docker image otherwise you will face some error.\n" , bg="black", fg="#990000",font=("Terminal",15), wraplength=800, justify="left")
        self.label3.grid(row=6, column=1, sticky='w',padx=5, pady=0)

        self.docker_label4=tk.Label(self.frame, text="$docker pull pmeher/volatility ",bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=7, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="5.Access your memory dump in docker using :",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=8, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="$docker run -it --name any_random_name -v C:\\Users\\path_of_your_memory_dump:/app/memory_dump_name pmeher/volatility \n\nExample : $docker run -it --name user -v C:\\Users\\admin\Desktop\memory_dump:/app/memory_dump pmeher/volatility ",bg="black",fg="#990000", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=9, column=1, sticky='w',padx=10, pady=10)

        self.docker_label4=tk.Label(self.frame, text="6.Click on next to see the volatility commands to analyze the memory dump file \n\n\n\n",bg="black", fg="#ccff33", font=("Terminal",15),justify="left")
        self.docker_label4.grid(row=10, column=1, sticky='w',padx=10, pady=10)


        
        self.windows_back = tk.Button(self.frame, text="Back",wraplength=1000,bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.linux_docker_selction)
        self.windows_back.grid(row=13, column=0, sticky='w', pady=(10, 0))
     
        self.windows_next = tk.Button(self.frame, text="Next",wraplength=1000, bg="#ccff33", fg="#b21e1e", font=("Terminal",20), justify="right", command=self.linux_volatility_cheatsheet)
        self.windows_next.grid(row=13, column=2, sticky='w', pady=(10, 0))

 ##############################################################################################################################################################################################################


    def macos_volatility_cheatsheet(self):

        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.cheatsheet_label = tk.Label(self.frame, text="VOLATILITY CHEATSHEET", bg="black", fg="#ccff33", font=("Terminal", 25), justify="left")
        self.cheatsheet_label.grid(row=0, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

        # Column headers
        columns = ["Use","Command Name", "Volatility 2 Command", "Volatility 3 Command"]
        for i, column in enumerate(columns):
            header_label = tk.Label(self.frame, text=column, bg="black", fg="#990000", font=("Terminal", 20), justify="left")
            header_label.grid(row=1, column=i, sticky='ew', padx=10, pady=20)

        commands_info = [
		    ("OS INFORMATION",
		    "IMAGEINFO", 
		    'vol.py -f “dump_file” imageinfo\n', 
		    'vol -f “dump_file” linux.info\n', 
		    ),
		    ("PROCESS INFORMATION",
		    "PSLIST", 
		    'vol.py -f “dump_file” --profile <profile> pslist\n', 
		    'vol -f “dump_file” linux.pslist', 
		    ),
		    ("PROCESS INFORMATION","PSSCAN", 
		    'vol.py -f “dump_file” --profile <profile> pslist\n', 
		    'vol -f “dump_file” linux.psscan\n', 
		    ),
		    ("PROCESS INFORMATION","PSTREE", 
		    'vol.py -f “dump_file” ‑‑profile <profile> pstree\n', 
		    'vol -f “dump_file” linux.pstree\n', 
		    ),
		    ("PROCESS INFORMATION","PROCDUMP", 
		    'vol.py -f “dump_file” ‑‑profile <profile> procdump \n-p <PID> ‑‑dump-dir=“/path/to/dir\n', 
		    'vol -f “dump_file” -o “/path/to/dir” \nlinux.dumpfiles ‑‑pid <PID>', 
		    ),
		    ("PROCESS INFORMATION","MEMDUMP", 
		    'vol.py -f “dump_file” ‑‑profile <profile> memdump \n-p <PID> ‑‑dump-dir=“/path/to/dir\n', 
		    'vol -f “dump_file” -o “/path/to/dir” \nlinux.memmap ‑‑dump ‑‑pid <PID>\n', 
		    ),
		    ("PROCESS INFORMATION","DLLS", 
		    'vol.py -f “dump_file” ‑‑profile <profile> dlllist \n-p <PID>\n', 
		    'vol -f “dump_file” linux.dlllist ‑‑pid <PID>\n', 
		    ),
		    ("PROCESS INFORMATION","CMDLINE", 
		    'vol.py -f “dump_file” ‑‑profile <profile> cmdline\nvol.py -f “dump_file” ‑‑profile <profile> cmdscan\nvol -f “dump_file” ‑‑profile <profile> consoles\n', 
		    'vol -f “dump_file” linux.cmdline\n', 
		    ),
		    ("NETWORK INFORMATION","NETSCAN", 
		    'vol.py -f “dump_file” ‑‑profile <profile> netscan\nvol.py -f “dump_file” ‑‑profile <profile> netstat\n', 
		    'vol.py -f “dump_file” linux.netscan\nvol -f “dump_file” linux.netstat\n', 
		    ),
		    ("REGISTRY","HIVELIST", 
		    'vol.py -f “dump_file” ‑‑profile <profile> hivescan\nvol.py -f “dump_file” ‑‑profile <profile> hivelist\n', 
		    'vol.py -f “dump_file” linux.registry.hivescan\nvol -f “dump_file” linux.registry.hivelist\n', 
		    ),

		    ("REGISTRY","PRINTKEY", 
		    'vol.py -f “dump_file” ‑‑profile <profile> printkey\nvol.py -f “dump_file” ‑‑profile <profile> printkey -K \n“Software\Microsoft\linux\CurrentVersion\n', 
		    'vol -f “dump_file” linux.registry.printkey\nvol -f “dump_file” linux.registry.printkey ‑‑key\n“Software\Microsoft\linux\CurrentVersion\n', 
		    ),

		    ("REGISTRY","HIVEDUMP", 
		    'vol.py -f “dump_file” ‑‑profile hivedump -o <offset>\n', 
		    'I’m not sure if this capability exists in Vol3;\nhowever,you may be able to extractregistry\nhives using filedump with the offset\n', 
		    ),
        ]
        

        # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (Use,cmd_name, vol2_cmd, vol3_cmd) in enumerate(commands_info):
            current_row = row_offset + i


            use_label = tk.Label(self.frame, text=Use, bg="black", fg="#ccff33", font=("Terminal",15), justify="left")
            use_label.grid(row=current_row, column=0, sticky='ew', padx=5)
    
            cmd_name_label = tk.Label(self.frame, text=cmd_name, bg="black", fg="#ccff33", font=("Terminal", 15), justify="center")
            cmd_name_label.grid(row=current_row, column=1, sticky='ew', padx=5)
    
            # Create Text widget for Volatility 2 command
            vol2_text_widget = tk.Text(self.frame, height=4, width=60, bg="black", fg="#ccff33",font=("Terminal", 11), wrap="none")
            vol2_text_widget.insert("1.0", vol2_cmd)
            vol2_text_widget.grid(row=current_row, column=2, sticky='w', padx=10)

            # Create Text widget for Volatility 3 command
            vol3_text_widget = tk.Text(self.frame, height=4, width=60, bg="black", fg="#ccff33", font=("Terminal", 11), wrap="none")
            vol3_text_widget.insert("1.0", vol3_cmd)
            vol3_text_widget.grid(row=current_row, column=3, sticky='w', padx=10)

        self.cheatsheet_label = tk.Label(self.frame, text="\n\n", bg="black", fg="#990000", font=("Terminal", 15), justify="left")
        self.cheatsheet_label.grid(row=17, column=0, columnspan=4, sticky='ew', padx=10, pady=10)
        
        self.macos_docker_NEXT = tk.Button(self.frame, text="next", bg="#ccff33", fg="#b21e1e", font=("Terminal",15), justify="right", command=self.macos_volatility_cheatsheet1)
        self.macos_docker_NEXT.grid(row=18, column=3, sticky='e', pady=(10, 10)) 


        self.macos_back_button = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",15), justify="right", command=self.MacOs_docker_selction)
        self.macos_back_button.grid(row=18, column=0, sticky='w', pady=(5, 0))

        


######################################################################################################################################
    def macos_volatility_cheatsheet1(self):
        # Clear the current view
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.cheatsheet_label = tk.Label(self.frame, text="VOLATILITY CHEATSHEET", bg="black", fg="#ccff33", font=("Terminal", 25), justify="left")
        self.cheatsheet_label.grid(row=0, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

        # Column headers
        columns = ["Use","Command Name", "Volatility 2 Command", "Volatility 3 Command"]
        for i, column in enumerate(columns):
            header_label = tk.Label(self.frame, text=column, bg="black", fg="#990000", font=("Terminal", 20), justify="left")
            header_label.grid(row=1, column=i, sticky='ew', padx=10, pady=20)

       	# Sample Data for the Cheatsheet (you would populate this with actual data)
        commands_info = [
            
            ("FILES","FILESCAN", 
            'vol.py -f “dump_file” ‑‑profile <profile> filescan', 
            'vol -f “dump_file” linux.filescan', 
            ),
            
            ("FILES","FILEDUMP", 
            'vol.py -f “dump_file” ‑‑profile <profile> \ndumpfiles ‑‑dump-dir=“/path/to/dir\n\nvol.py -f “dump_file” ‑‑profile <profile> dumpfiles \n‑‑dump-dir=“/path/to/dir” -Q <offset>\n\nvol.py -f “dump_file” ‑‑profile <profile> dumpfiles \n‑‑dump-dir=“/path/to/dir” -p <PID>', 
            'vol -f ““dump_file”” -o ““dump_file”” linux.dumpfiles\n\nvol -f “dump_file” -o “/path/to/dir” \nlinux.dumpfiles ‑‑virtaddr <offset>\n\nvol -f “dump_file” -o “/path/to/dir”\nlinux.dumpfiles ‑‑physaddr <offset>', 
            ),
            ("MISCELLANEOUS","MALFIND", 
            'vol.py -f “dump_file” ‑‑profile <profile> malfind\n', 
            'vol -f “dump_file” linux.malfind\n', 
            ),
            ("MISCELLANEOUS","YARASCAN", 
            'vol.py -f “dump_file” ‑‑profile <profile> filescan\n', 
            'vol -f “dump_file” linux.filescan\n', 
            )
            
            
        ]
        # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (Use, cmd_name, vol2_cmd, vol3_cmd) in enumerate(commands_info):
            current_row = row_offset + i
            use_label = tk.Label(self.frame, text=Use, bg="black", fg="#ccff33", font=("Terminal",10), justify="left")
            use_label.grid(row=current_row, column=0, sticky='ew', padx=5)
    
            cmd_name_label = tk.Label(self.frame, text=cmd_name, bg="black", fg="#ccff33", font=("Terminal", 10), justify="center")
            cmd_name_label.grid(row=current_row, column=1, sticky='ew', padx=5)
    
            vol2_text = tk.Text(self.frame, bg="black", fg="#ccff33", font=("Terminal", 10), height=3, width=55)
            vol2_text.insert("end", vol2_cmd)
            vol2_text.config(state="disabled")
            vol2_text.grid(row=current_row, column=2, sticky='w', padx=5)
    
            vol3_text = tk.Text(self.frame, bg="black", fg="#ccff33", font=("Terminal", 10), height=3, width=55)
            vol3_text.insert("end", vol3_cmd)
            vol3_text.config(state="disabled")
            vol3_text.grid(row=current_row, column=3, sticky='w', padx=5)
            
            
       # Dynamically create rows for each command
        row_offset = 2  # Starting row for the command entries
        for i, (Use,cmd_name, vol2_cmd, vol3_cmd) in enumerate(commands_info):
            current_row = row_offset + i


            use_label = tk.Label(self.frame, text=Use, bg="black", fg="#ccff33", font=("Terminal",15), justify="left")
            use_label.grid(row=current_row, column=0, sticky='ew', padx=5)
    
            cmd_name_label = tk.Label(self.frame, text=cmd_name, bg="black", fg="#ccff33", font=("Terminal", 15), justify="center")
            cmd_name_label.grid(row=current_row, column=1, sticky='ew', padx=5)
    
            # Create Text widget for Volatility 2 command
            vol2_text_widget = tk.Text(self.frame, height=3, width=50, bg="black", fg="#ccff33",font=("Terminal", 11), wrap="none")
            vol2_text_widget.insert("1.0", vol2_cmd)
            vol2_text_widget.grid(row=current_row, column=2, sticky='w', padx=10)

            # Create Text widget for Volatility 3 command
            vol3_text_widget = tk.Text(self.frame, height=3, width=50, bg="black", fg="#ccff33", font=("Terminal", 11), wrap="none")
            vol3_text_widget.insert("1.0", vol3_cmd)
            vol3_text_widget.grid(row=current_row, column=3, sticky='w', padx=10)


        self.cheatsheet_label = tk.Label(self.frame, text="\n\n\n\n Note :If you want to try more plugins please try this coammnd:\n\n$ vol.py -h\n\n", bg="black", fg="#990000", font=("Terminal", 15), justify="left")
        self.cheatsheet_label.grid(row=10, column=0, columnspan=4, sticky='ew', padx=10, pady=10)
        
        self.macos_back_button = tk.Button(self.frame, text="Back", bg="#ccff33", fg="#b21e1e", font=("Terminal",15), justify="right", command=self.macos_volatility_cheatsheet)
        self.macos_back_button.grid(row=10, column=0, sticky='w', pady=(5, 0))

        self.macos_sample = tk.Button(self.frame, text="Click hre to see \nsample Document", bg="#ccff33", fg="#b21e1e", font=("Terminal",15), justify="right", command=self.sample_Document)
        self.macos_sample.grid(row=9, column=2, sticky='e', pady=(5, 0))
       
##############################################################################################################################################################################################################
##############################################################################################################################################################################################################

    def sample_Document(self):
        # Replace 'document_url' with the actual URL of the document
        document_url = 'https://drive.google.com/file/d/1nt60lq1229gq2YJpB5PR3LDjzJDy-Wc4/view?usp=drive_link'

        # Open the URL in the default web browser
        webbrowser.open(document_url)

######################################################################################################################################
######################################################################################################################################
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

