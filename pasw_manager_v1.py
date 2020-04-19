from tkinter import *
import re
import logging
import os
import pickle

logging.basicConfig()
logger=logging.getLogger()
logger.setLevel(logging.INFO)

pasw_file=os.path.relpath(".pasw")

def load_passwords():
    if os.path.exists(pasw_file):
        with open(pasw_file,"rb") as fh:
            client_passwords_dict=pickle.load(fh)
            logger.info(f"finished loading {len(client_passwords_dict)} passwords from {pasw_file}")
            return client_passwords_dict
    else:
        logger.info(f"{pasw_file} doesn't exist so will return empty dictionary")
        return {}

def save_passwords(client_pasw_dict):
    with open(pasw_file,"wb") as fh:
        pickle.dump(client_pasw_dict,fh)
        logger.info(f"finished dumping {len(client_pasw_dict)} client passwords")

def renderAllPasswords():
    logger.info("will render all passwords")
    listBox.delete(0,END)
    counter = 0
    for client, password in client_pasw_dict.items():
        listBox.insert(counter, f"{client} : {password}")
        counter += 1

def search_passwords(event):
    logger.info(f"search_passwords is called with event {event}")
    logger.info(f"entered key symbol is {event.keysym}")
    search_text=searchBox.get()
    if event.keysym!='BackSpace':
        search_text+=event.char
    else:
        logger.info(f"BackSpace was pressed : {event.keysym}")
        search_text=search_text[:-1]
    logger.info(f"current searchBox text : {search_text}")
    listBox.delete(0,END)
    new_client_pasw_dict={}
    counter=0
    for client,pasw in client_pasw_dict.items():
        if re.search(search_text.lower(),client.lower()):
            new_client_pasw_dict[client]=pasw
            listBox.insert(counter,f"{client} : {pasw}")
        if search_text=="":
            logger.info("search box is empty so will render all passwords")
            renderAllPasswords()

def open_new_client_frame():
    logger.info(f"will add a new client")
    frameBody.grid_remove()
    frameNewClient.grid()

def confirm_new_client():
    new_client_name=clientNameEntry.get()
    new_client_pasw=newPasswordEntry.get()
    client_pasw_dict[new_client_name]=new_client_pasw
    save_passwords(client_pasw_dict)
    renderAllPasswords()
    frameNewClient.grid_remove()
    frameBody.grid()

def cancel_new_client():
    frameNewClient.grid_remove()
    frameBody.grid()

def edit_client_pasw():
    client_pasw_lines=listBox.get(0,END)
    if len(client_pasw_lines)>0:
        client_pasw_line=client_pasw_lines[0]
        client,pasw=client_pasw_line.split(":")
        logger.info(f"will edit {client},{pasw}")


window=Tk()
window.title("Password manager")
window.geometry("700x500")

# frameBody will contain search box, client:pasw listBox and Add/Edit buttons
frameBody=Frame(window, pady=20)
frameBody.grid()

frameHeader=Frame(frameBody,pady=20)
frameHeader.grid(pady=10)

searchLabel=Label(frameHeader, text="Search:",font="Arial 15",width=10)
searchLabel.grid(row=0,column=0)

searchBox=Entry(frameHeader, width=60,font="Arial 15")
searchBox.grid(row=0,column=1)
searchBox.bind("<Key>",search_passwords)

listBox=Listbox(frameBody,font="Arial 15",width=60,justify=CENTER)
listBox.grid(pady=10)

client_pasw_dict=load_passwords()
renderAllPasswords()

addClientButton=Button(frameBody, text="Add New Client", font="Arial 15", width=40,padx=10,pady=10,bg="coral",activebackground="green",command=open_new_client_frame)
addClientButton.grid(pady=10)

editClientButton=Button(frameBody, text="Add New Client", font="Arial 15", width=40,padx=10,pady=10,bg="coral",activebackground="green",command=edit_client_pasw)
editClientButton.grid(pady=10)


# frame widget when adding new client
frameNewClient=Frame()
clientLabel=Label(frameNewClient,text="Client :",font="Arial 15", fg="coral",width=20)
clientNameEntry=Entry(frameNewClient,width="20",font="Arial 15")
newPasswordLabel=Label(frameNewClient,text="Password :", font="Arial 15",fg="coral",width=20)
newPasswordEntry=Entry(frameNewClient,width=20,font="Arial 15")
newClientConfirmButton=Button(frameNewClient,text="Submit", font="Arial 15", width=20,command=confirm_new_client)
newClientCancelButton=Button(frameNewClient,text="Cancel",font="Arial 15",width=20,command=cancel_new_client)
clientLabel.grid(row=0,column=0,pady=10)
clientNameEntry.grid(row=0,column=1,pady=10)
newPasswordLabel.grid(row=1,column=0,pady=10)
newPasswordEntry.grid(row=1,column=1,pady=10)
newClientConfirmButton.grid(row=2,column=0, pady=10)
newClientCancelButton.grid(row=2,column=1, pady=10)

window.mainloop()